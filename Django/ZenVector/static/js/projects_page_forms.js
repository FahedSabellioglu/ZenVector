$('.modal').on('hidden.bs.modal', function(){
    $(this).find('form')[0].reset();
    $('.tags_container').empty();

});

$("#projectModal").on('hidden.bs.modal',function (e) {
    e.preventDefault();
        var error_element = document.getElementById("project_name_error");
        error_element.style.display='none';

});

$("#projectForm").off().on('submit',function (event) {
    event.preventDefault();
    var project_name = document.getElementById("project_name").value;
    var error_element = document.getElementById("project_name_error");
    var project_users = document.getElementById("newProjectUsers").value;


    var check = true;
    var includesCheck = true;

    if ($.trim(project_users).length !== 0)
    {
        $.each(project_users.split(','),function(index,value){

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
        error_element.innerHTML = 'One or more of the emails is not valid';
        error_element.style.display = 'block';
        return ;
    }

  if (includesCheck === false)
      {
          error_element.innerHTML = 'One or more the emails are not registered to the app';
          error_element.style.display = 'block';
          return ;
      }
    error_element.style.display = 'none';
    if ($.trim(project_name) === '' || $.trim(project_name).length < 3 || $.trim(project_name).length >26) {

        error_element.innerHTML = 'meaningful name please...';
        error_element.style.display = 'block';
        return false;
    }
    $.ajax({
        type: "POST",
        url: "CreateProject/",
        data: {usr_email: '{{ request.user.email }}', csrfmiddlewaretoken: csrftoken, p_name: project_name,
                members:project_users},
        success: function (e) {
            location.reload(true);

        },
        error: function (e) {
            error_element.innerHTML = 'Server Error, Please contact us.';
            error_element.style.display = 'block';
        }
    });
});





$("#upgradeForm").off().on('submit',function (event) {
    event.preventDefault();

    var Card_Number = document.getElementById('CreditNumber').value;

    var security_number = document.getElementById('csv_number').value;

    var month_exp = document.getElementById('MonthCredit').value;

    var year_exp = document.getElementById('YearCredit').value;

    var error_control = document.getElementById("upgrade_error");

    error_control.style.display = 'none';

    // console.log($("#upgradeForm").attr("data-type"));

    if ($.trim(Card_Number).length !== 16)
    {
        error_control.innerHTML = "Credit # is a 16 digit number.";
        error_control.style.display = 'block';
        return false;
    }
    else if ($.trim(security_number).length !== 3){
        error_control.innerHTML = "Security number at least 3 digits.";
        error_control.style.display = 'block';
        return false;
    }

    $.ajax({
        type: "POST",
        url: "/PutTogether/Upgrade/",
        data: {usr_email: '{{ request.user.email }}', csrfmiddlewaretoken: csrftoken,
            number:Card_Number,security:security_number,m_exp:month_exp,y_exp:year_exp},
        success: function (e) {
            // console.log(e);
            // location.replace('/PutTogether/Projects/'+e.project_id.toString()+'/');
            location.reload(true);    //Why?????

        },
        error: function (e) {
            console.log("error");
        }
    });
});

$("#editModal").on('submit',function (e) {
    e.preventDefault();
});

function editDetails() {

        var projectTitle = document.getElementById("projectTitle").value;
        console.log(projectTitle);

        var members =document.getElementById("teamMembers").value;
        console.log(members);

        var projectid = $('#edit_project_title').attr("projectid");
        console.log(projectid);

        $.ajax({
            type:"POST",
            url:"ChangeProjectDetails/",
            data:{project_id: projectid,members:members,title:projectTitle,csrfmiddlewaretoken:csrftoken},
            success:function (e) {
                location.reload(true)
            },
            error:function (e) {
                console.log(e)
            }
        })
}

$(document).on('click','#editId',function () {
    var project_id = $(this).data('id');
    console.log(project_id);
    $('#edit_project_title').attr("projectid",project_id);

    var element = document.getElementById(project_id);

    var title = element.getElementsByTagName('a')[0].innerHTML;
    var title= $.trim(title);
    console.log(title);
    var createdBy = element.getElementsByTagName('p')[0].innerHTML;
    var createdBy = createdBy.split(':')[1];
    console.log(createdBy);
    // var nMembers = element.getElementsByTagName('p')[1].innerHTML;
    // var nMembers = nMembers.split(':')[1];
    // console.log(nMembers);
    var nTasks = element.getElementsByTagName('p')[2].innerHTML;
    var nTasks = nTasks.split(':')[1];
    console.log(nTasks);
    var date = element.getElementsByTagName('p')[3].innerHTML;
    console.log(date);
    date = date.split('Date &amp; Time Created: ')[1];

    console.log(date);


    document.getElementById("projectTitle").value = title;
    // document.getElementById('project_creation_time').value =formatDate(date+" "+time);
    document.getElementById('project_creation_time').value =date;

});

// function formatDate(date) {
//     var d = new Date(date),
//         month = '' + (d.getMonth() + 1),
//         day = '' + d.getDate(),
//         year = d.getFullYear(),
//         hours=d.getHours(),
//         minutes=d.getMinutes();
//     console.log(d);
//
//     if (month.length < 2)
//         month = '0' + month;
//     if (day.length < 2)
//         day = '0' + day;
//
//     var a=[year,month,day].join('-');
//     var b=[hours,minutes].join(':');
//     return [a,b].join('T');
// }
//

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

$(document).on('click','#deleteId',function () {
    var project_id = $(this).data('id');
    $('#edit_project_title').attr("projectid",project_id);
    var project_id = $("#edit_project_title").attr('projectid')

    $('#deleteConfirmation').data('id',project_id);
    $('#editModal').modal('hide');
    $('#deleteConfirmation').modal('show');
});


function createprojectmodal(){
       $('#projectModal').modal('show');
}


 function deleteProject(){
    var project_id = $("#deleteConfirmation").data('id');
    $('#edit_project_title').attr("projectid",project_id);
    // var project_id = $("#edit_project_title").attr('projectid');
    console.log(project_id);
       $.ajax({
           type:"POST",
           url:"DeleteProject/",
           data:{project_id:project_id,csrfmiddlewaretoken:csrftoken},
           success:function () {
               location.reload(true);
           },
           error:function () {
               console.log("NOT CORRECT");
           }
       })
}




window.addEventListener('keydown', function(e) {
    if (e.keyIdentifier == 'U+000A' || e.keyIdentifier == 'Enter' || e.keyCode == 13) {
        e.preventDefault();
        if (e['path'][7].id === 'inviteModalForm')
        {
                console.log('hre');
                 return false;
        }
    }
}, true);

$(document).on('click','#add-user',function () {
    var project_id = $(this).data('id');
    $("#InviteForm").attr('data-projectid',project_id);

    $.ajax({
        type: "GET",
        url: "getMembers",
        data: {project_id:project_id},
        success: function (e) {
           var  div_element = document.getElementsByClassName('tags_container');
           $('.tags_container').empty();
          $.each(JSON.parse(e['users']),function(index,value){
            $('.tags_container').append("<span data-id="+value['pk']+" class='tag'>"+value['pk']+"<span class='close'></span></span>");
          });

        },
        error: function (e) {
            console.log("NOT");
        }
    });
});

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}


$("#InviteForm").off().on('submit',function (event) {
    event.preventDefault();
    var id = document.getElementById("InviteForm").getAttribute("data-projectid");
    var users = document.getElementById('selectedUsers').value;

    var email_error = document.getElementById('add_user_errors');
    email_error.style.display = 'none';
    var user_array = users.split(',');
    var check = true;

    if ($.trim(users).length !== 0)
    {
            $.each(user_array,function(index,value){

        if (!validateEmail(value))
        {
               check = false;
        }

      });

        if (check === false)
        {
            email_error.innerHTML = 'One or of the emails is not valid';
            email_error.style.display = 'block';
            return;
        }
    }



    $.ajax({
        type: "POST",
        url: "InviteMember",
        data: {users: users ,project_id:id, csrfmiddlewaretoken: csrftoken},
        success: function (e) {

            $('#addUserModal').modal('hide');
            location.reload(true);
        },
        error: function (e) {
            email_error.innerHTML  = "SERVER ERROR";
            email_error.style.display = 'block';

        }
    });
});


