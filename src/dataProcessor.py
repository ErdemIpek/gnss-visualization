import pandas as pd
import numpy as np

class GnssDataProcessor:
    """
    GNSS data processing including loading, projections,
    heading calculation, and visualization.
    """

    def __init__(self, filePath, gnssHeight=1500):
        self.filePath = filePath
        self.gnssHeight = gnssHeight
        self.data = None

    def loadData(self):
        """Load data from a CSV file into a Pandas DataFrame."""
        try:
            self.data = pd.read_csv(self.filePath)
            requiredColumns = {'time_s', 'x_mm', 'y_mm', 'roll_deg', 'pitch_deg'}
            if not requiredColumns.issubset(self.data.columns):
                raise ValueError(f"Data must contain the columns: {requiredColumns}")
        except Exception as e:
            print(f"Error loading data: {e}")
            return False
        return True

    def calculateProjection(self):
        """
        calculate the projection of the GNSS module on the ground plane.
        adds 'x_proj' and 'y_proj' columns to the pandas dataframe.
        """
        if self.data is None:
            print("Data is not loaded yet!")
            return False

        try:
            self.data['x_proj'] = self.data['x_mm'] + self.gnssHeight * np.sin(np.radians(self.data['pitch_deg']))
            self.data['y_proj'] = self.data['y_mm'] + self.gnssHeight * np.sin(np.radians(self.data['roll_deg']))
        except Exception as e:
            print(f"Error during projection calculation: {e}")
            return False
        return True

    def calculateHeading(self):
        """
        calculate the heading angle between each consecutive point.
        adds 'heading_angle' column to the dataframe.
        """
        if self.data is None:
            print("Data is not loaded yet!")
            return False

        try:
            # Calculate heading for each consecutive point
            headings = np.arctan2(np.diff(self.data['y_mm']), np.diff(self.data['x_mm']))  # Radians
            self.data['heading_angle'] = np.append(np.degrees(headings), np.nan)  # Last point has no next point

            # If its last point use the last-1 point's heading.
            if np.isnan(self.data.loc[self.data.index[-1], 'heading_angle']):  # Correct way to access and modify last element
                self.data.loc[self.data.index[-1], 'heading_angle'] = self.data.loc[self.data.index[-2], 'heading_angle']  # Use previous heading for last point
        except Exception as e:
            print(f"Error during heading calculation: {e}")
            return False
        return True
