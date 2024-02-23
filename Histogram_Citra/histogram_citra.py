from PIL import Image, ImageOps
import matplotlib.pyplot as plt
import os



def process_images_in_folder(folder_path, operation, operand, num_images=5):
    # Get a list of all image files in the folder
    image_files = [f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))]

    # Display results for the first five images or the available number of images
    for i, image_file in enumerate(image_files[:num_images]):
        image_path = os.path.join(folder_path, image_file)
        print(f"\nProcessing Image {i + 1}: {image_path}")
        image_operations(image_path, operation, operand)


def apply_operation(img, operation, operand):
    if operation == '+':
        result_img = Image.eval(img, lambda x: x + operand)
    elif operation == '-':
        result_img = Image.eval(img, lambda x: x - operand)
    elif operation == '*':
        result_img = Image.eval(img, lambda x: x * operand)
    elif operation == '/':
        result_img = Image.eval(img, lambda x: x / operand)
    else:
        raise ValueError(f"Invalid operation: {operation}")

    return result_img

def image_operations(image_path, operation, operand):
    # Open the original image
    original_img = Image.open(image_path)

    # Convert the image to grayscale
    img_gray = ImageOps.grayscale(original_img)

    # Create a histogram for the original image
    histogram_original = img_gray.histogram()

    # Plot the original image, its grayscale version, and their histograms
    plt.subplot(2, 3, 1)
    plt.imshow(original_img)
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(2, 3, 2)
    plt.imshow(img_gray, cmap='gray')
    plt.title('Grayscale Image')
    plt.axis('off')

    plt.subplot(2, 3, 3)
    plt.bar(range(256), histogram_original, color='gray', alpha=0.7)
    plt.title('Original Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # Apply user-specified operation
    result_img = apply_operation(original_img, operation, operand)

    # Convert the resulting image to grayscale
    result_img_gray = ImageOps.grayscale(result_img)

    # Create a histogram for the resulting image
    histogram_result = result_img_gray.histogram()

    # Plot the resulting image, its grayscale version, and their histograms
    plt.subplot(2, 3, 4)
    plt.imshow(result_img)
    plt.title(f'Image {operation} Result')
    plt.axis('off')

    plt.subplot(2, 3, 5)
    plt.imshow(result_img_gray, cmap='gray')
    plt.title(f'Grayscale Result')
    plt.axis('off')

    plt.subplot(2, 3, 6)
    plt.bar(range(256), histogram_result, color='gray', alpha=0.7)
    plt.title(f'Histogram {operation} Result')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')

    # Adjust layout and display the figures
    plt.tight_layout()
    plt.show()

# Example usage+
image_set_folder = 'image_set'
operation = input("Enter operation (+, -, *, /): ")
operand = float(input("Enter operand value: "))
process_images_in_folder(image_set_folder, operation, operand)
