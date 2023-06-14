$(document).ready(function() {
	$.ajax({
		url: 'https://swapi-api.alx-tools.com/api/people/5/?format=json',
		method: 'GET',
		success: function(response) {
			const charaDiv = $('#character');
			const characterName = response.name;
			charaDiv.text(characterName);
		},
		error: function() {
			console.log(error);
		}
		});
});
