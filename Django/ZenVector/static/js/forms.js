 $("#SignUpForm").on('submit',function (e) {
        e.preventDefault();
    });

$("#loginForm").on('submit',function(e){
    e.preventDefault();
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
                location.reload(true);

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

        document.getElementById("name_error").style.display = 'none';
        var email_error = document.getElementById("email_error");
        email_error.style.display = 'none';
        document.getElementById('password_error').style.display = 'none';
        document.getElementById('repeat_error').style.display = 'none';




        if ($.trim(usr_name)== '' || usr_name.length < 6)
        {
            document.getElementById('name_error').style.display='block';

            return
        }

        if ($.trim(email) == '')
        {
            email_error.style.display ='block';
            return
        }

        if (password.length < 8)
        {
            document.getElementById('password_error').style.display='block';
            return;
        }

        if (password != repeat)
        {

            document.getElementById('repeat_error').style.display = 'block';
            return;
        }

        $.ajax({
            type:'POST',
            url:"Signup/",
            data:{name:usr_name,mail:email,pass:password,csrfmiddlewaretoken:csrftoken},
            success: function (e) {
                location.reload(true);
            },
            error:function (e) {
            email_error.innerHTML = e.responseJSON.reason;
            email_error.style.display = 'block';
            }
        });


    }


$(document).on('click', ".plans",function () {

    var value = $(this).data('type');
    $("#planPricingModal").attr("data-type",value);
});


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


    var error_control = document.getElementById("upgrade_error");

    error_control.style.display = 'none';


    if ($.trim(username)== '' || username.length < 6)
    {
        error_control.innerHTML = 'Please provide a meaningful name.';
        error_control.style.display = 'block';

        return
    }

    if ($.trim(email).length == 0)
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

    if (password != repeat_password)
    {
        error_control.innerHTML = "Passwords do not match";
         error_control.style.display = 'block';

        return;
    }

    if ($.trim(credit_number).length < 16){
        error_control.innerHTML = "Credit Card Number is a 16 digits number";
        error_control.style.display = 'block';
        console.log()
        return;
    }


    $.ajax({
        type: "POST",
        url: "/PutTogether/PlanBuy/",
        data: {csrfmiddlewaretoken: csrftoken, credit_n :credit_number,sec_n :security_number,exp_m: exp_month,exp_y: exp_year,
               mail:email,password:password,name:username,acc_type:account_type},
        success: function (e) {
            location.reload(true);

        },
        error: function (e) {
            error_control.innerHTML = e.responseJSON.reason;
            error_control.style.display = 'block';
            console.log(e);
            console.log("error");
        }
    });
});

$("#PasswordModal").off().on('submit',function (event) {
    event.preventDefault();
    var password_first = document.getElementById("first_password").value;
    var first_error = document.getElementById("first_pass_control");


    var password_second = document.getElementById('second_password').value;
    var second_error = document.getElementById("second_pass_control");

    first_error.style.display = 'none';
    second_error.style.display = 'none';


    if ($.trim(password_first) == '' || $.trim(password_first).length < 8) {
        first_error.style.display = 'block';
        return false;
    }
    else if ($.trim(password_first) != $.trim(password_second))
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



