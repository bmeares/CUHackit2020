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
            // displays number of players in lobby
            if (data.waiting_for_players){
              $('#message').empty();
              $("#message").append("<h2>Game ID: " + data.key + "</h2><br><h2>Number of players: " + data.players + "</h2>");
              return
            }
            if (data.currentStage == currentStage){
              return;
            }
            else {
                currentStage = data.currentStage;
                $("#sub").empty();
              	$('#message').empty();
                $("#message").append(data.hostMessage);
                if (data.buttons) {
                    for (let i = 0; i < data.buttons.length; i++) {
                        $("#sub").append("<div class='choices' id='choice" + i + "'>" + data.buttons[i] + "</div>");
                    }
                }
                if (data.table) {
		    console.log(data.table);
                    $("#sub").append("<p class='details'>" + JSON.stringify(data.table) + "</p>");
                    $("#sub").append("<button id='gameBtn' onclick=\"send('exit')\">Exit</button>");
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
