$(document).ready(() => {
  const URL = 'https://swapi-api.hbtn.io/api/films/?format=json';
  $.get(URL, (data) => {
    data.results.forEach(element => {
      $('UL#list_movies').append('<li>' + element.title + '</li>');
    });
  });
});
