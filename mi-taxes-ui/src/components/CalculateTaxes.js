const CalculateTaxes = () => {
    function calcTaxes(){
        fetch('http://localhost:5000/getAccountIncomeByYearEth/0xc40064b67833b8a3ae28eb2ba3fcaadd88f17e4b/2021')
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
            <button onClick={calcTaxes}>Skippa Da Clicka</button>>
        </>
    )
}

export default CalculateTaxes