months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

def main():
    while True:
        anno_domini = input("Date: ")

        try:
            if " " in anno_domini:
                anno_domini = anno_domini.replace(",","")
                day, month, year = anno_domini.split(" ")
                month = int(months.index(month.capitalize()))
                month += 1
                day = int(day)
                year = int(year)
                if month > 12 or day > 31 or len(year) > 4:
                    continue
                else:
                    print(f"{year}-{month:02d}-{day:02d}")
                    break


            elif "/" in anno_domini:
                day, month, year = anno_domini.split("/")
                day = int(day)
                month = int(month)
                year = int(year)
                if month > 12 or day > 31 or len(year) > 4:
                    continue

                else:
                    print(f"{year}-{month:02d}-{day:02d}")
                    break
                
        except ValueError:
            continue
            









   
main()