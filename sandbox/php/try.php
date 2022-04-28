<?php
// echo "hello-php\n";

function first($msg)
{
    echo $msg;
}

first("Hello1\n");
// $second = first; // PHP Warning:  Use of undefined constant first...
// $second('Hello2-second');



//////////////////// Closure & Callable
function callFunc1(Closure $closure) {
    $closure();
}

function callFunc2(Callable $callback) {
    $callback();
}

$function = function() {
    echo "Hello, World!\n";
};

callFunc1($function); // Hello, World!
callFunc2($function); // Hello, World!

//callFunc1("xy"); // Catchable fatal error: Argument 1 passed to callFunc1() must be an instance of Closure, string given
//callFunc2("xy"); // Hello, World! => Catchable fatal error: Uncaught TypeError: Argument 1 passed to callFunc2() must be callable, string given

// The __invoke() method is called when a script tries to call an object as a function.
class CallableClass
{
    public function __invoke($x)
    {
        var_dump('var_dump1', $x, 'after_x');
    }
}
$obj = new CallableClass;
$obj(5);
var_dump(is_callable($obj));
//////////////////// /Closure & Callable
