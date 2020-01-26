let currentStage = 0;

function send(action){
  $.ajax({
    type: 'POST',
    url: '/info',
    data: {'exit': true},
    success: function(data){
      console.log(data);
      json = JSON.parse(data);
      if (json.dest) window.location = json.dest;
      else if (json.message) alert(json.message);
    }
  });
}

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
                    $("#sub").append("<button onclick=\"send('exit')\">Exit</button>");
                }
            }
        }
    })
}

function start() {
    setInterval(pull, 1000);
}

function begin_game(){
  $.ajax({
    type: 'POST',
    url: "/info",
    data: {},
  });
}
