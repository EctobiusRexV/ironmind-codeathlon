$('#ul-buy-tickets-btn').click(function () {
    alert('Le bouton fonctionne')
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