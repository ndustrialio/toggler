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
- `TOGGL_DEFAULT_DESCRIPTION`: the default description to use for toggl time entries

*Note: Only one project is supported at this time.*

Then run
```
python toggler.py
```

That will fill in all your missing toggle entries: 
- 8 ($$ billable) hours each weekday that does not have any existing time entry, 
- Covering the time range
  - from 90 days before the end of last month 
  - to the end of last month


# UAYOR: Use at your own risk, and keep away from the reach of micro managers :)
