seconds = int(input("Enter the number of seconds (>= 0 and < 8640000): "))
seconds_in_minute = 60
seconds_in_hour = 60 * 60
seconds_in_day = 24 * 60 * 60
days = seconds // seconds_in_day
remaining_seconds = seconds % seconds_in_day
hours = remaining_seconds // seconds_in_hour
remaining_seconds %= seconds_in_hour
minutes = remaining_seconds // seconds_in_minute
remaining_seconds %= seconds_in_minute
sec = remaining_seconds
day_word = "день" if days % 10 == 1 and days % 100 != 11 else "дні" if 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14) else "днів"
time_format = f"{str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(sec).zfill(2)}"
result = f"{days} {day_word}, {time_format}"
print(result)
