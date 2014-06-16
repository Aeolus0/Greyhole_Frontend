$(document).ready(function(){
    var socket = io.connect('http://' + document.domain + ':' + location.port + '/stats_and_logs');
    socket.on('logs_resp', function(msg) {
        $('#logs_resp').append('<p>Received: ' + msg.data + '</p>');
    });
    socket.on('work_queue_resp', function(msg) {
        $('#work_queue_resp').append('<p>Received: ' + msg.data + '</p>');
    });
    socket.on('iostat_resp', function(msg) {
        $('#iostat_resp').append('<p>Received: ' + msg.data + '</p>');
    });
    socket.on('raw_usage_resp', function(msg) {
        $('#raw_usage_resp').append('<p>Received: ' + msg.data + '</p>');
    });
    $('form#emit').submit(function(event) {
        socket.emit('my event', {data: $('#emit_data').val()});
        return false;
    });
    $('form#broadcast').submit(function(event) {
        socket.emit('my broadcast event', {data: $('#broadcast_data').val()});
        return false;
    });
});