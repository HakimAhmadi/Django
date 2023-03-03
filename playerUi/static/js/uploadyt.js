$(document).ready(function() {

    $("#rs-minimize").click();
    $("#video_info").hide();


    $("#ytdownload").click(function (){
        $("#loading_icon").show();
    });
    
    $('#ytsubmit').click( function(event) {

        event.preventDefault();

        var url = $('#ytlink').val();

        var video_id = url.split("=")[1];

        $.getJSON("https://www.googleapis.com/youtube/v3/videos", {
            part: "snippet",
            id: video_id,
            key: "AIzaSyBpuUv5Xa-HxaYEJZRXAVdi9yl1gbbPIzo"

        }, function(data) {
            var video = data.items[0];

            var title = video.snippet.title;
            var release_date = video.snippet.publishedAt.slice(0, 10);
            var thumbnail_url = "https://img.youtube.com/vi/" + video.id + "/sddefault.jpg"
            var video_url = "https://www.youtube.com/watch?v=" + video.id;
            
            // console.log(title,release_date,thumbnail_url,video_url);

            $("#video_info").show();
            $("#title").val(title);
            $("#release_date").val(release_date);
            $("#thumbnail_url").attr("src",thumbnail_url);
            $("#video_url").val(video_url);

        });


        // $.ajax({
        //     type: 'POST',
        //     url: 'loadytfile',
        //     headers: {
        //         'X-CSRFToken': $('input[name="csrfmiddlewaretoken"]').val()
        //       },
        //     data: { 'url': url },
        //     success: function (response) {
        //         $("#video_info").show();
        //         $("#title").val(response.title);
        //         $("#release_date").val(response.release_date);
        //         $("#thumbnail_url").attr("src",response.thumbnail_url);
        //         $("#video_url").text(response.video_url);
        //         console.log(response.thumbnail_url);
                
        //     },
        //     error: function(response) {
        //         $('#video-info').html('<p>Error: ' + response.error + '</p>');
        //     }
        // });
    });

});

