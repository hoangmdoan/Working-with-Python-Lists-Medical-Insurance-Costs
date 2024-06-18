class Employee:
    def __init__(self, name, department):
        self._name = name
        self._department = department

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_department(self):
        return self._department

    def set_department(self, department):
        self._department = department

    def pay(self):
        return 0.0  # Base class, no specific pay calculation

    def __str__(self):
        return f"Employee Name: {self._name}, Department: {self._department}"

class CommissionPaid(Employee):
    def __init__(self, name, department, base_rate, sales):
        super().__init__(name, department)
        self._base_rate = base_rate
        self._sales = sales

    def get_base_rate(self):
        return self._base_rate

    def set_base_rate(self, base_rate):
        self._base_rate = base_rate

    def get_sales(self):
        return self._sales

    def set_sales(self, sales):
        self._sales = sales

    def pay(self):
        if self._sales > 10000:
            commission_rate = 0.02
        elif self._sales >= 5000:
            commission_rate = 0.01
        else:
            commission_rate = 0.0
        return self._base_rate + self._sales * commission_rate

    def __str__(self):
        return (
            f"Employee Type: Commission Paid, "
            f"{super().__str__()}, "
            f"Weekly Pay: ${self.pay():.2f}"
        )

class HourlyPaid(Employee):
    def __init__(self, name, department, hourly_rate, hours):
        super().__init__(name, department)
        self._hourly_rate = hourly_rate
        self._hours = hours

    def get_hourly_rate(self):
        return self._hourly_rate

    def set_hourly_rate(self, hourly_rate):
        self._hourly_rate = hourly_rate

    def get_hours(self):
        return self._hours

    def set_hours(self, hours):
        self._hours = hours

    def pay(self):
        if self._hours > 40:
            overtime_hours = self._hours - 40
            overtime_pay = overtime_hours * self._hourly_rate * 1.5
            regular_pay = 40 * self._hourly_rate
            return regular_pay + overtime_pay
        else:
            return self._hours * self._hourly_rate

    def __str__(self):
        return (
            f"Employee Type: Hourly Paid, "
            f"{super().__str__()}, "
            f"Weekly Pay: ${self.pay():.2f}"
        )

def total_pay(employee_list):
    return sum(emp.pay() for emp in employee_list)

def print_employee_list(employee_list):
    for emp in employee_list:
        print(emp)
    print(f"Total Weekly Pay: ${total_pay(employee_list):.2f}")

# Example usage (replace with your actual data)
if __name__ == "__main__":
    employees = [
        CommissionPaid("Fname1 Lname1", "Marketing", 500, 30000),
        CommissionPaid("Fname2 Lname2", "Sales", 1000, 8000),
        HourlyPaid("Fname3 Lname3", "Accounting", 20.5, 55.0),
        HourlyPaid("Fname4 Lname4", "Finance", 30, 35.0),
    ]

    print_employee_list(employees)
