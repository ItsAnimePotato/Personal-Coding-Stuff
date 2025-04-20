// Because this is a literal single page application
// we detect a callback from Spotify by checking for the hash fragment
import { redirectToAuthCodeFlow, getAccessToken } from "./authCodeWithPkce";
import { urlList } from "./smList";

const clientId = "205f326a865e4840ac5230dc7937a368";
const params = new URLSearchParams(window.location.search);
const code = params.get("code");

if (!code) {
  redirectToAuthCodeFlow(clientId);
} else {
  const accessToken = await getAccessToken(clientId, code);
  const pProfile = await fetchProfile(accessToken);
  populateUI(pProfile);
  const qProfile = await fetchQueue(accessToken);
  populateQueue(qProfile);
  populateTable(qProfile);
}

async function fetchProfile(code) {
  const result = await fetch("https://api.spotify.com/v1/me", {
    method: "GET",
    headers: { Authorization: `Bearer ${code}` },
  });

  return await result.json();
}

function populateUI(profile) {
  document.getElementById("displayName").innerText = profile.display_name;
  document.getElementById("avatar").setAttribute("src", profile.images[0].url);
  document.getElementById("id").innerText = profile.id;
  document.getElementById("email").innerText = profile.email;
  document.getElementById("uri").innerText = profile.uri;
  document
    .getElementById("uri")
    .setAttribute("href", profile.external_urls.spotify);
  document.getElementById("url").innerText = profile.href;
  document.getElementById("url").setAttribute("href", profile.href);
  document.getElementById("imgUrl").innerText = profile.images[0].url;
  document.getElementById("uri").innerText = profile.uri;

  //date and time of creation
  const now = new Date();
  const currentDateTime = now.toLocaleString();
  document.getElementById("dateTime").innerText = currentDateTime;
}

async function fetchQueue(code) {
  const result = await fetch("https://api.spotify.com/v1/me/player/queue", {
    method: "GET",
    headers: { Authorization: `Bearer ${code}` },
  });

  return await result.json();
}

function populateQueue(profile) {
  document.getElementById("currentSong").innerText =
    profile.currently_playing.name;
  document.getElementById("fullQueueLength").innerText = profile.queue.length;
  document.getElementById("nextSong").innerText = profile.queue[0].name;
}

function populateTable(profile) {
  let table = document.getElementById("tableBody");
  for (let i = 0; i < profile.queue.length; i++) {
    var song = profile.queue[i];
    var songName = song.name;
    var type = song.type;
    var person = "undefined";
    var songOfSM = false;

    if (type === "episode") {
      person = song.show.publisher;
    } else {
      var artistNames = song.artists.map((artist) => artist.name).join(", ");
      person = artistNames;
      songOfSM = smSong(song);
    }

    let row = `<tr>
      <td>${i + 1}</td>
      <td>${songName}</td>
      <td>${person}</td>
      <td>${songOfSM}</td>
      <td>${type}</td>
    </tr>`;
    table.innerHTML += row;
  }
}

function smSong(song) {
  for (let i = 0; i < song.artists.length; i++) {
    let artistURL = song.artists[i].external_urls.spotify;
    return areUrlsEqual(artistURL);
  }
}

function areUrlsEqual(artistURL) {
  return urlList.some((url) => url === artistURL);
}
