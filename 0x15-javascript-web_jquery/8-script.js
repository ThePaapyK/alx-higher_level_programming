$.ajax({
	type: 'GET',
	url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
	success: function (movies) {
		for (let movie of movies.results) {
			$("#list_movies").append('<li>' + movie.title + '</li>');
		}
	}
});

