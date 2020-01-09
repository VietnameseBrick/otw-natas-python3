<?php

$key='qw8J';
$pswd = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$plaintext=json_encode($pswd);
function xor_encrypt($in,$key) {
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$feed=xor_encrypt($plaintext,$key);
$cookie=base64_encode($feed);
echo($cookie);
?>
