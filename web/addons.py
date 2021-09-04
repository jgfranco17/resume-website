import datetime

class TimeFunction:
    def __init__(self, timezone:int):
        self.timezone = timezone

    def timestamps(self, precision):
        now = datetime.datetime.utcnow() + datetime.timedelta(seconds=self.timezone * 3600)
        times = {
            'second': now.strftime("%d %b %Y, %I:%M:%S %p"),
            'minute': now.strftime("%d %b %Y, %I:%M %p"),
            'day': now.strftime("%d %b %Y")
        }
        try:
            return times[precision.lower()]
        except Exception:
            return now.strftime("%d %b %Y, %I:%M:%S %p")

    @staticmethod
    def time_interval(start_period):
        def convert_timedelta(duration):
            try:
                seconds = duration.seconds
                years = (duration.days // 7) // 52
                week_count = ((duration.days // 7) % 52) if years > 0 else (duration.days // 7)
                months = int(week_count // 4.3)
                weeks = int(months % 4.345)
                days = duration.days % 7
                hours = seconds // 3600
                minutes = (seconds % 3600) // 60
                seconds = (seconds % 60)

                return years, months, weeks, days, hours, minutes, seconds

            except ValueError as ve:
                print(f"Value error: {ve}")
            except Exception as e:
                print(f"Error: {e}")

        try:
            years, months, weeks, days, hours, minutes, seconds = convert_timedelta(datetime.datetime.utcnow() - start_period)
            age = []
            if years:
                age.append(f"{years} years" if years > 1 else f"{years} year")
            if months:
                age.append(f"{months} months")
            if weeks:
                age.append(f"{weeks} weeks")
            if days:
                age.append(f"{days} days")
            if hours:
                age.append(f"{hours} hours")
            if minutes:
                age.append(f"{minutes} minutes")
            if seconds:
                age.append(f"{seconds} seconds")

            return str(', '.join(age))

        except Exception as e:
            print(f'Time interval computation error: {e}')