// Tooltip
$('#example').tooltip(options)

// Wow.js
$(document).ready(function() {
    new WOW().init();
});

// Navigating to the contact section
$("#contact-link").click(function() {
    $('html, body').animate({
        scrollTop: $("#contact").offset().top - 100
    }, 2000);
    return false;
});