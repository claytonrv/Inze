import React, { useState } from 'react';

import axios from 'axios';
import { useTranslation } from 'react-i18next';

import InvoiceJsonResultsTable from './InvoiceJsonResultsTable';

import API from '../services/api';

import '../style/components/CSVUploader.css';

export default function CSVUploader () {
    const { t } = useTranslation();
    axios.defaults.baseURL = 'http//localhost:8000';
    const [invoiceFiles, setInvoiceFiles] = useState([])
    const [invoiceResult, setInvoiceResult] = useState({"invoiceRecords": []});
    const [invoiceNameList, setInvoiceNameList] = useState("")

    const handleFilesChange = (event:any) => {
        if(event){
            setInvoiceFiles(Array.from(event.target.files)); 
        }else{
            setInvoiceFiles([])
        }
    }

    const retrieveCreditCardRecordsByBillFileName = (billFileNames:[string]) => {
        let nameList = ""
        billFileNames.forEach(fileName => {
            if(!nameList){
                nameList += fileName
            }
            nameList += (","+fileName)
        })
        API.get('/credit-card-records', {params:{
            files:nameList
        }}).then((creditCardRecords:any) => {
            setInvoiceResult({"invoiceRecords": creditCardRecords.data})
            setInvoiceNameList(nameList)
        }).catch(err => {
            console.log(`Error while retrieving credit card records. ${err}`)
        })
        
        /*API.get('/credit-card-records', {params:{
            user:1
        }}).then((creditCardRecords:any) => {
            setInvoiceResult({"invoiceRecords": creditCardRecords.data})
        }).catch(err => {
            console.log(`Error while retrieving credit card records. ${err}`)
        })*/
    }

    const handleFilesUpload = () => {
        const formData = new FormData();
        invoiceFiles.map((file:any) => {
            return formData.append( 
                "file", 
                file, 
                file.name
            ); 
        })
        API.post('bill-upload', formData, {
            headers:{
                'Content-type': 'multipart/form-data',
            }
        }).then( (fileNameList) => {
            console.log(fileNameList.data)
            retrieveCreditCardRecordsByBillFileName(fileNameList.data)
        }).catch( err => {
            console.log(`Error while uploading csv files. ${err}`)
        })
    }

    return (
        <div className="upload-content">
            <div id='upload'>
                <label htmlFor="file_upload">{t('app.selectFilesButton')}</label>
                <input type="file" id="file_upload" multiple={true} onChange={handleFilesChange} />
                <span>{invoiceFiles.length} {t("app.selectedFiles")}</span>
                <button onClick={handleFilesUpload}>
                    {t("app.processButton")}
                </button>
            </div>
            {invoiceResult && (<InvoiceJsonResultsTable {...invoiceResult} />)}
        </div>
    )
}