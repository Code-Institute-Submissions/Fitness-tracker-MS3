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