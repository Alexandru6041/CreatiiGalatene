<?php
    $email_input = $_POST['email'];
    $password_input = $_POST['password'];
    $username_input = $_POST['email'];
    

    $host = "localhost";
    $dbname = "creatiigalatene";
    $username = "root";
    $password = "mWJA&&-84%tyWKuVKzpdke7P3dmLEVB#A%w!aqx7f7A6wWvmUS";

    $conn = mysql_connect(hostname: $host, username: $username, password: $password, database: $dbname);

    if(mysqli_connect_errno())
    {
        die("Connection Error: " . mysqli_connect_error());
    }
    echo "Hello World";
?>