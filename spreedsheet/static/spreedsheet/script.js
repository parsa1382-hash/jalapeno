function showfunc(el) {
	document.getElementById(el).style.display = "block";
}

function hidefunc(el) {
	document.getElementById(el).style.display = "none";
	document.getElementById(el).reset();
}

function task(el, task_id, group, task_form_id){
	var xhttp = new XMLHttpRequest();
	xhttp.onload = function() {
    	document.getElementById(task_form_id).innerHTML = this.responseText;
    }
	xhttp.open("GET", "/spreedsheet/task_edit_html/" + group + "/" + task_id + "/" + task_form_id, true);
	xhttp.send();
	document.getElementById(task_form_id).style.display = "block";
}