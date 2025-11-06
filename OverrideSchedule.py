from ParseDate import ParseDate

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
            "OverrideStart": Start,
            "OverrideEnd": End
        })

    Overrides.sort(key = lambda o : o["OverrideStart"])

    return Overrides