<?php

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$data = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D" ;

echo json_encode($defaultdata); 
?>

<br><br><br>

<?php

echo base64_decode($data);

?>