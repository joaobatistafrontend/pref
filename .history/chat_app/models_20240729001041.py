<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body {
  margin: 0 auto;
  max-width: 800px;
  padding: 0 20px;
}

.container {
  border: 2px solid #dedede;
  background-color: #f1f1f1;
  border-radius: 5px;
  padding: 10px;
  margin: 10px 0;
}

.darker {
  border-color: #ccc;
  background-color: #ddd;
}

.container::after {
  content: "";
  clear: both;
  display: table;
}

.container img {
  float: left;
  max-width: 60px;
  width: 100%;
  margin-right: 20px;
  border-radius: 50%;
}

.container img.right {
  float: right;
  margin-left: 20px;
  margin-right:0;
}

.time-right {
  float: right;
  color: #aaa;
}

.time-left {
  float: left;
  color: #999;
}
</style>
<script   src="https://code.jquery.com/jquery-3.1.1.min.js"   integrity="sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8="   crossorigin="anonymous"></script>
</head>
<body>

<h2>{{room}} - DjChat</h2>

<div id="display">

<!-- <div class="container darker">
  <b>Tom</b><p>Hello Everyone, How Are You Guys Doing?</p>
  <span class="time-left">20th, April 2021</span>
</div> -->

</div>

<script>
$(document).ready(function(){

setInterval(function(){
    $.ajax({
        type: 'GET',
        url : "/getMessages/{{room}}/",
        success: function(response){
            console.log(response);
            $("#display").empty();
            for (var key in response.messages)
            {
                var temp="<div class='container darker'><b>"+response.messages[key].user+"</b><p>"+response.messages[key].value+"</p><span class='time-left'>"+response.messages[key].date+"</span></div>";
                $("#display").append(temp);
            }
        },
        error: function(response){
            alert('An error occured')
        }
    });
},1000);
})
</script>


<div class="container">
    <style>
    input[type=text], select {
    width: 100%;
    padding: 12px 20px;
    margin: 8px 0;
    display: inline-block;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    }

    input[type=submit] {
    width: 100%;
    background-color: #4CAF50;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    }

    input[type=submit]:hover {
    background-color: #45a049;
    }

    div {
    border-radius: 5px;
    background-color: #f2f2f2;
    padding: 20px;
    }
    </style>

    <form id="post-form">
        {% csrf_token %}
        <input type="hidden" name="username" id="username" value="{{username}}"/>
        <input type="hidden" name="room_id" id="room_id" value="{{room_details.id}}"/>
        <input type="text" name="message" id="message" width="100px" />
        <input type="submit" value="Send">
    </form>
</div>


</body>

<script type="text/javascript">
  $(document).on('submit','#post-form',function(e){
    e.preventDefault();

    $.ajax({
      type:'POST',
      url:'/send',
      data:{
          username:$('#username').val(),
          room_id:$('#room_id').val(),
          message:$('#message').val(),
        csrfmiddlewaretoken:$('input[name=csrfmiddlewaretoken]').val(),
      },
      success: function(data){
         //alert(data)
      }
    });
    document.getElementById('message').value = ''
  });
</script>

</html>