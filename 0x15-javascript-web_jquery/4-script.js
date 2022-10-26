$(document).ready(() => {
  $('DIV#toggle_header').click(() => {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else if ($('header').hasClass('red')) {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  });
});
