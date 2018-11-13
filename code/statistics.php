<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN"
"http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns = "http://www.w3.org/1999/xhtml">
<head>
<title>Statistic</title>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
</head>

<body>
    <style>
    
    
    </style>
        <div class="container-fluid chessheader">
                <div class="container text-center" style="background:none;" >
                    <br>
                    <h1 class="tittle"> Blog Statistics </h1>
                </div>
            </div>
            <br>
  <a class='btn' type="button" href='main.html'> Return</a>
    
<?php
    $conn = mysqli_connect("localhost", "root", "", "expressyourself");
	
	if (!$conn) {
		die("Connection failed: " . mysqli_connect_error());
	}
    
    $sql = "SELECT * FROM blog ORDER BY  likes DESC LIMIT 10";
    $result = mysqli_query($conn, $sql);
    $ranking = 0;
    
    echo "<h2 class='text-center'> Blog Statistics</h2>";
    echo "<table class='table table-bordered table-hover text-center'>
        <tr>
        <th>Ranking</th>
        <th>Username</th>
        <th>Blog-Name</th>
        <th>Number of Likes</th>
        <th>People who Visited</th>

        </tr>";
    while($row = mysqli_fetch_assoc($result)) {
        $ranking++;
        echo "<tr>";
        echo "<td class='text-center'>" . $ranking . "</td>";
        echo "<td class='text-center'>" . $row['username'] . "</td>";
        echo "<td class='text-center'>" . $row['blogName'] . "</td>";
        echo "<td class='text-center'>" . $row['likes'] . "</td>";
        echo "<td class='text-center'>" . $row['visit'] . "</td>";
        echo "</tr>";
    }  
    echo '</table>';
    
    if (mysqli_query($conn, $sql)) {
	} 
    else { 
		echo "Error: " . $sql . " " . mysqli_error($conn);
	}
	
	mysqli_close($conn);
?>

</body>
</html>

   

