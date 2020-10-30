HourlyRate = int(input("What is your hourly wage? "))

HoursWorked = int(input("How many hours have you worked this week? "))

if HoursWorked >= 40:
    AmountOver = (HoursWorked - 40) * (HourlyRate / 2)
    Total = (HoursWorked * HourlyRate) + AmountOver
    print(Total)

if HoursWorked <= 40:
    Total = (HoursWorked * HourlyRate)
    print(Total)
    



