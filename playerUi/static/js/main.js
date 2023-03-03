$(document).ready(function () { 

    var player = $('#audio')[0];
    var p_bar = $('#progress-bar');

    $(".song-card").click(function () { 

        $("#rs-maximize").click();
        var songTitle = $(this).find(".card-title").text();
        var songFile = "media/audio/" + songTitle + ".mp3";

        $("#audio-source").attr("src", songFile);

        var rs = $("#right-sidebar");
        rs.find($("#rs-image")).attr("src",$(this).find("img").attr("src"));
        rs.find('p').text(songTitle);

        player.load();
        player.play();
        $("#play").hide();
        $("#pause").show();

    });

    $("#audio").on("timeupdate", function () {
        p_bar.attr("value", player.currentTime/player.duration);
        console.log(player.currentTime/player.duration);
    });

});