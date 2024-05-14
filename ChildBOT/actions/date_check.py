from datetime import datetime


def convert_date(date_str):
    month_pl = {
        "styczeń": "January", "luty": "February", "marzec": "March", "kwiecień": "April", "maj": "May",
        "czerwiec": "June", "lipiec": "July", "sierpień": "August", "wrzesień": "September", "październik": "October",
        "listopad": "November", "grudzień": "December", "sty": "Jan", "lut": "Feb", "mar": "Mar", "kwi": "Apr",
        "maj": "May", "cze": "Jun", "lip": "Jul", "sie": "Aug", "wrz": "Sep", "paź": "Oct", "lis": "Nov", "gru": "Dec"
    }

    for pl_month, en_month in month_pl.items():
        date_str = date_str.replace(pl_month, en_month)

    return date_str


def get_date(data_str):
    data_str = convert_date(data_str)
    data_str = data_str.lower()

    date_formats = [
        "%d %b %Y", "%d %B %Y", "%d %b %y", "%d %B %y",
        "%d %B", "%d %b", "%d-%B-%y", "%d.%B.%y", "%d/%B/%y",
        "%d-%B-%Y", "%d.%B.%Y", "%d/%B/%Y",
        "%d-%b-%Y", "%d.%b.%Y", "%d/%b/%Y",
        "%d-%B", "%d.%B", "%d/%B",
        "%d-%b", "%d.%b", "%d/%b",
        "%d %m %Y", "%d-%m-%Y", "%d/%m/%Y", "%d.%m.%Y",
        "%d %m %y", "%d-%m-%y", "%d/%m/%y", "%d.%m.%y",
        "%B %d", "%B-%d", "%B/%d", "%B.%d",
        "%B %d %Y", "%B/%d/%Y", "%B-%d-%Y", "%B.%d.%Y",
        "%B %d %y", "%B-%d-%y", "%B/%d/%y", "%B.%d.%y",
        "%d/%m", "%d-%m", "%d %m", "%d.%m",
    ]

    for date_format in date_formats:
        try:
            data = datetime.strptime(data_str, date_format)
            if "%Y" not in date_format:
                data = data.replace(year=datetime.now().year)
            return data
        except ValueError:
            pass

    return None
