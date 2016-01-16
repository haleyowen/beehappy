$(function(){
  $('.beehappy').keyup(function(e) {
    if(e.keyCode == 13) {
      var text = $(this).val();
      console.log(text);
    }
  });

  $('.bh-form').submit(function(event) {
    var form = event.target;
    var isInsult = true;
    var valList = [];
  
    for (var i = 0; i < form.length; i++) {
      if (form[i].className.indexOf("beehappy") > -1) {
        valList.push(form[i].value);
      }
    }

    var payload = JSON.stringify({messageList: valList});

    $.ajax("/bh-validate", {
      type: 'POST',
      contentType: 'application/json',
      data: payload, 
      success: function (data) {
        data = $.parseJSON(data);
        console.log(data);
      }
    });
    

    if (isInsult) {
      event.preventDefault();
    }
  });
});
