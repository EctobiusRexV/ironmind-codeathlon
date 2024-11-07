$('#ul-buy-tickets-btn').click(function () {

    const api = '/api/';

    $.ajax({
        url: api + 'siegesItem',
        type: 'GET',
        success: function (data) {
            
        },
    });

    alert("Ticket commandé, merci de votre achat!")

    
});


$(document).ready(function () {
    const api = '/api/';

    $.ajax({
        url: api + 'items',
        type: 'GET',
        success: function (data) {
            console.log(data);
        },
    });
});