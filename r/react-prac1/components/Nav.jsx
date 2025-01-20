import './nav.css';
import { Link } from 'react-router-dom';

function Nav(){

    return (
        <>
        <nav>
            <Link to='/' className='nav-logo'>You<span className="logo-span">Brand</span></Link>

            <div className="search
            "><input type="text" maxLength={30} placeholder='Search an item'/>
            <button type="button">Search</button>
            </div>

            <div className="nav-links">
                <Link to='/' className='nav-link'>Home</Link>
                <Link to='/cart' ><button>🛒</button></Link>
                <Link to='/contact' className='nav-link'>Contact</Link>
            </div>


        </nav>
        </>
    
    )
 
}

export default Nav;