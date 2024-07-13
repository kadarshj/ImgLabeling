# ImgLabeling

## Image Labeling Tool

### Functionality

**Displaying Labeled Images (`python imageLabeling.py`)**

The script loads a raw image and its associated labeled images (if available) from specified directories. It then displays them in the same window. Each labeled image is shown alongside the raw image.

**Interactive Labeling (`python label.py`)**

The script `label.py` allows users to interactively create labeled images by assigning labels to specific regions within the raw image. This feature involves GUI components for drawing or selecting regions and assigning labels.

### Requirements

- Python 3.x
- Matplotlib
- NumPy
- OpenCV (for image loading)

### Usage

1. **Setup Environment**
    - Setup
    - Ensure Python and required libraries are installed.
    ```bash
    python3.8 -m venv myenv
    source myenv/bin/activate
    pip install -r requirements.txt
    sudo apt-get install python3-tk
    ```

2. **Run the Script to Load a Raw Image and Its Associated Labeled Images**

    Modify `imageLabeling.py` to specify your raw image path (`raw_image_path`) and labeled images directory (`labeled_images_dir`).

    Execute the script:
    ```bash
    python imageLabeling.py
    ```

#### Output:

![Screenshot](https://raw.githubusercontent.com/kadarshj/ImgLabeling/main/Screenshot/Screenshot_from_2024-07-13_23-11-18.png?raw=true)

**Viewing Labeled Images**

The script will display the raw image and its corresponding labeled images (if available) using Matplotlib.

**Interactive Labeling**

Run the script to load a raw image and allow users to interactively create labeled images by assigning labels to specific regions within the raw image.

Press key s to save labeled image by creating rectangle. After pressing key s please input the class name in command line.
Press Esc key to exit from labeling image windows

Modify `label.py` to specify your raw image path (`raw_image_path`) and labeled images directory (`labeled_images_dir`).

### Execute the script:
### ```bash
### python label.py

![Screenshot 1](https://raw.githubusercontent.com/kadarshj/ImgLabeling/main/Screenshot/Screenshot_from_2024-07-13_23-07-10.png?raw=true)
![Screenshot 2](https://raw.githubusercontent.com/kadarshj/ImgLabeling/main/Screenshot/Screenshot_from_2024-07-13_23-09-00.png?raw=true)
![Screenshot 3](https://raw.githubusercontent.com/kadarshj/ImgLabeling/main/Screenshot/Screenshot_from_2024-07-13_23-09-38.png?raw=true)
![Screenshot 4](https://raw.githubusercontent.com/kadarshj/ImgLabeling/main/Screenshot/Screenshot_from_2024-07-13_23-10-39.png?raw=true)