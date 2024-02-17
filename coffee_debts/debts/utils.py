from django.db.models import Sum, F
from .models import UserDebtSummary

def pay_coffee_for_all():
    # Get all debts and order by total_debt in descending order
    debts = UserDebtSummary.objects.all().annotate(
        ordered_debt=F('total_debt')
    ).order_by('-ordered_debt')

    if not debts:
        print("No debts found.")
        return

    # The person with the highest debt
    highest_debtor = debts.first()

    # Calculate the total debt for all other users
    total_other_debts = debts.aggregate(Sum('total_debt'))['total_debt__sum'] - highest_debtor.total_debt

    # Check if the highest debtor's debt covers everyone else's
    if highest_debtor.total_debt >= total_other_debts:
        # Subtract the total of other's debts from the highest debtor's debt
        highest_debtor.total_debt -= total_other_debts
        highest_debtor.save()

        # Optionally reset other users' debts to 0 or adjust as per specific requirements
        for debtor in debts[1:]:
            debtor.total_debt = 0
            debtor.save()
        
        return f"{highest_debtor.user.username} has paid coffee for everyone, remaining debt: {highest_debtor.total_debt}"    
    else:
        return f"{highest_debtor.user.username} does not have enough to cover everyone's coffee."

