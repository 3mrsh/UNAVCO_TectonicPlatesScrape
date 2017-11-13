# UNAVCO Tectonic Plates Scrape
This Scrape was done as part of Lab 4 for Earth 202.
It extracts the displacements of 30 stations over time to calculate their Velocities in the North, East and Vertical direcitons.
It accounts for Earthquakes by analyzing the average velocity for each point relative to its immediate neighbors and comparing that to the mean; what lies furhter than 2 standard deviations away is considered an anomaly (an earthquake) and not considered in our average velocity.
This code automatically creates a workbook and stores its values inside of it.

##Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites
This code is done in Python 2.7.13 on macOS and relies on a few dependencies. For it to run, please install the following if you don't have them already:
```
Requests, XLSXWriter, URLlib2, BeautifulSoup
```
(Some may come already installed, but it's been so long since I've installed them that I've forgotten which!)

## Running the Code
To run the code, simply:
1) Download the repository. 
2) Open Python on your Terminal or favorite Python IDE
3) Run the following:
```
execfile('path_to_the_tectonicPlates.py_file')
```

## Notes on customization:
The IDs of the stations we analyze are provided in the sites variable. Any can be substituted in there.
The name of the Excel file may be changes in the declaration of our workbook variable.
The condition for outliers may be altered in our reject_outliers function.
