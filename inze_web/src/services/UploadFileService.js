import axios from 'axios';

const UploadFiles = (filesList:any) => {
    var result;
    axios.post('http://localhost:8082/upload_files', filesList, {
        headers:{
            'Content-type': 'multipart/form-data'
        }
    }).then( jsonInvoices => {
        console.log(jsonInvoices)
        result = jsonInvoices;
    }).catch( err => {
        console.log(`Error while uploading csv files. ${err}`)
        result = [{}];
    })
    return result;
}


export default UploadFiles;