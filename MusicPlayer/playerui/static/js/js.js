$(document).ready(function (){

    var rt_collapse = $("#recent-tab-collapse");
    var ft_collapse = $("#folder-tab-collapse");
    var st_collapse = $("#song-tab-collapse");
    var rt_expand = $("#recent-tab-expand");
    var ft_expand = $("#folder-tab-expand");
    var st_expand = $("#song-tab-expand");

    $("#recent-tab-expand, #folder-tab-expand, #song-tab-expand").hide();

    rt_collapse.click(function (){
        $("#recent-tab").hide();
        $("#recent-tab-expand").show();
        rt_collapse.hide();
    });
    ft_collapse.click(function (){
        $("#folder-tab").hide();
        ft_collapse.hide();
        $("#folder-tab-expand").show();
    });
    st_collapse.click(function (){
        $("#song-tab").hide();
        st_collapse.hide();
        $("#song-tab-expand").show();
    });

    rt_expand.click(function (){
        $("#recent-tab").show();
        $("#recent-tab-expand").hide();
        rt_collapse.show();
    });
    ft_expand.click(function (){
        $("#folder-tab").show();
        ft_collapse.show();
        $("#folder-tab-expand").hide();
    });
    st_expand.click(function (){
        $("#song-tab").show();
        st_collapse.show();
        $("#song-tab-expand").hide();
    });

    var rs_min = $("#rs-minimize");
    var rs_max = $("#rs-maximize");
    var rs = $("#right-sidebar");

    rs_min.click(function (){
        rs.hide();
        rs_max.show();
        rs_min.hide();
    });

    rs_max.click(function (){
        rs.show();
        rs_max.hide();
        rs_min.show();
    });

    var pause = $("#pause");
    var play = $("#play");
    var p_bar = $("#progress-bar");
    var player = $("#audio")[0];

    pause.css("display","none");
    play.click(function (){
        // $('.audio').prop("volume", 0.1);
        player.volume = 0.1;

        // $("#audio").trigger("play");
        player.play();
        
        p_bar.attr("max", player.duration);

        pause.show();
        play.hide();

    });

    pause.click(function (){
        player.pause();
        pause.hide();
        play.show();
        
    });

    $("#audio").on("timeupdate", function(){

        p_bar.attr("value",player.currentTime);
        console.log();
    });

});

