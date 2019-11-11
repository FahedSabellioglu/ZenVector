 function changeDetails() {

        var assignedTo = document.getElementById("assignedToD").value;
        console.log(assignedTo);

        var deadline = document.getElementById("deadlineD").value;
        console.log(deadline);

        var detail = document.getElementById("taskDetailsD").value;
        console.log(detail);

        var status =document.getElementById("statusD").value;
        console.log(status);

      // It sould get the task ID and check if the card status has changed, if it has been changed, add the task to the new state.
        document.getElementById(status).innerHTML+=
              "<div class='card'><div class='card-header card-header-danger2'>" + "Card Title !!!" +
              "<button type='button' style='position: absolute; right: 1rem;' class='btn btn-just-icon btn-sm' data-toggle='modal' data-target='#detailModal'>"+
              "<i class='material-icons'>menu</i></button></div> <class='card-body card-text'>" + detail+ "</div></div>";
      // If it is not, it should change the card content.
      // document.getElementById(task ID).innerHTML=
      //         "<div class='card'><div class='card-header card-header-danger2'>" + "Card Title !!!" +
      //         "<button type='button' style='position: absolute; right: 1rem;' class='btn btn-just-icon btn-sm' data-toggle='modal' data-target='#detailModal'>"+
      //         "<i class='material-icons'>menu</i></button></div> <class='card-body card-text'>" + detail+ "</div></div>";

}


$(document).on('click','.menu-button',function () {

    var task_id = $(this).data('id');
    console.log(task_id);
    $('#edit_task_title').attr("taskid",task_id);
    // console.log($("#edit_task_title").attr('taskid'));


});


 function deleteTask(){

    var x = confirm("Are you sure you want to delete?");
    var task_id = $("#edit_task_title").attr('taskid');
    if (x){

       $.ajax({
           type:"POST",
           url:"DeleteTask/",
           data:{taskid:task_id,csrfmiddlewaretoken:csrftoken},
           success:function () {
               location.reload(true);
           },
           error:function () {
               console.log("NOT CORRECT");
           }
       })
    }
    else{
      console.log(x);
      return false;
    }
}

$("#addTaskForm").on('submit',function (e) {
    e.preventDefault();
});


function addTask() {

      var title_error = document.getElementById("task_name_error");
      var descrip_error = document.getElementById("task_descrip");
      var deadline_error = document.getElementById('task_deadline');
      var email_value = document.getElementById('project_owner').value;
      var task_error = document.getElementById("task_error");
      task_error.style.display = 'none';

      title_error.style.display = 'none';
      descrip_error.style.display = 'none';
      deadline_error.style.display = 'none';

      var title = document.getElementById("taskTitle").value;

      var assignedTo = document.getElementById("assignedTo").value;

      var deadline = document.getElementById("deadline");

      var detail = document.getElementById("taskDetails").value;

      var status = document.getElementById("status").value;

      var dateControl = document.querySelector('input[type="datetime-local"]');

      if ($.trim(title).length < 2)
      {
          title_error.innerHTML = "Please provide a meaningful name";
          title_error.style.display = 'block';
          return false;
      }

      //   if ($.trim(dateControl.value).length == 0){
      //       deadline_error.innerHTML = "Please choose the deadline";
      //       deadline_error.style.display = 'block';
      //       return false;
      // }

      if ($.trim(detail).length < 5){
          descrip_error.innerHTML = "Please provide a meaningful description";
          descrip_error.style.display = 'block';
          return false;
      }

      $.ajax({
         type:"POST",
         url:"NewTask/",
         data: {title:title,assign_to: assignedTo,time:"09/09/2019",descrip:detail,list_name:status,csrfmiddlewaretoken:csrftoken},
          success:function () {
               location.reload(true);
          },
          error:function () {
             task_error.style.display = 'block';
          }

      });



      // document.getElementById(status).innerHTML +=
      //     "<div class='card'><div class='card-header card-header-danger2'>" + title +
      //     "<button type='button' style='position: absolute; right: 1rem;' class='btn btn-just-icon btn-sm' data-toggle='modal' data-target='#detailModal'>"+
      //     "<i class='material-icons'>menu</i></button></div> <class='card-body card-text'>" + detail+ "</div></div>";

      // $('#addTaskModal').modal('hide');
  }

$("#addListForm").on('submit',function(e) {
    e.preventDefault();
// });
});

function addList(e) {
    console.log("hererer");
    var error_element = document.getElementById('list_name');
    error_element.style.display = 'none';
    var title = document.getElementById("listTitle").value;
    error_element.innerHTML="You can't leave the list name empty";

      var color = document.getElementById("headerColor").value;
      console.log(color);

   if ($.trim(title).length  == 0){
        error_element.innerHTML="You can't leave the list name empty";
        error_element.style.display = 'block';
        return false;}
       $.ajax({
        type:'POST',
        url:"NewState/",
        data:{name:title,color:color,csrfmiddlewaretoken:csrftoken},
        success:function (e) {
            location.reload(true)
        },
        error:function (e) {
            console.log(e);
            error_element.innerHTML = e.responseJSON.message;
            error_element.style.display = 'block';


        }
    });
  // document.getElementById("board").innerHTML +=
  //     "<div class='col-xs-6 col-md-3'><div class='card-list'><div class='card-header'><h4 class='card-list-title'>"
  //     +title+"</h4></div><div class='card-list-body text-center' id="+title+"><div class='card'><div class='card-header "+
  //     " card-header-danger2'>Task Title <button type='button' style='position: absolute; right: 1rem;'class='btn btn-just-icon"+
  //     " btn-sm' data-toggle='modal' data-target='#detailModal'><i class='material-icons'>menu</i></button></div> "+
  //     "<class='card-body card-text'>Please click to detail button to change task details</div></div></div></div>"



}

$("#addTask").click(function(){
$("#addTaskModal").modal({backdrop: "static"});
});

$("#addList").click(function(){
$("#addListModal").modal({backdrop: "static"});
});

$("#detailModal").click(function(){
$("#detailModal").modal({backdrop: "static"});
});


 /* Custom Dragula JS */
// dragula([
// document.getElementById("to-do"),
// document.getElementById("doing"),
// document.getElementById("done"),
// ]);

removeOnSpill.on("drag", function(el) {
  el.className.replace("ex-moved", "");
  console.log(el.className);
})
.on("dropremoveOnSpill", function(el) {
  el.className += "ex-moved";
  console.log(el.className);
})
.on("over", function(el, container) {
  container.className += "ex-over";
  console.log(el.className);
})
.on("out", function(el, container) {
  container.className.replace("ex-over", "");
  console.log(el.className);
});