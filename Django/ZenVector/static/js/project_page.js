// // $("#detailModal").off().on('submit',function (event) {
//     // event.preventDefault();
//     console.log('ere');
//     var assignedTo = document.getElementById("assignedToD").value;
//     console.log(assignedTo);
//
//     var deadline = document.getElementById("task_edit_deadline").value;
//     console.log(deadline);
//
//     var detail = document.getElementById("taskDetailsD").value;
//     console.log(detail);
//
//     var status =document.getElementById("statusD").value;
//     console.log(status);
// });

$("#detailModal").on('submit',function (e) {
    e.preventDefault();
});

function changeDetails() {

        // var assignedTo = document.getElementById("assignedTo").value;
        // console.log(assignedTo);

        var deadline = document.getElementById("task_edit_deadline").value;
        var detail = document.getElementById("taskDetailsD").value;
        var status =document.getElementById("statusD").value;
        var taskid = $('#edit_task_title').attr("taskid");
            // data:{task_id: taskid,assignto:assignedTo,time:deadline,detail:detail,status:status,csrfmiddlewaretoken:csrftoken},

        $.ajax({
            type:"POST",
            url:"ChangeTaskDetails/",
            data:{task_id: taskid,time:deadline,detail:detail,status:status,csrfmiddlewaretoken:csrftoken},
            success:function (e) {
                location.reload(true)
            },
            error:function (e) {
                console.log(e)
            }
        })
}

$(document).on('click','.menu-button',function () {

    var task_id = $(this).data('id');
    $('#edit_task_title').attr("taskid",task_id);

    var element = document.getElementById(task_id);


    var element_p = element.getElementsByTagName('pre')[0].innerHTML;

    var details = element_p.split("<")[0];

    var date = element_p.split('12px">')[1].split('Given by:')[0].split("Deadline: ")[1];

    var list_title = $(this).parent().parent().parent().attr("id");

    document.getElementById("taskDetailsD").value = details;

    var select_item= document.getElementById('assignedToTasks');

    $.ajax({
           type:"GET",
           url:"getTaskUsers/",
           data:{taskid:task_id,csrfmiddlewaretoken:csrftoken},
           success:function (e) {

                  $('#assignedToTasks').empty();
                  $.each(JSON.parse(e['users']),function(index,value){

                    $('#assignedToTasks').append("<option value='"+value['pk']+"'>"+value['pk']+"</option>");
                  });
                  console.log("HERRE");
               console.log(e);
               // location.reload(true);
           },
           error:function () {
               // console.log("NOT CORRECT");
           }
       });

    document.getElementById('task_edit_deadline').value = formatDate(date);



});

function formatDate(date) {
    var d = new Date(date),
        month = '' + (d.getMonth() + 1),
        day = '' + d.getDate(),
        year = d.getFullYear();

    if (month.length < 2)
        month = '0' + month;
    if (day.length < 2)
        day = '0' + day;

    return [year, month, day].join('-');
}


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

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}

$("#addTaskModal").on('hidden.bs.modal',function (e) {
    e.preventDefault();

      var title_error = document.getElementById("task_name_error");
      var descrip_error = document.getElementById("task_descrip");
      var deadline_error = document.getElementById('task_deadline');
      var task_error = document.getElementById("task_error");

      var assigned_to_error = document.getElementById("add_task_users");
      assigned_to_error.style.display = 'none';

      task_error.style.display = 'none';
      title_error.style.display = 'none';
      descrip_error.style.display = 'none';
      deadline_error.style.display = 'none';

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

      // var deadline = document.getElementById("deadline");

      var detail = document.getElementById("taskDetails").value;

      var status = document.getElementById("status").value;

      var dateControl = $("#task_form_deadline").val();

      var assigned_to_error = document.getElementById("add_task_users");
      assigned_to_error.style.display = 'none';

      var check = true;
      var includesCheck = true;
      if ($.trim(assignedTo).length !== 0)
        {
            $.each(assignedTo.split(','),function(index,value){

            if (!validateEmail(value))
            {
                   check = false;
            }

            else if (!usrOptions['data'].includes(value)){
                includesCheck = false;

            }
              });
        }

      if (check === false)
      {
          assigned_to_error.innerHTML = 'One or more of the emails is not valid';
          assigned_to_error.style.display = 'block';
          return ;
      }

      if (includesCheck === false)
      {
          assigned_to_error.innerHTML = 'One or more of the users are not added to the proejct.';
          assigned_to_error.style.display = 'block';
          return ;
      }

      if ($.trim(title).length < 2)
      {
          title_error.innerHTML = "Please provide a meaningful name";
          title_error.style.display = 'block';
          return false;
      }

      if ($.trim(dateControl).length === 0){
            deadline_error.innerHTML = "Please choose the deadline";
            deadline_error.style.display = 'block';
            return false;
      }
      if ($.trim(detail).length < 5){
          descrip_error.innerHTML = "Please provide a meaningful description";
          descrip_error.style.display = 'block';
          return false;
      }

      $.ajax({
         type:"POST",
         url:"NewTask/",
         data: {title:title,assign_to: assignedTo,date:dateControl,descrip:detail,list_name:status,csrfmiddlewaretoken:csrftoken},
          success:function () {
               location.reload(true);
          },
          error:function () {
             task_error.style.display = 'block';
          }

      });

  }

$("#addListForm").on('submit',function(e) {
    e.preventDefault();
});

function addList(e) {
    var error_element = document.getElementById('list_name');
    error_element.style.display = 'none';
    var title = document.getElementById("listTitle").value;
    error_element.innerHTML="You can't leave the list name empty";

    var color = document.getElementById("headerColor").value;

   if ($.trim(title).length  === 0){
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




}

$("#addTask").click(function(){
$("#addTaskModal").modal({backdrop: "static"});
});



$(function(){
    var dtToday = new Date();
    var month = dtToday.getMonth() + 1;
    var day = dtToday.getDate();
    var year = dtToday.getFullYear();
    var year1 = dtToday.getFullYear()+10;
    if(month < 10)
        month = '0' + month.toString();
    if(day < 10)
        day = '0' + day.toString();
    var minDate = year + '-' + month + '-' + day;
    var maxDate = year1 + '-' + month + '-' + day;
    $('#task_form_deadline').attr('min', minDate);
    $('#task_form_deadline').attr('max', maxDate);

    $('#task_edit_deadline').attr('min', minDate);
    $('#task_edit_deadline').attr('max', maxDate);
});


$("#addList").click(function(){
$("#addListModal").modal({backdrop: "static"});
});

// $("#detailModal").click(function(){
// $("#detailModal").modal({backdrop: "static"});
// });

// dragula.drake.on("drag", function(el) {
// el.className.replace("ex-moved", "");
// })
// .on("drop", function(el) {
// el.className += "ex-moved";
// })
// .on("over", function(el, container) {
// container.className += "ex-over";
// })
// .on("out", function(el, container) {
// container.className.replace("ex-over", "");
// });

// dragula.removeOnSpill:false
//     .on("drag", function(el) {
//   el.className.replace("ex-moved", "");
//   console.log(el.className);
// }).on("dropremoveOnSpill", function(el) {
//   el.className += "ex-moved";
//   console.log(el.className);
// })
// .on("over", function(el, container) {
//   container.className += "ex-over";
//   console.log(el.className);
// })
// .on("out", function(el, container) {
//   container.className.replace("ex-over", "");
//   console.log(el.className);
// });



 function deleteList(){
    var list_id = $("#stateId").data('stateid');
    console.log(list_id);
       $.ajax({
           type:"POST",
           url:"DeleteList/",
           data:{list_id:list_id,csrfmiddlewaretoken:csrftoken},
           success:function () {
               location.reload(true);
           },
           error:function () {
               console.log("NOT CORRECT");
           }
       })
}

$(document).on('click','#deleteListId',function () {
    var list_id=$(this).data('idstate');
    console.log(list_id);
    $('#stateId').data("stateid",list_id);
});


 $('form input').keydown(function (e) {
    if (e.keyCode == 13) {
        console.log('here check');
        e.preventDefault();
        return false;
    }
});