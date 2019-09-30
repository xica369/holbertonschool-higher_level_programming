// fetches and replaces the name
// of this URL: https://swapi.co/api/people/5/?format=json
// The name must be displayed in the HTML tag DIV#character

$.getJSON('https://swapi.co/api/people/5/?format=json', function (data) {
    $('DIV#character').html(data['name']);
  });
