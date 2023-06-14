$(document).ready(function() {
	$.ajax({
		    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
		    method: 'GET',
		    success: function(response) {
			    const listMoviesUl = $('#list_movies');
			    response.results.forEach(function(movie) {
				    const movieTitle = movie.title;
				    const listItem = $('<li>').text(movieTitle);
				    listMoviesUl.append(listItem);
			    });
		    },
		    error: function() {
			    console.log('Error');
		    }
	});
});
