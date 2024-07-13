import cv2
import numpy as np

# Global variables
drawing = False  # True if the mouse is pressed
mode = True  # True for rectangle mode; toggle to switch modes
ix, iy = -1, -1
label_color = 255  # The label color/value for labeling the image (white)

# Mouse callback function
def draw(event, x, y, flags, param):
    global ix, iy, drawing, mode, label_image, img

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            img_draw = img.copy()  # Create a copy of the original image for drawing
            if mode:
                cv2.rectangle(img_draw, (ix, iy), (x, y), (0, 255, 0), 2)
                cv2.imshow('image', img_draw)  # Display the updated image
            else:
                cv2.circle(img_draw, (x, y), 5, (0, 0, 255), 2)
                cv2.imshow('image', img_draw)  # Display the updated image

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode:
            cv2.rectangle(img, (ix, iy), (x, y), (0, 255, 0), 2)
            update_label_image_rectangle(ix, iy, x, y)
        else:
            cv2.circle(img, (x, y), 5, (0, 0, 255), 2)
            update_label_image_circle(x, y)
        cv2.imshow('image', img)  # Update display after drawing is done

def update_label_image_rectangle(x1, y1, x2, y2):
    global label_image
    min_x = min(x1, x2)
    max_x = max(x1, x2)
    min_y = min(y1, y2)
    max_y = max(y1, y2)
    label_image[min_y:max_y, min_x:max_x] = label_color

def update_label_image_circle(cx, cy, radius=5):
    global label_image
    cv2.circle(label_image, (cx, cy), radius, label_color, -1)

def save_label_image(path):
    global img
    labeled_img = img.copy()
    # Use the cvtColor() function to grayscale the image 
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_BGR2GRAY) 
    #labeled_img[label_image == 0] = 0  # Set background to black
    labeled_img[label_image == 1] = 0  # keep Entire Raw Image
    cv2.imwrite(path, labeled_img)
    print(f"Labeled image saved to {path}")

if __name__ == "__main__":
    # Load the raw image
    image_path = 'nailpolish.jpg'
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Failed to load image '{image_path}'.")

    # Initialize the label image with zeros (black) and same size as img
    label_image = np.zeros_like(img[:,:,0], dtype=np.uint8)

    cv2.namedWindow('image')
    cv2.setMouseCallback('image', draw)

    while True:
        cv2.imshow('image', img)
        k = cv2.waitKey(1) & 0xFF
        if k == ord('m'):
            mode = not mode  # Toggle between rectangle and circle mode
            print(f"Mode toggled to {'rectangle' if mode else 'circle'}")
        elif k == ord('s'):
            imgLabel = input('Enter the label name: ')
            save_label_image(f'labelImg/{imgLabel}.png')
            break
        elif k == 27:  # ESC key to exit
            break

    cv2.destroyAllWindows()
