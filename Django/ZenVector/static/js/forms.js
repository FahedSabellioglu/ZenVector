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
                console.log(e.responseJSON.reason);
            },
            error:function (e) {
            email_error.innerHTML = e.responseJSON.reason;
            email_error.style.display = 'block';
            }
        });


    }

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
        success: function () {
            location.replace('/PutTogether/');
        },
        error: function () {
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



