import { useState } from 'react';

const CalculateTaxes = () => {
    const [addressInput, setAddressInput] = useState('');
    const [yearInput, setYearInput] = useState(new Date().getFullYear().valueOf())

    function calcTaxes(address, year){
        console.log(addressInput)
        console.log(yearInput)
        let url = 'http://localhost:5000/getAccountIncomeByYearEth/' + addressInput + '/' + yearInput;
        fetch(url)
        .then(response => {
            if(!response.ok){
                throw new Error(`HTTP error: ${response.status}`)
            }
            return response.json()
        })
        .then(response => {
            console.log(response)
        })
    }

    return (
        <>
            {/* 
                container, 
                need an input field
                need a year selection field
                the input field can be populated by the user
                or auto filled from metamask
                then just need a submit button
            */}
            <div className="calcTaxContainer">
                <h3 className="calcTaxHeader">
                        ETH Mining Income Tax
                </h3>
                <div className="calcTaxForm">
                    
                    <div className="addressForm">
                        <label>Wallet Address</label>
                        <input defaultValue={addressInput} onInput={e => setAddressInput(e.target.value)}/>
                    </div>
                    <div className="yearForm">
                        <label>Year</label>
                        <input type="number" min="2000" max="4000" defaultValue={yearInput} onInput={e => setYearInput(e.target.value)}/>
                    </div>
                    <div className="calcTaxSubmit">
                        <button className="calcTaxSubmitButton" onClick={() => calcTaxes()}>Submit</button>
                    </div>
                </div>
            </div>
        </>
    )
}

export default CalculateTaxes