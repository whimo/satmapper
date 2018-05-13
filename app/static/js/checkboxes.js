$(document).ready(function() {
    let osm_map_osm_polygons = osm_raw_polygons.map(function(arr) {return L.polygon(arr);});
    let dg_map_osm_polygons = osm_raw_polygons.map(function(arr) {return L.polygon(arr);});
    let osm_map_points = dg_raw_polygons.map(function(arr) {return L.circle(arr, {radius: 1});});
    let dg_map_points = dg_raw_polygons.map(function(arr) {return L.circle(arr, {radius: 1});});
    
    
    function add_polygons(polygons, map){
        polygons.forEach(function(current){
            current.addTo(map);
        });
    }
    
    function remove_polygons(polygons, map)
    {
        polygons.forEach(function(current){
            if (current)
                map.removeLayer(current);
        });
    }
    
    $('#osm_checkbox1').checkbox({
        onChecked: function() {console.log('onChecked osm1'); add_polygons(osm_map_osm_polygons, osm_map);},
        onUnchecked: function() {console.log('onUnchecked osm1'); remove_polygons(osm_map_osm_polygons, osm_map);}
    });
    
    $('#dg_checkbox1').checkbox({
        onChecked: function() {console.log('onChecked dg1'); add_polygons(osm_map_points, osm_map);},
        onUnchecked: function() {console.log('onUnchecked dg1'); remove_polygons(osm_map_points, osm_map);}
    });
    
    $('#osm_checkbox2').checkbox({
        onChecked: function() {console.log('onChecked osm2'); add_polygons(dg_map_osm_polygons, dg_map);},
        onUnchecked: function() {console.log('onUnchecked osm2'); remove_polygons(dg_map_osm_polygons, dg_map);}
    });
    
    $('#dg_checkbox2').checkbox({
        onChecked: function() {console.log('onChecked dg2'); add_polygons(dg_map_points, dg_map);},
        onUnchecked: function() {console.log('onUnchecked dg2'); remove_polygons(dg_map_points, dg_map);}
    });
    
    reset_checkboxes();
});