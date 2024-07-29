# Payroll Management System
This Payroll Management System is a Python-based project designed to manage employee information, attendance, salary, and other payroll-related activities efficiently. The system uses a MySQL database for data storage and retrieval.

  ![Screenshot 2024-07-29 182951](https://github.com/user-attachments/assets/be95a591-6181-4c44-88ba-3eba71f95ae7)


# Features
## __Employee Management__

- Register new employees with details like Employee ID, Name, Date of Birth, Date of Joining, Address, City, Department, Phone Number, and Aadhar Number.
- Search and display basic employee details using Employee ID.
- Update employee records.
- Remove employee records.
- Attendance Management

![Screenshot 2024-07-29 183010](https://github.com/user-attachments/assets/28079211-ed25-472a-81da-51ff3009f9ba)

![Screenshot 2024-07-29 183024](https://github.com/user-attachments/assets/0718b806-2296-48e8-a8ec-6ad57f0c6310)

![Screenshot 2024-07-29 183037](https://github.com/user-attachments/assets/6a888313-4c37-4b90-8815-a7eb0e6c8a1e)

![Screenshot 2024-07-29 183049](https://github.com/user-attachments/assets/536452fa-a225-42ab-b348-68ac781d54c3)

- Enter attendance information, including total working days, days present, and leave deductions.
- Generate attendance reports for employees.
  
![Screenshot 2024-07-29 183101](https://github.com/user-attachments/assets/d2f4ba04-3a6f-4293-8590-c36afe2182aa)

![Screenshot 2024-07-29 183112](https://github.com/user-attachments/assets/98aaeb4c-ee5a-4d7d-957d-94067434b35d)

## Salary Management

- Enter and manage salary details, including basic salary, DA, TA, HRA, MA, bonuses, and deductions (leave, PF, PT).
- Generate salary reports and display net salary.
- Update salary details.
- Generate employee pay slips.

![Screenshot 2024-07-29 183125](https://github.com/user-attachments/assets/81800bbf-c1d8-4865-88f2-01338fdb6b29)

![Screenshot 2024-07-29 183135](https://github.com/user-attachments/assets/737893fc-3f4d-4370-8bda-0d654d5ef5e3)

![Screenshot 2024-07-29 183146](https://github.com/user-attachments/assets/fef1ae94-45fd-4b71-8888-d4486c0c559d)



## Prerequisites
- Python 3.x
- MySQL
- MySQL Connector for Python (`mysql-connector-python`)

## Installation

### Clone the repository:

```bash
git clone https://github.com/gungunjain36/PayRoll-Management-System.git
cd payroll-management-system
```
### Install the required Python packages:

```bash
pip install mysql-connector-python
```
### Set up the MySQL database:

- Create a database named PAYROLLMS.
- Create the necessary tables (employee, department, leave_record, salary) in the database. You can use the provided SQL scripts in the sql_scripts directory.
## Usage

### Run the Python script:
```bash
python main.py
```

### Follow the on-screen instructions to navigate through the various functionalities:

1. Register a New Employee
2. Search for Employee Basic Details
3. Remove an Employee
4. Update Employee Basic Info
5. Enter Attendance Info of an Employee
6. Search for Attendance-Leave Details of an Employee
7. Enter Salary Details of an Employee
8. Show Salary and Deductions Info of an Employee
9. Update Salary of an Employee
10. Display Payment Slip of an Employee

## Database Schema

### Employee Table
- emp_id (Primary Key)
- name
- dob (Date of Birth)
- doj (Date of Joining)
- address
- city
- phone
- aadhar
  
### Department Table
- emp_id (Foreign Key)
- department
- department_id
- Leave Record Table
- emp_id (Foreign Key)
- working_days
- days_present
- days_absent
- leave_deductions
  
### Salary Table
- emp_id (Foreign Key)
- department_id
- basic
- da (Dearness Allowance)
- ta (Travel Allowance)
- hra (House Rent Allowance)
- ma (Medical Allowance)
- bonus
- leave_deductions
- pf (Provident Fund)
- pt (Professional Tax)
- gross_salary
- net_salary
  
## Contributing
Feel free to contribute to this project by submitting issues or pull requests. Any contributions, big or small, are appreciated!

## Contact
For any questions or suggestions, please contact gungunjainxia@gmail.com
