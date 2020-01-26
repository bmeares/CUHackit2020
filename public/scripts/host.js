let currentStage = 0;

function pull() {
    $.ajax({
        type: 'GET',
        url: '',
        success: function(data) {
            if (data.currentStage == currentStage)
                return;
            else {
                currentStage = data.currentStage;
                $("#sub").empty();
                $("#message").text("<p>" + data.message + "</p>");
                if ("buttons" in data) {
                    for (let i = 0; i < data.buttons.length; i++) {
                        $("#sub").append("<div id='choice" + i "'>" + data.buttons[i] + "</div>");
                    }
                }
                if ("table" in data) {
                    $("#sub").append("<p>" + data.table + "</p>");
                    $("#sub").append("<button onclick='send('exit')'>Exit</button>");
                }
            }
        }
    })
}

function start() {
    setInterval(pull, 1000);
}
