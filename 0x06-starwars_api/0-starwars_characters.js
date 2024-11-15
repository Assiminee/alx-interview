#!/usr/bin/node
const request = require('request');

function getCharacters(movieId) {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request(url, (err, response, body) => {
        if (err) {
            console.error('Error fetching movie:', err);
            return;
        }

        if (response.statusCode !== 200) {
            console.error(`Failed to retrieve movie data: ${response.statusCode}`);
            return;
        }

        const movieData = JSON.parse(body);

        movieData.characters.forEach(characterUrl => {
            request(characterUrl, (err, response, body) => {
                if (err) {
                    console.error('Error fetching character:', err);
                    return;
                }

                if (response.statusCode !== 200) {
                    console.error(`Failed to retrieve character data: ${response.statusCode}`);
                    return;
                }

                const characterData = JSON.parse(body);
                console.log(characterData.name);
            });
        });
    });
}

const args = process.argv.slice(2);
if (args.length !== 1) {
    console.log("Usage: node starwars_characters.js <movie_id>");
} else {
    const movieId = args[0];
    getCharacters(movieId);
}
