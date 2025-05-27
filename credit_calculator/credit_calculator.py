import math
import argparse


def calculate_diff_payments(principal, periods, interest):
    payments = []
    i = interest / (12 * 100)
    total_payment = 0
    for m in range(1, periods + 1):
        Dm = principal / periods + i * (principal - (principal * (m - 1)) / periods)
        Dm_rounded = math.ceil(Dm)
        payments.append(Dm_rounded)
        print(f"Month {m}: payment is {Dm_rounded}")
        total_payment += Dm_rounded
    overpayment = total_payment - principal
    print(f"Overpayment = {overpayment}")

def calculate_annuity_payment(principal, periods, interest):
    i = interest / (12 * 100)
    A = principal * (i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1)
    A_rounded = math.ceil(A)
    overpayment = A_rounded * periods - principal
    print(f"Your annuity payment = {A_rounded}!")
    print(f"Overpayment = {overpayment}")

def calculate_principal(payment, periods, interest):
    i = interest / (12 * 100)
    P = payment / ((i * math.pow(1 + i, periods)) / (math.pow(1 + i, periods) - 1))
    P_rounded = math.floor(P)
    overpayment = payment * periods - P_rounded
    print(f"Your loan principal = {P_rounded}!")
    print(f"Overpayment = {overpayment}")

def calculate_periods(principal, payment, interest):
    i = interest / (12 * 100)
    n = math.log(payment / (payment - i * principal), 1 + i)
    n_ceil = math.ceil(n)

    years = n_ceil // 12
    months = n_ceil % 12

    time_str = ""
    if years > 0:
        time_str += f"{years} year" + ("s" if years > 1 else "")
    if months > 0:
        if years > 0:
            time_str += " and "
        time_str += f"{months} month" + ("s" if months > 1 else "")

    print(f"It will take {time_str} to repay this loan!")
    overpayment = payment * n_ceil - principal
    print(f"Overpayment = {overpayment}")

def main():
    parser = argparse.ArgumentParser(description="Credit Calculator")
    parser.add_argument("--type", choices=["annuity", "diff"], help="Type of payment")
    parser.add_argument("--payment", type=float, help="Monthly payment amount")
    parser.add_argument("--principal", type=float, help="Loan principal")
    parser.add_argument("--periods", type=int, help="Number of months")
    parser.add_argument("--interest", type=float, help="Interest rate without % sign")

    args = parser.parse_args()


    if args.type not in ("annuity", "diff"):
        print("Incorrect parameters")
        return

    not_none_params = sum(x is not None for x in [args.payment, args.principal, args.periods, args.interest])


    if args.interest is None:
        print("Incorrect parameters")
        return


    for param in [args.payment, args.principal, args.periods, args.interest]:
        if param is not None and param < 0:
            print("Incorrect parameters")
            return
        if param == 0:
            print("Incorrect parameters")
            return

    if args.type == "diff":

        if args.payment is not None:
            print("Incorrect parameters")
            return

        if args.principal is None or args.periods is None:
            print("Incorrect parameters")
            return
        calculate_diff_payments(args.principal, args.periods, args.interest)
    else:

        if not_none_params < 3:
            print("Incorrect parameters")
            return

        if args.payment is None:

            if args.principal is not None and args.periods is not None:
                calculate_annuity_payment(args.principal, args.periods, args.interest)
            else:
                print("Incorrect parameters")
        elif args.principal is None:

            if args.payment is not None and args.periods is not None:
                calculate_principal(args.payment, args.periods, args.interest)
            else:
                print("Incorrect parameters")
        elif args.periods is None:

            if args.principal is not None and args.payment is not None:
                calculate_periods(args.principal, args.payment, args.interest)
            else:
                print("Incorrect parameters")
        else:
            print("Incorrect parameters")

if __name__ == "__main__":
    main()
