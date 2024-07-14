# Report: Occupancy Grid Creation and Visualization using OpenCV and Matplotlib

## Introduction

This report details a Python script that creates an occupancy grid map from an overhead room image. The grid map visually represents occupied and free spaces within the room. The script leverages OpenCV for image processing and Matplotlib for visualization.

## Script Overview

The script comprises two main functions:
1. `create_occupancy_grid(image_path, grid_size)`: Processes the image and generates the occupancy grid.
2. `visualize_occupancy_grid(occupancy_grid)`: Visualizes the occupancy grid using Matplotlib.

### Function 1: create_occupancy_grid

#### Inputs:
- `image_path`: The file path to the overhead image of the room.
- `grid_size`: The size of each grid cell in pixels.

#### Steps:
1. **Capture the Image**:
    ```python
    image = cv2.imread(image_path)
    ```
    The image is read using OpenCV's `cv2.imread()` function.

2. **Preprocess the Image**:
    ```python
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY)
    ```
    - Convert the image to grayscale using `cv2.cvtColor()`.
    - Apply binary thresholding with a threshold value of 128 to convert the grayscale image to a binary image.

3. **Define the Grid**:
    ```python
    height, width = binary_image.shape
    grid_height = height // grid_size
    grid_width = width // grid_size
    occupancy_grid = np.zeros((grid_height, grid_width))
    ```
    - Determine the dimensions of the grid based on the image size and grid cell size.
    - Initialize an empty occupancy grid of zeros.

4. **Classify Occupancy**:
    ```python
    for i in range(grid_height):
        for j in range(grid_width):
            cell = binary_image[i*grid_size:(i+1)*grid_size, j*grid_size:(j+1)*grid_size]
            occupancy = np.mean(cell) < 128  # Threshold to classify occupancy
            occupancy_grid[i, j] = occupancy
    ```
    - Iterate through each cell in the grid.
    - Calculate the mean value of the pixels within each cell.
    - Classify the cell as occupied if the mean pixel value is below 128.

#### Output:
- Returns the generated occupancy grid as a 2D NumPy array.

### Function 2: visualize_occupancy_grid

#### Inputs:
- `occupancy_grid`: The occupancy grid to be visualized.

#### Steps:
1. **Visualize the Grid**:
    ```python
    plt.imshow(occupancy_grid, cmap='gray')
    plt.title('Occupancy Grid Map')
    plt.xlabel('Width')
    plt.ylabel('Height')
    plt.show()
    ```
    - Use Matplotlib to display the occupancy grid as a grayscale image.
    - Add title and axis labels for better understanding.

## Example Usage

The script concludes with an example of how to use these functions:

```python
image_path = 'room_image.jpg'  # Path to the overhead image of the room
grid_size = 10  # Size of each grid cell in pixels

occupancy_grid = create_occupancy_grid(image_path, grid_size)
visualize_occupancy_grid(occupancy_grid)
```

- **`image_path`**: Specify the path to the room image.
- **`grid_size`**: Define the size of each grid cell.

## Conclusion

This script provides a straightforward method to generate and visualize occupancy grids from overhead images. The use of OpenCV and Matplotlib ensures efficient image processing and visualization. The resulting occupancy grid can be useful in various applications, including robotics and spatial analysis.
