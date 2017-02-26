function AboutCntrl($log) {
  this.view = 'hello to about page';
}


AboutCntrl.$inject = ['$log'];

angular
  .module('ActorNetwork')
  .controller('AboutCntrl', AboutCntrl);
