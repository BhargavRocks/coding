<!DOCTYPE html>
<head>
<title>This is my website </title>
<style>


</style>
</head>
<body>
      <h1> Hi welcome to my site! </h1><hr>
      
    
<p id="note"> This is the text going to changed when you will click on button below me </P>
<script>
function myfunction{   
							document.getElementById('note').innerHTML="hello world!";
                   }
</script>
<button type="button" onclick="myfunction()"> Click here </button>
	

</body>
</html>
