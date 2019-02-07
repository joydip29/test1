
class Student:
	stu_name = []

	def insert_name(self,student_name):
		self.stu_name.append(student_name)
		return len(self.stu_name)-1
	
	def fetch_name(self,student_roll):
		if student_roll >= len(self.stu_name):
			return 'No student is there with that name'
		else:
			return self.stu_name[student_roll


if __name__ == '__main__':
	student = Student()
	print('details of student john has been updated with roll no',student.insert_name('John'));
	print('Student name associated with roll no 0',student.fetch_name(0))

