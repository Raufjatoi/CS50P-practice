def main ():
    bill = input('Enter bill : ')
    per = input('Enter percentage : ')
    tip = ( bill_def (bill)* per_def(per) /100 )
    print(f'Tip amount is {tip:.2f}')

def bill_def(bill):
    return float(bill.replace('$',''))
def per_def(per):
    return float(per.replace('%',''))
main()
