import React from 'react';

import CSVUploader from '../components/CSVUploader'

import '../style/pages/Landing.css';

export default function Landing(){
    return (
        <div className="content-wrapper">
            <CSVUploader />
        </div>
    )
}