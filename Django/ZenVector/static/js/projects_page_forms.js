$("#projectForm").off().on('submit',function (event) {
    event.preventDefault();
    var project_name = document.getElementById("project_name").value;
    var error_element = document.getElementById("project_name_error");
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

    if ($.trim(Card_Number).length < 16)
    {
        error_control.innerHTML = "Credit # is a 16 digit number.";
        error_control.style.display = 'block';
        return false;
    }
    else if ($.trim(security_number).length < 3){
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
    console.log("func editmodal");
    e.preventDefault();
});

function editDetails() {
    console.log("func editDetails");
        // var assignedTo = document.getElementById("assignedTo").value;
        // console.log(assignedTo);
        //
        // var deadline = document.getElementById("task_edit_deadline").value;
        // console.log(deadline);
        //
        // var detail = document.getElementById("taskDetailsD").value;
        // console.log(detail);
        //
        // var status =document.getElementById("statusD").value;
        // console.log(status);
        //
        // var taskid = $('#edit_task_title').attr("taskid");
        //
        // console.log(taskid);
        //
        // $.ajax({
        //     type:"POST",
        //     url:"ChangeTaskDetails/",
        //     data:{task_id: taskid,assignto:assignedTo,time:deadline,detail:detail,status:status,csrfmiddlewaretoken:csrftoken},
        //     success:function (e) {
        //         location.reload(true)
        //     },
        //     error:function (e) {
        //         console.log(e)
        //     }
        // })
}


$(document).on('click','.menu-button',function () {

        console.log("clicked menu");
        var task_id = $(this).data('id');
        console.log(task_id);

    //
    // var task_id = $(this).data('id');
    // console.log(task_id);
    // $('#edit_task_title').attr("taskid",task_id);
    //
    // var element = document.getElementById(task_id);
    //
    // var element_p = element.getElementsByTagName('p')[0].innerHTML;
    //
    // var details = element_p.split(' Descrip: ')[1].split(' Deadline:')[0];
    //
    // var date = element_p.split("Deadline: ")[1].split(" Given by")[0];
    //
    //
    // var list_title = $(this).parent().parent().parent().attr("id");
    //
    // document.getElementById("taskDetailsD").value = details;
    //
    // document.getElementById('task_edit_deadline').value = formatDate(date);

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


    // var x = confirm("Are you sure you want to delete?");
    // var task_id = $("#edit_task_title").attr('taskid');
    // if (x){
    //
    //    $.ajax({
    //        type:"POST",
    //        url:"DeleteTask/",
    //        data:{taskid:task_id,csrfmiddlewaretoken:csrftoken},
    //        success:function () {
    //            location.reload(true);
    //        },
    //        error:function () {
    //            console.log("NOT CORRECT");
    //        }
    //    })
    // }
    // else{
    //   console.log(x);
    //   return false;
    // }
}