import axios from 'axios';

const API = axios.create({
    baseURL: 'http://localhost:8000',
    headers:{
        'Authorization': 'Token 7a9f1def25c69d5a1f24863a071b119e545b52ca'
    },
});

export default API;