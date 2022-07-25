<?php

function getNumbers1($startNum = 2000, $endNum = 3200) {
    $numbers = [];

    for ($number = $startNum; $number <= $endNum; $number++) {
        if ($number % 7 == 0 && $number % 5 != 0) {
            array_push($numbers, $number);
        }
    }

    return join(",", $numbers);
}

echo getNumbers1();

// ************************************************************ //

// using generator
function getNumbers2($startNum = 2000, $endNum = 3200) {
    for ($number = $startNum; $number <= $endNum; $number++) {
        if ($number % 7 == 0 && $number % 5 != 0) {
           yield $number;
        }
    }
}

$numbers = [];
foreach (getNumbers2() as $number) {
        array_push($numbers, $number);
}
echo join(",", $numbers);

?>