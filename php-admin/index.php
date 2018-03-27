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


try {
  $pdo->prepare("DROP TABLE SurveyResults")->execute();
  $pdo->prepare("CREATE TABLE SurveyResults (EM1 CHAR(40),TEAM CHAR(20),AA CHAR(1),AB CHAR(1),AC CHAR(1),AD CHAR(1),AE CHAR(1),AF CHAR(1),AG CHAR(1),AH CHAR(1),AI CHAR(1),AJ CHAR(1),AK CHAR(1),AL CHAR(1),AM CHAR(1),AN CHAR(1),AO CHAR(1),AP CHAR(1),AQ CHAR(1),AR CHAR(1),AS1 CHAR(1),AT1 CHAR(1),AU CHAR(1),AV CHAR(1),AW CHAR(1),AX CHAR(1),AY CHAR(1),AZ CHAR(1),BA CHAR(1),BB CHAR(1),BC CHAR(1),BD CHAR(1),BE CHAR(1),BF CHAR(1),BG CHAR(1),BH CHAR(1),BI CHAR(1),BJ CHAR(1),BK CHAR(1),BL CHAR(1),BM CHAR(1),BN CHAR(1),BO CHAR(1),BP CHAR(1),TA1 CHAR(40),TA2 CHAR(40),TA3 CHAR(40),TB1 CHAR(40),TB2 CHAR(40),TB3 CHAR(40))")->execute();
} catch(Expection $e) {
  printf("Error: %s\n", $e->getMessage());
}
?>
