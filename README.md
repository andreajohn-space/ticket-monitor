# Ticket Monitor

A small Python script that checks Napoli's TicketOne event feed for an AC
Milan match and emails an alert when it finds a match.

## Requirements

- Python 3
- A Gmail account with an app password

Install the Python dependency:

```sh
python3 -m pip install -r requirements.txt
```

## Configure

Set these environment variables before running the script:

| Variable | Description |
| --- | --- |
| `EMAIL_USER` | Gmail address used to send the alert |
| `EMAIL_PASS` | Gmail app password (not your regular account password) |
| `EMAIL_TO` | Address that should receive the alert |

For example, in macOS or Linux:

```sh
export EMAIL_USER="you@gmail.com"
export EMAIL_PASS="your-app-password"
export EMAIL_TO="you@example.com"
python3 ticket-monitor.py
```

The script checks the feed once each time it runs. If you schedule it, use a
conservative interval and follow TicketOne's terms and access rules. The script
only sends an email alert; it does not purchase tickets.

## Notes

- The event feed and ticket availability can change; alerts are not guaranteed.
- Keep email credentials out of source control and logs.
