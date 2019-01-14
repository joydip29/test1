

import unittest

# This is the class we want to test. So, we need to import it
import Student as StudentClass


class Test(unittest.TestCase):
	student = StudentClass.Student()
	student_roll = []
	student_name = []
	def test_0_insert_name(self):
		print("Start insert_name test\n")
		for i in range(4):
			name = 'name' + str(i)
			self.student_name.append(name)
			student_roll = self.student.insert_name(name)
			self.assertIsNotNone(student_roll)
			self.student_roll.append(student_roll)
		print("student_roll length = ", len(self.student_roll))
		print(self.student_roll)
		print("student_name length = ", len(self.student_name))
		print(self.student_name)
		print("\nFinish insert_name test\n")

	def test_1_get_name(self):
		print("\nStart fetch_name test\n")
		length = len(self.student_roll) 
		print("student_roll length = ", length)
		print("student_name length = ", len(self.student_name))
		for i in range(6):
			if i < length:
				self.assertEqual(self.student_name[i], self.student.fetch_name(self.student_roll[i]))
			else:
				print("Testing for fetch_name no student test")
				self.assertEqual('No student is there with that name', self.student.fetch_name(i))
		print("\nFinish get_name test\n")


if __name__ == '__main__':
	unittest.main()