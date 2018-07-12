# toggler
simple toggl logger

### Installation
```bash
pip install -r requirements.txt
```

### How to use

Define these environment variables

- `TOGGL_API_TOKEN`: your personal toggl api token 
- `TOGGL_PROJECT_ID`: the project id to use for toggl time entries

*Note: Only one project is supported at this time.*

Then run
```
python toggler.py
```

That will fill in all your missing toggle entries: 
- 8 hours each weekday that does not have any existing time entry, 
- Covering the time range
  - from 90 days before the end of the current month 
  - to the end of the current month (ish)



# UAYOR (Use at your own risk :)
