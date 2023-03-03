$(document).ready(function (){

    var rt_collapse = $("#recent-tab-collapse");
    var ft_collapse = $("#folder-tab-collapse");
    var st_collapse = $("#song-tab-collapse");
    var rt_expand = $("#recent-tab-expand");
    var ft_expand = $("#folder-tab-expand");
    var st_expand = $("#song-tab-expand");

    $("#recent-tab-expand, #folder-tab-expand, #song-tab-expand").hide();

    function hide(hide_list){
        for (var i = 0; i < hide_list.length; i++){
            console.log(hide_list[i]);
            $(hide_list[i]).hide();
        }
    }
    function show(show_list){
        for (var i = 0; i < show_list.length; i++){
            console.log(show_list[i]);
            $(show_list[i]).show();
        }
    }

    rt_collapse.click(function (){
        hide(["#recent-tab",rt_collapse]);
        show(["#recent-tab-expand"]);
    });
    ft_collapse.click(function (){
        hide(["#folder-tab",ft_collapse]);
        show(["#folder-tab-expand"]);
    });
    st_collapse.click(function (){
        hide(["#song-tab",st_collapse]);
        show(["#song-tab-expand"]);
    });

    rt_expand.click(function (){
         
        hide(["#recent-tab-expand"]);
        show(["#recent-tab",rt_collapse]); 
    });
    ft_expand.click(function (){
        hide(["#folder-tab-expand"]);
        show(["#folder-tab",ft_collapse]); 
    });
    st_expand.click(function (){
        hide(["#song-tab-expand"]);
        show(["#song-tab",st_collapse]); 
    });

    var rs_min = $("#rs-minimize");
    var rs_max = $("#rs-maximize");
    var rs = $("#right-sidebar");

    rs_min.click(function (){
        hide([]);
        show([]);
        hide([rs,rs_min]);
        show([rs_max]);
    });

    rs_max.click(function (){
        hide([rs_max]);
        show([rs,rs_min]);
    });

    var pause = $("#pause");
    var play = $("#play");
    var p_bar = $("#progress-bar");
    var player = $("#audio")[0];

    pause.css("display","none");
    play.click(function (){
        // $('.audio').prop("volume", 0.1);
        // player.volume = 0.1;

        // $("#audio").trigger("play");
        player.play();

        pause.show();
        play.hide();

    });

    pause.click(function (){
        player.pause();
        pause.hide();
        play.show();
            
    });

    $("#audio").on("timeupdate", function(){

        p_bar.attr("value", player.currentTime/player.duration);
    });


});

