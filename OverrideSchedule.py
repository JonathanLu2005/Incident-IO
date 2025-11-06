from ParseDate import ParseDate
from datetime import datetime

def GenerateOverrides(OverrideData, FromTime, UntilTime):
    """ Extracts each individual override from its array
    
    Arguments:
    - OverrideData (list[dict]): Info about each override
    - FromTime (datetime): Start of time period
    - UntilTime (datetime): End of time period

    Returns:
    - Overrides (list[dict]): Array of each override
    """
    Overrides = []

    for Override in OverrideData:
        OverrideStart = ParseDate(Override["start_at"])
        OverrideEnd = ParseDate(Override["end_at"])

        if OverrideEnd <= FromTime or OverrideStart >= UntilTime:
            continue 

        Start = max(OverrideStart, FromTime)
        End = min(OverrideEnd, UntilTime)

        Overrides.append({
            "User": Override["user"],
            "OverrideStart": Start.isoformat(),
            "OverrideEnd": End.isoformat()
        })

    Overrides.sort(key = lambda o : o["OverrideStart"])

    return Overrides

def InsertOverrides(BaseSchedule, Overrides):
    """ Insert overrides by adding entries thats affected by the override
    
    Arguments:
    - BaseSchedule (list[dict]): Oncall schedule without overrides 
    - Overrides (list[dict]): All overrides

    Returns:
    - Result (list[dict]): Schedule with overrides
    """
    i = j = 0

    Result = []

    while i < len(BaseSchedule) and j < len(Overrides):
        Entry = BaseSchedule[i]
        Override = Overrides[j]

        EntryStart = datetime.fromisoformat(Entry["StartAt"])
        EntryEnd = datetime.fromisoformat(Entry["EndAt"])

        OverrideStart = datetime.fromisoformat(Override["OverrideStart"])
        OverrideEnd = datetime.fromisoformat(Override["OverrideEnd"])

        if EntryEnd <= OverrideStart:
            Result.append(Entry)
            i += 1
            continue 

        if OverrideEnd <= EntryStart:
            j += 1
            continue 

        if EntryStart < OverrideStart:
            Result.append({
                "User": Entry["User"],
                "StartAt": EntryStart.isoformat(),
                "EndAt": OverrideStart.isoformat(),
            })

        Result.append({
            "User": Override["User"], 
            "StartAt": max(EntryStart, OverrideStart).isoformat(),
            "EndAt": min(EntryEnd, OverrideEnd).isoformat(),
        })

        if EntryEnd > OverrideEnd:
            BaseSchedule[i]["StartAt"] = OverrideEnd.isoformat()
            j += 1
        else:
            i += 1

    while i < len(BaseSchedule):
        Result.append(BaseSchedule[i])
        i += 1

    return Result