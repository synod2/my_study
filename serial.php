<?php
    class superclass{
        //public $first;
        //public $second;
        public $string;
    }
    
    $test = new superclass;
//$test -> first = 'gil';
   // $test -> second = 'no';
    $test -> string = '01041...';
    
    $str = serialize($test);
    echo $str;

    $newtest = unserialize($str);
    
    #echo $newtest->first."<br>";
   # echo $newtest->second."<br>";
    echo $newtest->string."<br>";

?>