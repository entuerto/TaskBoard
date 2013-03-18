
var taskboard = angular.module('taskboard', ['taskServices', 'ui.bootstrap.dialog'], 
  function($routeProvider, $locationProvider, $dialogProvider) {

  $routeProvider.
      when('/tasks', {templateUrl: 'index.html', controller: TaskCtrl}).
      when('/tasks/:id', {templateUrl: 'index.html', controller: TaskCtrl}).
      otherwise({redirectTo: '/tasks'});

  // configure html5 to get links working
  // If you don't do this, you URLs will be base.com/#/home rather than base.com/home
  $locationProvider.html5Mode(true);
});


// define functions here, they will be present in $scope in all controllers.
taskboard.run(function($rootScope) {
  $rootScope.hello = function() {
    console.log('hello');
  }
});

function EditCtrl($scope, dialog, Task, editedTask) {
   $scope.task = editedTask;

   $scope.close = function(result){
      dialog.close(result);
  };
}

function TaskCtrl($scope, $dialog, Task) {
   $scope.tasks = Task.query();

   $scope.orderProp = ['priority','due'];


   $scope.createTask = function (newTask) {
      newTask.$save();
      $scope.tasks.push(newTask);           
   };
 
   $scope.updateTask = function(task) {                
      task.$update();
   };
   
   $scope.deleteTask = function (task) {
      task.$delete();
      //$scope.tasks = _.without($scope.tasks, task);      
   }

   $scope.editTask = function (task) {
      var d = $dialog.dialog({ backdrop: true,
                               keyboard: true,
                               backdropClick: true,
                               templateUrl: '/details.html',
                               resolve: { editedTask: function() { 
                                  return task;
                               } },
                               controller: 'EditCtrl' });
      d.open();
   };
   
}
//TaskCtrl.$inject = ['$scope', 'Task'];



/* Services */
angular.module('taskServices', ['ngResource']).factory('Task', function($resource){
  return $resource('/tasks', {}, {
    query: {method:'GET', isArray:true},
    save: {method:'POST'}
  });
});


  

