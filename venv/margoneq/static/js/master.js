$(document).ready(function(){

        $("#sendregister").click(function(){
            $.ajax({
                type: "POST",
                url: $("$registrationForm").data('url'),
                success: function(response){
                   $("#validAlert").setText(response.alertvalue.value);
    }
 });
        }
    }
