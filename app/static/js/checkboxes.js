$(document).ready(function() {
    $('#osm_checkbox').checkbox({
        onChecked: function() {console.log('onChecked osm');},
        onUnchecked: function() {console.log('onUnchecked osm');}
    });
    
    $('#l8_checkbox').checkbox({
        onChecked: function() {console.log('onChecked l8');},
        onUnchecked: function() {console.log('onUnchecked l8');}
    });
});