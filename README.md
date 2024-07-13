# ImgLabeling

# Image Labeling Tool

Functionality

Displaying Labeled Images(python imageLabeling.py)

The script loads a raw image and its associated labeled images (if available) from specified directories. It then displays them in the same window. Each labeled image is shown alongside the raw image.

Interactive Labeling (python label.py)

the script label.py allow users to interactively create labeled images by assigning labels to specific regions within the raw image. This feature would involve GUI components for drawing or selecting regions and assigning labels. 
using Requirements

    Python 3.x
    Matplotlib
    NumPy
    OpenCV (for image loading)

Usage

    Setup Environment
        Setup 
        Ensure Python and required libraries are installed.
        
        python3.8 -m venv myenv
        source myenv/bin/activate

        pip install -r requirements.txt

        sudo apt-get install python3-tk

    Run the Script to loads a raw image and its associated labeled images (if available) from specified directories.

        Modify imageLabeling.py to specify your raw image path (raw_image_path) and labeled images directory (labeled_images_dir).

        Execute the script:

        bash

    python imageLabeling.py

    Output:

    ![Screenshot](https://raw.githubusercontent.com/kadarshj/ImgLabeling/blob/main/Screenshot/Screenshot_from_2024-07-13_23-11-18.png)

Viewing Labeled Images

    The script will display the raw image and its corresponding labeled images (if available) using Matplotlib.

Interactive Labeling

    Run the Script to loads a raw image allow users to interactively create labeled images by assigning labels to specific regions within the raw image.

        Modify label.py to specify your raw image path (raw_image_path) and labeled images directory (labeled_images_dir).

        Execute the script:

        bash

    python label.py

    ![Screenshot 1](https://raw.githubusercontent.com/kadarshj/ImgLabeling/blob/main/Screenshot/Screenshot_from_2024-07-13_23-07-10.png)
    ![Screenshot 2](https://raw.githubusercontent.com/kadarshj/ImgLabeling/blob/main/Screenshot/Screenshot_from_2024-07-13_23-09-00.png)
    ![Screenshot 3](https://raw.githubusercontent.com/kadarshj/ImgLabeling/blob/main/Screenshot/Screenshot_from_2024-07-13_23-09-38.png)
    ![Screenshot 4](https://raw.githubusercontent.com/kadarshj/ImgLabeling/blob/main/Screenshot/Screenshot_from_2024-07-13_23-10-39.png)