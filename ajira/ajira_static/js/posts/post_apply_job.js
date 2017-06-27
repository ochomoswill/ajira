/**
 * Created by ochomoswill on 6/16/17.
 */
var loader = ""+
    "<div style='color:white' class='alert alert-info alert-dismissible fade show' role='alert'>" +
        "<button type='button' class='close' data-dismiss='alert' aria-label='Close'>" +
        "<span aria-hidden='true'>&times;</span>" +
        "</button>" +
        "<strong>KIndly wait as we process the data...</strong>" +
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

function job_application(){

    setLoader();

    // var url = "{% url 'register_ajiriwa' %}";
    var url = "/applicant_details/";


    /* ENTERED FIELD DATA */
    var applicantEmail = document.getElementById("emailAddress").value;
    var applicantPhoneNo = document.getElementById("phoneNo").value;
    var jobId = document.getElementById("btnWithJobID").value;



    /* END OF ENTERED FIELD DATA */


    var data = "&applicantEmail="+applicantEmail+
            "&jobId="+jobId+
        "&applicantPhoneNo="+applicantPhoneNo;

    post(data,url);


    setTimeout(function() {
        document.getElementById("update_message").innerHTML = "";
    }, 3000);

    //reset form;
    reset_job_application_form();
}


function reset_job_application_form()
{
    document.getElementById("phoneNo").value = "";

}
