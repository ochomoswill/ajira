/**
 * Created by ochomoswill on 5/23/17.
 */

var loader = ""+
    "<div style='color:white' class='alert alert-info alert-dismissible fade show' role='alert'>" +
        "<button type='button' class='close' data-dismiss='alert' aria-label='Close'>" +
        "<span aria-hidden='true'>&times;</span>" +
        "</button>" +
        "<strong>Kindly wait as we process the data...</strong>" +
        "</div>";


function alert(message) {

    var alert_message = "" +
        "<div style='color:white' class='alert alert-success alert-dismissible fade show' role='alert'>" +
        "<button type='button' class='close' data-dismiss='alert' aria-label='Close'>" +
        "<span aria-hidden='true'>&times;</span>" +
        "</button>" +
        "<strong>"+message+"</strong>" +
        "</div>";

    return alert_message;

}

//For getting CSRF token
function getCookie(name) {
          var cookieValue = null;
          if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
               var cookie = jQuery.trim(cookies[i]);
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) == (name + '=')) {
            cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
             }
          }
      }
    return cookieValue;
}

function post(data, url) {


    var request = new XMLHttpRequest();

    request.open("POST", url, true);

    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    // Only send the token to relative URLs i.e. locally.
    request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    request.onreadystatechange = function() {
        console.log("request.readyState = "+ request.readyState +"request.status = "+ request.status );
        if(request.readyState == 4 && request.status == 200) {

            var obj = JSON.parse(request.responseText);

            if(obj.errormsg)
            {
                document.getElementById("message").innerHTML = "";
                document.getElementById("update_message").innerHTML = alert(obj.errormsg);
            }
            else
            {
                document.getElementById("message").innerHTML = "";
                document.getElementById("update_message").innerHTML = alert(obj.successful);
                window.location="/my_profile/" + obj.slug ;
            }

            console.log("posted the data");
        }

    };

    request.send(data);
}

function setLoader()
{
    document.getElementById("message").innerHTML = loader;
}

function resetLoader()
{
    document.getElementById("message").innerHTML = "";
}


function fetch_post_login_data(){

    setLoader();

    // var url = "{% url 'register_ajiriwa' %}";
    var url = "/login_view/";


    /* ENTERED FIELD DATA */

    var email_address = document.getElementById("emailAddress").value;
    var atpos = email_address.indexOf("@");
    var dotpos = email_address.lastIndexOf(".");
    if (atpos<1 || dotpos<atpos+2 || dotpos+2>=email_address.length) {
        document.getElementById("divEmailAddress").className = "form-group has-danger";
        document.getElementById("emailAddress_validate_text").innerHTML = "The email address is invalid!";
        resetLoader();
        return;
    }else{
        document.getElementById("divEmailAddress").className = "form-group";
        document.getElementById("emailAddress_validate_text").innerHTML = "";
    }


    var pwd = document.getElementById("inputPassword").value;
    if(pwd.length < 8){
        document.getElementById("divInputPassword").className = "form-group has-danger";
        document.getElementById("inputPassword_validate_text").innerHTML = "Password must be at least 8 characters long!";
        resetLoader();
        return;
    }else{
        document.getElementById("divInputPassword").className = "form-group";
        document.getElementById("inputPassword_validate_text").innerHTML = "";
    }

    /* END OF ENTERED FIELD DATA */


    var data = "&email_address="+email_address+
                "&pwd="+pwd;

    post(data,url);


    setTimeout(function() {
        document.getElementById("update_message").innerHTML = "";
    }, 3000);

    //reset form;
    reset_login_form();
}


function reset_login_form()
{
    document.getElementById("emailAddress").value = "";

    document.getElementById("inputPassword").value = "";
}