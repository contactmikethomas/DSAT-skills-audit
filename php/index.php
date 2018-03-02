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

$txt = "INSERT INTO SurveyResults (EM1,TEAM,AA,AB,AC,AD,AE,AF,AG,AH,AI,AJ,AK,AL,AM,AN,AO,AP,AQ,AR,AS1,AT1,AU,AV,AW,AX,AY,AZ,BA,BB,BC,BD,BE,BF,BG,BH,BI,BJ,BK,BL,BM,BN,BO,BP,TA1,TA2,TA3,TB1,TB2,TB3) VALUES ('".$_POST['EM1']."',"."'".$_POST['TEAM']."',"."'".$_POST['AA']."',"."'".$_POST['AB']."',"."'".$_POST['AC']."',"."'".$_POST['AD']."',"."'".$_POST['AE']."',"."'".$_POST['AF']."',"."'".$_POST['AG']."',"."'".$_POST['AH']."',"."'".$_POST['AI']."',"."'".$_POST['AJ']."',"."'".$_POST['AK']."',"."'".$_POST['AL']."',"."'".$_POST['AM']."',"."'".$_POST['AN']."',"."'".$_POST['AO']."',"."'".$_POST['AP']."',"."'".$_POST['AQ']."',"."'".$_POST['AR']."',"."'".$_POST['AS']."',"."'".$_POST['AT']."',"."'".$_POST['AU']."',"."'".$_POST['AV']."',"."'".$_POST['AW']."',"."'".$_POST['AX']."',"."'".$_POST['AY']."',"."'".$_POST['AZ']."',"."'".$_POST['BA']."',"."'".$_POST['BB']."',"."'".$_POST['BC']."',"."'".$_POST['BD']."',"."'".$_POST['BE']."',"."'".$_POST['BF']."',"."'".$_POST['BG']."',"."'".$_POST['BH']."',"."'".$_POST['BI']."',"."'".$_POST['BJ']."',"."'".$_POST['BK']."',"."'".$_POST['BL']."',"."'".$_POST['BM']."',"."'".$_POST['BN']."',"."'".$_POST['BO']."',"."'".$_POST['BP']."',"."'".$_POST['TA1']."',"."'".$_POST['TA2']."',"."'".$_POST['TA3']."',"."'".$_POST['TB1']."',"."'".$_POST['TB2']."',"."'".$_POST['TB3']."')";

try { 
  $pdo->prepare($txt)->execute();
  print("Survey Submitted");
} catch(Expection $e) {
  printf("Error: %s\n", $e->getMessage());
}
?>



