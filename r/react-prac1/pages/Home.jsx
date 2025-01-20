import Card from '../components/card'
import './home.css'

const Home = () => {
    const items = [
        {img : '../assets/tee1.jpg', id: 1, rating: '4.4' , details : 'Adidas Slides' , price: 201.99},
        {img : '../assets/bg.jpg', id: 2, rating: '4.4' , details : 'Slides' , price: 23.99},
        {img : '../assets/bg.png', id: 3, rating: '4.4' , details : 'Adidas' , price: 31.99},
    ]
    

    return(
        <>
        <main className='content'>
            <div className='hero'></div>
            <section className="top-content">
                <div className="text-content">
                <h2>Wear your stories</h2>
                <p>Lorem ipsum dolor sit, amet <br />consectetur adipisicing <br/> elit. Libero veniam nobis molestiae.</p>
                <button className="cta">Check full Catalog</button>
                </div>
                <img className='hero-img' src="./assets/bg.png" alt="" />
            </section>
            <div className="divider">
                <h2>Itenerary</h2>
            </div>
            <section className="products">
            {items.map(item => <Card item={item} key={item.id} {...item} />)}
        </section>
        </main>
        
        
        
        </>


    )
}

export default Home