import re
import time


class EmailTimeParser(object):

  def __init__(self):
    self.days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    self.months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']
    self.weekdays_short = ['mon', 'tue', 'wed', 'thu', 'thurs', 'fri', 'sat', 'sun']
    self.months_short = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']


  def parse(self, email):
    stamp = self._clean_email(email)
    adder = 0

    mins = re.search("^(\d+){0,3}(m|min|minute|mins|minutes)$", stamp)
    if mins:
      adder += int(mins.groups()[0]) * 60

    hours = re.search("^(\d+){0,3}(h|hr|hours|hrs|hour)$", stamp)
    if hours:
      adder += int(hours.groups()[0]) * 60 *60

    days = re.search("^(\d+){0,3}(d|days|day|dys)$", stamp)
    if days:
      adder += int(days.groups()[0]) * 60 *60 *24

    weeks = re.search("^(\d+){0,2}(w|weeks|week|wk|wks)$", stamp)
    if weeks:
      adder += int(weeks.groups()[0]) * 60 *60 *24*7

    months = re.search("^(\d+){0,1}(month|months|mo)$", stamp)
    if months:
      adder += int(months.groups()[0]) * 60 *60 *24*30

    years = re.search("^(\d+){0,2}(yrs|yr|years|year|y)$", stamp)
    if years:
      adder += int(years.groups()[0]) * 60 *60 *24*365

    return adder


  def _clean_email(self, email):
    return email.split('@')[0].lower()



if __name__ == '__main__':
  pass
