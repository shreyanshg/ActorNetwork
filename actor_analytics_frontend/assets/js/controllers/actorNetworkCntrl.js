function ActorNetworkController($http, $scope,  NetworkService, $stateParams) {
  var _this = $scope;
  _this.isLoading = true;
  _this.actor_details = [];
  _this.search = $stateParams.search;
  _this.isGraphPresent = false
   var color = d3.scale.category20();
  _this.options = {
        chart: {
            type: 'forceDirectedGraph',
            height: 300,
            width: (function(){ return nv.utils.windowSize().width*(2/3) })(),
            margin:{top: 20, right: 20, bottom: 20, left: 20},
            color: function(d){
                return color(d.group)
            },
            nodeExtras: function(node) {
                node && node
                  .append("text")
                  .attr("dx", 8)
                  .attr("dy", ".35em")
                  .text(function(d) { return d.name })
                  .style('font-size', '10px');
            }
        }
    };
  NetworkService
      .get_actor(_this.search)
      .then(function(response) {
        //console.log("response recieved");
        _this.actor_details= response;
        _this.isLoading = false;
        //_this.status = true;
      }, function(error){
        _this.isLoading = false;
      });
}



ActorNetworkController.$inject = ['$http', '$scope', 'NetworkService', '$stateParams'];

angular
  .module('ActorNetwork')
  .controller('ActorNetworkController', ActorNetworkController);
