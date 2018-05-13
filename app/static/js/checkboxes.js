$(document).ready(function() {
    let osm_map_osm_polygons = osm_raw_polygons.map(function(arr) {return L.polygon(arr);});
    let dg_map_osm_polygons = osm_raw_polygons.map(function(arr) {return L.polygon(arr);});
    //let osm_map_points = dg_raw_polygons.map(function(arr) {return L.circle(arr, {radius: 1});});
    //let dg_map_points = dg_raw_polygons.map(function(arr) {return L.circle(arr, {radius: 1});});
    let osm_pic = null;
    let dg_pic = null;
    
    if (imageUrl != null && bounds_coords1 != null && bounds_coords2 != null)
    {
        let imageBounds = [bounds_coords1, bounds_coords2];
    
        osm_pic = L.imageOverlay(imageUrl, imageBounds);
        dg_pic = L.imageOverlay(imageUrl, imageBounds);
    }    
    
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
    
    function add_picture(pic, map)
    {
        if (pic)
            pic.addTo(map);
    }
    
    function remove_picture(pic, map)
    {
        if (pic)
            map.removeLayer(pic);
    }
    
    $('#osm_checkbox1').checkbox({
        onChecked: function() {console.log('onChecked osm1'); add_polygons(osm_map_osm_polygons, osm_map);},
        onUnchecked: function() {console.log('onUnchecked osm1'); remove_polygons(osm_map_osm_polygons, osm_map);}
    });
    
    $('#dg_checkbox1').checkbox({
        onChecked: function() {console.log('onChecked dg1'); add_picture(osm_pic, osm_map);},
        onUnchecked: function() {console.log('onUnchecked dg1'); remove_picture(osm_pic, osm_map);}
    });
    
    $('#osm_checkbox2').checkbox({
        onChecked: function() {console.log('onChecked osm2'); add_polygons(dg_map_osm_polygons, dg_map);},
        onUnchecked: function() {console.log('onUnchecked osm2'); remove_polygons(dg_map_osm_polygons, dg_map);}
    });
    
    $('#dg_checkbox2').checkbox({
        onChecked: function() {console.log('onChecked dg2'); add_picture(dg_pic, dg_map);},
        onUnchecked: function() {console.log('onUnchecked dg2'); remove_picture(dg_pic, dg_map);}
    });
    
    reset_checkboxes();
});