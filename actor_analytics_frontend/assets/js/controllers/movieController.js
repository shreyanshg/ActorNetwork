function MovieController($http, $scope, NetworkService, $stateParams){
  var _this = $scope;
  _this.isLoading = true;
  _this.movie_details = [];
  _this.search = $stateParams.search;

  NetworkService
      .get_movie(_this.search)
      .then(function(response) {
        //console.log("response recieved");
        _this.movie_details= response;
        _this.isLoading = false;
        //_this.status = true;
      }, function(error){
        _this.isLoading = false;
      });

}




MovieController.$inject = ['$http', '$scope', 'NetworkService', '$stateParams'];

angular
  .module('ActorNetwork')
  .controller('MovieController', MovieController);
