file = input("file: ").lower().strip()
file_name, file_type = file.split(".")

match file_type:
    case "jpg" | "jpeg":
        print(f"image/jpeg")
    case "png" | "gif":
        print(f"image/{file_type}")
    case "txt":
        print("text/plain")
    case "pdf" | "zip":
        print(F"application/{file_type}")
    case _:
        print("application/octet-stream")
