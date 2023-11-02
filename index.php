

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Comment</title>
</head>
<body>
    <iframe width="933" height="394" src="https://www.youtube.com/embed/j5jm5iP6cJM" title="Youssei B - Doorgaan (Prod. Kraaimusic." frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    <form action="index.php" method="post">
        Name: <input type="text" name="name"><br>
        E-mail: <input type="text" name="email"><br>
        comment:<input type="text" name="comment"><br>
        <button type="submit" name="submit">submit</button>
        </form>
</body>

<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "module_13";

$conn = mysqli_connect($servername, $username, $password, $dbname);
    // Check connection
    if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
    }
    // if ($result->num_rows > 0) {
    //     // output data of each row
    //     while($row = $result->fetch_assoc()) {
    //       echo "id: " . $row["id"]. " - Name: " . $row["name"]. " " . $row["email"]. " " . $row["comment"]. " " . $row["date"]. "<br>";
    //     }
    //   } else {
    //     echo "0 results";
    //   }
    //   $conn->close();


      $sql = "SELECT * FROM comments";
      $result = $conn->query($sql);
      
      if ($result->num_rows > 0) {
        // output data of each row
        while($row = $result->fetch_assoc()) {
            $row["name"]. " " . $row["email"]. "  - Commented:  " . $row["comment"]. " " . $row["date"]. "<br>";
        }
      } else {
        echo "0 results";
      }
      $conn->close();

      $conn = mysqli_connect($servername, $username, $password, $dbname);
    // Check connection
    if (!$conn) {
    die("Connection failed: " . mysqli_connect_error());
    }
    if (isset($_POST['submit'])) {
      
        // Taking all 5 values from the form data(input)
        $name =  $_REQUEST['name'];
        $comment =  $_REQUEST['comment'];
        
       
        // Performing insert query execution
        // here our table name is college
       
        
        $sql = "INSERT INTO comments (name, comment) VALUES ('$name', '$comment')";


        if ($conn->query($sql) === TRUE) {
          // echo "New record created successfully";
        } else {
          echo "Error: " . $sql . "<br>" . $conn->error;
        }
 
       
        // Close connection
        mysqli_close($conn);
    }
      ?>
    

</html>