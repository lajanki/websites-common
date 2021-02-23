// Show the hadoop section if url ends with "#hadoop".
if(window.location.hash == "#hadoop") {
    $('a[href="#hadoop"]').tab('show');
    $("#cowsay").css("display", "none");
}

// Custom handler to remove media from embedded timeline widgets.
// https://stackoverflow.com/questions/26731150/how-to-hide-images-from-embed-twitter-timeline/30357106
$('.photo').on('DOMSubtreeModified propertychange',"#twitter-widget-0", function() {
    $(".twitter-timeline").contents().find(".timeline-Tweet-media").css("display", "none");
    $(".twitter-block").css("height", "100%");

    // Hide the loaders
    $(".loader").css("display", "none");
    $("#little_youtube_card").css("display", "block");
    $("#quote_bot_card").css("display", "block");
});

// Start playing #descriptor_video on mouseover and enlarge on click
$("#descriptor_video").on("mouseover", function() {
    $("#descriptor_video")[0].play();
});
$("#descriptor_video").on("mouseout", function() {
    $("#descriptor_video")[0].pause();
});
$("#descriptor_video").on("click", function() {
    var current_width = $("#descriptor_video")[0].width;
    var new_width = 200;
    if (current_width != 600) {
        new_width = 600;
    }
    $("#descriptor_video")[0].width = new_width;
});

// Change knight-icon to animated version on mouseover
$("#chess-img").on("mouseover", function() {
    $("#chess-img").attr('src', './img/knight_fill_anim.gif');
});
$("#chess-img").on("mouseout", function() {
    $("#chess-img").attr('src', './img/knight_fill_static.png');
});

// Link date_profiler <div> (image) to the website
$("#date-profiler").on("click", function() {
    window.open("https://date-profiler-dot-webhost-common.appspot.com", "_blank");
});

// Make the "refresh" button in the #cowsay <div> to fetch a new thought from file and show
// a thought on page load.
$("#new-thought").on("click", getThought);
$(document).ready(getThought);

// Hide the #cowsay <div> when the "about" or "Hadoop" sections are opened.
$(".sub-page").on("click", function() { $("#cowsay").css("display", "none") });
// ...show it when "home" is clicked.
$("#home-button").on("click", function() { $("#cowsay").css("display", "block") });


// Make AJAX request to fetch a new showerthought from using /_cowsay route
function getThought() {
    $.ajax({
        url: "./_cowsay",
        success: function(response) {
            $("#cowsay-pre").html(response);
        },
    });
}
