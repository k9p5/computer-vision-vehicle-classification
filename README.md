# Classifying and measuring vehicles
This project has been developed at the Kempten University of Applied Sciences for the lecuture "Bildverarbeitung und maschinelles Sehen". All rights reserved

<br>

## The Team
- Jakob Bleickert: Video processing
- Lukas Harzheim: Taking measurement
- Konstantin Paulus: Image classification

<br>

## Project Structure

``/saved_models`` <br>
In this directory you can find the ML model that has been exported from google colab <br><br>
``/presentation_materials`` <br>
Here you can find meterial that have been used for the presentation <br><br>
``/notebooks`` <br>
This directory has been used in order to develop the algorithms <br><br>
``/datasets`` <br>
Here you can find the videos and image that have been used for analysation <br><br><br>

## Important Notebooks (/notebooks/*)
``video_preprocessing.ipynb`` <br>
Is extracting frame from a sequence that contains a vehicle in the center of the image <br><br>
``take_measurements.ipynb`` <br>
Is taking measurements of the given frame that is containing a vehicle <br><br>
``classification_model_training.ipynb`` <br>
Can be used in order to train the classification model <br><br>
``classification_daihatsu.ipynb`` <br>
Is applying the model to one of our datasets <br><br>
``classification_rule_based.ipynb`` <br>
Tries to evaluate an alternative approach for classifying the image <br><br>
``combination_of_algorithms.ipynb`` <br>
Is combining all algorithms that can be used to process a given video <br><br><br>

## Testing the source code
**The *.ipynb files can be executed with jupyter notebook** <br>
Make sure you have insalled the following packages in your environment: <br>

```
# Requires the latest pip
$ pip install --upgrade pip

# Current stable release of tensorflow for CPU and GPU 
$ pip install tensorflow==2.5.0

# For processing images
$ pip install opencv-python==4.5.2.54

# Displaying charts and images
$ pip install matplotlib==3.4.2

# For scientific computing
$ pip install numpy==1.20.3

# Might come in handy
$ pip install scipy==1.7.0
```
