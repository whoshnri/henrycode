import {Link} from 'react-router-dom';
import './navbar.css'

function Nav(){
    return (
        <nav>
            <div>
                <Link to='/' className='nav-logo'>Movie App</Link>
            </div>

            <div className="nav-links">
                <Link to='/' className='nav-link'>Home</Link>
                <Link to='/favourites' className='nav-link'>Favourites</Link>
            </div>


        </nav>
    )
}

export default Nav