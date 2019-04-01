var http = require('http');
var express = require('express');
var app = express();


app.get('/', function(req, res) {
	res.send('Hello Mohawk\n');
});


app.get('/music'), function(req,res){
	// Get Music List
	console.log("get list of music");

	res.send('[{"id":1, "title":"Oh Canada"},{"id":2, "title":"test"}]');
});

app.get('/music/:title'), function(req, res){

	//Get /music/Oh Canada
	console.log(req.params.name)

	// => Oh canada
	
	res.send('{"id":1, "title":"' + req.params.name + '"}');
});

app.get('/test'), function(req, res){

	const spawn = require("child_process").spawn;
	const pythonProcess = spawn('python', ["./lightShowEngine/test.py"]);


	/*
	pythonProcess.stdout.on('data', (data) => {
		res.send('{"message":""}');
	});
	*/

	res.send('{"message":"python script success"}');
});


app.listen(6969);

console.log('Listening on port 6969....');
