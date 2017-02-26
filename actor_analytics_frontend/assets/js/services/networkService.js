function NetworkService($http) {
  var getActorAPIURL = 'http://localhost:8000/actor_analytics/actors';
  var getMovieAPIURL = 'http://localhost:8000/actor_analytics/movies';

  function get_actor(actor_name) {
    return $http
      .get(getActorAPIURL+'?search='+actor_name)
      .then(function(response) {
        console.log(response);
        return response.data;
      }, function(error) {
        console.error(error);
      });
  }

  function get_movie(movie_name) {
    return $http
      .get(getMovieAPIURL+'?search='+movie_name)
      .then(function(response) {
        console.log(response);
        return response.data;
      }, function(error) {
        console.error(error);
      });
  }
  return {
    get_actor: get_actor,
    get_movie: get_movie
  }
}


angular
  .module('ActorNetwork')
  .factory('NetworkService', NetworkService);
