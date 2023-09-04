const API_KEY = '998767bc596baf03801aee2e9854a831';

function fetchWeatherData(location) {
  const apiUrl = `http://api.openweathermap.org/data/2.5/weather?q=${location}&units=metric&appid=${API_KEY}`;

  fetch(apiUrl)
    .then((data) => data.json())
    .then((jsonData) => {
      document.getElementById("text_location").innerHTML = jsonData.name;
      document.getElementById("text_location_country").innerHTML = jsonData.sys.country;
      document.getElementById("text_temp").innerHTML = Math.round(jsonData.main.temp);
      document.getElementById("text_feelslike").innerHTML = jsonData.main.feels_like;
      document.getElementById("text_desc").innerHTML = jsonData.weather[0].description;
    })
    const iconCode = jsonData.weather[0].icon;
    const iconUrl = 'http://openweathermap.org/img/w/${iconCode}.png';
    document.getElementById("icon").src = iconUrl;

}

const searchButton = document.getElementById("search-button");
searchButton.addEventListener("click", () => {
  const locationInput = document.getElementById("search-input").value;
  fetchWeatherData(locationInput);
});