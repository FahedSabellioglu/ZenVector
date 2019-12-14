$("#projectForm").off().on('submit',function (event) {
    console.log("project form here");
    event.preventDefault();
    var project_name = document.getElementById("project_name").value;
    console.log(project_name);
    var error_element = document.getElementById("project_name_error");
    console.log(error_element);
    error_element.style.display = 'none';
    if ($.trim(project_name) == '' || $.trim(project_name).length < 3 || $.trim(project_name).length >26) {
        error_element.style.display = 'block';
        return false;
    }
    $.ajax({
        type: "POST",
        url: "CreateProject/",
        data: {usr_email: '{{ request.user.email }}', csrfmiddlewaretoken: csrftoken, p_name: project_name},
        success: function (e) {
            location.reload(true);

        },
        error: function (e) {
            console.log("error");
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

    console.log($("#upgradeForm").attr("data-type"));

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
    var date = date.split(':  ')[1];
    // var date_time=date.split('  ');
    // var date=date_time[0];
    // var time=date_time[1].split(' ')[0];
    // console.log(date);
    // console.log(time);
    // console.log(date+" "+time);


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
    $('#detailModal').modal('hide');
    $('#deleteConfirmation').data('id',project_id);
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


// function sendEmail() {
//     console.log("send clicked");
//     var email = document.getElementById('inviteNewMember').value;
//     console.log(email);
//
//        $.ajax({
//        type:"POST",
//        url:"sendEmail/",
//        data:{csrfmiddlewaretoken:csrftoken},
//        // data:{email:email, csrfmiddlewaretoken:csrftoken},
//        success:function () {
//            location.reload(true);
//        },
//        error:function () {
//            console.log("NOT CORRECT");
//        }
//     })
//
// }






$(document).on('click','#add-user',function () {
    var project_id = $(this).data('id');
    $("#InviteForm").attr('data-projectid',project_id);
});






$("#InviteForm").off().on('submit',function (event) {
    event.preventDefault();
    var id = document.getElementById("InviteForm").getAttribute("data-projectid");
    var users = document.getElementById('selectedUsers').value;


    $.ajax({
        type: "POST",
        url: "InviteMember",
        data: {users: users ,project_id:id, csrfmiddlewaretoken: csrftoken},
        success: function (e) {
            console.log("HERE");
            //
            // $('#addUserModal').modal('hide');
            // Location.reload(true);
        },
        error: function (e) {
            console.log("ERROR");
            // error_control.innerHTML  = e.responseJSON.reason;
            // error_control.style.display = 'block';

        }
    });
});
