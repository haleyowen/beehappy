$(function(){
  $("#post_button").click(function() {
    post_message();
  });

  get_messages();

  function get_messages() {
    $.ajax({
      url: "/messages",
      dataType: "json",
      success: function (data) {
        update_message_list(data);
      }
    });
  }

  function post_message() {
    var new_message = $("#post_message").val();

    $.ajax({
      url: "/messages",
      type: "POST",
      dataType: "json",
      data: { "text": new_message },
      success: function (data) {
        get_messages();
      }
    });
  }

  function update_message_list(message_data) {
    $("#message_list").html("");
    $.each(message_data, function(index, value) {
      $("#message_list").append("<li>" + value.text + "</li>");
    });
  }

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
