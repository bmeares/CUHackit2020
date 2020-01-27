function login() {
    username = $("#username").val();
    password = $("#password").val();

    $.ajax({
        type: 'POST',
        url: '/login_user',
        data: $('form').serialize(),
        success: function(data) {
          json = JSON.parse(data);
          if (json.dest) window.location = json.dest;
          else if (json.message) alert(json.message);
          else console.log(json);
        }
    })
}

function register() {
    $.ajax({
        type: 'POST',
        url: '/register_user',
        data: $('form').serialize(),
        success: function(data) {
          json = JSON.parse(data);
          if (json.dest) window.location = json.dest;
          else if (json.message) alert(json.message);
        }
    })
}

function joinGame() {
    $.ajax({
        type: 'POST',
        url: '/join_game',
        data: $('form').serialize(),
        success: function(data) {
          json = JSON.parse(data);
          if (json.dest) window.location = json.dest;
          else if (json.message) alert(json.message);
        }
    })
}

function createGame(i) {
    let data = {game: "HackerFall", numRounds: 0}

    if(i == 0) {
      data = {game: "Trivia", numRounds: $("#numRounds").val()}
    }

    $.ajax({
        type: 'POST',
        url: '/new_game',
        data: data,
        success: function(data) {
          json = JSON.parse(data);
          if (json.dest) window.location = json.dest;
          else if (json.message) alert(json.message);
        }
    })
}
