var socket = io.connect('http://' + document.domain + ':' + location.port);

socket.on( 'connect', function() {
  socket.emit( 'my event', {
    data: 'User Connected'
  } )
  var form = $( 'form' ).on( 'submit', function( e ) {
    e.preventDefault()
    let user_name = $( '.user_name' ).val()
    let user_input = $( '.chat_input' ).val()
    socket.emit( 'my event', {
      user_name : user_name,
      message : user_input
    } )
    $( '.chat_input' ).val( '' ).focus()
  } )
} )
socket.on( 'my response', function( msg ) {

  if( typeof msg.user_name !== 'undefined' ) {
    var now = new Date(Date.now());
    var formatted = now.getHours() + ":" + now.getMinutes();
    $( '#messages' ).append( `  <p class="mb-3">${formatted} <b class="username">${msg.user_name}</b> <i class="message">${msg.message}</i></p>
    <hr>` )
    var $chat = $("#messages");
    $chat.scrollTop($chat[0].scrollHeight);

  }
})