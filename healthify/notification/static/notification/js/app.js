angular.module('healthify', ['ui.bootstrap.datetimepicker']);

angular.module('healthify')
    .config(function ($interpolateProvider, $httpProvider) {
        // interpolation will make us to define starting and ending braces as we want
        $interpolateProvider.startSymbol('[[');
        $interpolateProvider.endSymbol(']]');

        //this is used to set cookies and headers, which are used to send http requests through angular
        $httpProvider.defaults.xsrfCookieName = 'csrftoken';
        $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
    });