$(document).ready(() => {
  const URL = 'https://swapi-api.hbtn.io/api/people/5/?format=json';
  $.get(URL, (data) => {
    $('DIV#character').html(data.name);
  });
});
