var app = angular.module('plunker', []);

app.controller('MainCtrl', function($scope, $http) {
    vm = this;

    // Set the Map Options to be applied when the map is set.
    var mapOptions = {
        zoom: 10,
        scrollwheel: false,
        center: new google.maps.LatLng(51.5074, 0.1278),
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        mapTypeControl: false,
        styles: [{"featureType":"road","elementType":"labels","stylers":[{"visibility":"on"}]},{"featureType":"poi","stylers":[{"visibility":"off"}]},{"featureType":"administrative","stylers":[{"visibility":"off"}]},{"featureType":"road","elementType":"geometry.fill","stylers":[{"color":"#000000"},{"weight":1}]},{"featureType":"road","elementType":"geometry.stroke","stylers":[{"color":"#000000"},{"weight":0.8}]},{"featureType":"landscape","stylers":[{"color":"#ffffff"}]},{"featureType":"water","stylers":[{"visibility":"off"}]},{"featureType":"transit","stylers":[{"visibility":"off"}]},{"elementType":"labels","stylers":[{"visibility":"off"}]},{"elementType":"labels.text","stylers":[{"visibility":"on"}]},{"elementType":"labels.text.stroke","stylers":[{"color":"#ffffff"}]},{"elementType":"labels.text.fill","stylers":[{"color":"#000000"}]},{"elementType":"labels.icon","stylers":[{"visibility":"on"}]}],
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, google.maps.MapTypeId.TERRAIN]
        }
    }

    // Set a blank infoWindow to be used for each to state on click
    var infoWindow = new google.maps.InfoWindow({
        content: ""
    });

    // Set the map to the element ID and give it the map options to be applied
    vm.map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

    // Create the state data layer and load the GeoJson Data
    var stateLayer = new google.maps.Data();
    //stateLayer.loadGeoJson('https://gist.githubusercontent.com/dmarg/b2959e771ae680acbc95/raw/815a03f55d028dace4371c27d0b787ca0f2f2b5d/states.json');
    //stateLayer.loadGeoJson('ldn.geo.json');
    stateLayer.loadGeoJson('london_postcodes.geo.json');
    // Set and apply styling to the stateLayer
    stateLayer.setStyle(function(feature) {
        //console.log(feature['id'])
        console.log(feature.f.gid)
        return {
            fillColor: getColor(Math.random(feature.f.gid)*80), // call function to get color for state based on the COLI (Cost of Living Index)
            fillOpacity: 0.8,
            strokeColor: '#b3b3b3',
            strokeWeight: 1,
            zIndex: 1
        };
    });

    // Add mouseover and mouse out styling for the GeoJSON State data
    stateLayer.addListener('mouseover', function(e) {
        stateLayer.overrideStyle(e.feature, {
            strokeColor: '#2a2a2a',
            strokeWeight: 2,
            zIndex: 2
        });
    });

    stateLayer.addListener('mouseout', function(e) {
        stateLayer.revertStyle();
    });

    // Adds an info window on click with in a state that includes the state name and COLI
    stateLayer.addListener('click', function(e) {
        console.log(e);
        console.log(e.feature.f);
        infoWindow.setContent(
            '<div style="line-height:1.00;overflow:hidden;white-space:nowrap;">' +
            'Zone : <br>' +
            '<br> gid: ' + e.feature.f.gid +
            '<br> geom: ' + e.feature.f.geom +
            '</div>'
        );

        var anchor = new google.maps.MVCObject();
        anchor.set("position", e.latLng);
        infoWindow.open(vm.map, anchor);
    });


    // Final step here sets the stateLayer GeoJSON data onto the map
    stateLayer.setMap(vm.map);


    // add for loop markers 
    
    var locations = [
        ['car_name', 'lon','lat','val1',  'val2'], 
        ['car a ', 51.43929, -0.103417, 4,  10],
        ['car b ', 51.42929, -0.062417, 5,  1],
        ['mycar', 51.42829, -0.082417, 3,  10],
        ['botvan', 51.4374, 0.1038, 2,  5],
        ['gvan', 51.4274, 0.1234, 2, 7],
        ['lavan', 51.42929, -0.1134178, 2 , 7],
        ['uvan', 51.43929, -0.123417, 2, 8],
        ['zvan', 51.439996, -0.1679940, 2, 9]
    ];
    

    // load json file
    //var load_json_data = read_json_file()
    //var locations = load_json_data['responseJSON']

    var infowindow = new google.maps.InfoWindow();
    var marker, i;

    for (i = 0; i < locations.length; i++) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            map: vm.map
            //console.log(i)
        });

        google.maps.event.addListener(marker, 'click', (function(marker, i) {
            return function() {
                infowindow.setContent('car : ' + String(locations[i][0])+ '<br>'
                                      + 'val1 : ' + String(locations[i][3]));
                infowindow.open(vm.map, marker);
            }
        })(marker, i));
    }


    for (i = 0; i < locations.length; i++) {
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][2], locations[i][1]),
            map: vm.map
        })
    };

    // add html table 
    createTable(locations)


    // add simple markers 
    /*
     var marker = new google.maps.Marker({
          position: {lat: 51.5074 , lng: 0.1278},
          map: vm.map,
          title: 'Uluru (Ayers Rock)'
         });


     var marker = new google.maps.Marker({
          position: {lat: 51.5374 , lng: 0.1178},
          map: vm.map,
          title: 'Uluru (Ayers Rock)'
         });
    */
    // ---------------------- function  ----------------------  // 

    // color polygons with values 
    // returns a color based on the value given when the function is called
    function getColor(coli) {
        var colors = [
            '#337DFF',
            '#33FF55',
            '#AC33FF',
            '#FF7733',
            '#33FFF9'
        ];

        return coli <= 20 ? colors[4] :
            30 < coli ? colors[3] :
            40 < coli ? colors[2] :
            60 < coli ? colors[1] :
            colors[0];
    }

    // js list -> html table 
    // https://stackoverflow.com/questions/15164655/generate-html-table-from-2d-javascript-array
    function createTable(tableData) {
        var table = document.createElement('table');
        var tableBody = document.createElement('tbody');
        table.style.border = '1px solid black';
        table.style.width = '500px';
        table.style.height = '300px';
        table.style.margin = '-400px 0px 0px 800px';
        tableData.forEach(function(rowData) {
            var row = document.createElement('tr');

            rowData.forEach(function(cellData) {
                var cell = document.createElement('td');
                // modify table style 
                cell.style.color="red";
                cell.appendChild(document.createTextNode(cellData));
                row.appendChild(cell);

            });

            tableBody.appendChild(row);
        });

        table.appendChild(tableBody);
        document.body.appendChild(table);
    }

    // load json file 
    // https://stackoverflow.com/questions/6813114/how-can-i-load-jquery-if-it-is-not-already-loaded/42013103#42013103
    function read_json_file() {
    //Do stuff with jQuery
    loaded_json = jQuery.getJSON('./car_data.json')
    console.log(loaded_json)
    return loaded_json
    }

    if(typeof jQuery=='undefined') {
        var headTag = document.getElementsByTagName("head")[0];
        var jqTag = document.createElement('script');
        jqTag.type = 'text/javascript';
        jqTag.src = 'jquery.js';
        jqTag.onload = read_json_file;
        headTag.appendChild(jqTag);
    } else {
         read_json_file();
    }


    // ---------------------- function  ----------------------  // 




});