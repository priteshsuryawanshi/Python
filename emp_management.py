#Employee management system

employee_id = 0		#global variable to auto-generate employee ID

def insert_employee(employee_list):
	print ("in insert_employee")
	
	emp_name = (input("Enter employee name:"))
	emp_dob = (input("Enter DOB in dd/mm/yy format:"))
	emp_city = (input("Enter Address of the employee:"))
	emp_salary = (input("Enter employee's salary:"))
	
	emp_dict = create_emp_dict(emp_name, emp_dob, emp_city, emp_salary)
	
	global employee_id	#by mentioning "global" keyword we tell the function to use the global variable
	employee_id += 1
	employee_list[employee_id] = emp_dict
	
	print ("\nEmployee inserted successfully")
	
def create_emp_dict(name, dob, city, salary):
	print ("in create_emp_dict")
	
	emp = {}
	emp["name"] = name
	emp["dob"] = dob
	emp["city"] = city
	emp["salary"] = salary
	
	return emp

def search(choice, employee_list):
	search_employee_id = eval(input("Enter employee ID to be searched:"))
	display(choice, employee_list, search_employee_id)

def delete(employee_list):
	delete_employee_id = eval(input("Enter employee ID to be deleted:"))
	
	
def display(choice, employee_list, *args):
	if choice == 3:
		print ("\nEmployee details are as below:\n")
		for key, value in employee_list.items():
			print ("employee ID : {}".format(key))
			for inner_key, inner_value in value.items():
				print("{} : {}".format(inner_key, inner_value))
			print ()	#to insert new line
	else:
		employee_id = args[0]
		print ("employee ID : {}".format(employee_id))
		for key, value in employee_list.get(employee_id).items():
			print("{} : {}".format(key, value))
		print ()	#to insert new line
		
def main():
	employee_list = {}
		
	while True:
		choice = eval(input("""1. Insert an employee\n2. Edit employee details\n3. Display all\n4. Search an Employee\n5. Delete an Employee\n6. Exit\nPlease enter your choice:"""))
						
		if choice == 1:
			insert_employee(employee_list)
			print ("Inserted Employee details are:")
			display(choice, employee_list, employee_id)
		elif choice == 2:
			edit()
			print ("Edited Employee details:")
			display(choice, employee_list, employee_id)
		elif choice == 3:
			display(choice, employee_list)
		elif choice == 4:
			search(choice, employee_list)
		elif choice == 5:
			delete()
		elif choice == 6:
			break
		else:
			break
			
	



if __name__ == "__main__":
	main()