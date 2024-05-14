from datetime import datetime

# used for "month:day" format
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


# print(get_date("4 styczeń 2024"))
# print(get_date("4.01.2024"))
# print(get_date("4 sty 2024"))
# print(get_date("4/01/2024"))
# print(get_date("4-01-2024"))
# print(get_date("04/01/2024"))
# print(get_date("4 lip 2024"))
# print(get_date("5 wrzesień 2024"))
# print(get_date("7 lip 2024"))
# print(get_date("9 gru 2024"))
# print(get_date("12 luty"))
# print(get_date("4 SIERpień"))
# print(get_date("15 MAJ"))
# print(get_date("sie 20"))
# print(get_date("10 05 24"))
# print(get_date("4 wrzesień 24"))
# print(get_date("4.wrzesień.24"))


test_dates = [
    "4 10 24", "4-10-24", "4/10/24", "4.10.24",
    "4 styczeń 2024", "4-styczeń-2024", "4/styczeń/2024", "4.styczeń.2024",
    "4.01.2024", "4/01/2024", "4 01 2024", "4-01-2024",
    "4 sty 2024", "4-sty-2024", "4.sty.2024", "4/sty/2024",
    "4 lipiec", "4/lipiec", "4.lipiec", "4-lipiec",
    "7 lip", "7-lip", "7/lip", "7.lip",
    "4 wrzesień 24", "4/wrzesień/24", "4-wrzesień-24", "4.luty.24", "maj 15", "maj 15 2024",
    "styczeń 20 24", "15-05"
]

for test_data in test_dates:
    print(f"{test_data}: {get_date(test_data)}")