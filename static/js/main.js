import WebFont from 'webfontloader';

require('materialize-css');

WebFont.load({
  google: {
    families: ['Material Icons'],
  },
});

$(() => {
  $('.dropdown-trigger').dropdown({ hover: false });
}); // end of document ready
