import {useNavigate} from "react-router-dom";
function NavBar(){

    let navigate = useNavigate();
    function routeChange(route){
        navigate(route);
    }

    return <>
        <nav className="navbar">
            <div onClick={() => routeChange('/')} className = "brand">
                <img />
                <h1>MiTaxes</h1>
            </div>
            <div className = "pages">
                <h2 onClick={() => routeChange('/calculate-taxes')}>Calculate Taxes</h2>
                <h2 onClick={() => routeChange('/about')}>About</h2>
                <h2 onClick={() => routeChange('/donate')}>Donate</h2>
            </div>
        </nav>
    </>
}

export default NavBar;
