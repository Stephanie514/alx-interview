#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const baseUrl = 'https://swapi.dev/api';

function fetchAndPrintCharacters(movieId) {
  const movieUrl = `${baseUrl}/films/${movieId}/`;

  request(movieUrl, (error, response, body) => {
    if (error) {
      console.error('Error fetching the movie details:', error);
      return;
    }

    const movieDetails = JSON.parse(body);

    const characterUrls = movieDetails.characters;

    characterUrls.forEach((characterUrl) => {
      request(characterUrl, (error, response, body) => {
        if (error) {
          console.error('Error fetching the character details:', error);
          return;
        }

        const characterDetails = JSON.parse(body);

        console.log(characterDetails.name);
      });
    });
  });
}

fetchAndPrintCharacters(movieId);
