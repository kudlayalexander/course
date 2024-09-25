class Subject:
    def __init__(self, subject_id, subject_name):
        self.subject_id = subject_id
        self.subject_name = subject_name

    def __str__(self):
        return f"Subject(subject_id={self.subject_id}, subject_name='{self.subject_name}')"