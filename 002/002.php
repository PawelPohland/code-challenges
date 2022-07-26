<?php

// n! = 1 * 2 * ... * (n - 1) * n
function factorial1($number) {
    $result = 1;

    for ($i = 1; $i <= $number; $i++) {
        $result *= $i;
    }

    return $result;
}

// n! = 1 * 2 * ... * (n - 2) * (n-1)! * n
function factorial2($number) {
    if ($number <= 1) {
        return 1;
    }
    
    return factorial2($number - 1) * $number;
}

// using generator
function factorial3($number) {
    if ($number <= 1) {
        yield 1;
    }

    $result = 1;

    for ($i = 1; $i <= $number; $i++) {
        $result *= $i;
        yield $result;
    }
}

// *************************************************** //

if (!function_exists("readline")) {
    function readline($message) {
        $fh = fopen("php://stdin", "r");
        echo $message;

        $userInput = trim(fgets($fh));
        fclose($fh);

        return $userInput;
    }
}

$number = (int)readline("Enter a number: ");

echo "$number! = " . factorial1($number) . PHP_EOL;
echo "$number! = " . factorial2($number) . PHP_EOL;

$factorials = array();
foreach (factorial3($number) as $f) {
    array_push($factorials, $f);
}

echo "$number! = " . $factorials[count($factorials) - 1] . PHP_EOL;

?>