setTimeout(function(){
    var messages = document.querySelectorAll('#message');
    messages.forEach(function(message){
      message.style.display = 'none';
    });
  }, 8000);