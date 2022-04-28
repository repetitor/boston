<?php
require_once __DIR__ . '/../vendor/autoload.php';

//use App\App;
//
//try {
//    $app = new App();
//    $app->run();
//} catch (Exception $e) {
//    echo $e->getMessage();
//}

$datetime = '2022-04-28 12:29:19';
//echo \Carbon\Carbon::now()->format('d.m.Y');
echo \Carbon\Carbon::createFromFormat('Y-m-d H:i:s', $datetime)->format('d.m.Y');
echo \Carbon\Carbon::createFromFormat('Y-m-d H:i:s', $datetime);
echo "\npublic\n";
