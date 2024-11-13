from dataProcessor import GnssDataProcessor
from plotter import GnssPlotter

def main(filePath):
   
    processor = GnssDataProcessor(filePath)

    if not processor.loadData():
        print("Failed to load data.")
        return

    if not processor.calculateProjection():
        print("Failed to calculate projections.")
        return

    if not processor.calculateHeading():
        print("Failed to calculate heading angles.")
        return

    plotter = GnssPlotter()
    if not plotter.plotVehiclePath(processor.data):
        print("Failed to plot vehicle path.")
        return

if __name__ == "__main__":
    main('data/gnssData.csv')
