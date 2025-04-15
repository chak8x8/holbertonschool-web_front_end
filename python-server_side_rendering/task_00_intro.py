#!/usr/bin/env python3

def generate_invitations(template, attendees):
    if not isinstance (template, str):
        print("Error: template must be a string.")
        return
    if not isinstance (attendees, list) or not all (isinstance(a, dict) for a in attendees):
        print("Error: attendees must be a list of dictionaries.")
        return
    
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, person in enumerate(attendees, start=1):
        safe = {key: (person.get(key) or "N/A") for key in placeholders}

        filled_invite = template.format(**safe)
        filename = "output_{}.txt".format(idx)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(filled_invite)

        print("Created {}".format(filename))