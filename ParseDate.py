from datetime import datetime
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