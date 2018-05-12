$(document).ready(function (){    
    osm_map = L.map('osm_map').setView(default_coords, default_zoom);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
       attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'       
    }).addTo(osm_map);
    
    dg_map = L.map('dg_map').setView(default_coords, default_zoom);
    L.tileLayer('https://{s}.tiles.mapbox.com/v4/digitalglobe.316c9a2e/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoiZGlnaXRhbGdsb2JlIiwiYSI6ImNqZGFrZ2c2dzFlMWgyd2x0ZHdmMDB6NzYifQ.9Pl3XOO82ArX94fHV289Pg', {
        attribution: '&copy; DigitalGlobe Premium Imagery - <a href="https://wiki.openstreetmap.org/wiki/DigitalGlobe">Terms & Feedback</a>'
    }).addTo(dg_map);
});
