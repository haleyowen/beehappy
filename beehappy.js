$(function(){
  $('.beehappy').keyup(function(e) {
    if(e.keyCode == 13) {
      var text = $(this).val();
      console.log(text);
    }
  });

  $('.bh-form').submit(function(event) {
    var form = event.target;
    for (var i = 0; i < form.length; i++) {
      if(form[i].class == "beehappy") {
        console.log(form[i]);
      }
    }
    event.preventDefault();
  });
});
