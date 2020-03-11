
var imagePaths = []
function readURL(input,laneno) {
    var s = "#"+laneno
    console.log(s);
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            ele = document.querySelector(s).setAttribute('src', e.target.result)
        };

        reader.readAsDataURL(input.files[0]);

        imagePaths.push(input.files[0].path);
    }
}

function something(e){
    var size = imagePaths.length;
    console.log(imagePaths);
    let {PythonShell} = require('python-shell');
    var path = require("path");
    console.log("in method");
    if(size != 5){
        swal("Select images of all the lanes.");
        return;
    }
    var options = {
        scriptPath : path.join(__dirname, '/engine/'),
        args:imagePaths
    }
    let pyshell = new PythonShell('Cupcakes.py', options);

    var message = "";

    pyshell.on('message', function(msg) {
        //console.log(msg);
        message = message.concat(msg + "<br/>");
    });

    pyshell.end(function(err,code,signal) {
        document.getElementById("order").innerHTML = message;
    });
}