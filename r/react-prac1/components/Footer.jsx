import { Link } from "react-router-dom"
import './footer.css'


const Footer = () => {

    return(
        <>
        <footer>

        <div className="left">
        <Link to='/' className='footer-logo'>You<span className="logo-span">Brand</span></Link>

        <div className="copyright">Copyright &copy; YouBrand 2025</div>

        </div>

           <div className="get-in-touch">
            <h1>Get Notified On New Stuff!</h1>
            <div className="input">
                 <input type="text" placeholder="Email" className="text" />
                 <button className="send">Send</button>
            </div>
           </div>


        </footer>
        </>


    )


}

export default Footer