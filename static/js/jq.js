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

            if ($(this).attr('data-update') == 'false')
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
                                if (!send_button.parents('li').find('.fa-play').hasClass('fa-rotate-90'))
                                    send_button.parents('li').find('.fa-play').click();
                                send_button.parents('form').remove();
                            }
                            else
                                $('ul.parents').prepend(data.new_comment);
                        }
                    }
                });
            else
                $.ajax({
                    url: link,
                    data: {
                        csrfmiddlewaretoken: csrftoken,
                        text: text.val()
                    },
                    type: 'post',
                    success: function (data) {
                        $('#comment.commenting').remove();
                        send_button.removeAttr('disabled');
                        if (data.success == true){
                            $('.comment-text.update').html(data.new_text);
                            $('.comment-text').removeClass('update');
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

    $('body').on('click', 'a.update-comment', function (e) {
       $('#comment.commenting').remove();

       var update_form = $('#comment').clone(true, true);
       $(this).parent().after(update_form);
       update_form.addClass('commenting');
       var update_button = update_form.find('button');

       update_button.attr('data-update', 'true');
       update_button.html(update_button.attr('data-update-text'));
       update_button.attr('data-url', $(this).attr('data-url'));
       update_form.find('input').val($(this).parent().find('.comment-text').html());
       $(this).parent().find('.comment-text').addClass('update');
    });

    $('body').on('click', 'a.delete-comment', function (e) {
       var comment = $(this).parent().parent();

       if (!$(this).hasClass('in-process'))
       {
           $(this).addClass('in-process');
           $.ajax({
               url: $(this).data('url'),
               data: {
                   csrfmiddlewaretoken: csrftoken
               },
               type: 'post',
               success: function (data) {
                   if (data.success == true)
                       comment.slideUp();
                   $(this).removeClass('in-process');
               }
           });
       }

        e.preventDefault();
        e.stopPropagation();

    });

    $('body').on('click', '.fa-play', function (e) {
       $(this).toggleClass('fa-rotate-90');
       $(this).parent().parent().find('.children').first().slideToggle();
    });

});