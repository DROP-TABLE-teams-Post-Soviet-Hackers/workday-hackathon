import cv2
import numpy as np
from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model("keras_model.h5", compile=False)

# Load the labels
class_names = open("labels.txt", "r").readlines()

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

cam = cv2.VideoCapture(0)


# return true if the current posture is bad
# if logs = True, prints logs
def is_bad_posture(logs=False):
    try:
        result, img_read = cam.read()

        # if there is a problem with a camera
        if not result:
            return False

        # save the image
        cv2.imwrite("image.png", img_read)

        # Replace this with the path to your image
        image = Image.open("image.png").convert("RGB")

        # resizing the image to be at least 224x224 and then cropping from the center
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.LANCZOS)

        # turn the image into a numpy array
        image_array = np.asarray(image)

        # Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

        # Load the image into the array
        data[0] = normalized_image_array

        # Predicts the model
        prediction = model.predict(data)
        prediction_index = np.argmax(prediction)
        predicted_class = class_names[prediction_index]
        confidence_score = prediction[0][prediction_index]

        predicted_classname = predicted_class[2:]

        if logs:
            print("Class:", predicted_classname, end="")
            print("Confidence Score:", confidence_score)

        if prediction_index == 1:
            return True

        return False

    except Exception as e:
        print("Error while classifying:", e)
