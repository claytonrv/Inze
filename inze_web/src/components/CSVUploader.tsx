import React, { useState } from 'react';

import axios from 'axios';
//import UploadFiles from '../services/UploadFileService';
import InvoiceJsonResultsTable from './InvoiceJsonResultsTable';

import '../style/components/CSVUploader.css';

export default function CSVUploader () {

    const [invoiceFiles, setInvoiceFiles] = useState([])
    const [invoiceResult, setInvoiceResult] = useState();

    const handleFilesChange = event => {
        setInvoiceFiles(Array.from(event.target.files)); 
    }

    const handleFilesUpload = () => {
        const formData = new FormData(); 
        invoiceFiles.map(file => {
            formData.append( 
                "file", 
                file, 
                file.name
            ); 
        })
        axios.post('http://localhost:8082/upload_files', formData, {
            headers:{
                'Content-type': 'multipart/form-data'
            }
        }).then( jsonInvoices => {
            console.log(jsonInvoices.data)
            setInvoiceResult({"invoices": jsonInvoices.data});
        }).catch( err => {
            console.log(`Error while uploading csv files. ${err}`)
            setInvoiceResult([{}]);
        })
    }

    return (
        <div className="upload-content">
            <div id='upload'>
                <label for="file_upload">Selecionar arquivos</label>
                <input type="file" id="file_upload" multiple="multiple" onChange={handleFilesChange} />
                <span>{invoiceFiles.length} arquivos selecionados</span>
                <button onClick={handleFilesUpload}>
                    Processar arquivos
                </button>
            </div>
            {invoiceResult && (<InvoiceJsonResultsTable {...invoiceResult} />)}
        </div>
    )
}