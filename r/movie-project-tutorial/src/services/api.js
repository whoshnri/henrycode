const API_KEY = "6f404741b9fd5c09247b0676b8847f0f";
const API_URL = "https://api.themoviedb.org/3";

export const getPoplarMovies = async () => {
    const response = await fetch(`${API_URL}/movie/popular?api_key=${API_KEY}`);
    const data = await response.json();
    console.log(data.results);
    return data.results;
}

export const searchMovies = async (query) => {
    const response = await fetch(`${API_URL}/search/movie?api_key=${API_KEY}&query=${encodeURIComponent(query)}`);
    const data = await response.json();
    return data.results;
}




