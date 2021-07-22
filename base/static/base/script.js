function test(room){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	};
	xhttp.open("GET", "change_release/"+room, true);
	xhttp.send();
}

//127.0.0.1:8000/change_release/1