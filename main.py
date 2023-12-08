# Семестровий Залік1 Гліб Кобрин ІКСМ-1

while True:
    try:
        user_input = float(
            input("Введіть значення, більше якого ви хочете побачити результати: ")
        )
        with open("measure.txt", "r") as file:
            for line in file:
                time, measurement = line.split()
                if float(measurement) > user_input:
                    print(time, measurement)
        break
    except:
        print("Введений запит не є числовим значенням")

with open("measure.txt", "r") as file:
    for line in file:
        time, measurement = line.split()
        if float(measurement) > user_input:
            print(time, measurement)
