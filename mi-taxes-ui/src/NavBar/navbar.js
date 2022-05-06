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
                <h1>
                    <a href="/">MiTaxes</a>
                </h1>
            </div>
            <div className = "pages">
                <h2 onClick={() => routeChange('/calculate-taxes')}>
                    <a href="/calculate-taxes">Calculate Taxes</a>
                </h2>
                <h2 onClick={() => routeChange('/about')}>
                    <a href="/about">About</a>
                </h2>
                <h2 onClick={() => routeChange('/donate')}>
                    <a href="/donate">Donate</a>
                </h2>
            </div>
        </nav>
    </>
}

export default NavBar;
