class CollegeDirectory:
    def __init__(self, dirName):
        self.dirName = dirName
        self.students = []

    def addStudent(self, studentName, emailAddress):
        self.students[studentName] = emailAddress

    def getEmailList(self):
        emails = []
        for key in self.students:
            entry = key + " <" + self.students[key] + ">"
            emails.append(entry)
        return emails
        
        
