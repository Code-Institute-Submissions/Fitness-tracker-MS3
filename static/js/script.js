/*
    jQuery for MaterializeCSS initialization
*/

$(document).ready(function() {
    $(".sidenav").sidenav({ edge: "right" });
    $('.datepicker').datepicker({
        format: "dd mmmm, yyyy",
        yearRange: 4,
        showClearBtn: true,
        i18n: {
            done: "Select"
        }
    });

    $('select').formSelect();
    $('#textarea1').val('New Text');
    M.textareaAutoResize($('#textarea1'));
});


/*
    image random generator
*/
var images = ["workout1.jpg", "workout2.jpg", "workout3.jpg", "workout4.jpg", "workout5.jpg", "workout6.jpg"]

function chose() {
    var rand = Math.floor(Math.random() * images.length);
    document.getElementByClassName("card-image").src = "static/images/" + images[rand];
}