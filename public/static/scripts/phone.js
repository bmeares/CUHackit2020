let currentStage = 0;
let nextStage = false;

function pull() {
    $.ajax({
        type: 'GET',
        url: '',
        success: function(data) {
            if (nextStage && data.currentStage == currentStage)
                return;
            else {
                currentStage = data.currentStage;
                $("#userIn").empty();
                $("#message").text("<p>" + data.message + "</p>");
                if ("input" in data) {
                    $("#userIn").append("<input type='text' id='inputText' placeholder='Your answer'>");
                    $("#userIn").append("<br>");
                    $("#userIn").append("<button onclick='send('inputText')'>Submit</button>");
                }
                if ("buttons" in data) {
                    for (let i = 0; i < data.buttons.length; i++) {
                        $("#userIn").append("<button id='button" + i + "' onclick='send(" + i + ")'>" + data.buttons[i] + "</button>");
                    }
                }
                if ("table" in data) {
                    $("#userIn").append("<p>" + data.table + "</p>");
                    $("#userIn").append("<button onclick='send('exit')'>Exit</button>");
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
        url: '',
        data: data,
        success: function(data) {
            nextStage = true;
        }
    })
}

function start() {
    setInterval(pull, 1000);
}
