function login() {
    $.ajax({
        type: 'POST',
        url: '/login',
        data: $('form').serialize(),
        success: function(data) {
            console.log(data);
        }
    })
}

function register() {
    $.ajax({
        type: 'POST',
        url: '/register',
        data: $('form').serialize(),
        success: function(data) {
            console.log(data);
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
        }
    })
}
