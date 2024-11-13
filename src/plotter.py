import matplotlib.pyplot as plt

class GnssPlotter:
    """
    Class to handle the visualization of GNSS data from dataProcessor.py, including vehicle path and projections.
    """

    @staticmethod
    def plotVehiclePath(data):
       
        if data is None:
            print("Data is not loaded yet!")
            return False

        try:
            plt.figure(figsize=(12, 8))
            plt.plot(data['x_mm'], data['y_mm'], marker='o', label='Vehicle Path (Location)', color='green')
            plt.scatter(data['x_proj'], data['y_proj'], color='red', marker='x', label='GNSS Projections')

            for i in range(len(data)):  # Skip last point since it has no heading
                pointName = f"Point{i+1}"
                plt.annotate(f"{pointName}\nHeading: {data['heading_angle'].iloc[i]:.2f}°",
                             (data['x_mm'].iloc[i], data['y_mm'].iloc[i]),
                             textcoords="offset points", xytext=(10,10), ha='center', fontsize=8, color='blue')
                plt.plot([data['x_mm'].iloc[i], data['x_proj'].iloc[i]],
                         [data['y_mm'].iloc[i], data['y_proj'].iloc[i]], 'k--', linewidth=0.7)

            plt.xlabel('X Position (mm)')
            plt.ylabel('Y Position (mm)')
            plt.legend()
            plt.title('Vehicle Path with GNSS Projections and Heading Angles')
            plt.grid(True)
            plt.tight_layout()
            plt.show()
        except Exception as e:
            print(f"Error during plotting: {e}")
            return False
        return True
