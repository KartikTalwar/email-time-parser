import re
import time


class MessageThenParser(object):

  def __init__(self):
    pass


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

  parser = MessageThenParser()

  # lmao tests
  for i in [('1min',60), ('1mins',60), ('2minutes',120), ('100minute',6000), ('100mins',6000)]:
    print parser.parse(i[0]) == i[1], i,'=>',parser.parse(i[0])

  for i in [('1hr',3600), ('2hrs',7200), ('10hours',36000), ('24hours',3600*24), ('0hr',0)]:
    print parser.parse(i[0]) == i[1], i,'=>',parser.parse(i[0])

  for i in [('1day',3600*24), ('10dys', 3600*10*24), ('2days', 3600*24*2)]:
    print parser.parse(i[0]) == i[1], i,'=>',parser.parse(i[0])

  for i in [('1wk',3600*24*7), ('10weeks', 3600*10*24*7), ('2wks', 3600*24*2*7), ('2w', 3600*24*2*7)]:
    print parser.parse(i[0]) == i[1], i,'=>',parser.parse(i[0])

  for i in [('1mo',3600*24*30), ('2months', 3600*24*2*30), ('10month', 3600*24*10*30)]:
    print parser.parse(i[0]) == i[1], i,'=>',parser.parse(i[0])

  for i in [('1yr',3600*24*365), ('2y', 3600*24*2*365), ('10years', 3600*24*10*365)]:
    print parser.parse(i[0]) == i[1], i,'=>',parser.parse(i[0])
