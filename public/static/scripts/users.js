function login() {
    username = $("#username").val();
    password = $("#password").val();

    $.ajax({
        type: 'POST',
        url: '/login_user',
        data: $('form').serialize(),
        // data:{
          // username: username,
          // password: password
        // },
        success: function(data) {
            // console.log(data);
          window.location = data;
        }
    })
}

function register() {
    $.ajax({
        type: 'POST',
        url: '/register_user',
        data: $('form').serialize(),
        success: function(data) {
            console.log(data);
          window.location = data;
        }
    })
}

function joinGame() {
    $.ajax({
        type: 'POST',
        url: '/join_game',
        data: $('form').serialize(),
        success: function(data) {
            console.log(data);
          window.location = data;
        }
    })
}

function createGame() {
    $.ajax({
        type: 'POST',
        url: '/new_game',
        data: {game: "Trivia"},
        success: function(data) {
            console.log(data);
          console.log('oy m8');
          window.location = data;
        }
    })
}
