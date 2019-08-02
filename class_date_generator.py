from datetime import date, timedelta

#get first and last day of the semester
first_day = date(2019, 9, 4)
last_day = date(2019, 12, 13)

#get range of dates between them
delta = last_day - first_day

#pass all dates of semester into list
semester = [(first_day + timedelta(days=i)) for i in range(delta.days + 1)]

#filter out unnecessary dates using weekday indexing (0 = Monday, 6 = Sunday)
semester_filtered = [d for d in semester if d.weekday() == 0 or d.weekday() == 2 or d.weekday() == 4]

#set up conversion from integer to string
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

#get list of dates in the format: "{Day}, {Month} {Date}, {Year}"
for d in semester_filtered:
    print(weekdays[d.weekday()] + ', ' + d.strftime('%B %d'))
