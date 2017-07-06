angular.module('healthify')
    .controller('notificationController', [
        '$scope',
        '$timeout',
        'MainService',
        'ImageUtils',
        function ($scope, $timeout, MainService, ImageUtils) {
            $scope.notification = {};
            $scope.validHeader = false;
            $scope.validContent = false;
            $scope.validImage = false;

            $scope.checkUrl = function(){
                ImageUtils.isImage($scope.notification.url).then(function(data){
                    $scope.validImage = data;
                });
            };

            $scope.checkWordCountHeader = function () {
                var word = $scope.notification.header, min = 20, max = 150;
                
                if (word && (word.length >= min && word.length <= max)){
                    $scope.validHeader = true;
                } else {
                    $scope.validHeader = false;
                }
            };

            $scope.checkWordCountContent = function () {
                var word = $scope.notification.content, min = 20, max = 300;
                
                if (word && (word.length >= min && word.length <= max)){
                    $scope.validContent = true;
                } else {
                    $scope.validContent = false;
                }
            };

            $scope.add = function(notification){
                notification.scheduledTime = $scope.data.dateDropDownInput;
                $scope.notification = notification;
                MainService.addNotification(notification);
            }
        }
    ]);