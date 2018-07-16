#Employee management system

employee_id = 0		#global variable to auto-generate employee ID

def get_employee_details(employee_list, *args):
	#print ("in get_employee_details")
	
	emp_name = (input("Enter employee name:"))
	emp_dob = (input("Enter DOB in dd/mm/yy format:"))
	emp_city = (input("Enter Address of the employee:"))
	emp_salary = (input("Enter employee's salary:"))
	
	emp_dict = create_emp_dict(emp_name, emp_dob, emp_city, emp_salary)
	
	if args:
		insert_employee(emp_dict, employee_list, args[0])
	else:
		insert_employee(emp_dict, employee_list)
	
def insert_employee(emp_dict, employee_list, *args):
	if args:
		employee_list[args[0]] = emp_dict
		print ("\nEmployee details modified successfully")
	else:
		global employee_id	#by mentioning "global" keyword we tell the function to use the global variable
		employee_id += 1
		employee_list[employee_id] = emp_dict
		print ("\nEmployee inserted successfully")
	
def create_emp_dict(name, dob, city, salary):
	#print ("in create_emp_dict")
	
	emp = {}
	emp["name"] = name
	emp["dob"] = dob
	emp["city"] = city
	emp["salary"] = salary
	
	return emp

def edit(choice, employee_list):
	edit_employee_id = eval(input("Enter employee ID of employee to be modified:"))
	#search for id, if not found throw error
	if edit_employee_id in employee_list:
		#display existing details here
		display(choice, employee_list, edit_employee_id)
		get_employee_details(employee_list, edit_employee_id)
		display(choice, employee_list, edit_employee_id)
	else:
		print ("\nNo match found\n")

def search(choice, employee_list):
	search_employee_id = eval(input("Enter employee ID to be searched:"))
	if search_employee_id in employee_list:
		display(choice, employee_list, search_employee_id)
	else:
		print ("\nNo match found\n")

def delete(choice, employee_list):
	delete_employee_id = eval(input("Enter employee ID to be deleted:"))
	if delete_employee_id in employee_list:
		del employee_list[delete_employee_id]
		print ("Employee information deleted\n")
	else:
		print ("\nNo match found\n")
	
	
def display(choice, employee_list, *args):
	if len(employee_list) == 0:
		print ("\nNo employee records\n")	
	elif choice == 3:
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
			get_employee_details(employee_list)
			print ("\nInserted Employee details are:\n")
			display(choice, employee_list, employee_id)
		elif choice == 2:
			edit(choice, employee_list)
			print ("\nModified Employee details are:\n")
		elif choice == 3:
			display(choice, employee_list)
		elif choice == 4:
			search(choice, employee_list)
		elif choice == 5:
			delete(choice, employee_list)
		elif choice == 6:
			break
		else:
			break
			
	



if __name__ == "__main__":
	main()