var imagePaths = []

function readReferenceURL(input,laneno) {
    var s = "#"+laneno
    localStorage.clear();
    console.log(s);
    if (input.files && input.files[0]) {
        var reader = new FileReader();

        reader.onload = function (e) {
            ele = document.querySelector(s).setAttribute('src', e.target.result)
        };

        reader.readAsDataURL(input.files[0]);
        localStorage.setItem("reference",input.files[0].path);
    }
}
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

    console.log(localStorage.getItem("reference"));
    imagePaths.unshift(localStorage.getItem("reference"));
    console.log(imagePaths);
    var size = imagePaths.length;
    let {PythonShell} = require('python-shell');
    var path = require("path");
    console.log("in method");
    console.log(size);
    if(size != 5){
        swal("Select images of all the lanes.");
        return;
    }
    swal({
        title: "Submitted",
        text: "Results are Loading",
        icon: "success",
      });
    var options = {
        scriptPath : path.join(__dirname, '/engine/'),
        args:imagePaths
    }
    let pyshell = new PythonShell('Cupcakes.py', options);

    var message = "";

    pyshell.on('message', function(msg) {
        //console.log(msg);
        message = message.concat(msg );
    });

    pyshell.end(function(err,code,signal) {
        console.log(message);
        // var resultsWindow  = window.open("results.html")
        localStorage.setItem("results",message);
        window.location.href = "results.html"
    });
}
function myFunction(e)
{
    var message = localStorage.getItem("results");
    document.getElementById("order").innerHTML = message;
}