#!/usr/bin/node
const request = require('request');
const API_URL = 'https://swapi-api.hbtn.io/api';

if (process.argv.length < 3) {
  console.log('Please provide a movie ID as an argument');
  process.exit(1);
}

const movieId = process.argv[2];
const movieUrl = `${API_URL}/films/${movieId}/`;

const fetchCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (err, res, body) => {
      if (err) {
        return reject(err);
      }
      try {
        const character = JSON.parse(body);
        resolve(character.name);
      } catch (parseError) {
        reject(parseError);
      }
    });
  });
};

request(movieUrl, async (err, res, body) => {
  if (err) {
    return console.error('Request failed:', err);
  }

  if (res.statusCode !== 200) {
    return console.error('Failed to retrieve movie data:', res.statusCode);
  }

  try {
    const movieData = JSON.parse(body);
    const characterURLs = movieData.characters;

    const characterNamePromises = characterURLs.map(fetchCharacterName);

    const characterNames = await Promise.all(characterNamePromises);
    console.log(characterNames.join('\n'));
  } catch (parseError) {
    console.error('Failed to parse response:', parseError);
  }
});
