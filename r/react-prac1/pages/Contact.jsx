
import './contact.css'



function Contact(){

    function mailout(){

    }

    return(
        <>

        <div className="main">

            <img src="../assets/contact.jpg" alt="" />
            

            <form action="get">
                <h2>Reach Out To Us</h2>
                <div className="names">
                    <input type="text" placeholder='Firstname' className="firstname" />
                    <input type="text"name="lastname" className="lastname" placeholder='Lastname' />
                </div>
                
                <input placeholder='Emial' type="text" className="email-addr" />
                <textarea type="text" placeholder='Your message goes here......' max-length='200' rows='8' className="mail-message" />
                <button type="button" className='form-button' onClick={mailout}><img height='20px' src="../assets/send.svg" alt="" /></button>

            </form>


        </div>
        
        
        
        
        
        </>

    )




}

export default Contact