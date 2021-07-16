function test(room){
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
	};
	xhttp.open("GET", "change_release/"+room, true);
	xhttp.send();
}