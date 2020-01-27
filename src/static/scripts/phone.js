let currentStage = 0;
// let nextStage = false;
let submitted = false;

function pull() {
    $.ajax({
        type: 'GET',
        url: '/info',
        success: function(data) {
            if (data.waiting_for_players){
              $("#message").empty();
              $("#message").append('<h2>Number of Players: ' + data.players + "</h2>");
              return
            }

            if (data.currentStage == currentStage && submitted)
                return;
            else {
                submitted = false;
                currentStage = data.currentStage;
                $("#userIn").empty();
                $("#message").empty();
                $("#message").append("<h2>" + data.phoneMessage + "</h2>");
		if (data.quit) {
                    $("#userIn").append("<button class='userBtn' onclick=\"send('exit')\">End game</button>");
		    return
		}
                if (data.input) {
                    $("#userIn").append("<input type='text' id='inputText' placeholder='Your answer'>");
                    $("#userIn").append("<br>");
                    $("#userIn").append("<button class='userBtn' onclick=\"send('inputText')\">Submit</button>");
                }
                if (data.buttons) {
                    for (let i = 0; i < data.buttons.length; i++) {
                        $("#userIn").append("<button class='userBtn' id='button" + i + "' onclick='send(" + i + ")'>" + data.buttons[i] + "</button>");
                    }
                }
                if (data.table) {
                    $("#userIn").append("<p class='details'>" + JSON.stringify(data.table) + "</p>");
                    $("#userIn").append("<button class='userBtn' onclick=\"send('exit')\">Exit</button>");
                }
            }
        }
    })
}

function send(i) {
    let data = {};

    if (typeof i === "number") {
        data["buttonText"] = $("#button" + i).text();
    }
    else if (i === "inputText") {
        data["inputText"] = $("#inputText").val();
    }
    else if (i === "exit") {
        data["exit"] = true
    }
    $.ajax({
        type: 'POST',
        url: '/info',
        data: data,
        success: function(data) {
            // nextStage = true;
            submitted = true;
            $('userIn').empty();
            json = JSON.parse(data);
            if (json.dest) window.location = json.dest;
            else if (json.message) alert(json.message);
        }
    })
}

function start() {
    setInterval(pull, 1000);
}
