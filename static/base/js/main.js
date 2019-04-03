jQuery(document).ready(function(){
    var video = document.querySelector("#videoElement");
    
    if (navigator.mediaDevices.getUserMedia) {
      navigator.mediaDevices.getUserMedia({ video: true })
        .then(function (stream) {
            video.srcObject = stream;
        
            run()
        })
        .catch(function (err0r) {
          console.log("Something went wrong!");
        });
    }
});

function stop(e) {
    var stream = video.srcObject;
    var tracks = stream.getTracks();

    for (var i = 0; i < tracks.length; i++) {
        var track = tracks[i];
        track.stop();
    }

    video.srcObject = null;
}

function run(){
    var v = document.getElementById('videoElement');
    var canvas = document.getElementById('c');
    var context = canvas.getContext('2d');
    
    var cw = v.width;
    var ch = v.height;
    canvas.width = cw;
    canvas.height = ch;
    
    v.addEventListener('play', function(){ 
        record(this,context,cw,ch); 
    },false);
};

var _faces = [];

function record(v,c,w,h) {
    c.drawImage(v,0,0,w,h);    
    _faces.forEach(function (face) {
        draw(v,c,face);
    });
    setTimeout(record,20,v,c,w,h);
}

function draw(v,c,face) {
    var w = v.width;
    var h = v.height;
    var color = BASE_CONFIG['color'];
    var person = face.user.fullname;

    jQuery('#username_face').val(face.user.username);
    jQuery('#password_face').val(face.user.password);

    c.font = '16px Arial';    
    c.fillStyle = 'rgb('+ color[2] + ',' + color[1] + ',' + color[0]+')'; 
    c.strokeStyle = c.fillStyle;

    var x = face.rect[0]
    var y = face.rect[1]
    var w = face.rect[2]
    var h = face.rect[3]

    c.rect(x, y, w, h);
    c.stroke();
    c.fillText(person, x + (person.length - w/2), y - 10);
}

function success(response) {
    if (response) {
        _faces = [];
        response.faces.forEach(function (face, i) {
            _faces.push({
                rect: face,
                user: JSON.parse(response.users[i])
            })
        });
    }
}

function face_detector(image_src) {
    if (image_src){
        var url = "face_detector/";
        var data = {
            "url": image_src
        };
    
        $.ajax({
            type: "POST",
            url: url,
            data: data,
            success: success,
            dataType: "json"
        });
    }
}

function takePicture() {
    var video = document.getElementById('videoElement');
    var canvas = document.getElementById('c');
    var context = canvas.getContext('2d');
    
    canvas.width = video.width;
    canvas.height = video.height;
    context.drawImage(video, 0, 0, canvas.width, canvas.height);
    
    var data = canvas.toDataURL('image/png');
    photo.setAttribute('src', data); 
    
    face_detector(data);
 }

var closeDetect;
function dectect() {
    closeDetect = setInterval(takePicture, 1000);
    document.getElementById("btnLoginFace1").style.display = "none";
    document.getElementById("btnLoginFace2").style.display = "initial";
    document.getElementById("btnLoginFace3").style.display = "initial";
}

function stop() {
    clearInterval(closeDetect);
}