/**
 * Created by konstantin on 09.04.2017.
 */

function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
           var cookie = jQuery.trim(cookies[i]);
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
         }
      }
  }
return cookieValue;
}

var csrftoken = getCookie('csrftoken');

$(document).ready(function () {

    $('.add-comment').click(function (e) {
        var send_button = $(this);
        var link = $(this).data('url');
        var text = $(this).parent().find('input');
        if (text.val() != undefined && text.val() != ''){
            send_button.attr('disabled', 'disabled');

            $.ajax({
                url: link,
                data: {
                    csrfmiddlewaretoken: csrftoken,
                    text: text.val(),
                },
                type: 'post',
                success: function (data) {
                    text.val('');
                    send_button.removeAttr('disabled');
                    if (data.success == true){
                        $('ul.parents').prepend(data.new_comment);
                    }

                }
            });

            e.preventDefault();
            e.stopPropagation();
        }
    });
});