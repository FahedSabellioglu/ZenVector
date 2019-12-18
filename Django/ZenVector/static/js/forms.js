 $("#SignUpForm").on('submit',function (e) {
        e.preventDefault();
    });

$("#loginForm").on('submit',function(e){
    e.preventDefault();
});

$('form input').keydown(function (e) {
    if (e.keyCode == 13) {
        console.log('here check');
        e.preventDefault();
        return false;
    }
});

function loginControl(){
    var email_element = document.getElementById('email_login');
    var password_element = document.getElementById('password_login');
    var element = document.getElementById('password_error_login');

    element.style.display = 'none';


    email = email_element.value;
    password = password_element.value;

    $.ajax({
        type: "POST",
        url: "Login/",
        data:{mail:email,password:password,csrfmiddlewaretoken: csrftoken},
        success: function(e) {
            location.href = "/PutTogether/Projects/";
       },
        error:function(e){
            var element = document.getElementById('password_error_login');
            var message = e.responseJSON.reason;
            element.innerHTML = message;
            element.style.display='block'
        }

    })
}

function Control(event) {

        usr_name = document.getElementById("usr_name").value;
        email = document.getElementById("email").value;
        password = document.getElementById("password").value;
        repeat = document.getElementById("password_repeat").value;

        acc_type = $("#signupModal").attr('data-type');
        console.log(acc_type);

        document.getElementById("name_error").style.display = 'none';
        var email_error = document.getElementById("email_error");
        email_error.style.display = 'none';
        document.getElementById('password_error').style.display = 'none';
        document.getElementById('repeat_error').style.display = 'none';

        if ($.trim(usr_name)=== '' || usr_name.length < 6)
        {
            document.getElementById('name_error').style.display='block';

            return;
        }

        if ($.trim(email) === '')
        {
            email_error.style.display ='block';
            return;
        }

        if (password.length < 8)
        {

            document.getElementById('password_error').style.display='block';
            return;
        }

        if (password !== repeat)
        {
            document.getElementById('repeat_error').style.display = 'block';
            return;
        }


        $("#"+event.id).attr("disabled", true);
        $("#"+event.id).removeClass('active_button');

        $.ajax({
            type:'POST',
            url:"Signup/",
            data:{name:usr_name,mail:email,pass:password,csrfmiddlewaretoken:csrftoken,acc_type:acc_type},
            success: function (e) {
                $("#"+event.id).attr("disabled", false);
                $("#"+event.id).addClass('active_button');

                location.reload(true);
            },
            error:function (e) {

                $("#"+event.id).attr("disabled", false);
                $("#"+event.id).addClass('active_button');
            email_error.innerHTML = e.responseJSON.reason;
            email_error.style.display = 'block';
            }
        });


    }

$(document).on('click', ".plans",function () {

    var value = $(this).data('type');
    $("#signupModal").attr("data-type",value);
    $("#planPricingModal").attr("data-type",value);
    $("#UpgradeModal").attr("data-type",value);
    console.log(value);
    $("#downGrade").attr("data-type",value);

});

$("#downGradeForm").off().on('submit',function (event) {
    event.preventDefault();
    var account_type = $("#downGrade").attr("data-type");

    var error_control = document.getElementById("projects_count");
    error_control.style.display = "none";
    $.ajax({
        type: "POST",
        url: "/PutTogether/DownGrade/",
        data: {usr_email: '{{ request.user.email }}', csrfmiddlewaretoken: csrftoken,account_type:account_type},
        success: function (e) {
            location.reload(true);    //Why?????

        },
        error: function (e) {
            console.log(e);
            error_control.innerHTML = e.responseJSON.reason;
            error_control.style.display='block';
        }
    });
});

// a function to hide the login modal and show the forgot modal
function ForgotPassModal(){
    $('#loginModal').modal('hide');
    $('#forgotPasswordModal').modal('show');
}

// Sending Code to user ( Forgot Pass )
$("#ForgotPasswordForm").off().on('submit',function (event) {
    // SENDING AN EMAIL TO THE USER
    event.preventDefault();

    var usr_email = document.getElementById('email_forgot_pass');

    var error_control = document.getElementById('email_error_forgot');

    var inputgroup = document.getElementById("forget_password_gorup");

    error_control.style.display = 'none';

    $.ajax({
        type: "POST",
        url: "/PutTogether/forgotPass/",
        data: {usr_email: usr_email.value , csrfmiddlewaretoken: csrftoken},
        success: function (e) {
            document.getElementById("ModalMessageTitle").innerHTML = 'Notification';
            document.getElementById("ModelMessage").innerHTML = "Please check your email.";
            $('#forgotPasswordModal').modal('hide');
            $("#Notification").modal("show");
        },
        error: function (e) {
            error_control.innerHTML  = e.responseJSON.reason;
            error_control.style.display = 'block';

        }
    });
});

// NOT USED, JUST KEEP IT
// $("#ForgotPasswordCodeForm").off().on('submit',function (event) {
//     event.preventDefault();
//
//     var code = document.getElementById('email_forgot_Code').value;
//
//     var error_control = document.getElementById('email_error_Code');
//
//     var usr_email =  $('#forgorPasswordCodeModal').attr('data-email');
//
//     error_control.style.display = 'none';
//     $.ajax({
//         type: "POST",
//         url: "/PutTogether/CheckCode/",
//         data: {usr_email: usr_email, code:code , csrfmiddlewaretoken: csrftoken},
//         success: function (e) {
//             $('#forgorPasswordCodeModal').modal('hide');
//             $('#PasswordResetModal').attr('data-email',usr_email);
//             $('#PasswordResetModal').modal('show');
//         },
//         error: function (e) {
//             error_control.innerHTML = e.responseJSON.reason;
//             error_control.style.display = 'block';
//
//         }
//     });
// });
// $("#passwordResetForm").off().on('submit',function (event) {
//     event.preventDefault();
//     var password_first = document.getElementById("first_password_Reset").value;
//     var first_error = document.getElementById("first_pass_control_Reset");
//
//     var password_second = document.getElementById('second_password_Reset').value;
//     var second_error = document.getElementById("second_pass_control_Reset");
//
//     var usr_email = $("#PasswordResetModal").attr("data-email");
//
//     first_error.style.display = 'none';
//     second_error.style.display = 'none';
//
//     if ($.trim(password_first) === '' || $.trim(password_first).length < 8) {
//         first_error.style.display = 'block';
//         return false;
//     }
//     else if ($.trim(password_first) !== $.trim(password_second))
//     {
//         second_error.style.display = 'block';
//         return false;
//     }
//
//     $.ajax({
//         type: "POST",
//         url: "/PutTogether/PasswordReset/",
//         data: {password:password_first, email:usr_email, csrfmiddlewaretoken: csrftoken},
//         success: function () {
//             location.reload(true);
//         },
//         error: function () {
//             second_error.innerHTML = "Something went wrong, Try again";
//             second_error.style.display = 'block';
//         }
//     });
// });

//Upgrading from a plan to a higher plan ( Home Page Code only )
$("#upgradeForm").off().on('submit',function (event) {
    event.preventDefault();

    var Card_Number = document.getElementById('CreditNumber').value;

    var security_number = document.getElementById('csv_number').value;

    var month_exp = document.getElementById('MonthCredit').value;

    var year_exp = document.getElementById('YearCredit').value;

    var error_control = document.getElementById("upgrade_error");

    var account_type = $("#UpgradeModal").attr("data-type");

    error_control.style.display = 'none';

    if ($.trim(Card_Number).length !== 16)
    {
        console.log("HERER");
        error_control.innerHTML = "Credit # is a 16 digit number.";
        error_control.style.display = 'block';
        return;
    }
    else if ($.trim(security_number).length !== 3){
        error_control.innerHTML = "Security number at least 3 digits.";
        error_control.style.display = 'block';
        return;
    }
    $.ajax({
        type: "POST",
        url: "/PutTogether/Upgrade/",
        data: {usr_email: '{{ request.user.email }}', csrfmiddlewaretoken: csrftoken,
            number:Card_Number,security:security_number,m_exp:month_exp,y_exp:year_exp,account_type:account_type},
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

// Buying a plan in the first signup
$("#planPricingModal").off().on('submit',function (event) {
    event.preventDefault();

    var account_type = $(this).attr('data-type');

    var username = document.getElementById("p_usr_name").value;

    var email = document.getElementById("p_email").value;

    var password = document.getElementById("p_password").value;

    var repeat_password = document.getElementById("p_password_repeat").value;

    var credit_number = document.getElementById('creditCardNumber').value;

    var security_number = document.getElementById("p_secu_num").value;

    var exp_month = document.getElementById("expmonth").value;

    var exp_year = document.getElementById('yearExp').value;


    var error_control = document.getElementById("plan_error");

    error_control.style.display = 'none';


    if ($.trim(username) === '' || username.length < 6)
    {
        error_control.innerHTML = 'Please provide a meaningful name.';
        error_control.style.display = 'block';

        return
    }

    if ($.trim(email).length === 0)
    {
        error_control.innerHTML = "Email can't be empty";
    error_control.style.display = 'block';

        return
    }

    if (password.length < 8)
    {
        error_control.innerHTML = "Password should be more than 8 characters";
        error_control.style.display = 'block';

        return;
    }

    if (password !== repeat_password)
    {
        error_control.innerHTML = "Passwords do not match";
         error_control.style.display = 'block';

        return;
    }

    if ($.trim(credit_number).length !== 16){
        error_control.innerHTML = "Credit Card Number is a 16 digits number";
        error_control.style.display = 'block';
        return;
    }
    if (isNaN($.trim(credit_number))){
        error_control.innerHTML = "Credit Card Number is a 16 digits number";
        error_control.style.display = 'block';
        return;
    }

    if ($.trim(security_number).length !== 3){
        error_control.innerHTML = "Security Number is a 3 digits number";
        error_control.style.display = 'block';
        return;
    }

    if (isNaN($.trim(security_number))){
        error_control.innerHTML = "Security Number is a 3 digits number";
        error_control.style.display = 'block';
        return;
    }

    $.ajax({
        type: "POST",
        url: "/PutTogether/PlanBuy/",
        data: {csrfmiddlewaretoken: csrftoken, credit_n :credit_number,sec_n :security_number,exp_m: exp_month,exp_y: exp_year,
               mail:email,pass:password,name:username,acc_type:account_type},
        success: function (e) {
            location.reload(true);

        },
        error: function (e) {
            error_control.innerHTML = e.responseJSON.reason;
            error_control.style.display = 'block';
        }
    });
});

// Reset Password
$("#PasswordModal").off().on('submit',function (event) {
    event.preventDefault();
    var password_first = document.getElementById("first_password").value;
    var first_error = document.getElementById("first_pass_control");


    var password_second = document.getElementById('second_password').value;
    var second_error = document.getElementById("second_pass_control");

    first_error.style.display = 'none';
    second_error.style.display = 'none';


    if ($.trim(password_first) === '' || $.trim(password_first).length < 8) {
        first_error.style.display = 'block';
        return false;
    }
    else if ($.trim(password_first) !== $.trim(password_second))
    {
        second_error.style.display = 'block';
        return false;
    }

    $.ajax({
        type: "POST",
        url: "/PutTogether/PasswordChange/",
        data: {password:password_first, csrfmiddlewaretoken: csrftoken},
        success: function () {
            location.reload(true);
        },
        error: function () {
            console.log("error");
        }
    });
});

$("#DeleteModel").off().on('submit',function (event) {
    event.preventDefault();
    var password = document.getElementById("delete_password").value;
    var password_error = document.getElementById("delete_password_control");

    password_error.style.display = 'none';

    if ($.trim(password) == '' || $.trim(password).length < 8) {
        password_error.style.display = 'block';
        return false;
    }

    $.ajax({
        type: "POST",
        url: "/PutTogether/DeleteAccount/",
        data: {password:password, csrfmiddlewaretoken: csrftoken},
        success: function (e) {
            location.reload(true);
        },
        error: function (e) {
            password_error.innerHTML = e.responseJSON.reason;
            password_error.style.display = 'block';
        }
    });
});


$('.modal').on('hidden.bs.modal', function(){
    $(this).find('form')[0].reset();
});
