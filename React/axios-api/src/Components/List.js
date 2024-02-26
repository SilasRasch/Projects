import React, { Component } from 'react';
import axios from 'axios';
import'../style.css';

class List extends Component {
    constructor(props) {
        super(props)
        this.getMovies()
    }

    state = { movies: [] }

    onMovieSelect = (movie) => {
        this.props.movieSelected(movie)
    }

    render() {
        return(
            <div className='movie-list animate'>
                <h1 className='list-title'>{this.props.title}</h1>
                {this.state.movies.map(movie => { return <h4 className='list-element' 
                onClick={() => this.onMovieSelect(movie)} key={movie.Title}>{movie.Title} {movie.Year}</h4> })}
            </div>
        )
    }

    async getMovies() {
        const url = "https://api.themoviedb.org/3/discover/movie"
    
        var response = await axios.get(url, {
          headers: {
            accept: 'application/json',
            Authorization: 'Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4ZmEyYjhjNmQwMDQ4MTk3N2Y3NzI3OTk0YzJmYmM2ZCIsInN1YiI6IjY1Y2NiMDg3ZTIxMDIzMDE0N2MyYzkwOSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.BwFeu_3u5wBtENJBtc-0YqpRkuSl4bXhPW9ydCr0cp8'
          }
        })
        var data = await response.data
        console.log(data.results)
        
        var movies = []
        data.results.forEach(m => {
          var movie = {
            Title: m.title,
            Poster: "https://image.tmdb.org/t/p/original/" + m.poster_path,
            Plot: m.overview,
            Year: m.release_date.slice(0, 4)
          }
          movies.push(movie)
        })
        // console.log(movies)
        this.setState({movies: movies})
        return movies
      }
}

export default List