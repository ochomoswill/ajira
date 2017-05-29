/**
 * Created by ochomoswill on 5/21/17.
 */

var loader = ""+
    "<div class='alert alert-info alert-dismissible fade show' role='alert'>" +
        "<button type='button' class='close' data-dismiss='alert' aria-label='Close'>" +
        "<span aria-hidden='true'>&times;</span>" +
        "</button>" +
        "<strong>KIndly wait as we process the data...</strong>" +
        "</div>";


function alert(message) {

    var alert_message = "" +
        "<div class='alert alert-success alert-dismissible fade show' role='alert'>" +
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

            document.getElementById("message").innerHTML = "";
            document.getElementById("update_message").innerHTML = alert(obj.data);



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

function reg_ajiriwa(){

    setLoader();

    // var url = "{% url 'register_ajiriwa' %}";
    var url = "/register_ajiriwa/";


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


    var name = document.getElementById("fullName").value;


    var idNumber = document.getElementById("idNumber").value;
    if(idNumber.length < 8)
    {
        document.getElementById("divIdNumber").className = "form-group has-danger";
        document.getElementById("idNumber_validate_text").innerHTML = "ID Number must be 6 digits!";
        resetLoader();
        return;
        if(idNumber.length > 8)
        {
            document.getElementById("divIdNumber").className = "form-group has-danger";
            document.getElementById("idNumber_validate_text").innerHTML = "ID Number must be 6 digits!";
            return;
        }
    }else{
        document.getElementById("divIdNumber").className = "form-group";
        document.getElementById("idNumber_validate_text").innerHTML = "";
    }



    var birthDate = document.getElementById("birthDate").value;


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


    var confirm_pwd = document.getElementById("retypedPassword").value;
    if (confirm_pwd != pwd) {
        document.getElementById("divRetypedPassword").className = "form-group has-danger";
        document.getElementById("retypedPassword_validate_text").innerHTML = "Passwords don't not match!";
        resetLoader();
        return;
    }else{
        document.getElementById("divRetypedPassword").className = "form-group";
        document.getElementById("retypedPassword_validate_text").innerHTML = "";
    }


    /*getting the landlord name from dropdown list*/
    var selectConstituencyObj = document.getElementById("selectConstituency");
    var constituency = selectConstituencyObj.options[selectConstituencyObj.selectedIndex].value;


    /*getting the landlord name from dropdown list*/
    var selectCountyObj = document.getElementById("selectCounty");
    var county = selectCountyObj.options[selectCountyObj.selectedIndex].value;


    /*getting the country from dropdown list*/
    var selectSkillObj = document.getElementById("selectSkill");
    var skills = selectSkillObj.options[selectSkillObj.selectedIndex].value;


    var phoneNumber = document.getElementById("phoneNumber").value;
    var termsCondition = document.getElementById("terms_conditions").value;


    /* END OF ENTERED FIELD DATA */


    var data = "&email_address="+email_address+
        "&name="+name+
        "&idNumber="+idNumber+
        "&birthDate="+birthDate+
        "&pwd="+pwd+
        "&constituency="+constituency+
        "&county="+county+
        "&skills="+skills+
        "&phoneNumber="+phoneNumber;

    post(data,url);


    setTimeout(function() {
        document.getElementById("update_message").innerHTML = "";
    }, 3000);

    //reset form;
    reset_ajiriwa_registration_form();
}


function reset_ajiriwa_registration_form()
{
    document.getElementById("emailAddress").value = "";

    document.getElementById("fullName").value = "";

    document.getElementById("idNumber").value = "";

    document.getElementById("birthDate").value = "";

    document.getElementById("inputPassword").value = "";

    document.getElementById("retypedPassword").value = "";

    /*getting the constituency from dropdown list*/
    var selectConstituencyObj = document.getElementById("selectConstituency");
    selectConstituencyObj.value = "INIT";

    /*getting the county from dropdown list*/
    var selectCountyObj = document.getElementById("selectCounty");
    selectCountyObj.value = "INIT";

    /*getting the skills from dropdown list*/
    var selectSkillObj = document.getElementById("selectSkill");
    selectSkillObj.value = "INIT";

    document.getElementById("phoneNumber").value = "";

    document.getElementById("terms_conditions").checked = false;
}
