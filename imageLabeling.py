import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

# Function to load raw image
def load_raw_image(raw_image_path):
    # Load raw image using Matplotlib
    raw_image = mpimg.imread(raw_image_path)
    if raw_image is None:
        raise FileNotFoundError(f"Error: Raw image '{raw_image_path}' not found.")
    return raw_image

# Function to load labeled images
def load_labeled_images(labeled_images_dir):
    labeled_images = {}
    for filename in os.listdir(labeled_images_dir):
        if filename.endswith('.png') or filename.endswith('.jpg'):
            label_name = os.path.splitext(filename)[0]  # Extract label name without extension for heading
            label_image_path = os.path.join(labeled_images_dir, filename)
            label_image = mpimg.imread(label_image_path)
            if label_image is None:
                raise FileNotFoundError(f"Error: Labeled image '{filename}' not found or cannot be loaded.")
            labeled_images[label_name] = label_image
    return labeled_images

# Example usage
if __name__ == '__main__':
    raw_image_path = 'nailpolish.jpg'
    labeled_images_dir = 'labelImg/'

    try:
        # Load raw image
        raw_image = load_raw_image(raw_image_path)

        # Load labeled images
        labeled_images = load_labeled_images(labeled_images_dir)

        # Plotting both raw image and labeled images in the same window
        num_images = len(labeled_images) + 1  # Number of images to display (raw image + labeled images)
        fig, axs = plt.subplots(1, num_images, figsize=(15, 6))  # Adjust figsize as needed

        # Display raw image
        axs[0].imshow(raw_image)
        axs[0].set_title('Raw Image')
        axs[0].axis('off')

        # Display each labeled image
        for i, (label_name, label_image) in enumerate(labeled_images.items(), start=1):
            axs[i].imshow(label_image, cmap='gray')  # Assuming labeled images are grayscale
            axs[i].set_title(f'Labeled Image: {label_name}')
            axs[i].axis('off')

        plt.tight_layout()  # Adjust layout
        plt.show()

    except Exception as e:
        print(f"Error: {e}")
