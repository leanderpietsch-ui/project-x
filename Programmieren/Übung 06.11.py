class Exam:
    def __init__(self, examiner, subject, course_number):
        self.examiner = examiner
        self.subject = subject
        self.course_number = course_number
        self.participants = []
        self.results = []
    
    def get_number_of_participants(self):
        return len(self.participants)
    
    def add_participant(self, participant):
        self.participants.append(participant)
    
    def set_results(self, result):
        self.results.append(result)



class WrittenExam(Exam):
    TYPE = "Klausur"
    def __init__(self,examiner, subject, course_number, date, time , duration):
        super().__init__(examiner, subject, course_number)
        self.date = date
        self.time = time
        self.duration = duration
    

Exam1 = Exam ("Dr. Smith", "Mathematics", "MATH101")
Exam1.add_participant("Alice")
Exam1.add_participant("Bob")
print(Exam1.get_number_of_participants())  # Output: 2
print(Exam1.__dict__)

WrittenExam1 = WrittenExam("Dr. Jones", "Physics", "PHYS201", "2024-12-15", "10:00", "2 hours")
WrittenExam1.add_participant("Charlie")
print(WrittenExam1.get_number_of_participants())  # Output: 1
print(WrittenExam1.TYPE)  # Output: Klausur
print(WrittenExam1.__dict__) 

Exam1.set_results({"Alice": 85, "Bob": 90})
print(Exam1.results)  # Output: [{'Alice': 85, 'Bob': 90}]




    
    
