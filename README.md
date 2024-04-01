# Camera---Project

###Introduction 
This application allows users to take photos with their webcam, add descriptions to them, and save them to a database directory. The idea for this project came from the desire to learn more about the CV2 module. The CV2 module is a module with a wide range of applications. Simply put, this module is used for photo and video processing and is widely used in more advanced projects.

### Overview
The application consists of two main classes: `App` and `Button`. The `App` class is responsible for creating the main window and managing the functionality of the camera app, while the `Button` class provides a method for creating custom-styled buttons.

### App Class
- **Initialization**:
  - The `__init__` method sets up the main window, including title, icon, background image, buttons, webcam display, and database directory.
  
- **Button Creation**:
  - The `setButton` method in the `Button` class is used to create buttons with custom styling and functionality.

- **Functionality**:
  - `displayPhotoCatalog`: Opens the directory where photos are saved.
  - `takePhoto`: Opens a new window for taking photos, allowing users to add descriptions.
  - `addWebcam`: Captures video from the webcam and displays it in a label.
  - `processWebcam`: Continuously updates the webcam display.
  - `addImageToLabel`: Adds the captured image to the label for preview.
  - `acceptPhoto`: Saves the captured photo with a description to the database directory.
  - `tryAgain`: Closes the photo-taking window.

- **Start Method**:
  - `start`: Initiates the main event loop for the application.

### Button Class
- **setButton Method**:
  - Creates a button widget with specified attributes and returns it.

### Usage
1. Run the script to start the Camera App.
2. Click on "Take a Photo" to open the photo-taking window.
3. Enter a description and click "Accept" to save the photo.
4. Click "Try again" to retake the photo if needed.
5. Click on "Display Photo Catalog" to open the directory where photos are saved.

### Requirements
- Python 3.x
- Tkinter
- OpenCV (cv2)
- Pillow (PIL)
- Ensure that `camera.png` and `bg.png` are present in the same directory as the script.
