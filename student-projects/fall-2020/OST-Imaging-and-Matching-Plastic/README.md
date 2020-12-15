# Ost_PlasticPartMatching, 12/10/20
by Tobias Grab, Felicity Liao, Young Seok Kim

Requisites:
- Commonly used python libraries
- OpenCV version 3.4.2.16 or older!
	To install use one of the following codelines
		pip install opencv-python==3.4.2.16
		conda install -c menpo opencv
- We used Spyder as IDE
- The Data is also saved in this repo, even though this is not optimal. We suggest to copy them into a local folder and in order to not run into any issues.
  In most of the programs, the paths have to be changed. Where the data is stored, where the test images are as well as where the keras Models are saved. 




Project Description:
The Project goal was to match an image of a random pattern of a plastic part to a database full of similar images. 
The original approach was to use stucture images of the plastic parts but this approach only worked for a few materials. All the code we used for this approach
is in the "MVP" folder. It includes some pretty cool preprocessing ideas using a hough transoformaiton for line detection. This first approach was only feasible
for a few material combinations. We therefore changed the approach and started to use the surface pattern.
Luckily the algorithms we chose for our first approach still performed pretty well.

Folder description

-SurfaceRecognition
	- Comparisons
		- getBestMatches: Can be used to get the best matches for the algorithm and test image of choice
		- main_comparison: Framework that uses the code of getBestMatches in order to get the best matches for algorithms and all images in our test database
				   in order to be able to compare the performance of the algorithms
		- Feature_matching: First working implementation of the openCV algorithms that can be used to compare an image to the database and displays the match
		- timeMeas_novel: Program that was used to measure matching time for the autoencoder approaches
		- timeMeas_oldButGold: Program that was used to measure matching time for the OpenCV algorithms
	- CreatingModels
		- autoencoder: Code that can be used to create a convolutional autoencoder
		- autoencoder_invariant: Code that was to create a rotational invariant convolutional autoencoder (rotational invariance did not work)
	- GUI
		- GUI: Revised version of the GUI: Choose between algorithms and select test file
		- GUI_actuallyWorks: Our first version of the GUI, you have to select the algorithm you want to use in the program
	- Preprocessing
		- artificialData: Can be used to generate more surface images using the real ones we have
		- compressData: This programm was used to downscale the original microscope images and preform a histogram equalization
		
	- template_trial: Matching approach that we also tried, but didn't persue