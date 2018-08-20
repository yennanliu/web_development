angular.module('myApp', []).controller('namesCtrl', function($scope) {
    $scope.names = [
    {car_name:'car_a',lon: 'lon',lat:'lat',val1:'val1'},
	{car_name:'car_a',lon: 51.43929,lat:-0.103417,val1:1},
	{car_name:'car_b',lon: 51.43929,lat:-0.113417,val1:9},
	{car_name:'car_c',lon: 53.43929,lat:-0.153417,val1:9}
	  
    ];
});

