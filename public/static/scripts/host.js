let currentStage = 0;

function pull() {
    $.ajax({
        type: 'GET',
        url: '/info',
        success: function(data) {
            if (data.waiting_for_players){
              $("#message").text(data.key);
              return
            }
            if (data.currentStage == currentStage){
              return;
            }
            else {
                currentStage = data.currentStage;
                $("#sub").empty();
                $("#message").text(data.message);
                if (data.buttons) {
                    for (let i = 0; i < data.buttons.length; i++) {
                        $("#sub").append("<div id='choice" + i + "'>" + data.buttons[i] + "</div>");
                    }
                }
                if (data.table) {
                    $("#sub").append("<p>" + data.table + "</p>");
                    $("#sub").append("<button onclick='send('exit')'>Exit</button>");
                }
            }
        }
    })
}

function start() {
    console.log('mafia2');
    setInterval(pull, 1000);
}
