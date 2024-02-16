import React from 'react';
import'../style.css';

const Movie = props => {
    if (props.movie) {
        return(
            <div className='movie-wrapper animate'>
                <h2>{props.movie.Title}</h2>
                <p>{props.movie.Year}</p>
                <p className='plot'>{props.movie.Plot}</p>
                <div style={{display: 'flex', justifyContent: 'center', margin: '0'}}>
                    <img className='movie-poster' alt='movie' src={props.movie.Poster}></img>
                </div>
            </div>
        )
    }
    return null
}

export default Movie