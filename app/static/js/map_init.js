$(document).ready(function (){    
    osm_map = L.map('osm_map').setView(default_coords, default_zoom);
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
       attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'       
    }).addTo(osm_map);
    
    l8_map = L.map('l8_map').setView(default_coords, default_zoom);
    L.tileLayer('https://{s}.sat.owm.io/sql/{z}/{x}/{y}/?appid=50429daa6bd544f63f18cbc295417135&overzoom=true&op=truecolor&from=l8&order=best', {
        attribution: '&copy; <a href="https://owm.io/">VANE</a> contributors'
    }).addTo(l8_map);
});