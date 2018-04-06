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
    stateLayer.loadGeoJson('ldn.geo.json');
    // Set and apply styling to the stateLayer
    stateLayer.setStyle(function(feature) {
        //console.log(feature['id'])
        console.log(feature.f.gid)
        return {
            fillColor: getColor(feature.f.gid), // call function to get color for state based on the COLI (Cost of Living Index)
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
        ['car a ', 51.43929, -0.103417, 4],
        ['car b ', 51.42929, -0.062417, 5],
        ['mycar', 51.42829, -0.082417, 3],
        ['botvan', 51.4374, 0.1038, 2],
        ['gvan', 51.4274, 0.1234, 2],
        ['lavan', 51.42929, -0.1134178, 2],
        ['uvan', 51.43929, -0.123417, 2],
        ['zvan', 51.439996, -0.1679940, 2]
    ];

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
                infowindow.setContent(locations[i][0]);
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
        table.style.width = '300px';
        tableData.forEach(function(rowData) {
            var row = document.createElement('tr');

            rowData.forEach(function(cellData) {
                var cell = document.createElement('td');
                cell.appendChild(document.createTextNode(cellData));
                row.appendChild(cell);
            });

            tableBody.appendChild(row);
        });

        table.appendChild(tableBody);
        document.body.appendChild(table);
    }
});