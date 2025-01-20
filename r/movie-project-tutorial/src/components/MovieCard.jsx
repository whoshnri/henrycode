import './MovieCard.css'

function Card({movie}){

function addToFav(){
     
}


return(
    <div className="movie-card">
        <div className="movie-poster"><img src={'https://image.tmdb.org/t/p/w500' + movie.poster_path
        } alt={movie.title + ' image'} /></div>

        <div className="movie-overlay">
            <button type="button" className='favorite-btn'  onClick={addToFav}>💛</button>
        </div>
        <div className="movie-info">
        <h3>{movie.title}</h3>
        <p>{movie.release_date}</p>
        </div>
    </div>



)



}

export default Card