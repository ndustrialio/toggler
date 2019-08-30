# toggler
simple toggl logger

### Installation
```bash
pip install -r requirements.txt
```

### How to use

Define these environment variables

- `TOGGL_API_TOKEN`: your personal toggl api token
- `TOGGL_PROJECT_ID`: the project id to use for toggl time entries. See below.
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

### How to get projectID
- Open Toggl in your browser, navigate to the project
- In the URL, the last ID is that projectID, e.g. "https://toggl.com/app/projects/615158/edit/30715891" - the projectID is 30715891

# UAYOR: Use at your own risk, and keep away from the reach of micro managers :)
