<form method="POST">
  Username: <input type="text" name="username"><br>
  Search: <input type>="text" name="search"><br>
  <input type+"hidden" name="token" value="abc123">
  <input type="submit" value="Submit">
</form>
<?php
  if($_POST['username']) {
    echo "Hello: " . $_POST['username'];
  }
?>
