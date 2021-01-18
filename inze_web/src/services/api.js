import axios from 'axios';

const API = axios.create({
    baseURL: 'http://localhost:8000',
    headers:{
        'Authorization': 'Token 607a5644cc8fec6f6cd0c83daaf8555546c1a194'
    },
});

export default API;