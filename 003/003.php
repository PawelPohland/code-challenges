<?php

class Dictionary {
    private $dict;

    public function __construct() {
        $this->dict = [];
    }

    public function insert($key, $value) {
        $this->dict[$key] = $value;
    }

    public function print() {
        echo "{";
        
        $counter = 1;
        
        foreach ($this->dict as $key => $value) {
            echo "$key: $value";

            if ($counter != count($this->dict)) {
                echo ", ";
            }

            $counter++;
        }

        echo "}" . PHP_EOL;
    }
}

function genDictionary($max_key) {
    $dictionary = new Dictionary();

    for ($k = 1; $k <= $max_key; $k++) {
        $dictionary->insert($k, $k * $k);
    }

    return $dictionary;
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

$max_key = (int)readline("Enter a number: ");
$dictionary = genDictionary($max_key);
$dictionary->print();

?>