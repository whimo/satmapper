$(document).ready(function() {
    $('#reset_button').click(function() {
        $('#osm_checkbox').checkbox('check');
        $('#dg_checkbox').checkbox('check');
        
        osm_map.setView(default_coords, default_zoom);
        dg_map.setView(default_coords, default_zoom); 
    });
});