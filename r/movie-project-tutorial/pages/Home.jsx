import Card from '../src/components/MovieCard'
import { useState , useEffect } from 'react';
import './home.css'
import {searchMovies , getPoplarMovies} from '../src/services/api'

function Home(){

    const [movies , setMovies] = useState([]);
    const [error , setError] = useState(null);
    const [loading , setLoading] = useState(true);
    const [search, setSearch] = useState(''); // Added search state

    useEffect(() => {  
        const loadPopularMovies = async () => {
            try{
                const popularMovies = await getPoplarMovies(); // Fixed typo
                setMovies(popularMovies);
            }catch(error){
                console.log(error);
                setError('Failed to load movies');
            }finally{
                setLoading(false);
            }
        }
        loadPopularMovies();
     },[]);

    const handleSearch = async (e) =>{
        e.preventDefault();
       if (!search.trim()){
            return;
        }
        if(loading){
            return
        }
        setLoading(true);
        try{
            const searchResults = await searchMovies(search);
            setMovies(searchResults);
            setError(null);
        }catch (error){
            console.log(error);
            setError('Failed to load search results');
        }finally{
            setLoading(false);
        }
        // document.querySelector('.search-message').innerHTML = 'Search results for ' + search; // Fixed template literal
        setSearch('');
    }

    
    return (
        <> 
        <div className="home">
                <form onSubmit={handleSearch} className='search'>
                    <input type="text" placeholder='Search for movies....' className='search-input' value = {search} onChange={(e) => setSearch(e.target.value)}/>
                    <button type='submit' className='search-button'>Search</button>
                </form>
                <p className="search-message"></p>

            {error && <div className="error-message">{error}</div>}

            {loading ? (<div className="loading">Loading...</div>)
             : (<div className="movies-grid">
                {movies.map((movie) => 
               (<Card movie={movie} key={movie.id}/>))
            }
            </div> )}
            
            
            {/* the key is used as a unique identifier which is useful when mapping dynamically */}



        </div>
        </>

    )


}

export default Home