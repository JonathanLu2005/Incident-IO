from datetime import timedelta

def GenerateBaseSchedule(ScheduleData, FromTime, UntilTime, StartTime):
    """ Converts the schedule into array of oncall for each user whilst factoring in from and until time

    Arguments:
    - ScheduleData (dict): Holds the provided oncall schedule
    - FromTime (datetime): Start of the time period
    - UntilTime (datetime): End of the time period
    - StartTime (datetime): Start for oncall period

    Returns:
    - list[dict]: Schedule for each user and when their oncall starts and end
    """
    Users = ScheduleData["users"]
    IntervalDays = ScheduleData["handover_interval_days"]
    IntervalDelta = timedelta(days=IntervalDays)

    Schedule = []
    UserIndex = 0
    CurrentStart = StartTime 

    while CurrentStart < UntilTime:
        CurrentEnd = CurrentStart + IntervalDelta 
        User = Users[UserIndex]

        if CurrentEnd > FromTime and CurrentStart < UntilTime:
            TruncatedStart = max(CurrentStart, FromTime)
            TruncatedEnd = min(CurrentEnd, UntilTime)

            Schedule.append({
                "User": User,
                "StartAt": TruncatedStart.isoformat(),
                "EndAt": TruncatedEnd.isoformat(),
            })

            CurrentStart = CurrentEnd 
            UserIndex = (UserIndex + 1) % len(Users)
    
    return Schedule