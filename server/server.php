<?php

if (isset($_GET['frame'])) {
    $folder = isset($_GET['html']) && $_GET['html'] === true ? "frames_br" : "frames";
    $filename = "frame" . $_GET['frame'] . ".txt";
    if (file_exists("$folder/$filename")) {
        $data = file_get_contents("$folder/$filename");
        echo $data;
    } else {
        echo "";
    }
}
