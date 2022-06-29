#Face Recognition using One-Shot learning technique and Siamese Network.

A Siamese Network model has trained for face recognition. First model was trained with custom dataset for "positive" & "anchor" and a dataset from "www.cs.umass.edu/lfw/lfw.tgz" downloaded for "Negative".

Model was trained in "TensorFlow" library & other scripts was written in python. 

Model was trained in Google colab & other scripts were run in VS code. All libraries have mentioned in a block of notebook, just by running the block all libraries will be imported. 

How to use - 

1. Mount to Google drive
2. Download the dataset for "Negative" 
3. Run "capture_images_from_webcam[anchor] .py" for capturing anchor images by pressing "Space" and "ESC" to exit
4. Process (3) again with "capture_images_from_webcam[positive] .py" for "Positive" 
5. Upload those data in /data/anchor & /data/positive
6. Create another folder named "negative"
7. Run rest of the code from notebook 
8. After training the model, create /data/application_data, /data/application_data/input_image and /data/application_data/verification_images
9. Then run "Copying images in verification for testing" section from notebook
10. Upload the capture image to "/data/application_data/input_image"
11. Run the last two blocks then you will see the model's result in input image. 

# Thank You
