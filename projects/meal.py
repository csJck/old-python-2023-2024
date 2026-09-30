def main():
    x = convert(input("What time is it: "))
    m = ""
    try:
        t, m = x.split(" ")
    except ValueError:
        t = x
    t = float(t)
    if m.lower() in ["p.m.", "pm", "p.m"] and t < 12:
        t += 12

    if 7 <= t <= 8:
        print("breakfast time")
    elif 12 <= t <= 13:
        print("lunch time")
    elif 18 <= t <= 19:
        print("dinner time")
    else:
        return


def convert(time):
    meridiem = ""
    try:
        hours, minutes, meridiem = time.replace(" ", ":").split(":")
    except ValueError:
        hours, minutes = time.split(":")

    hours, minutes = int(hours), float(minutes)
    minutes = minutes / 60
    time = hours + minutes
    time = str(time)
    time = time + " " + meridiem
    return time


if __name__ == "__main__":
    main()
