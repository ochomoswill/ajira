/**
 * Created by ochomoswill on 6/1/17.
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

function post(data, url, message_id, update_message_id) {


    var request = new XMLHttpRequest();

    request.open("POST", url, true);

    request.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    // Only send the token to relative URLs i.e. locally.
    request.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
    request.onreadystatechange = function() {
        console.log("request.readyState = "+ request.readyState +"request.status = "+ request.status );
        if(request.readyState == 4 && request.status == 200) {

            var obj = JSON.parse(request.responseText);

            document.getElementById(message_id).innerHTML = "";
            document.getElementById(update_message_id).innerHTML = alert(obj.data);

            // document.getElementById("experience_message").innerHTML = "";
            // document.getElementById("experience_update_message").innerHTML = alert(obj.data);



            console.log("posted the data");
        }

    };

    request.send(data);
}

function setLoader(message_id)
{
    document.getElementById(message_id).innerHTML = loader;
    // document.getElementById("experience_message").innerHTML = loader;
}

function resetLoader(message_id)
{
    document.getElementById(message_id).innerHTML = "";
    // document.getElementById("experience_message").innerHTML = "";
}


function getEditFieldValues()
{

    setLoader("message");

    var url = "/update_profile_details/";

    var fullname = document.getElementById("fullName").value;
    var about = document.getElementById("about").value;
    var constituencyObj = document.getElementById("selectConstituency");
    var constituency = constituencyObj.options[constituencyObj.selectedIndex].value;

    var countyObj = document.getElementById("selectCounty");
    var county = countyObj.options[countyObj.selectedIndex].value;

    var skills = document.getElementById("addSkill").value;
    var phoneNumber= document.getElementById("phoneNumber").value;

    var preferredLocationObj = document.getElementById("preferredLocation");
    var preferredLocation = preferredLocationObj.options[preferredLocationObj.selectedIndex].text;

    var expectedSalary = document.getElementById("expectedSalary").value;

    var data = "&fullname="+fullname+
        "&about="+about+
        "&constituency="+constituency+
        "&county="+county+
        "&skills="+skills+
        "&phoneNumber="+phoneNumber+
        "&preferredLocation="+preferredLocation+
        "&expectedSalary="+expectedSalary;

    post(data,url, "message", "update_message");


    setTimeout(function() {
        document.getElementById("update_message").innerHTML = "";
    }, 3000);


}

function getAddExperienceValues()
{

    setLoader("experience_message");

    var url = "/add_experience/";

    var jobTitle = document.getElementById("jobTitle").value;
    var company = document.getElementById("company").value;
    var location = document.getElementById("location").value;
    var fromDate = document.getElementById("fromDate").value;
    var toDate = document.getElementById("toDate").value;
    var jobDescription = document.getElementById("jobDescription").value;


    var data = "&jobTitle="+jobTitle+
        "&company="+company+
        "&location="+location+
        "&fromDate="+fromDate+
        "&toDate="+toDate+
        "&jobDescription="+jobDescription;

    post(data,url, "experience_message","experience_update_message");


    setTimeout(function() {
        document.getElementById("experience_update_message").innerHTML = "";
    }, 3000);

    resetAddExperienceValues();


}

function resetAddExperienceValues()
{

    document.getElementById("jobTitle").value = "";
    document.getElementById("company").value = "";
    document.getElementById("location").value = "";
    document.getElementById("fromDate").value = "";
    document.getElementById("toDate").value = "";
    document.getElementById("jobDescription").value = "";



}

