$(document).ready(function() {    
    $('#osm_checkbox1').checkbox({
        onChecked: function() {console.log('onChecked osm1');},
        onUnchecked: function() {console.log('onUnchecked osm1');}
    });
    
    $('#dg_checkbox1').checkbox({
        onChecked: function() {console.log('onChecked dg1');},
        onUnchecked: function() {console.log('onUnchecked dg1');}
    });
    
    $('#osm_checkbox2').checkbox({
        onChecked: function() {console.log('onChecked osm2');},
        onUnchecked: function() {console.log('onUnchecked osm2');}
    });
    
    $('#dg_checkbox2').checkbox({
        onChecked: function() {console.log('onChecked dg2');},
        onUnchecked: function() {console.log('onUnchecked dg2');}
    });
    
    $('#osm_checkbox1').checkbox('check');
    $('#dg_checkbox2').checkbox('check');
});