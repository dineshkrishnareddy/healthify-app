angular.module('healthify')
    .factory('MainService', [
        'MainFactory',
        function(MainFactory) {

            return {

                addNotification: function (notification) {

                    return MainFactory.httpService({
                        method: 'POST',
                        url: '/api/notification',
                        data: notification
                    });
                }
            }
        }
    ]);