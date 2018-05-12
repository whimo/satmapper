$(document).ready(function() {
    $('#reset_button').click(function() {
        $('#osm_checkbox').checkbox('check');
        $('#l8_checkbox').checkbox('check');
        
        osm_map.setView(default_coords, default_zoom);
        l8_map.setView(default_coords, default_zoom); 
    });
});