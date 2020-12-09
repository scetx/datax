# Ost_PlasticPartMatching
The Project is to match an image of a random pattern of a plastic part to a database full of similar images. The original approach was to use stucture images 
of the plastic parts but this approach only worked for a few materials, which is why we changes the approach to using the surface pattern of a defined spot.
We implemented different algorithms using the openCV library (Version 3.4.2.16) and also created our own model. We wrote code to compare these algorithms and
visualize everything with a GUI.

The GIT repo does not contain any images, those are saved on the google drive.
In the "MVP" folder there is the code that was used for the MVP and the original idea (Using the structure image).
The "Surface_recognition" folder has all the currently used code in it for creating the models, preprocessing the data, creating artificial images and comparing the algorithms
