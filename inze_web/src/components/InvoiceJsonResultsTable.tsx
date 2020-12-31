import React from 'react'

import PropTypes from 'prop-types';

import '../style/components/InvoiceResultsTable.css'

export default function InvoiceJsonResultsTable(props){
    return (
        <table className="styled-table">
            <thead>
                <tr>
                    <th>amount</th>
                    <th>category</th>
                    <th>day</th>
                    <th>installment</th>
                    <th>installment_amount</th>
                    <th>month</th>
                    <th>store</th>
                    <th>year</th>
                </tr>
            </thead>
            <tbody>
                {
                    props.invoices.map( invoice  => {
                    return (
                        <tr key={invoice.store}>
                            <td>{ invoice.amount} </td>
                            <td>{ invoice.category ? invoice.category : "-"} </td>
                            <td>{ invoice.day} </td>
                            <td>{ invoice.installment ? invoice.installment : "-"} </td>
                            <td>{ invoice.installment_amount ? invoice.installment_amount : "-"} </td>
                            <td>{ invoice.month} </td>
                            <td>{ invoice.store ? invoice.store : "-"} </td>
                            <td>{ invoice.year} </td>
                        </tr>
                        )
                    })
                }
            </tbody>
        </table>
    )
}

InvoiceJsonResultsTable.propTypes = {
    invoices: PropTypes.arrayOf(PropTypes.shape({
        amount: PropTypes.number.isRequired,
        category: PropTypes.string.isRequired,
        day: PropTypes.string.isRequired,
        installment: PropTypes.any,
        installment_amount: PropTypes.any,
        month: PropTypes.number.isRequired,
        store: PropTypes.string.isRequired,
        year: PropTypes.string.isRequired
    }))
};

InvoiceJsonResultsTable.defaultProps ={
    invoices: [{
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