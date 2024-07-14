
```python
import cv2
import numpy as np
import matplotlib.pyplot as plt

def create_occupancy_grid(image_path, grid_size):
    # Step 1: Capture the image
    image = cv2.imread(image_path)
    
    # Step 2: Preprocess the image
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)

    # Step 3: Define the grid
    height, width = binary_image.shape
    grid_height = height // grid_size
    grid_width = width // grid_size

    occupancy_grid = np.zeros((grid_height, grid_width))

    # Step 4: Classify occupancy
    for i in range(grid_height):
        for j in range(grid_width):
            cell = binary_image[i*grid_size:(i+1)*grid_size, j*grid_size:(j+1)*grid_size]
            occupancy = np.mean(cell) < 128  # Threshold to classify occupancy
            occupancy_grid[i, j] = occupancy

    return occupancy_grid

def visualize_occupancy_grid(occupancy_grid):
    plt.imshow(occupancy_grid, cmap='gray')
    plt.title('Occupancy Grid Map')
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.show()

# Example usage
image_path = 'room_image.jpg'  # Path to the overhead image of the room
grid_size = 10  # Size of each grid cell in pixels

occupancy_grid = create_occupancy_grid(image_path, grid_size)
visualize_occupancy_grid(occupancy_grid)
```
