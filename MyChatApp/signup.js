function hasNumbers(t)
{
return /\d/.test(t);
}
var currentuser;
function signajaxrequest(){
            var username = document.getElementById("username").value;
            var letters = /^[0-9a-zA-Z]+$/;
            var first_name = document.getElementById("first_name").value;
            var last_name = document.getElementById("last_name").value;
            var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
            var email = document.getElementById("email").value;
            var password = document.getElementById("password").value;
            if(!username.match(letters) || jQuery.isEmptyObject(username))
            {

                alert('username must comprises of alphanumeric characters only');
            }
            else if(hasNumbers(first_name) || jQuery.isEmptyObject(first_name) ||hasNumbers(last_name) || jQuery.isEmptyObject(last_name)){
              alert("first and last name should not be empty and should not contain a number");

            }
            else if (!email.match(mailformat) ||jQuery.isEmptyObject(email)) {

              alert('enter a proper email');
            }
            else if (password.length<8 || jQuery.isEmptyObject(password)) {
              alert('password length must be atleast 8 characters');

            }
            else {

        $.ajax({
        method:'POST',
        url: 'http://127.0.0.1:8000/user/createprofile',
//        contentType: 'application/json',
        data: {
          'first_name' : first_name,
          'last_name'  : last_name,
          'username'   : username,
          'email'      : email,
          'password'   :password,
          'profile_pic': null,
        },
        dataType: 'json',
        success: function (data) {
            currentuser=data.data.username;
            alert(data.data.username);
            window.open('Login Page.html',"_self")

        }
      });
    }
    }


    function loginajaxrequest(){
                var username = document.getElementById("username").value;
                var letters = /^[0-9a-zA-Z]+$/;

                var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
                var email = document.getElementById("email").value;
                var password = document.getElementById("password").value;
                if(!username.match(letters) || jQuery.isEmptyObject(username))
                {

                    alert('username must comprises of alphanumeric characters only');
                }
                else if (!email.match(mailformat) ||jQuery.isEmptyObject(email)) {

                  alert('enter a proper email');
                }
                else if (password.length<8 || jQuery.isEmptyObject(password)) {
                  alert('password length must be atleast 8 characters');

                }
                else {

            $.ajax({
            method:'POST',
            url: 'http://127.0.0.1:8000/user/login',
    //        contentType: 'application/json',
            data: {
              'username'   : username,
              'email'      : email,
              'password'   :password,
            },
            dataType: 'json',
            success: function (data) {
                currentuser=username;
                alert(data.key);
                window.open('chat_box.html',"_self")

            }
          });
        }
        }
