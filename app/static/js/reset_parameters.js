$(document).ready(function() {
    $('#reset_button').click(function() {
        reset_checkboxes();
        
        osm_map.setView(default_coords, default_zoom);
        dg_map.setView(default_coords, default_zoom); 
    });
});