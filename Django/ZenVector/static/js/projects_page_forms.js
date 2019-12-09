$("#projectForm").off().on('submit',function (event) {
    console.log("project form here");
    event.preventDefault();
    var project_name = document.getElementById("project_name").value;
    console.log(project_name);
    var error_element = document.getElementById("project_name_error");
    console.log(error_element);
    error_element.style.display = 'none';
    if ($.trim(project_name) == '' || $.trim(project_name).length < 3) {
        error_element.style.display = 'block';
        return false;
    }
    $.ajax({
        type: "POST",
        url: "CreateProject/",
        data: {usr_email: '{{ request.user.email }}', csrfmiddlewaretoken: csrftoken, p_name: project_name},
        success: function (e) {
            // location.replace('/PutTogether/Projects/'+e.project_id.toString()+'/');
            location.reload(true);    //Why?????

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

    return false;



<<<<<<< Updated upstream
    // $.ajax({
    //     type: "POST",
    //     url: "/PutTogether/Upgrade/",
    //     data: {usr_email: '{{ request.user.email }}', csrfmiddlewaretoken: csrftoken,
    //         number:Card_Number,security:security_number,m_exp:month_exp,y_exp:year_exp},
    //     success: function (e) {
    //         // console.log(e);
    //         // location.replace('/PutTogether/Projects/'+e.project_id.toString()+'/');
    //         location.reload(true);    //Why?????
    //
    //     },
    //     error: function (e) {
    //         console.log("error");
    //     }
    // });
=======
    $.ajax({
        type: "POST",
        url: "CreateProject/",
        // usr_email: '{{ request.user.email }}',
        data: { csrfmiddlewaretoken: csrftoken, p_name: project_name},
        success: function (e) {
            // location.replace('/PutTogether/Projects/'+e.project_id.toString()+'/');
            location.reload(true);

        },
        error: function () {
            console.log("error");
        }
    });
>>>>>>> Stashed changes
});



$("#editModal").on('submit',function (e) {
    console.log("func editmodal");
    e.preventDefault();
});

function editDetails() {

        var projectTitle = document.getElementById("projectTitle").value;
        console.log(projectTitle);

        var project_creation_time = document.getElementById("project_creation_time").value;
        console.log(project_creation_time);

        // var projectDetails = document.getElementById("projectDetails").value;
        // console.log(projectDetails);

        var members =document.getElementById("teamMembers").value;
        console.log(members);

        var projectid = $('#edit_project_title').attr("projectid");
        console.log(projectid);

        $.ajax({
            type:"POST",
            url:"ChangeProjectDetails/",
            data:{project_id: projectid,members:members,title:projectTitle,time:project_creation_time,csrfmiddlewaretoken:csrftoken},
            // data:{project_id: projectid,members:members,title:projectTitle,time:project_creation_time,detail:projectDetails,csrfmiddlewaretoken:csrftoken},
            success:function (e) {
                location.reload(true)
            },
            error:function (e) {
                console.log(e)
            }
        })
}


$(document).on('click','#edit-t',function () {
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
    var nMembers = element.getElementsByTagName('p')[1].innerHTML;
    var nMembers = nMembers.split(':')[1];
    console.log(nMembers);
    var nTasks = element.getElementsByTagName('p')[2].innerHTML;
    var nTasks = nTasks.split(':')[1];
    console.log(nTasks);
    var date = element.getElementsByTagName('p')[3].innerHTML;
    var date = date.split(':')[3];
    console.log(date);

    document.getElementById("projectTitle").value = title;
    // document.getElementById("projectDetails").value = "bla bla and bla";
    document.getElementById('project_creation_time').value = formatDate(date);

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


 function deleteProject(){

    console.log("func delete");
    var x = confirm("Are you sure you want to delete?");
    var project_id = $("#edit_project_title").attr('projectid');
    if (x){

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
    else{
      console.log(x);
      return false;
    }
}


function sendEmail() {
    console.log("send clicked");
    var email = document.getElementById('inviteNewMember').value;
    console.log(email);

       $.ajax({
       type:"POST",
       url:"sendEmail/",
       data:{csrfmiddlewaretoken:csrftoken},
       // data:{email:email, csrfmiddlewaretoken:csrftoken},
       success:function () {
           location.reload(true);
       },
       error:function () {
           console.log("NOT CORRECT");
       }
    })

}