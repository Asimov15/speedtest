<?php
/* David Zuccaro 25/10/2020 Speedtest version 0.01 */
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en">
	<head>
		<meta http-equiv='Content-Type' content='text/html;charset=utf-8'/>
		<meta http-equiv='refresh' content='900'/>
		<link rel='stylesheet' type='text/css' href='speedtest.css'/>
		<title>1 Smith Street Melbourne Internet Speed</title>
		<script type='text/javascript'>
			function setop(opt)
			{
				var element = document.getElementById("date");
				element.value = opt;
			}
		</script>
	</head>
	<?php
		function RandomString()
		{
			$characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
			$randstring = '';
			for ($i = 0; $i < 10; $i++) 
			{
				$randstring = $randstring . $characters[rand(0, strlen($characters) - 1)];
			};

			return $randstring;
		};
		$outfn = RandomString() . '.png';
		$sp_command = '/usr/bin/python3 speedgraph.py -f ' . $outfn . ' 2>&1';
		exec($sp_command); 

		echo("<body>\n");
		echo("	<div id='header'>\n");
		echo("		<h1>Speed Tester</h1>\n");
		echo("	</div>\n");
		echo("	<form action='index.php' method='get'>\n");
		echo("		<div class='dates'>\n");
		echo("			<div id='wrapper'>\n");
		echo("				<div id='outer1'>\n");
		echo("				</div><!-- end #outer1 -->\n");
		echo("				<div id='outer2'>\n");
		echo("				</div><!-- end #outer2 -->\n"); 
		echo("				<div id='outer3'>\n");
		echo("				</div><!-- end #outer3 -->\n"); 
		echo("				<div id='outer4'>\n");
		echo("				</div><!-- end #outer4 -->\n"); 
		echo("			</div><!-- end #wrapper -->\n");
		echo("			<div id='footer'>\n");
		echo("			</div>\n");
		echo("		</div>\n");
		echo("	</form>\n");
		echo("	<div class='graph'>\n");
		echo("		<img class='dz' alt='Speed Test' src='images/" . $outfn . "'/>\n");
		echo("	</div>\n");
		echo("	<div class='validate2'>\n");
		echo("		<a href='http://jigsaw.w3.org/css-validator/check/referer'><img style='border:0;width:89px;height:31px' src='http://jigsaw.w3.org/css-validator/images/vcss' alt='Valid CSS!' /></a>\n");
		echo("		<a href='http://validator.w3.org/check?uri=referer'><img src='http://www.w3.org/Icons/valid-xhtml10' alt='Valid XHTML 1.0 Strict' height='31' width='89' /></a>\n");	   
		echo("	</div>\n");
		echo("</body>\n");
		echo("</html>\n");
	?>
