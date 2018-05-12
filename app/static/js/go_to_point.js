$(document).ready(function(){    
    $("#go_button").click(function() {
        let latitude = $('#latitude').val();
        if (latitude === '' || isNaN(latitude))
        {
            alert('Latitude should be a valid number!');
            return;
        }
        
        let longitude = $('#longitude').val();
        if (longitude === '' || isNaN(longitude))
        {
            alert('Longitude should be a valid number!');
            return;
        }
        
        let new_coords = [parseFloat(latitude), parseFloat(longitude)];
        
        osm_map.setView(new_coords);
        dg_map.setView(new_coords);
    });
});