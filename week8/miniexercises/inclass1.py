# broken_payroll.py

def calculate_pay(hours_worked, hourly_rate):
    total_pay = 0
    
    if hours_worked > 40:
        overtime_hours = hours_worked - 40
        total_pay = 40 * hourly_rate + (overtime_hours * hourly_rate) * 1.5
    else:
        total_pay = hours_worked * hourly_rate

    return total_pay

if __name__ == "__main__":
    # TEST CASES (once you fix the script)
    print(calculate_pay(35, 10))   # Expect 350.0 (no overtime)
    print(calculate_pay(40, 10))   # Expect 400.0 (exactly 40 hours)
    print(calculate_pay(45, 10))   # Expect 475.0 (5 hours of overtime)
