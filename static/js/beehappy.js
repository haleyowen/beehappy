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
    contentType: "application/json",
    data: JSON.stringify({ "text": new_message }),
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

$(function(){
  get_messages();

  $('.beehappy').keyup(function(e) {
    if(e.keyCode == 13) {
      var text = $(this).val();
      console.log(text);
    }
  });

  $('.bh-form').submit(function(e) {
    var form = e.target;
    var isInsult = false;
    var valList = [];

    for (var i = 0; i < form.length; i++) {
      if (form[i].className.indexOf("beehappy") > -1) {
        valList.push(form[i].value);
      }
    }

    $.ajax("/bh-validate", {
      async: false,
      type: 'POST',
      contentType: 'application/json',
      data: JSON.stringify({messageList: valList}),
      success: function (data) {
        console.log("success");
        var message = $.parseJSON(data)["messages"];

        $.each(message, function (index, value) {
          console.log(value);
          isInsult |= value;
        });

        console.log(isInsult);

        if (isInsult) {
          alert("message blocked... too mean");
        }
      }
    });

    if (isInsult) {
      return false;
    }

    console.log("post away");
  });
});
