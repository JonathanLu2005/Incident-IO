#!/usr/bin/env python3

import os
import subprocess

FromTime = "2025-11-07T17:00:00Z"
UntilTime = "2025-11-21T17:00:00Z"

RenderScript = os.path.join(os.getcwd(), "render-schedule")
TestsDir = os.path.join(os.getcwd(), "Tests")

def RunTest(TestFolder):
    """ Retrieves files for each tests to run

    Arguments:
    - TestFolder (str): Name for folder with specific test
    
    Returns:
    - None
    """
    ScheduleFile = os.path.join(TestsDir, TestFolder, "schedule.json")
    OverridesFile = os.path.join(TestsDir, TestFolder, "overrides.json")

    Cmd = [
        "python", RenderScript,
        "--schedule", ScheduleFile,
        "--overrides", OverridesFile,
        "--from", FromTime,
        "--until", UntilTime
    ]

    Result = subprocess.run(Cmd, capture_output=True, text=True, check=True)

def Main():
    """ Run all tests and prints result

    Returns:
    - None
    """
    TestFolders = sorted([f for f in os.listdir(TestsDir) if f.lower().startswith("test")])
    Passed, Failed = 0, 0

    for Test in TestFolders:
        Success = RunTest(Test)
        if Success:
            Passed += 1
        else:
            Failed += 1

    print(f"\nTests completed. Passed: {Passed}, Failed: {Failed}")

if __name__ == "__main__":
    Main()