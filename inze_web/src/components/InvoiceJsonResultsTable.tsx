import React from 'react'

import PropTypes from 'prop-types';

import '../style/components/InvoiceResultsTable.css'

export default function InvoiceJsonResultsTable(props:any){
    return (
        <table className="styled-table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>Spent Amount</th>
                    <th>Purchase category</th>
                    <th>Purchase date</th>
                    <th>Purchase Location</th>
                    <th>Installment</th>
                    <th>Installments number</th>
                </tr>
            </thead>
            <tbody>
                {
                    props.invoiceRecords.map( (invoice:any, index:number)  => {
                    return (
                        <tr key={index}>
                            <td>{ index+1 }</td>
                            <td>{ invoice.amount} </td>
                            <td>{ invoice.category ? invoice.category : "-"} </td>
                            <td>{ invoice.date} </td>
                            <td>{ invoice.store ? invoice.store : "-"} </td>
                            <td>{ invoice.installment_payment ? invoice.installment_payment : "-"} </td>
                            <td>{ invoice.installment_total ? invoice.installment_total : "-"} </td>
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