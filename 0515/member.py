class Member:

    def __init__(self, num, name, phone):
        self.num = num
        self.name = name
        self.phone = phone
    def info(self):
        print('\t', self.num, '\t', self.name, '\t', self.phone)