/**
 * Created by ochomoswill on 6/2/17.
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

function post_job_details(){

    setLoader();

    var url = "/post_job_details/";


    /* ENTERED FIELD DATA */
    //var jobTitle = document.getElementById("jobTitle").value;

    var jobTitleObj = document.getElementById("jobTitle");
    var jobTitle = jobTitleObj.options[jobTitleObj.selectedIndex].text;

    var jobDescription = document.getElementById("jobDescription").value;

    /*getting the constituency name from dropdown list*/
    var selectConstituencyObj = document.getElementById("selectConstituency");
    var constituency = selectConstituencyObj.options[selectConstituencyObj.selectedIndex].value;

    /*getting the county name from dropdown list*/
    var selectCountyObj = document.getElementById("selectCounty");
    var county = selectCountyObj.options[selectCountyObj.selectedIndex].value;

    // var phoneNumber = document.getElementById("phoneNumber").value;



    /* END OF ENTERED FIELD DATA */


    var data = "&jobTitle="+jobTitle+
        "&jobDescription="+jobDescription+
        "&constituency="+constituency+
        "&county="+county;

    post(data,url);


    setTimeout(function() {
        document.getElementById("update_message").innerHTML = "";
    }, 3000);

    //reset form;
    reset_post_job_form();
}


function reset_post_job_form()
{
    //document.getElementById("jobTitle").value = "";
    var jobTitleObj = document.getElementById("jobTitle");
    jobTitleObj.value = "INIT";

    document.getElementById("jobDescription").value = "";

    var selectConstituencyObj = document.getElementById("selectConstituency");
    selectConstituencyObj.value = "INIT";

    var selectCountyObj = document.getElementById("selectCounty");
    selectCountyObj.value = "INIT";

    document.getElementById("phoneNumber").value = "";

}
