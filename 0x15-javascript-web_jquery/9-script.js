$(document).ready(function() {
	$.ajax({
		url: 'https://fourtonfish.com/hellosalut/?lang=fr',
		method: 'GET',
		success: function(response) {
			const helloDiv = $('#hello');
			const translation = response.hello;
			helloDiv.text(translation);
		},
		error: function() {
			console.log(error);
		}
	});
});
