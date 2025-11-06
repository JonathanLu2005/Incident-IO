import argparse
import json
from OncallSchedule import GenerateBaseSchedule
from OverrideSchedule import GenerateOverrides
from ParseDate import ParseDate

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
    Overrides = GenerateOverrides(OverridesData, FromTime, UntilTime)
    print(Overrides)

if __name__ == "__main__":
    Main()
