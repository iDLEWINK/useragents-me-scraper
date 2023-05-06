from datetime import datetime, date, timedelta


def get_week_timeframe():
    """ Returns two _Date values - start_date (today) and end_date (date 7 days after start_date)

    Returns
    -------
    _Date 
      The date today.
    _Date
      The date excatly 7 days after today.
    """
    start_date = date.today()
    end_date = start_date + timedelta(days=7)
    return start_date, end_date


def is_outdated(end_date):
    """ Returns true or false depending on whether the date today is past the end date argument or not.

    Parameters
    ----------
    end_date : str
      The date that the date today is going to be compared to

    Returns
    -------
    boolean
      True if the date is outdated. False if the date is not outdated.
    """

    end_date = datetime.strptime(str(end_date), '%Y-%m-%d').date()
    return date.today() > end_date
