import cv2
import numpy as np
import tensorflow as tf

# Load your pre-trained age detection model
model = tf.keras.models.load_model('C:/Users/Ronak/Desktop/Age_Detection/Age_model.keras')


# Function to preprocess the image
def preprocess_image(image):
    image = cv2.resize(image, (48, 48))  # Resize to the input shape of your model
    image = image.astype('float32') / 255.0  # Normalize
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Initialize video capture
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Preprocess the frame for prediction
    preprocessed_frame = preprocess_image(frame)

    # Predict age
    predictions = model.predict(preprocessed_frame)
    age = int(predictions[0][0])  # Assuming the output is a single age value

    # Display age on the frame
    cv2.putText(frame, f'Age: {age}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the frame
    cv2.imshow('Age Detection', frame)

    # Break loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
