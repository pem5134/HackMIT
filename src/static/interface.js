// $.getJson("https://bitcoin.toshi.io/api/v0/addresses/1AeZL1f5YSDo6bhMcinuU3xFZgVjffYyPQ/transactions", function( data ) {
//         var trans = data["transactions"][0]["outputs"][0]["addresses"][0];
//         document.querySelector('transaction').innerHTML = trans;
//       })

function on_request_success(response) {
	var data = JSON.parse(response);
	console.log(response);
	console.log(data[0][0][1]);
}

$.ajax({
	url: "http://localhost:5000/data",
	type: 'GET',
	cache: false,
	success: on_request_success
}
);