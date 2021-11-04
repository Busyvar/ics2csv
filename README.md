#Ics2Csv
A simple python script to convert specific data from icalendar to a csv file.
##Usage
![data processing workflow](ics2csv_data_processing.png)
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
##build dependencies
- Python3
- pyinstaller
- easygui (optional in CLI : for graphical use)
- icalendar

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