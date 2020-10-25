<?php
	$sp_command = '/usr/bin/python3 test1.py 2>&1';
	exec($sp_command, $message); 
	echo($message[0]);
?>
