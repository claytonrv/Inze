import React from 'react'

import PropTypes from 'prop-types';

import '../style/components/InvoiceResultsTable.css'

import { useTranslation } from 'react-i18next';

export default function InvoiceJsonResultsTable(props:any){
    const { t } = useTranslation();
    return (
        <table className="styled-table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>{t('tableHeader.spentValue')}</th>
                    <th>{t('tableHeader.spentCategory')}</th>
                    <th>{t('tableHeader.spentDate')}</th>
                    <th>{t('tableHeader.spentLocation')}</th>
                    <th>{t('tableHeader.spentInstallment')}</th>
                </tr>
            </thead>
            <tbody>
                {
                    props.invoiceRecords.map( (invoice:any, index:number)  => {
                    return (
                        <tr key={index}>
                            <td>{ index+1 }</td>
                            <td>{ t('tableBody.spentCurrency', {amount: invoice.amount})} </td>
                            <td>{ invoice.category ? invoice.category : "-"} </td>
                            <td>{ t('tableBody.spentDate', {date: new Date(invoice.date)})} </td>
                            <td>{ invoice.store ? invoice.store : "-"} </td>
                            <td>{ invoice.installment_payment ? invoice.installment_payment+"/" : ""}{ invoice.installment_total ? invoice.installment_total : ""} </td>
                        </tr>
                        )
                    })
                }
            </tbody>
        </table>
    )
}

InvoiceJsonResultsTable.propTypes = {
    invoiceRecords: PropTypes.arrayOf(PropTypes.shape({
        amount: PropTypes.string.isRequired,
        category: PropTypes.string.isRequired,
        day: PropTypes.string.isRequired,
        installment: PropTypes.any,
        installment_amount: PropTypes.any,
        month: PropTypes.string.isRequired,
        store: PropTypes.string.isRequired,
        year: PropTypes.string.isRequired
    }))
};

InvoiceJsonResultsTable.defaultProps ={
    invoiceRecords: [{
        amount: "",
        category: "",
        day: "",
        installment: null,
        installment_amount: null,
        month: "",
        store: "",
        year: ""
    }]
};