$(document).ready(() => {
  const URL = 'https://fourtonfish.com/hellosalut/?lang=fr';
  $.get(URL, (data) => {
    $('DIV#hello').html(data.hello);
  });
});
