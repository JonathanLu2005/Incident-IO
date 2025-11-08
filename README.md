# Incident.io On-Call Scheduler

This is my solution to the provided take-home assessment.

---

## Setup Instructions

This project uses **Python 3.12+**.

To install dependencies, run:

```bash
pip install -r requirements.txt
```

---

## Running the Script

From the **project root directory**, run:

```bash
./render-schedule \
  --schedule=schedule.json \
  --overrides=overrides.json \
  --from='2025-11-07T17:00:00Z' \
  --until='2025-11-21T17:00:00Z'
```

### On Windows:
```bash
python render-schedule --schedule schedule.json --overrides overrides.json --from "2025-11-07T17:00:00Z" --until "2025-11-21T17:00:00Z"
```

---

## Input Files

You’ll need two JSON files in the main directory:

- **`schedule.json`** — defines the base on-call rotation  
- **`overrides.json`** — defines temporary coverage overrides  

You can replace these with your own files to test different scenarios.

---

## Testing

To verify functionality, the repository includes a **`Tests/`** folder containing multiple cases.

You can automatically run all tests with:

```bash
python Tests.py
```

---

## Notes

**Video Walkthrough:** [https://youtu.be/3KUJEluZp6o](https://youtu.be/3KUJEluZp6o)