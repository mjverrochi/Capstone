### Capstone: CNN Image Classification with Streamlit App

### Problem Statement


I’ve been hired by ABC Waste Corp. to look into how operations, global impact, and revenue could be improved.

I will build an image classifier in an effort to classify waste types. With waste types classified, ABC Waste Corp. can dispose of each waste class differently to achieve these goals.



### Summary

The CNN notebook begins by creating train and test variables for train and test images. Within the train and test folders are the images, split into the two classifications, Biodegradable and Non-Biodegradable. Images are 3 dimensional. Before Modeling, I rescaled the images to be between 0 and 1, rather than 1 and 255 using ImageDataGenerator. I then generated both labels and data using flow_from_directory since the ImageDataGenerator was used.
At this point I began building the CNN model. My first layer is resizing the images. I did this in an effort to shorten the time it would take to run the model and to my suprise it did not effect accuracy or loss much. After experimenting with different layers and layer types, my final model has 7 layers total. 2 convolutional2D layers, 2 maxpool2D layers, the resizing layer, a flatten layer, and the output layer with 'sigmoid' activation as this is a binary classificaiton.

Once the CNN model was compiled and fit I decided to add the prebuilt network EfficientNet to the model to try to increase performance. I rescled the images back to be between 1 and 255 and also resized images to 224 pixels by 224 pixels, as this is what EfficientNetB0 calls for. After experimenting with different layer combinations, I settled on a 5 layer construction.
I plotted histograms to visualize the predictions for both the CNN model and for after when the EffNet was added.
Using Streamlit I created an image classifier that takes uploaded images and classifies what classification the image falls into.


### Conclusions and Recommendations

Both the CNN model and adding EffNet performed very well. The baseline was about 50%. The CNN model has an accuracy of 87%, validation accuracy of 81%, loss of 0.31, and validation loss of 0.41. The EffNet has an accuracy of 93%, a validation accuracy of 92%, a loss of 0.23, and validation loss of 0.21. Although there is slight overfitting, these scores tell us that the model is much more accurate than just assigning all images the same class. 
ABC Waste Corp. could use the image classification app to process their waste items and funnel them to the correct disposal path, if they choose to. With the different paths available for ABC Waste Corp. to dispose of their waste, I suggest they look further into cost-benefit-analysis of different disposal options. Not only could they have a more positive impact on the environment, they could see great revenue as well. The Streamlit app would be a valuable tool in the classifying their waste items. 

---

### What's Next

Things I would like to look into as the project continues:
I was working on an SVM model to see if that would perform as well as or better than the CNN Model. Completing that model in hopes of having a better performing model will be done in the near future.

