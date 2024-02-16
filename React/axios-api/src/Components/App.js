import React, { Component } from 'react';
import List from './List';
import Movie from './Movie';
import '../style.css'

class App extends Component {
  state = { selectedMovie: null, movies: null }

  movieSelectCallback = (movie) => {
    this.setState({selectedMovie: movie})
  }

  render() {
    return (
    <div>
      <h1 className='title'>Nyetflix</h1>
      {/* <button onClick={ this.getMovies }>Click me!</button> */}
      <div style={{display: 'flex'}}>
        <List title="My movies" movieSelected={this.movieSelectCallback} />
        <Movie movie={this.state.selectedMovie}/>
      </div>
      <p></p>
    </div>
    )
  }
}

export default App;