<?php
    $currentDirectory = getcwd();
    $uploadDirectory = "/uploads_local/";
    $uploadDir = "uploads_local/";

    $errors = []; // Store errors here

    $fileExtensionsAllowed = ['jpeg','jpg','png']; // These will be the only file extensions allowed 

    $fileName = $_FILES['the_file']['name'];
    $fileSize = $_FILES['the_file']['size'];
    $fileTmpName  = $_FILES['the_file']['tmp_name'];
    $fileType = $_FILES['the_file']['type'];
    $fileExtension = strtolower(end(explode('.',$fileName)));

    $uploadPath = $currentDirectory . $uploadDirectory . basename($fileName);
    //echo "$uploadDirectory"."$fileName";
    #echo "$currentDirectory"."$uploadDirectory"."$fileName";
    #echo "$fileString";

    if (isset($_POST['submit'])) {

            if (! in_array($fileExtension,$fileExtensionsAllowed)) {
              $errors[] = "This file extension is not allowed. Please upload a JPEG or PNG file";
            }

            if ($fileSize > 4000000) {
              $errors[] = "File exceeds maximum size (4MB)";
            }

            if (empty($errors)) {
              sleep(2);
              $didUpload = move_uploaded_file($fileTmpName, $uploadPath);

                  if ($didUpload) {
                    $imgFile = $uploadDir.$fileName;
                    $fileString = file_get_contents("$imgFile");
                    echo "The file " . basename($fileName) . " has been uploaded to local server"."<br>";
                    echo "Uploading on Server..."."<br>";
                              // set array to send data to remote server
                            $remoteData = array(
                                'fileName' => $fileName,
                                'fileExt'  => $fileExtension,
                                'fileData' => base64_encode($fileString)                                
                            );
                            // start curl set up for remote file upload
                            $curl = curl_init();
                            curl_setopt($curl, CURLOPT_URL, 'http://10.1.2.5/server.php');
                            curl_setopt($curl, CURLOPT_TIMEOUT, 30);
                            curl_setopt($curl, CURLOPT_AUTOREFERER,    true);
                            curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
                            curl_setopt($curl, CURLOPT_POSTFIELDS, $remoteData);
                            
                            $headers = array(
                              "Connection: keep-alive",
                              "Keep-Alive: timeout=5, max=100",
                            );
                            curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
                            /*
                            //for debug only!
                            curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
                            curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);
                            */
                            $response = curl_exec($curl);
                            curl_close($curl);
                            echo $response ."<br>";
                  } 
                  else {
                    echo "Your file not uploaded to server."."<br>";
                    echo "An error occurred. Please contact the administrator."."<br>";
                  }
            } 
            else {
                  foreach ($errors as $error) {
                        echo $error . "These are the errors" . "<br>";
                    }
             }

    }
    //delete the file present in local folder
    $command_exec = escapeshellcmd("python3 /home/linux-vm/Documents/'Internship 2021'/Company-Project/Web-Py-Tf-Img/PythonScripts/'Comman Files'/deleteImg.py $fileN");
    echo "End of Client(upload) Program"."<br>";
?>
