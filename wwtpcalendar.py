# #%%
# from datetime import datetime, timedelta
# import holidays
# import calendar
# import matplotlib.pyplot as plt

# # Define the cantonal holidays
# cantonal_holidays = {
#     'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
#     'Bern': holidays.CountryHoliday('CH', prov='BE'),
#     'Graubunden': holidays.CountryHoliday('CH', prov = 'GR'),
#     'Neuenburg': holidays.CountryHoliday('CH',prov = 'NE'),
#     'Soleure': holidays.CountryHoliday('CH', prov = 'SO'),
#     'Vaud': holidays.CountryHoliday('CH', prov = 'VD'),
#     'Ticino' : holidays.CountryHoliday('CH', prov = 'TI'),
#     'Basel': holidays.CountryHoliday('CH', prov = 'BS'),
#     'Lucerne': holidays.CountryHoliday('CH', prov = 'LU'),
#     'Geneva': holidays.CountryHoliday('CH', prov = 'GE'),
#     'Schwyz': holidays.CountryHoliday('CH', prov = 'SZ'),
#     'Jura': holidays.CountryHoliday('CH', prov = 'JU'),
#     'Glarus': holidays.CountryHoliday('CH', prov = 'GL')

#     # Add more cantonal holidays here...
# }

# #%%
# def get_sample_schedule(start_date, end_date, wwtp):
#     schedule = {}
#     current_date = start_date

#     while current_date <= end_date:
#         shipment_date = current_date + timedelta(days=1)  # Samples shipped overnight
#         arrival_date = shipment_date.replace(hour=9, minute=0)  # Samples arrive at 9 am

#         # Adjust shipment and arrival dates for holidays
#         canton_holidays = cantonal_holidays.get(wwtp.canton, {})
#         while shipment_date in canton_holidays or arrival_date in canton_holidays:
#             shipment_date += timedelta(days=1)
#             arrival_date += timedelta(days=1)

#         # Determine which samples to take
#         samples = []
#         sample_date = current_date - timedelta(days=1)
#         for _ in range(5):
#             samples.append(sample_date)
#             sample_date -= timedelta(days=1)

#         sample_dates = samples[::-1]  # Reverse order to match most recent to oldest
#         alternate_biweekly = False  # Flag for alternating biweekly selection

#         for _ in range(2):
#             if alternate_biweekly:
#                 sample_dates.append(sample_dates[-1] - timedelta(days=2))
#             else:
#                 sample_dates.append(sample_dates[-1] - timedelta(days=1))

#             alternate_biweekly = not alternate_biweekly

#         schedule[arrival_date] = sample_dates
#         current_date += timedelta(days=1)

#     return schedule

# #%%
# # Define a class for wastewater treatment plants
# class WWTP:
#     def __init__(self, name, canton, send_day):
#         self.name = name
#         self.canton = canton
#         self.send_day = send_day

# # Create the wastewater treatment plants
# wwtps = [
#     WWTP('Zurich', 'Zurich', 'Monday'),
#     WWTP('Chur', 'Graubunden', 'Monday'),
#     WWTP('Neuchatel', 'Neuenberg', 'Monday'),
#     WWTP('Lausanne', 'Vaud', 'Monday'),
#     WWTP('Solothurn', 'Soleure', 'Monday'),
#     WWTP('Laupen', 'Bern', 'Tuesday'),
#     WWTP('Lugano', 'Ticino', 'Tuesday'),
#     WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
#     WWTP('Basel', 'Basel', 'Tuesday'),
#     WWTP('Buholz', 'Lucerne', 'Tuesday'),
#     WWTP('Geneva', 'Geneva', 'Wednesday'),
#     WWTP('Bern', 'Bern', 'Wednesday'),
#     WWTP('Schwyz', 'Schwyz', 'Wednesday'),
#     WWTP('Porrentruy', 'Jura', 'Wednesday'),
#     WWTP('Glarnerland', 'Glarus', 'Wednesday'),
# ]

# # Example usage
# start_date = datetime.now()
# end_date = datetime(2024, 7, 31)

# # Generate the schedule for each WWTP
# wwtp_schedules = {}
# for wwtp in wwtps:
#     wwtp_schedule = get_sample_schedule(start_date, end_date, wwtp)
#     wwtp_schedules[wwtp.name] = wwtp_schedule

# # Generate calendar figure
# fig, ax = plt.subplots(figsize=(12, 8))
# cal = calendar.Calendar()
# month_names = calendar.month_name[1:]

# for month in range(1, 13):
#     month_days = cal.itermonthdates(end_date.year, month)
#     month_days = [day for day in month_days if day.month == month]

#     for wwtp in wwtps:
#         wwtp_schedule = wwtp_schedules[wwtp.name]
#         month_schedule = [wwtp_schedule.get(day, []) for day in month_days]
#         sample_days = [day.day for week in month_schedule for day in week]

#         # Convert month_days to matplotlib dates
#         month_days_mdates = [mdates.date2num(day) for day in month_days]

#         ax.plot_date(month_days_mdates, sample_days, marker='o', linestyle='-', label=wwtp.name)

# ax.set_title('WWTP Sample Schedule')
# ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# ax.grid(True)
# plt.tight_layout()
# plt.show()


# # %%
# from datetime import datetime, timedelta
# import holidays
# import calendar
# import matplotlib.pyplot as plt
# import matplotlib.dates as mdates

# # Define the cantonal holidays
# cantonal_holidays = {
#     'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
#     'Bern': holidays.CountryHoliday('CH', prov='BE'),
#     'Graubunden': holidays.CountryHoliday('CH', prov = 'GR'),
#     'Neuenburg': holidays.CountryHoliday('CH',prov = 'NE'),
#     'Soleure': holidays.CountryHoliday('CH', prov = 'SO'),
#     'Vaud': holidays.CountryHoliday('CH', prov = 'VD'),
#     'Ticino' : holidays.CountryHoliday('CH', prov = 'TI'),
#     'Basel': holidays.CountryHoliday('CH', prov = 'BS'),
#     'Lucerne': holidays.CountryHoliday('CH', prov = 'LU'),
#     'Geneva': holidays.CountryHoliday('CH', prov = 'GE'),
#     'Schwyz': holidays.CountryHoliday('CH', prov = 'SZ'),
#     'Jura': holidays.CountryHoliday('CH', prov = 'JU'),
#     'Glarus': holidays.CountryHoliday('CH', prov = 'GL')

#     # Add more cantonal holidays here...
# }

# def get_sample_schedule(start_date, end_date, wwtp):
#     schedule = {}
#     current_date = start_date

#     while current_date <= end_date:
#         shipment_date = current_date + timedelta(days=1)  # Samples shipped overnight
#         arrival_date = shipment_date.replace(hour=9, minute=0)  # Samples arrive at 9 am

#         # Adjust shipment and arrival dates for holidays
#         canton_holidays = cantonal_holidays.get(wwtp.canton, {})
#         while shipment_date in canton_holidays or arrival_date in canton_holidays:
#             shipment_date += timedelta(days=1)
#             arrival_date += timedelta(days=1)

#         # Determine which samples to take
#         samples = []
#         sample_date = current_date - timedelta(days=1)
#         for _ in range(5):
#             samples.append(sample_date)
#             sample_date -= timedelta(days=1)

#         sample_dates = samples[::-1]  # Reverse order to match most recent to oldest
#         alternate_biweekly = False  # Flag for alternating biweekly selection

#         for _ in range(2):
#             if alternate_biweekly:
#                 sample_dates.append(sample_dates[-1] - timedelta(days=2))
#             else:
#                 sample_dates.append(sample_dates[-1] - timedelta(days=1))

#             alternate_biweekly = not alternate_biweekly

#         schedule[arrival_date] = sample_dates
#         current_date += timedelta(days=1)

#     return schedule

# # Define a class for wastewater treatment plants
# class WWTP:
#     def __init__(self, name, canton, send_day):
#         self.name = name
#         self.canton = canton
#         self.send_day = send_day

# # Create the wastewater treatment plants
# wwtps = [
#     WWTP('Zurich', 'Zurich', 'Monday'),
#     WWTP('Chur', 'Graubunden', 'Monday'),
#     WWTP('Neuchatel', 'Neuenberg', 'Monday'),
#     WWTP('Lausanne', 'Vaud', 'Monday'),
#     WWTP('Solothurn', 'Soleure', 'Monday'),
#     WWTP('Laupen', 'Bern', 'Tuesday'),
#     WWTP('Lugano', 'Ticino', 'Tuesday'),
#     WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
#     WWTP('Basel', 'Basel', 'Tuesday'),
#     WWTP('Buholz', 'Lucerne', 'Tuesday'),
#     WWTP('Geneva', 'Geneva', 'Wednesday'),
#     WWTP('Bern', 'Bern', 'Wednesday'),
#     WWTP('Schwyz', 'Schwyz', 'Wednesday'),
#     WWTP('Porrentruy', 'Jura', 'Wednesday'),
#     WWTP('Glarnerland', 'Glarus', 'Wednesday'),
# ]

# # Example usage
# start_date = datetime.now()
# end_date = datetime(2024, 7, 31)

# # Generate the schedule for each WWTP
# wwtp_schedules = {}
# for wwtp in wwtps:
#     wwtp_schedule = get_sample_schedule(start_date, end_date, wwtp)
#     wwtp_schedules[wwtp.name] = wwtp_schedule

# # Generate calendar figure
# fig, ax = plt.subplots(figsize=(12, 8))
# cal = calendar.Calendar()
# month_names = calendar.month_name[1:]

# for month in range(1, 13):
#     month_days = cal.itermonthdates(end_date.year, month)
#     month_days = [day for day in month_days if day.month == month]

#     for wwtp in wwtps:
#         wwtp_schedule = wwtp_schedules[wwtp.name]
#         month_schedule = [wwtp_schedule.get(day, []) for day in month_days]
#         sample_days = [day.day for week in month_schedule for day in week]

#         # Convert month_days to matplotlib dates
#         month_days_mdates = [mdates.date2num(day) for day in month_days]

#         ax.plot_date(month_days_mdates, sample_days, marker='o', linestyle='-', label=wwtp.name)

# ax.set_title('WWTP Sample Schedule')
# ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
# ax.grid(True)
# plt.tight_layout()
# plt.show()

# import datetime
#%%
import csv
import datetime
import holidays

# Define the WWTP class
class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

# Define the WWTPs and their shipment days
wwtps = [
    WWTP('Zurich', 'Zurich', 'Monday'),
    WWTP('Chur', 'Graubunden', 'Monday'),
    WWTP('Neuchatel', 'Neuenburg', 'Monday'),
    WWTP('Lausanne', 'Vaud', 'Monday'),
    WWTP('Solothurn', 'Solothurn', 'Monday'),
    WWTP('Laupen', 'Bern', 'Tuesday'),
    WWTP('Lugano', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
    WWTP('Basel', 'Basel-Stadt', 'Tuesday'),
    WWTP('Buholz', 'Lucerne', 'Tuesday'),
    WWTP('Geneva', 'Geneva', 'Wednesday'),
    WWTP('Bern', 'Bern', 'Wednesday'),
    WWTP('Schwyz', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy', 'Jura', 'Wednesday'),
    WWTP('Glarnerland', 'Glarus', 'Wednesday'),
]

# Define cantonal holidays
cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Solothurn': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel-Stadt': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
    # Add more cantonal holidays here...
}

# Get the start and end date of the next 52 weeks
current_date = datetime.datetime.now().date()
start_date = current_date - datetime.timedelta(days=current_date.weekday())
end_date = start_date + datetime.timedelta(weeks=52)

# Generate the list of dates for each week
weeks = []
while start_date <= end_date:
    week_dates = [start_date + datetime.timedelta(days=i) for i in range(7)]
    weeks.append(week_dates)
    start_date += datetime.timedelta(weeks=1)

# Generate the week-by-week table
table = [['Week'] + [wwtp.name for wwtp in wwtps]]

for week_dates in weeks:
    week_row = [week_dates[0].strftime('%Y-%m-%d')]
    for wwtp in wwtps:
        holidays_canton = cantonal_holidays.get(wwtp.canton, {})
        conflicting_holidays = [date.strftime('%Y-%m-%d') for date in week_dates if date in holidays_canton]

        if wwtp.shipment_day == 'Monday' and wwtp.canton == 'Zurich':
            conflicting_holidays += [date.strftime('%Y-%m-%d') for date in week_dates if date.weekday() >= 1 and date.weekday() <= 3 and date in holidays_canton]

        week_row.append(', '.join(conflicting_holidays))

    table.append(week_row)

# Save the week-by-week table as a CSV file
with open('wwtp_holidays.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

import csv
import datetime
import holidays

# Define the WWTP class
class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

# Define the WWTPs and their shipment days
wwtps = [
    WWTP('Zurich', 'Zurich', 'Monday'),
    WWTP('Chur', 'Graubunden', 'Monday'),
    WWTP('Neuchatel', 'Neuenburg', 'Monday'),
    WWTP('Lausanne', 'Vaud', 'Monday'),
    WWTP('Solothurn', 'Solothurn', 'Monday'),
    WWTP('Laupen', 'Bern', 'Tuesday'),
    WWTP('Lugano', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
    WWTP('Basel', 'Basel-Stadt', 'Tuesday'),
    WWTP('Buholz', 'Lucerne', 'Tuesday'),
    WWTP('Geneva', 'Geneva', 'Wednesday'),
    WWTP('Bern', 'Bern', 'Wednesday'),
    WWTP('Schwyz', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy', 'Jura', 'Wednesday'),
    WWTP('Glarnerland', 'Glarus', 'Wednesday'),
]

# Define cantonal holidays
cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Solothurn': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel-Stadt': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
    # Add more cantonal holidays here...
}

# Get the start and end date of the next 52 weeks
current_date = datetime.datetime.now().date()
start_date = current_date - datetime.timedelta(days=current_date.weekday())
end_date = start_date + datetime.timedelta(weeks=52)

# Generate the list of dates for each week
weeks = []
while start_date <= end_date:
    week_dates = [start_date + datetime.timedelta(days=i) for i in range(7)]
    weeks.append(week_dates)
    start_date += datetime.timedelta(weeks=1)

# Generate the week-by-week table
table = [['Week'] + [wwtp.name for wwtp in wwtps]]

for week_dates in weeks:
    week_row = [week_dates[0].strftime('%Y-%m-%d')]
    for wwtp in wwtps:
        holidays_canton = cantonal_holidays.get(wwtp.canton, {})
        conflicting_holidays = [date.strftime('%A') for date in week_dates if date in holidays_canton]

        if wwtp.shipment_day == 'Monday' and wwtp.canton == 'Zurich':
            conflicting_holidays += [date.strftime('%A') for date in week_dates if date.weekday() >= 1 and date.weekday() <= 3 and date in holidays_canton]

        week_row.append(', '.join(conflicting_holidays))

    table.append(week_row)

# Save the week-by-week table as a CSV file
with open('wwtp_holidays1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

import csv
import datetime
import holidays

# Define the WWTP class
class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

# Define the WWTPs and their shipment days
wwtps = [
    WWTP('Zurich (Mon)', 'Zurich', 'Monday'),
    WWTP('Chur (Mon)', 'Graubunden', 'Monday'),
    WWTP('Neuchatel (Mon)', 'Neuenburg', 'Monday'),
    WWTP('Lausanne (Mon)', 'Vaud', 'Monday'),
    WWTP('Solothurn (Mon)', 'Solothurn', 'Monday'),
    WWTP('Laupen (Tue)', 'Bern', 'Tuesday'),
    WWTP('Lugano (Tue)', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein (Tue)', 'Graubunden', 'Tuesday'),
    WWTP('Basel (Tue)', 'Basel-Stadt', 'Tuesday'),
    WWTP('Buholz (Tue)', 'Lucerne', 'Tuesday'),
    WWTP('Geneva (Wed)', 'Geneva', 'Wednesday'),
    WWTP('Bern (Wed)', 'Bern', 'Wednesday'),
    WWTP('Schwyz (Wed)', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy (Wed)', 'Jura', 'Wednesday'),
    WWTP('Glarnerland (Wed)', 'Glarus', 'Wednesday'),
]

# Define cantonal holidays
cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Solothurn': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel-Stadt': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
    # Add more cantonal holidays here...
}

# Get the start and end date of the next 52 weeks
current_date = datetime.datetime.now().date()
start_date = current_date - datetime.timedelta(days=current_date.weekday())
end_date = start_date + datetime.timedelta(weeks=52)

# Generate the list of dates for each week
weeks = []
while start_date <= end_date:
    week_dates = [start_date + datetime.timedelta(days=i) for i in range(7)]
    weeks.append(week_dates)
    start_date += datetime.timedelta(weeks=1)

# Generate the week-by-week table
table = [['Week'] + [wwtp.name for wwtp in wwtps]]

for week_dates in weeks:
    week_row = [week_dates[0].strftime('%A')]
    for wwtp in wwtps:
        holidays_canton = cantonal_holidays.get(wwtp.canton, {})
        conflicting_holidays = [date.strftime('%a - %d.%m') for date in week_dates if date in holidays_canton]
        
        if wwtp.shipment_day == 'Monday' and wwtp.canton == 'Zurich':
            conflicting_holidays += [date.strftime('%a - %d.%m') for date in week_dates if date.weekday() >= 1 and date.weekday() <= 3 and date in holidays_canton]

        week_row.append(', '.join(conflicting_holidays))

    table.append(week_row)

# Save the week-by-week table as a CSV file
with open('wwtp_holidays2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

import csv
import datetime
import holidays

# Define the WWTP class and their shipment days
class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

wwtps = [
    WWTP('Zurich (Mon)', 'Zurich', 'Monday'),
    WWTP('Chur (Mon)', 'Graubunden', 'Monday'),
    WWTP('Neuchatel (Mon)', 'Neuenburg', 'Monday'),
    WWTP('Lausanne (Mon)', 'Vaud', 'Monday'),
    WWTP('Solothurn (Mon)', 'Solothurn', 'Monday'),
    WWTP('Laupen (Tue)', 'Bern', 'Tuesday'),
    WWTP('Lugano (Tue)', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein (Tue)', 'Graubunden', 'Tuesday'),
    WWTP('Basel (Tue)', 'Basel-Stadt', 'Tuesday'),
    WWTP('Buholz (Tue)', 'Lucerne', 'Tuesday'),
    WWTP('Geneva (Wed)', 'Geneva', 'Wednesday'),
    WWTP('Bern (Wed)', 'Bern', 'Wednesday'),
    WWTP('Schwyz (Wed)', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy (Wed)', 'Jura', 'Wednesday'),
    WWTP('Glarnerland (Wed)', 'Glarus', 'Wednesday'),
]

# Define cantonal holidays
cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Solothurn': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel-Stadt': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
    # Add more cantonal holidays here...
}

# Get the start and end date of the next 52 weeks
current_date = datetime.datetime.now().date()
start_date = current_date - datetime.timedelta(days=current_date.weekday())
end_date = start_date + datetime.timedelta(weeks=52)

# Generate the list of dates for each week
weeks = []
while start_date <= end_date:
    week_dates = [start_date + datetime.timedelta(days=i) for i in range(7)]
    weeks.append(week_dates)
    start_date += datetime.timedelta(weeks=1)

# Generate the week-by-week table
table = [['Week'] + [wwtp.name for wwtp in wwtps]]

for week_dates in weeks:
    week_row = [week_dates[0].strftime('%A, %B %d, %Y')]
    for wwtp in wwtps:
        holidays_canton = cantonal_holidays.get(wwtp.canton, {})
        conflicting_holidays = [date.strftime('%a - %d.%m') for date in week_dates if date in holidays_canton]

        if wwtp.shipment_day == 'Monday' and wwtp.canton == 'Zurich':
            conflicting_holidays += [date.strftime('%a - %d.%m') for date in week_dates if 1 <= date.weekday() <= 3 and date in holidays_canton]

        week_row.append(', '.join(conflicting_holidays))

    table.append(week_row)

# Save the week-by-week table as a CSV file
with open('wwtp_holidays4.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

import csv
import datetime
import holidays

# Define the WWTP class and their shipment days
class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

wwtps = [
    WWTP('Zurich', 'Zurich', 'Monday'),
    WWTP('Chur', 'Graubunden', 'Monday'),
    WWTP('Neuchatel', 'Neuenburg', 'Monday'),
    WWTP('Lausanne', 'Vaud', 'Monday'),
    WWTP('Solothurn', 'Solothurn', 'Monday'),
    WWTP('Laupen', 'Bern', 'Tuesday'),
    WWTP('Lugano', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
    WWTP('Basel', 'Basel-Stadt', 'Tuesday'),
    WWTP('Buholz', 'Lucerne', 'Tuesday'),
    WWTP('Geneva', 'Geneva', 'Wednesday'),
    WWTP('Bern', 'Bern', 'Wednesday'),
    WWTP('Schwyz', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy', 'Jura', 'Wednesday'),
    WWTP('Glarnerland', 'Glarus', 'Wednesday'),
]

# Define cantonal holidays
cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Solothurn': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel-Stadt': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
    # Add more cantonal holidays here...
}

# Get the start and end date of the next 52 weeks
current_date = datetime.datetime.now().date()
start_date = current_date - datetime.timedelta(days=current_date.weekday())
end_date = start_date + datetime.timedelta(weeks=52)

# Generate the list of dates for each week
weeks = []
while start_date <= end_date:
    week_dates = [start_date + datetime.timedelta(days=i) for i in range(7)]
    weeks.append(week_dates)
    start_date += datetime.timedelta(weeks=1)

# Generate the week-by-week table
table = [['Week'] + ['Purple group'] + ['Orange group'] + ['Green group']]

for week_dates in weeks:
    week_row = [week_dates[0].strftime('%A, %B %d, %Y')]

    for wwtp in wwtps:
        if wwtp.shipment_day == 'Monday' and wwtp.canton == 'Zurich':
            group = 'Purple group'
        elif wwtp.shipment_day == 'Tuesday':
            group = 'Orange group'
        elif wwtp.shipment_day == 'Wednesday':
            group = 'Green group'
        else:
            group = ''

        holidays_canton = cantonal_holidays.get(wwtp.canton, {})
        conflicting_holidays = []
        for date in week_dates:
            if date in holidays_canton:
                holiday_name = holidays_canton.get(date)
                conflicting_holidays.append(f'{wwtp.name} | {date.strftime("%a")} {date.strftime("%d.%m")} ({holiday_name})')

        week_row.append('\n'.join(conflicting_holidays))

    table.append(week_row)

# Save the week-by-week table as a CSV file
with open('wwtp_holidays10.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

import csv
import datetime
import holidays

# Define the WWTP class and their shipment days
class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

wwtps = [
    WWTP('Zurich', 'Zurich', 'Monday'),
    WWTP('Chur', 'Graubunden', 'Monday'),
    WWTP('Neuchatel', 'Neuenburg', 'Monday'),
    WWTP('Lausanne', 'Vaud', 'Monday'),
    WWTP('Solothurn', 'Solothurn', 'Monday'),
    WWTP('Laupen', 'Bern', 'Tuesday'),
    WWTP('Lugano', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
    WWTP('Basel', 'Basel-Stadt', 'Tuesday'),
    WWTP('Buholz', 'Lucerne', 'Tuesday'),
    WWTP('Geneva', 'Geneva', 'Wednesday'),
    WWTP('Bern', 'Bern', 'Wednesday'),
    WWTP('Schwyz', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy', 'Jura', 'Wednesday'),
    WWTP('Glarnerland', 'Glarus', 'Wednesday'),
]

# Define cantonal holidays
cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Solothurn': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel-Stadt': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
    # Add more cantonal holidays here...
}

# Get the start and end date of the next 52 weeks
current_date = datetime.datetime.now().date()
start_date = current_date - datetime.timedelta(days=current_date.weekday())
end_date = start_date + datetime.timedelta(weeks=52)

# Generate the list of dates for each week
weeks = []
while start_date <= end_date:
    week_dates = [start_date + datetime.timedelta(days=i) for i in range(7)]
    weeks.append(week_dates)
    start_date += datetime.timedelta(weeks=1)

# Generate the week-by-week table
table = [['Week'] + ['Purple Group'] + ['Orange Group'] + ['Green Group']]

for week_dates in weeks:
    week_row = [week_dates[0].strftime('%A, %B %d, %Y')]

    for wwtp in wwtps:
        if wwtp.shipment_day == 'Monday':
            group = 'Purple Group'
        elif wwtp.shipment_day == 'Tuesday':
            group = 'Orange Group'
        elif wwtp.shipment_day == 'Wednesday':
            group = 'Green Group'
        else:
            group = ''

        holidays_canton = cantonal_holidays.get(wwtp.canton, {})
        conflicting_holidays = []
        for date in week_dates:
            if date in holidays_canton:
                holiday_name = holidays_canton.get(date)
                conflicting_holidays.append(f'{wwtp.name} | {date.strftime("%a %d.%m")} ({holiday_name})')

        week_row.append('\n'.join(conflicting_holidays))

    table.append(week_row)

# Save the week-by-week table as a CSV file
with open('wwtp_holidays11.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

import csv
import datetime
import holidays

# Define the WWTP class and their shipment days
class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

wwtps = [
    WWTP('Zurich', 'Zurich', 'Monday'),
    WWTP('Chur', 'Graubunden', 'Monday'),
    WWTP('Neuchatel', 'Neuenburg', 'Monday'),
    WWTP('Lausanne', 'Vaud', 'Monday'),
    WWTP('Solothurn', 'Solothurn', 'Monday'),
    WWTP('Laupen', 'Bern', 'Tuesday'),
    WWTP('Lugano', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
    WWTP('Basel', 'Basel-Stadt', 'Tuesday'),
    WWTP('Buholz', 'Lucerne', 'Tuesday'),
    WWTP('Geneva', 'Geneva', 'Wednesday'),
    WWTP('Bern', 'Bern', 'Wednesday'),
    WWTP('Schwyz', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy', 'Jura', 'Wednesday'),
    WWTP('Glarnerland', 'Glarus', 'Wednesday'),
]

# Define cantonal holidays
cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Solothurn': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel-Stadt': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
    # Add more cantonal holidays here...
}

# Generate the week-by-week table
current_date = datetime.datetime.now()
end_date = current_date + datetime.timedelta(weeks=52)  # Generate for the next 52 weeks

table = [['Week'] + [wwtp.name + ' | ' + wwtp.shipment_day for wwtp in wwtps]]

week_start = current_date - datetime.timedelta(days=current_date.weekday())  # Get the start of the current week
week_table = []
while week_start < end_date:
    week_dates = [week_start + datetime.timedelta(days=i) for i in range(7)]
    week_row = [week_start.strftime('%Y-%m-%d')]
    
    for wwtp in wwtps:
        if wwtp.shipment_day == 'Monday':
            group = 'Purple Group'
        elif wwtp.shipment_day == 'Tuesday':
            group = 'Orange Group'
        elif wwtp.shipment_day == 'Wednesday':
            group = 'Green Group'
        else:
            group = ''

        holidays_in_week = [date.strftime('%a %d.%m') for date in week_dates if date in cantonal_holidays[wwtp.canton]]
        if holidays_in_week:
            week_row.append(f'{group} | {wwtp.name} | {wwtp.shipment_day} | ' + ' | '.join(holidays_in_week))
        else:
            week_row.append('')

    week_table.append(week_row)
    week_start += datetime.timedelta(weeks=1)

table.extend(week_table)

# Save the table to a CSV file
filename = 'wwtp_holidays_table.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

print(f'Table saved to {filename}.')

# %%
import csv
import datetime
import holidays

# Define the WWTP class and their shipment days
class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

wwtps = [
    WWTP('Zurich', 'Zurich', 'Monday'),
    WWTP('Chur', 'Graubunden', 'Monday'),
    WWTP('Neuchatel', 'Neuenburg', 'Monday'),
    WWTP('Lausanne', 'Vaud', 'Monday'),
    WWTP('Solothurn', 'Solothurn', 'Monday'),
    WWTP('Laupen', 'Bern', 'Tuesday'),
    WWTP('Lugano', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
    WWTP('Basel', 'Basel-Stadt', 'Tuesday'),
    WWTP('Buholz', 'Lucerne', 'Tuesday'),
    WWTP('Geneva', 'Geneva', 'Wednesday'),
    WWTP('Bern', 'Bern', 'Wednesday'),
    WWTP('Schwyz', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy', 'Jura', 'Wednesday'),
    WWTP('Glarnerland', 'Glarus', 'Wednesday'),
]

# Define cantonal holidays
cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Solothurn': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel-Stadt': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
    # Add more cantonal holidays here...
}

# Generate the week-by-week table
current_date = datetime.datetime.now()
end_date = current_date + datetime.timedelta(weeks=52)  # Generate for the next 52 weeks

table = [['Week', 'Purple Group', 'Orange Group', 'Green Group']]

week_start = current_date - datetime.timedelta(days=current_date.weekday())  # Get the start of the current week
week_table = []
while week_start < end_date:
    week_dates = [week_start + datetime.timedelta(days=i) for i in range(7)]
    week_row = [week_start.strftime('%Y-%m-%d'), '', '', '']
    
    for wwtp in wwtps:
        if wwtp.shipment_day == 'Monday':
            group = 'Purple Group'
        elif wwtp.shipment_day == 'Tuesday':
            group = 'Orange Group'
        elif wwtp.shipment_day == 'Wednesday':
            group = 'Green Group'
        else:
            continue

        holidays_in_week = [
            f'{wwtp.name} | {date.strftime("%a %d.%m")}' 
            for date in week_dates 
            if date in cantonal_holidays[wwtp.canton]
        ]
        if holidays_in_week:
            week_row[1 + ['Purple Group', 'Orange Group', 'Green Group'].index(group)] = ', '.join(holidays_in_week)

    week_table.append(week_row)
    week_start += datetime.timedelta(weeks=1)

table.extend(week_table)

# Save the table to a CSV file
filename = 'wwtp_holidays_table1.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

print(f'Table saved to {filename}.')

# %%
import csv
import datetime
import holidays

# Define the WWTP class and their shipment days
class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

wwtps = [
    WWTP('Zurich', 'Zurich', 'Monday'),
    WWTP('Chur', 'Graubunden', 'Monday'),
    WWTP('Neuchatel', 'Neuenburg', 'Monday'),
    WWTP('Lausanne', 'Vaud', 'Monday'),
    WWTP('Solothurn', 'Solothurn', 'Monday'),
    WWTP('Laupen', 'Bern', 'Tuesday'),
    WWTP('Lugano', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
    WWTP('Basel', 'Basel-Stadt', 'Tuesday'),
    WWTP('Buholz', 'Lucerne', 'Tuesday'),
    WWTP('Geneva', 'Geneva', 'Wednesday'),
    WWTP('Bern', 'Bern', 'Wednesday'),
    WWTP('Schwyz', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy', 'Jura', 'Wednesday'),
    WWTP('Glarnerland', 'Glarus', 'Wednesday'),
]

# Define cantonal holidays
cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Solothurn': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel-Stadt': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
    # Add more cantonal holidays here...
}

# Generate the week-by-week table
current_date = datetime.datetime.now()
end_date = current_date + datetime.timedelta(weeks=52)  # Generate for the next 52 weeks

table = [['Week', 'Purple Group', 'Orange Group', 'Green Group']]

week_start = current_date - datetime.timedelta(days=current_date.weekday())  # Get the start of the current week
week_table = []
while week_start < end_date:
    week_dates = [week_start + datetime.timedelta(days=i) for i in range(7)]
    week_row = [week_start.strftime('%Y-%m-%d'), '', '', '']
    
    for group in ['Purple Group', 'Orange Group', 'Green Group']:
        group_wwtps = [wwtp.name for wwtp in wwtps if wwtp.shipment_day.startswith(group[0].lower())]
        holidays_in_week = ', '.join([
            f'{wwtp.name} | {date.strftime("%a %d.%m")}'
            for wwtp in wwtps
            for date in week_dates
            if date in cantonal_holidays[wwtp.canton] and wwtp.name in group_wwtps
        ])
        if holidays_in_week:
            group_column_index = 1 + ['Purple Group', 'Orange Group', 'Green Group'].index(group)
            existing_value = week_row[group_column_index]
            if existing_value:
                holidays_in_week = existing_value + ', ' + holidays_in_week
            week_row[group_column_index] = holidays_in_week
    week_table.append(week_row)
    week_start += datetime.timedelta(weeks=1)

table.extend(week_table)

# Save the table to a CSV file
filename = 'wwtp_holidays_table.csv'
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

print(f'Table saved to {filename}.')

# %%
import csv
import datetime
import holidays

class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

wwtps = [
    WWTP('Zurich', 'Zurich', 'Monday'),
    WWTP('Chur', 'Graubunden', 'Monday'),
    WWTP('Neuchatel', 'Neuenburg', 'Monday'),
    WWTP('Lausanne', 'Vaud', 'Monday'),
    WWTP('Solothurn', 'Soleure', 'Monday'),
    WWTP('Laupen', 'Bern', 'Tuesday'),
    WWTP('Lugano', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
    WWTP('Basel', 'Basel', 'Tuesday'),
    WWTP('Buholz', 'Lucerne', 'Tuesday'),
    WWTP('Geneva', 'Geneva', 'Wednesday'),
    WWTP('Bern', 'Bern', 'Wednesday'),
    WWTP('Schwyz', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy', 'Jura', 'Wednesday'),
    WWTP('Glarnerland', 'Glarus', 'Wednesday'),
]

cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Soleure': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
}

purple_group_wwtps = [wwtp for wwtp in wwtps if wwtp.shipment_day == 'Monday']
orange_group_wwtps = [wwtp for wwtp in wwtps if wwtp.shipment_day == 'Tuesday']
green_group_wwtps = [wwtp for wwtp in wwtps if wwtp.shipment_day == 'Wednesday']

week_start = datetime.datetime.now().date()
week_end = week_start + datetime.timedelta(days=6)
table = [['Week'] + ['Purple Group'] + ['Orange Group'] + ['Green Group']]

while week_start.year <= 2024:
    week_row = [week_start.strftime('%Y-%m-%d')]
    
    for group_wwtps, group in [(purple_group_wwtps, 'Purple Group'), (orange_group_wwtps, 'Orange Group'), (green_group_wwtps, 'Green Group')]:
        week_dates = [week_start + datetime.timedelta(days=i) for i in range(7)]
        holidays_in_week = [
            f'{wwtp.name} | {date.strftime("%a %d.%m")}'
            for wwtp in group_wwtps
            for date in week_dates
            if date in cantonal_holidays[wwtp.canton] and date.weekday() == wwtp.shipment_day_index
        ]
        
        group_column_index = 1 + ['Purple Group', 'Orange Group', 'Green Group'].index(group)
        existing_value = week_row[group_column_index]
        if existing_value:
            holidays_in_week = existing_value + ', ' + ', '.join(holidays_in_week)
        week_row[group_column_index] = holidays_in_week
    
    table.append(week_row)
    week_start += datetime.timedelta(days=7)
    week_end += datetime.timedelta(days=7)

with open('wwtp_table.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

# %%
import csv
import datetime
import holidays

class WWTP:
    def __init__(self, name, canton, shipment_day):
        self.name = name
        self.canton = canton
        self.shipment_day = shipment_day

wwtps = [
    WWTP('Zurich', 'Zurich', 'Monday'),
    WWTP('Chur', 'Graubunden', 'Monday'),
    WWTP('Neuchatel', 'Neuenburg', 'Monday'),
    WWTP('Lausanne', 'Vaud', 'Monday'),
    WWTP('Solothurn', 'Soleure', 'Monday'),
    WWTP('Laupen', 'Bern', 'Tuesday'),
    WWTP('Lugano', 'Ticino', 'Tuesday'),
    WWTP('Altenrhein', 'Graubunden', 'Tuesday'),
    WWTP('Basel', 'Basel', 'Tuesday'),
    WWTP('Buholz', 'Lucerne', 'Tuesday'),
    WWTP('Geneva', 'Geneva', 'Wednesday'),
    WWTP('Bern', 'Bern', 'Wednesday'),
    WWTP('Schwyz', 'Schwyz', 'Wednesday'),
    WWTP('Porrentruy', 'Jura', 'Wednesday'),
    WWTP('Glarnerland', 'Glarus', 'Wednesday'),
]

cantonal_holidays = {
    'Zurich': holidays.CountryHoliday('CH', prov='ZH'),
    'Bern': holidays.CountryHoliday('CH', prov='BE'),
    'Graubunden': holidays.CountryHoliday('CH', prov='GR'),
    'Neuenburg': holidays.CountryHoliday('CH', prov='NE'),
    'Soleure': holidays.CountryHoliday('CH', prov='SO'),
    'Vaud': holidays.CountryHoliday('CH', prov='VD'),
    'Ticino': holidays.CountryHoliday('CH', prov='TI'),
    'Basel': holidays.CountryHoliday('CH', prov='BS'),
    'Lucerne': holidays.CountryHoliday('CH', prov='LU'),
    'Geneva': holidays.CountryHoliday('CH', prov='GE'),
    'Schwyz': holidays.CountryHoliday('CH', prov='SZ'),
    'Jura': holidays.CountryHoliday('CH', prov='JU'),
    'Glarus': holidays.CountryHoliday('CH', prov='GL')
}

purple_group_wwtps = [wwtp for wwtp in wwtps if wwtp.shipment_day == 'Monday']
orange_group_wwtps = [wwtp for wwtp in wwtps if wwtp.shipment_day == 'Tuesday']
green_group_wwtps = [wwtp for wwtp in wwtps if wwtp.shipment_day == 'Wednesday']

week_start = datetime.datetime.now().date()
week_end = week_start + datetime.timedelta(days=6)
table = [['Week', 'Purple Group', 'Orange Group', 'Green Group']]

while week_start.year <= 2024:
    week_row = [week_start.strftime('%Y-%m-%d'), '', '', '']
    
    for group_wwtps, group in [(purple_group_wwtps, 'Purple Group'), (orange_group_wwtps, 'Orange Group'), (green_group_wwtps, 'Green Group')]:
        week_dates = [week_start + datetime.timedelta(days=i) for i in range(7)]
        holidays_in_week = [
            f'{wwtp.name} | {date.strftime("%a %d.%m")}'
            for wwtp in group_wwtps
            for date in week_dates
            if date in cantonal_holidays.get(wwtp.canton, {}) and date.weekday() == wwtp.shipment_day
        ]
        
        group_column_index = table[0].index(group)
        existing_value = week_row[group_column_index]
        if existing_value:
            holidays_in_week = existing_value + ', ' + ', '.join(holidays_in_week)
        week_row[group_column_index] = holidays_in_week
    
    table.append(week_row)
    week_start += datetime.timedelta(days=7)
    week_end += datetime.timedelta(days=7)

with open('wwtp_table.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(table)

# %%
