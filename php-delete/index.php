<?php
ini_set('display_errors', 1);

$vcapServices = json_decode(getenv('VCAP_SERVICES'), true);
$creds = $vcapServices['mysql'][0]['credentials'];

$pdo = new PDO(
  sprintf('mysql:host=%s;port=%d;dbname=%s', $creds['host'], $creds['port'], $creds['name']),
  $creds['username'],
  $creds['password'],
  array(PDO::MYSQL_ATTR_SSL_CAPATH => '/etc/ssl/certs')
);

$qry = "DELETE FROM SurveyResults WHERE ".$_POST['WHERE']." = ".$_POST['EQUALS'];

try {
  $pdo->prepare($qry)->execute();
  print($qry);
} catch(Expection $e) {
  printf("Error: %s\n", $e->getMessage());
}
?>
