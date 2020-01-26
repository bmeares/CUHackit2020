function login() {
    $.ajax({
        type: 'POST',
        url: '',
        data: $('form').serialize(),
        success: function(data) {
            console.log(data);
        }
    })
}

function register() {
    $.ajax({
        type: 'POST',
        url: '',
        data: $('form').serialize(),
        success: function(data) {
            console.log(data);
        }
    })
}
