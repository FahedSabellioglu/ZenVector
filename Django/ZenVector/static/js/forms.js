 $("#SignUpForm").on('submit',function (e) {
        e.preventDefault();
    });

$("#loginForm").on('submit',function(e){
    e.preventDefault();
})

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
