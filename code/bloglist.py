
from code import app
from flask import request
    
@app.route("/bloglist", methods=['GET', 'POST'])

def bloglist():
    if request.method == 'POST':
        return ""
    else:
        return """
<!DOCTYPE html>
<html>
<head>
</head>
<style>
</style>
<body>
<?php
$server = "tcp:expressyourself.database.windows.net";
$username = "cs476";
$password = "$up3rSecret";
$dbname = "expressyourself";

$conn = new mysqli($server, $username, $password, $dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

$sql = "SELECT username, blogName, imageSource, descr FROM blog";
$result = $conn->query($sql);

if ($result->num_rows > 0) {
    // output data of each row
    while($row = $result->fetch_assoc()) {
        echo "<br> Username: ". $row["username"]. " - Blog-Name: ". $row["blogName"]. " " . $row["descr"] . "<br>";
    }
} else {
    echo "0 results";
}

$conn->close();
?>
</body>
</html>
