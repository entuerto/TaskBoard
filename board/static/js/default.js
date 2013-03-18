
$(function() {
  $(".column").sortable({
     connectWith: ".column",

     stop: function(event, ui) {
       var sortorder='';
       $('.column').each(function() {
          var columnId = $(this).attr('id');
          $('.task').each(function() {
             sortorder += columnId + '=' + $(this).attr('sort-key') + '&'; 
          });
       });
       alert('SortOrder: ' + sortorder);
       /* Pass sortorder variable to server using ajax to save state  */
     }
  });

  $(".column").disableSelection();

  $('[rel=popover]').popover();
});

