import json

class RecordTranslator():

    def translate_record_list(self, record_list):
        json = "["
        for record in record_list:
            json += record+","
        json = json[:-1]
        json += "]"
        return json
