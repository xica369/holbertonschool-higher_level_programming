// fetches from https://fourtonfish.com/hellosalut/?lang=fr
// and displays the value of hello from that fetch in the HTML’s tag DIV#hello

$(document).ready(function () {
  $.getJSON('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
    $('DIV#hello').html(data['hello']);
  });
});
