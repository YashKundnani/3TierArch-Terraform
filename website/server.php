<?php

    function imageCreateFromGDImage($im, $ext, $name)
    {
        $fileExtensionsAllowed = ['jpeg','jpg','png'];
        if(!in_array($ext, $fileExtensionsAllowed)){
            echo "File Extension Not Allowed"."<br>";
            return;
        }
        echo "$ext"."<br>";
        if($ext == "jpg" || $ext == "jpeg")
        {
            imagejpeg($im, "$name");
            imagedestroy($im);
            return;
        }
        if($ext == "png"){
            imagepng($im, "$name");
            imagedestroy($im);
            return;
        }

    }

    $currentDirectory = getcwd();
    $uploadDirectory = "/uploads_server/";

            // check if post data is available or not
            if (isset($_POST['fileName']) && $_POST['fileData']){
                // save uploaded file
                $uploadDir = 'uploads_server/';
                $fileN = $uploadDir.$_POST['fileName'];
                $im = imagecreatefromstring(base64_decode(($_POST['fileData'])));
                $fileExt =$_POST['fileExt'];
                imageCreateFromGDImage($im, $fileExt, $fileN);              
                
                /*
                file_put_contents(
                    $uploadDir. $_POST['fileName'],
                    imageCreateFromGDImage(imagecreatefromstring(base64_decode(($_POST['fileData']))))                    
                );
                */
                // done
                    echo "Success"."<br>";
                    } 
                    else {
                        echo "Error : File not uploaded to remote server."."<br>";
                    }
    //run py script and get 'Identify' and 'Confidence'
    $command_exec = escapeshellcmd("python3 /home/linux-vm/Documents/'Internship 2021'/Company-Project/Web-Py-Tf-Img/PythonScripts/Tier2/FaceVerifyServer.py $fileN");
    sleep(2);
    $str_output  = shell_exec($command_exec);
    echo $str_output."<br>";
    //delete file present in server
    $command_exec = escapeshellcmd("python3 /home/linux-vm/Documents/'Internship 2021'/Company-Project/Web-Py-Tf-Img/PythonScripts/'Comman Files'/deleteImg.py $fileN");
    echo "End of Server Program"."<br>";
?>