#!/usr/bin/node

const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieID = process.argv[2];
const filmEndpoint = `https://swapi.dev/api/films/${movieID}/`;

// fetches and print character names
function fetchCharacterNames (characterURLs) {
  const characterPromises = characterURLs.map(url => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) {
          return reject(error);
        }
        if (response.statusCode !== 200) {
          return reject(new Error(`Error: Unable to fetch data (status code: ${response.statusCode})`));
        }
        const character = JSON.parse(body);
        resolve(character.name);
      });
    });
  });

  Promise.all(characterPromises)
    .then(names => {
      names.forEach(name => console.log(name));
    })
    .catch(error => {
      console.error(error);
    });
}

function fetchMovieDetails (movieID) {
  request(filmEndpoint, (error, response, body) => {
    if (error) {
      console.error(error);
      return;
    }
    if (response.statusCode !== 200) {
      console.error(new Error(`Error: Unable to fetch data (status code: ${response.statusCode})`));
      return;
    }

    const film = JSON.parse(body);
    const characterURLs = film.characters;
    fetchCharacterNames(characterURLs);
  });
}

fetchMovieDetails(movieID);
