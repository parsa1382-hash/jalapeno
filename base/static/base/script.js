function test(room){
	var xhttp = new XMLHttpRequest();
	xhttp.onload = function() {
    	document.getElementById("demo").innerHTML = this.responseText;
    }
	xhttp.open("GET", "change_release/"+room, true);
	xhttp.send();
}
