from employees import CommissionPaid, HourlyPaid, total_pay, print_employee_list

# Test Data (from the assignment instructions)
employees = [
    CommissionPaid("Fname1 Lname1", "Marketing", 500, 30000),
    CommissionPaid("Fname2 Lname2", "Sales", 1000, 8000),
    HourlyPaid("Fname3 Lname3", "Accounting", 20.5, 55.0),
    HourlyPaid("Fname4 Lname4", "Finance", 30, 35.0),
]

# Additional Test Cases
employees.extend([
    CommissionPaid("Alice Johnson", "Sales", 800, 12500),  # Commission over 10k
    CommissionPaid("Bob Smith", "Marketing", 650, 4800),   # Commission under 5k
    HourlyPaid("Eva Brown", "HR", 25, 40),                # No overtime
    HourlyPaid("David Lee", "IT", 32.5, 48),              # With overtime
])

# Output Results
print_employee_list(employees)
