# Ics2Csv
A simple python script to convert specific data from icalendar to a csv file.
## Usage
![demo_animation](./misc/demo.gif)

### Data flow
![data processing workflow](./misc/ics2csv_data_processing.png)

### command line options
>usage: ics2csv.py [-h] [--input INPUT_FILENAME] [--output OUTPUT_FILENAME] [--quiet]
>
>Process some calendar.
>
>optional arguments:
>  -h, --help            show this help message and exit
>  --input INPUT_FILENAME
>                        the ics calendar filename input
>  --output OUTPUT_FILENAME
>                        the csv filename to output
>  --quiet               use CLI only

## Installation
ics2csv is currently only tested for windows, you can launch ics2csv application as a standalone program.

## How to get ics file?
- https://help.zolasuite.com/portal/en/kb/articles/how-do-i-export-my-calendar-from-microsoft-outlook

## Building
### Dependency requirements
- Python3
- pyinstaller
- easygui (for graphical use)
- icalendar

To install all, use:
> pip install pyinstaller easygui icalendar

nb. pyinstaller might need admin right to install.

<!---
//diagram code for nomnoml
#direction: right
#fill: #ffde59
#arrowSize: 0.5
#lineWidth: 1.5
#title: ics2csv_data_processing
#spacing: 50

[<sender>Outlook, Gmail, ...]
[<transceiver>ics2csv.exe]
[<note>file.ics]
[<note>file.csv]
[<receiver>Excel, Google Sheet, ...]
[Outlook, Gmail, ...]-[file.ics]
[file.ics]-[ics2csv.exe]
[ics2csv.exe]-[file.csv]
[file.csv]-[Excel, Google Sheet, ...]
)
-->
### build command
>build.bat

## License
Creative Common CC0 2021
Dependencies mentioned in build dependencies section are distributed with their own license.
