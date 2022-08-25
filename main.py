print("\n\n")
print("\t\t\t\t\tWelcome")
print("\t\t\t\tTip Calculator")
print("\n\n")

total_bill=float(input("What's the total bill? $ "));

print("\n")

tip=float(input("Enter your tip percentage:-\n"))

print("\n")

no_of_people=float(input("How many people to split the bill within?\n"))

print("\n")
tip_percentage=tip/100;

total_tip=tip_percentage*total_bill;

bill_payable_with_tip=total_bill+total_tip;

divison=bill_payable_with_tip/no_of_people;
bill_per_share=round(divison,2);

print(f"The total Tip generated is: $ {total_tip}\n")
print(f"Bill payable with Tip is $ {bill_payable_with_tip}\n")
print(f"Each person should pay $ {bill_per_share}");