// fetches and lists all movies title by using this URL
// All movie titles must be list in the HTML tag UL#list_movies
// with jQuery API

$.getJSON('https://swapi.co/api/films/?format=json', function (data) {
    data['results'].forEach(function (val) {
      $('<li>' + val.title + '</li>').appendTo('UL#list_movies');
    });    
  });
