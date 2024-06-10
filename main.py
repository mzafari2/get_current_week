import datetime
def get_current_week():
    start_date = datetime.now() + timedelta(days = datetime.now().weeday())
    end_date = start_date + timedelta(days = 7)
    start_date= start_date.strftime("%B %d")
    end_date_date= end_date.strftime("%B %d")

    return(f"{start_date} - {end_date}")