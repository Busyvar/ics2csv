#ics2csv
#brief : convertit des événements de calendrier en champs de fichier csv

#from ics import Calendar
from icalendar import Calendar
import sys
import argparse

#arg parsing
parser = argparse.ArgumentParser(description='Process some calendar.')
parser.add_argument('--input', dest='input_filename', type=str, required=False,
                    help='the ics calendar filename input')
parser.add_argument('--output', dest='output_filename', required=False,
                    help='the csv filename to output')
parser.add_argument('--quiet', dest='quiet', required=False,
                    help='use CLI only', action="store_true")

args = parser.parse_args()
output_filename = args.output_filename
input_filename = args.input_filename
quiet = args.quiet
if not quiet:
	import easygui

#default options
if not input_filename:
	if not quiet:
		input_filename = easygui.fileopenbox()
	else:
		raise Exception("input file is mandatory when using quiet mode")
if not output_filename:
	output_filename = input_filename.replace('.ics','.csv')

cal = open(input_filename,'r')

g = open(input_filename,'rb')
c = Calendar.from_ical(cal.read())

COLS = "Titre;Date;Description"
parsed_events = ""

for component in c.walk():
	if component.name == "VEVENT":
		summary = component.get('summary')
		date = component.get('dtstart')
		description = component.get('description')
		if(summary):
			summary.replace('\n','')
		if(description):
			description.replace('\n','')
		if date:
			date = date.dt
		format_data = "{};{};{};\n".format(summary, date, description)
		parsed_events += format_data



#c = Calendar(cal.read())
cal.close()

output = open(output_filename,"w+")
output.write(COLS + '\n' + parsed_events)
output.close()

if not quiet:
	easygui.msgbox("Le calendrier: {}\n a généré la liste d'événement: {}".format(input_filename.rsplit("\\",1)[-1], output_filename.rsplit("\\",1)[-1]),"Génération terminé")