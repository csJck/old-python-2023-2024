class student:

    def __init__(self,name):
        self.name = name

    def pc_on(self):
        print(f"{self.name} has turned their pc on.")
        return self

    def open_browser(self):
        print(f"{self.name} has opened their browser.")
        return self


    def load_content(self):
        print(f"{self.name} has opened learning resources.")
        return self


    def study(self):
        print(f"{self.name} is now studying.")
        return self



student = student("jack")

student.pc_on().open_browser().load_content().study()

