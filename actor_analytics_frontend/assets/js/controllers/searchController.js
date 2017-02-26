function SearchController($scope, $location){
  $scope.search_text = ""
  $scope.query_type = "actors"
  $scope.search = function(search_text){
    if ($scope.query_type == "actors"){
      $location.path("actors/" + search_text)
    }
    else if ($scope.query_type == "movies"){
      $location.path("movies/" + search_text)
    }
  }
}

SearchController.$inject = ['$scope', '$location'];

angular
  .module('ActorNetwork')
  .controller('SearchController', SearchController);
