$(document).ready(function() {
    let osm_polygons = osm_raw_polygons.map(function(arr) {return L.polygon(arr);});
    
    
    function add_osm_polygons(map){
        osm_polygons.forEach(function(current){
            current.addTo(map);
        });
    }
    
    function remove_osm_polygons(map)
    {
        osm_polygons.forEach(function(current){
            map.removeLayer(current);
        });
    }
    
    $('#osm_checkbox1').checkbox({
        onChecked: function() {console.log('onChecked osm1'); add_osm_polygons(osm_map);},
        onUnchecked: function() {console.log('onUnchecked osm1'); remove_osm_polygons(osm_map);}
    });
    
    $('#dg_checkbox1').checkbox({
        onChecked: function() {console.log('onChecked dg1');},
        onUnchecked: function() {console.log('onUnchecked dg1');}
    });
    
    $('#osm_checkbox2').checkbox({
        onChecked: function() {console.log('onChecked osm2'); add_osm_polygons(dg_map);},
        onUnchecked: function() {console.log('onUnchecked osm2'); remove_osm_polygons(osm_map);}
    });
    
    $('#dg_checkbox2').checkbox({
        onChecked: function() {console.log('onChecked dg2');},
        onUnchecked: function() {console.log('onUnchecked dg2');}
    });
    
    $('#osm_checkbox1').checkbox('check');
    $('#dg_checkbox2').checkbox('check');
});