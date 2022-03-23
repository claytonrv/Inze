from django.shortcuts import render
from rest_framework import mixins, viewsets, status, views

from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from credit_card.models import CreditCardRecord
from credit_card.serializers import (
    CreditCardRecordSerializer,
    CreditCardRecordListSerializer,
)
from credit_card.utils import RecordTranslator


class CreditCardRecordViewset(
    viewsets.GenericViewSet,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
):
    def get_serializer_class(self):
        return CreditCardRecordListSerializer

    def get_queryset(self):
        base_queryset = CreditCardRecord.objects.all()
        params = self.request.query_params
        if params and params["files"]:
            file_name_list = params["files"].split(",")
            base_queryset = CreditCardRecord.objects.filter(file__in=file_name_list)
        return base_queryset


class CreditCardBillsUploadView(views.APIView):
    parser_classes = [MultiPartParser]

    def get_queryset(self):
        return CreditCardRecord.objects.all()

    def post(self, request, *args, **kwargs):
        translator = RecordTranslator()
        user = Token.objects.get(key=request.auth).user
        recordList = []
        file_name_list = []
        for file in request.data.getlist("file"):
            file_name = file.name
            file_name_list.append(file_name)
            for row in file:
                if row != b"date,category,title,amount\n":
                    recordList.append(
                        translator.translate_csv_row_to_record(row, user, file_name)
                    )
        serializer = CreditCardRecordSerializer(data=recordList, many=True)
        print(
            f'Received {len(request.data.getlist("file"))} files, {len(recordList)} invoice rows in total '
        )
        if serializer.is_valid():
            CreditCardRecord.objects.filter(file__in=file_name_list).delete()
            serializer.save()
            return Response(file_name_list, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
