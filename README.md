# Vehicle GNSS Data Visualization and Analysis

This project processes GNSS (Global Navigation Satellite System) data from a vehicle and visualizes the vehicle's path along with its roll and pitch. It allows for the calculation of the GNSS module's projection onto the ground plane and the determination of the vehicle's heading angle between consecutive points.

## Features
- Load GNSS data from a CSV file.
- Calculate GNSS module projection based on pitch and roll angles.
- Visualize the vehicle's movement and GNSS projections in 2D.
- Display the vehicle's pitch and roll in 3D for a more accurate representation of the vehicle's orientation.

## Project Structure

- `main.py`: The entry point to the application. It initializes the `DataProcessor` class, loads the data, processes it, and visualizes the results.
- `dataProcessor.py`: Contains the `DataProcessor` class responsible for:
  - Loading and validating data.
  - Calculating the GNSS projection.
  - Calculating the heading angle between points.
  - Generating 3D and 2D visualizations of the vehicle's path.

## Requirements
- Python 3.x
- `pandas`
- `numpy`
- `matplotlib`
- `mpl_toolkits.mplot3d` (for 3D visualization)

You can install the required libraries by running:

```bash
pip install pandas numpy matplotlib
