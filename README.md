# IRB-Infrastructures-project

I worked on a project for IRB Infrastructures while interning at AssertAI. This project will solve the issues and thefts at the toll booths. This will help smoothen the process and help the company find the missed vehicles using video analysis.

The videos to frames code will help to convert video files into images or frames as we technically call it. You need to change only 3 parts of the code; the input (videos) folder, the output folder (for saving the images) and the frame interval. Frame interval tells whether you want all the continuous frames or after an interval. If you set frame interval = 3 it means that the code will save every third frame in your output folder. 

When you train such a big set of images, it is difficult to upload on VSC (if done using a terminal) or on the drive (if you want to mount it on Google Colab). For this reason, I ran a script which distributes the images in the folder and make n folders by dividing the images. n is to be given as the input of your choice.

Then, I had to detect/test the images. This was done using a pre-trained model and run with yolov5. This model detected the type of vehicle car, LCV, truck, bus, etc. We have used lacs of images to train this model by annotating these classes. 

This process will then be incorporated in a complete GUI based setup. 
