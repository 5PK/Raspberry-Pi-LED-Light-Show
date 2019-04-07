function ajaxRequest(url) {
    var request = new XMLHttpRequest();
    request.open('GET', url);

    request.onload = function() {
        if (request.status === 200) {
            console.log('Response Text: ' + request.responseText);
            document.getElementById("message").innerHTML = "the " + url.slice(1) + " thread is active";
        } else {
            console.log('Request failed.  Returned status of: ' + request.status);
        }
    };
    request.send();
}


function songRequest(url) {

    var song = document.getElementById("songList").value;	
    
    console.log(url + song);	
	
    var request = new XMLHttpRequest();
    request.open('GET', url + song);

    request.onload = function() {
        if (request.status === 200) {
            console.log('Response Text: ' + request.responseText);
            document.getElementById("message").innerHTML = "the " + url.slice(1) + " thread is active";
        } else {
            console.log('Request failed.  Returned status of: ' + request.status);
        }
    };
    request.send();
}
