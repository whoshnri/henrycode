import { createContext, useContext , useState , useEffect } from "react";

const MovieContext = createContext();

export const useMovieContext = () => useContext(MovieContext)

export const MovieProvider = ({children}) => {  
    const [favourites , setFavourites] = useState([]);

    useEffect(() => {
        const storedFavs = JSON.parse(localStorage.getItem('favourites')) ;
        setFavourites(favs);
    },[])

    useEffect(() => {
        localStorage.setItem('favourites' , JSON.stringify(favourites))
    },[favourites])

    const addFavourite = (movie) => {
        setFavourites([...favourites , movie])
    }

    const removeFavourite = (movie) => {
        setFavourites(...favourites.filter(fav => fav.id !== movie.id))
    }

    const isFavourite = (movie) => {
        return favourites.some(fav => fav.id === movie.id)
    }

    return (
        <MovieContext.Provider>
            {children}
        </MovieContext.Provider>
    )



}












