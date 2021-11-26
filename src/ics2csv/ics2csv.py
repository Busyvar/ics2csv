#ics2csv
#brief : convertit des événements de calendrier en champs de fichier csv
#author: pelett "paulemmanuel.lett@posteo.net"

from icalendar import Calendar
import argparse


COLS = "Titre;Date;Description"

def get_safe_csv_field(data: str) -> str:
	return data.replace('\n','').replace('\r','').replace('"','').replace(';','')

def process_args():
    """arg parsing rules"""
    parser = argparse.ArgumentParser(description='Process some calendar.')
    parser.add_argument('--input', dest='input_filename', type=str, required=False,
                        help='the ics calendar filename input')
    parser.add_argument('--output', dest='output_filename', required=False,
                        help='the csv filename to output')
    parser.add_argument('--quiet', dest='quiet', required=False,
                        help='use CLI only', action="store_true")
    args = parser.parse_args()
    return args.output_filename, args.input_filename, args.quiet

def execute():
    """main execution flow for GUI and CLI"""
    output_filename , input_filename, quiet = process_args()
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

    c = get_calendar_from_input_file(input_filename)

    parsed_events = parse_events_from_calendar(c)

    generate_csv_file(parsed_events, output_filename)
    if not quiet:
        easygui.msgbox("Le calendrier: {}\n a généré la liste d'événement: {}".format(input_filename.rsplit("\\",1)[-1], output_filename.rsplit("\\",1)[-1]),"Génération terminé")

def get_calendar_from_input_file(input_filename: str):
    cal = open(input_filename,'r')
    c = Calendar.from_ical(cal.read())
    cal.close()
    return c

def parse_events_from_calendar(calendar:str) -> str:
    parsed_events = ""
    for component in calendar.walk():
        if component.name == "VEVENT":
            summary = component.get('summary')
            date = component.get('dtstart')
            description = component.get('description')
            if(summary):
                summary = get_safe_csv_field(summary)
            if(description):
                description = get_safe_csv_field(description)
            if date:
                date = date.dt
            format_data = "{};{};\"{}\";\n".format(summary, date, description)
            parsed_events += format_data
    return parsed_events

def generate_csv_file(parsed_events: str, output_filename:str):
    output = open(output_filename,"w+")
    output.write(COLS + '\n' + parsed_events)
    output.close()
