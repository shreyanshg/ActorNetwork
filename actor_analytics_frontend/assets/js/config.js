function Config($stateProvider, $urlRouterProvider, $urlMatcherFactoryProvider){
  $stateProvider
    .state('search', {
      url: '/',
      controller: 'SearchController as searchCntrl',
      templateUrl: 'templates/search_page.html'
    })
    .state('actors', {
      url: '/actors/:search',
      controller: 'ActorNetworkController as actorCntrl',
      templateUrl: 'templates/actor_detailed.html'
    })
    .state('movies', {
      url: '/movies/:search',
      controller: 'MovieController as movieCntrl',
      templateUrl: 'templates/movie_detailed.html'
    })
    .state('about', {
      url: '/about',
      controller: 'AboutCntrl as aboutCntrl',
      templateUrl: 'templates/about.html'
    });
    $urlRouterProvider.otherwise('/');
}
Config.$inject = ['$stateProvider', '$urlRouterProvider', '$urlMatcherFactoryProvider'];

angular
  .module('ActorNetwork')
  .config(Config);
