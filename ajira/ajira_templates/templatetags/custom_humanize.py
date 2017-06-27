from django import template
from datetime import datetime, timezone

register = template.Library()


# {% commrate.time|humanizetimediff %}


@register.filter
def humanizeTimeDiff(timestamp=None):
    """
    Returns a humanized string representing time difference
    between now() and the input timestamp.

    The output rounds up to days, hours, minutes, or seconds.
    4 days 5 hours returns '4 days'
    0 days 4 hours 3 minutes returns '4 hours', etc...
    """
    import datetime

    timeDiff = datetime.datetime.now(timezone.utc) - timestamp
    days = round(timeDiff.days)
    hours = round(timeDiff.seconds / 3600)
    minutes = round(timeDiff.seconds % 3600 / 60)
    seconds = round(timeDiff.seconds % 3600 % 60)

    str = ""
    tStr = ""
    if days > 0:
        if days == 1:
            tStr = "day ago"
        else:
            tStr = "days ago"
        str = str + "%s %s" % (days, tStr)
        return str
    elif hours > 0:
        if hours == 1:
            tStr = "hour ago"
        else:
            tStr = "hours ago"
        str = str + "%s %s" % (hours, tStr)
        return str
    elif minutes > 0:
        if minutes == 1:
            tStr = "min ago"
        else:
            tStr = "mins ago"
        str = str + "%s %s" % (minutes, tStr)
        return str
    elif seconds > 0:
        if seconds == 1:
            tStr = "sec ago"
        else:
            tStr = "secs ago"
        str = str + "%s %s" % (seconds, tStr)
        return str
    else:
        return None