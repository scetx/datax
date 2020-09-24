The whole code is not very clean (since it's only a first try) and not very well documented yet.


Description of files:

ImportScanCreateImage is for creating Sampledata Images out of the scanner images (with nice plots and stuff, but only one image at a time)

ImportScanCreateImage2 is for creating Sampledata out of all scanner images saved in the input folder and save them to a output folder
(Multiple files but without any plots)

MNIST_Cauto is a implementation of a convolutional autoencoder with keras (Sample code from the keras homepage), the autoencoder is not used yet

SiftFeaturesMatchKnn is the file that matches a test images to the correct image from the database. Does not work properly yet, only when
the exact same image is used. Either a bug in the code or illumination problems.