$(document).ready(function() {    
    $('#osm_checkbox').checkbox({
        onChecked: function() {console.log('onChecked osm');},
        onUnchecked: function() {console.log('onUnchecked osm');}
    });
    
    $('#dg_checkbox').checkbox({
        onChecked: function() {console.log('onChecked dg');},
        onUnchecked: function() {console.log('onUnchecked dg');}
    });
    
    $('#osm_checkbox').checkbox('check');
    $('#dg_checkbox').checkbox('check');
});