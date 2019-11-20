<?php 
// Receive GET Parameters

$Age = $_GET["Age"];
$Gender = $_GET["Gender"];
$Total_Bilirubin = $_GET["Total_Bilirubin"];
$Direct_Bilirubin = $_GET["Direct_Bilirubin"];
$Alkaline_Phosphotase = $_GET["Alkaline_Phosphotase"];
$Alamine_Aminotransferase = $_GET["Alamine_Aminotransferase"];
$Aspartate_Aminotransferase = $_GET["Aspartate_Aminotransferase"];
$Total_Proteins = $_GET["Total_Proteins"];
$Albumin = $_GET["Albumin"];
$Albumin_and_Globulin_Ratio = $_GET["Albumin_and_Globulin_Ratio"];

system("/usr/anaconda/bin/python3 test_model.py ".$Age." ".$Gender." ".$Total_Bilirubin." ".$Direct_Bilirubin." ".$Alkaline_Phosphotase." ".$Alamine_Aminotransferase." ".$Aspartate_Aminotransferase." ".$Total_Proteins." ".$Albumin." ".$Albumin_and_Globulin_Ratio." 2>&1");

?>
