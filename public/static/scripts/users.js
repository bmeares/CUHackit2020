function login() {
    username = $("#username").val();
    password = $("#password").val();

    $.ajax({
        type: 'POST',
        url: '/login_user',
        data: $('form').serialize(),
        success: function(data) {
          console.log(data);
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
          console.log(json);
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

function createGame() {
    $.ajax({
        type: 'POST',
        url: '/new_game',
        data: {game: "Trivia"},
        success: function(data) {
          json = JSON.parse(data);
          if (json.dest) window.location = json.dest;
          else if (json.message) alert(json.message);
        }
    })
}
