#!/usr/bin/node
const request = require('request');

function requestPromise(url) {
    return new Promise((resolve, reject) => {
        request(url, (err, response, body) => {
            if (err)
                reject(err);
            else
                resolve({ response, body });
        });
    });
}

async function getCharacters(movieId) {
    try {
        const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;
        const movieResponse = await requestPromise(url);
        const movieData = JSON.parse(movieResponse.body);

        for (const characterUrl of movieData.characters) {
            const characterResponse = await requestPromise(characterUrl);
            const characterData = JSON.parse(characterResponse.body);
            console.log(`${characterData.name}`);
        }
    } catch (err) {
        console.error('Error:', err);
    }
}

const args = process.argv.slice(2);
const movieId = args[0];
getCharacters(movieId);
