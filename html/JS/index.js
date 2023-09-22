console.log("Hello")

async function logMovies() {
    const response = await fetch("http://127.0.0.1:8000/data");
    const movies = await response.json();
    console.log(movies);
}

logMovies();