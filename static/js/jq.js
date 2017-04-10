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
        var parent = $(this).data('parent');

        if (text.val() != undefined && text.val() != ''){
            send_button.attr('disabled', 'disabled');

            $.ajax({
                url: link,
                data: {
                    csrfmiddlewaretoken: csrftoken,
                    text: text.val(),
                    parent: parent
                },
                type: 'post',
                success: function (data) {
                    text.val('');
                    send_button.removeAttr('disabled');
                    if (data.success == true){
                        if (data.parent == false){
                            send_button.parents('form').parent().append(data.new_comment);
                            send_button.parents('form').remove();
                        }
                        else
                            $('ul.parents').prepend(data.new_comment);
                    }
                }
            });

            e.preventDefault();
            e.stopPropagation();
        }
    });

    $('body').on('click', 'a.add-child', function (e) {
        $('#comment.commenting').remove();

        var new_form = $('#comment').clone(true, true);
        $(this).parent().after(new_form);
        new_form.addClass('commenting');
        new_form.find('button').attr('data-parent', $(this).data('parent'));
    });

});