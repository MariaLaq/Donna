import json
from datetime import datetime, timedelta


def load_events(filepath):
    """
    TODO: Open and parse the JSON file at `filepath`.
    """
    try:
        with open(filepath, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: File '{filepath}' is not a valid json.file")
        return []

pass

def upcoming_events(events, days=7):
    """
    TODO: Return only the events happening within the next `days` days.
    
    Think through:
    - What "right now" looks like as a datetime object
    - What the cutoff date is (today + `days`)
    - How to convert each event's date STRING into a datetime object
      so you can compare it
    - What condition means "this event is in range"
    """

    today = datetime.now()
    cutoff_date = today + timedelta(days=days)
    dates_in_range = []

    for event in events:
        event_datetime = datetime.strptime(event['date'], '%Y-%m-%d')
        if today <= event_datetime and event_datetime <= cutoff_date:
            print(event, "is in range")
            dates_in_range.append(event)

    return dates_in_range

pass

if __name__ == "__main__":
    events = load_events('events.json')
    print("Loaded events:", events)
    for e in upcoming_events(events):
        print(f"{e['date']}: {e['name']} ({e['type']})")