import argparse
import json
from datetime import datetime
from OncallSchedule import GenerateBaseSchedule
import sys

def ParseDate(Date):
    """ Convert dates from CLI into Python's datetime
    
    Arguments:
    - Date (str): Date received from CLI

    Returns:
    - datetime: Date in Python's datetime format
    """
    if Date.endswith("Z"):
        Date = Date[:-1] + "+00:00"

    try:
        return datetime.fromisoformat(Date)
    except ValueError:
        print(f"Invalid Date Time: {Date}", file=sys.stderr)
        sys.exit(1)

def Main():
    """ Parse CLI input and read JSON files into an object
    
    Returns:
    - None
    """
    Reader = argparse.ArgumentParser(
        description="Render on-call schedule with overrides applied."
    )

    Reader.add_argument("--schedule", required=True)
    Reader.add_argument("--overrides", required=True)
    Reader.add_argument("--from", dest="from_time", required=True)
    Reader.add_argument("--until", dest="until_time", required=True)
    Args = Reader.parse_args()

    FromTime = ParseDate(Args.from_time)
    UntilTime = ParseDate(Args.until_time)

    with open(Args.schedule) as f:
        ScheduleData = json.load(f)
    with open(Args.overrides) as f:
        OverridesData = json.load(f)

    StartTime = ParseDate(ScheduleData["handover_start_at"])
    BaseSchedule = GenerateBaseSchedule(ScheduleData, FromTime, UntilTime, StartTime)
    print(json.dumps(BaseSchedule, indent=2))

if __name__ == "__main__":
    Main()
