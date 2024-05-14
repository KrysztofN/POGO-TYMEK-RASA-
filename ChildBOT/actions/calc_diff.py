
# function to calculate the difference between
# date from the user and current date (UNIT TIMESTAMP)
def calc_dif(date1, date2):
    result = (date2 - date1)/86400
    return result
