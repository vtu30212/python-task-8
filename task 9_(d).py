try:
    initial_investment = float(input("Enter the initial investment amount: "))
    final_investment = float(input("Enter the final investment amount: "))
    roi = (final_investment - initial_investment) / initial_investment * 100
    print("Return on Investment (ROI): {:.2f}".format(roi))
except ValueError:
    print("Error: Please enter a valid numeric value for the investment amount.")
except ZeroDivisionError:
    print("Error: Initial investment amount cannot be zero.")
