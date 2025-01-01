class laptop:
    def __init__(self):
        self.ram=" "
        self.processor=" "
    def display(self):
        print("Ram: ",self.ram)
        print("Processor: ",self.processor)

hp = laptop()
hp.ram="8gb"
hp.processor="i5"

dell = laptop()
dell.ram="16gb"
dell.processor="i8"

hp.display()
dell.display()