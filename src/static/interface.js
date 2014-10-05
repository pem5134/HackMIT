// $.getJson("https://bitcoin.toshi.io/api/v0/addresses/1AeZL1f5YSDo6bhMcinuU3xFZgVjffYyPQ/transactions", function( data ) {
//         var trans = data["transactions"][0]["outputs"][0]["addresses"][0];
//         document.querySelector('transaction').innerHTML = trans;
//       })

function on_request_success(response) {
	var data = JSON.parse(response);
	console.log(data)
	//console.log(response);
	//console.log(data["transactions"][0]["outputs"][0]["addresses"][0]);
}

$.ajax({
	url: "http://localhost:5000/data",
	type: 'GET',
	cache: false,
	success: on_request_success
}
);

function makeTree(data) {
	window.open('http://localhost:5000/tree.html');
}

function createGraph(address) {
	$.ajax({
		dataType: "json",
		url: 'http://localhost:5000/_getData',
		data: {word: address},
		success: makeTree
	});
}

function sendToPython(list) {
	$.getJSON('http://localhost:5000/_array2python', {
        wordlist: JSON.stringify(list)
    }, function(data){
        console.log(data.result)
        $( "#result" ).text(data.result);
    });
}
