# COVID-19-Desktop-Tracker-v1.1

![Example Image of the software](/images/covid19_01.PNG)
![Example Plots](/images/covid-plot.jpg)

COVID-19 Desktop Tracker is a Graphical User Interface to retrieve and present data related to COVID-19 (SARS-CoV-2) built to run as a stand-alone software on Windows OS*.

This software enables the user to retrieve data, visualize the data in the form of graphs, and read some of the few latest news realted to Coronavirus.

Latest data and news is retrieved from three different APIs†. The software was written purely on Python 3.8 and utilizes PyQt for GUI design.

*This software has only been tested on Windows 10 64-bit Operating System.
†Latest data is subject to change depending on availability of APIs.


The latest data is retrieved from:
https://github.com/NovelCOVID/API

The data for the plots is retrieved from:
https://github.com/AlaeddineMessadi/COVID-19-REPORT-API

The News is retrieved from:
https://newsapi.org/

Plot data may differ from the latest data shown on the right because the plot data is updated on daily basis and is retrieved from a different API.

# How to run
To run the software make sure you have PyQt5, Python, and the font 'Montserrat' (provided in the files) installed. Run the "Main.py" to start the software.
