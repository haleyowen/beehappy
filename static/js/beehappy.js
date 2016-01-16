$(function(){
  $('.beehappy').keyup(function(e) {
    if(e.keyCode == 13) {
      var text = $(this).val();
      console.log(text);
    }
  });

  $('.bh-form').submit(function(event) {
    var form = event.target;
    var isInsult = false;

    for (var i = 0; i < form.length; i++) {
      if (form[i].className.indexOf("beehappy") > -1) {
        console.log(form[i]);
      }
    }

    if (isInsult) {
      event.preventDefault();
    }
  });
});
