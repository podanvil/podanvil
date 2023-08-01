// BEGIN TOGGLE DROPDOWN MENU
jQuery('.sshos-dropdown-menu-button').on('click', function(e) {
'use strict';
	e.preventDefault();
    /* dropdown menu button animation */
    jQuery('.sshos-dropdown-menu-button').toggleClass('sshos-dropdown-menu-button-active');
    /* toggle dropdown menu visibility */
    jQuery('.sshos-dropdown-menu-wrapper').toggleClass('sshos-dropdown-menu-wrapper-active');
});
// END TOGGLE DROPDOWN MENU


// BEGIN HIDE DROPDOWN MENU WHEN CLICKED OUTSIDE OF IT
jQuery(window).on('click touchstart', function(e) {
    /* hide accordion menu */
    jQuery('.sshos-dropdown-menu-button').removeClass('sshos-dropdown-menu-button-active');
    /* hide dropdown menu */
    jQuery('.sshos-dropdown-menu-wrapper').removeClass('sshos-dropdown-menu-wrapper-active');
});  
jQuery('.sshos-dropdown-menu-button, .sshos-dropdown-menu-wrapper').on('click touchstart', function(e) {
    event.stopPropagation();
});
// BEGIN HIDE DROPDOWN MENU WHEN CLICKED OUTSIDE OF IT