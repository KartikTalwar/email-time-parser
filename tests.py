import emailtimeparser

parser = emailtimeparser.EmailTimeParser()

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
