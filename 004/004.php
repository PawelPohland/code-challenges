<?php

abstract class ValuesContainer {
    protected $values;

    public function __construct(...$values) {
        if (count($values)) {
            $this->values = $values;
        } else {
            $this->values = [];
        }
    }

    abstract public function toString();
}

class cTuple extends ValuesContainer {
    public function __construct(...$values) {
        parent::__construct(...$values);
    }

    public function toString() {
        return "(" . implode(", ", $this->values) . ")";
    }
}

class cList extends ValuesContainer {
    public function __construct(...$values) {
        parent::__construct(...$values);
    }

    public function toString() {
        return "[" . implode(", ", $this->values) . "]";
    }
}

if (!function_exists("readline")) {
    function readline($message) {
        $fh = fopen("php://stdin", "r");
        echo $message;

        $userInput = trim(fgets($fh));
        fclose($fh);

        return $userInput;
    }
}

$userInput = readline("Enter comma-separated list of numbers: ");

// split by comma
$userInput = explode(",", $userInput);

// each value: remove whitespace, cast to int
// return int(value) or NULL if casting fails
$userInput = array_map(function($value) {
    $value = trim($value);

    if (strlen($value) > 0) {
        $i = intval($value, 10);

        // intval returns int(0) for strings
        if ($i == 0 && $value != "0") {
            // so if $value was not a string(0)
            return NULL;
        }
        return $i;
    }
    
    return NULL;
}, $userInput);

// filter out all int values (NULLs are rejected)
$userInput = array_filter($userInput, function($value) {
    return !is_null($value);
});

$tuple = new cTuple(...$userInput);
echo "Tuple: " . $tuple->toString() . PHP_EOL;

$list = new cList(...$userInput);
echo "List: " . $list->toString() . PHP_EOL;

?>