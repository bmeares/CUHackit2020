let currentStage = 0;
let nextStage = false;

function pull() {
    $.ajax({
        type: 'GET',
        url: '/info',
        success: function(data) {
            if (data.waiting_for_players){
              $("#message").text('Number of Players: ' + data.players);
              return
            }

            if (nextStage && data.currentStage == currentStage)
                return;
            else {
                currentStage = data.currentStage;
                $("#userIn").empty();
                $("#message").text(data.message);
                if (data.input) {
                    $("#userIn").append("<input type='text' id='inputText' placeholder='Your answer'>");
                    $("#userIn").append("<br>");
                    $("#userIn").append("<button onclick=\"send('inputText')\">Submit</button>");
                }
                if (data.buttons) {
                    for (let i = 0; i < data.buttons.length; i++) {
                        $("#userIn").append("<button id='button" + i + "' onclick='send(" + i + ")'>" + data.buttons[i] + "</button>");
                    }
                }
                if (data.table) {
                    $("#userIn").append("<p>" + JSON.stringify(data.table) + "</p>");
                    $("#userIn").append("<button onclick=\"send('exit')\">Exit</button>");
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
            nextStage = true;
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
