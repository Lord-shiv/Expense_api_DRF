from django.shortcuts import render
from rest_framework.views import APIView
import datetime
from expense_app.models import Expense
from rest_framework import status, response

# Create your views here.
class ExpenseSummaryStats(APIView):

    def get_amount_for_category(self, expense_list, category):
        expenses = expense_list.filter(category=category)
        amount = 0

        for expense in expenses:
            amount += expense.amount

        return {'amount':str(amount)}

    # from django.db.models import Sum
    # def get_amount_for_category(self, expense_list, category):
    #     expenses = expense_list.filter(category=category)
    #     total_amount = expenses.aggregate(Sum("amount"))
    #     print(total_amount)

    def get_category(self, expense):
        """return category of expense"""
        return expense.category

    def get(self, request):
        todays_date = datetime.date.today()
        a_year_ago = todays_date - datetime.timedelta(days=30 * 12)
        expenses = Expense.objects.filter(
            owner=request.user, date__gte=a_year_ago, date__lte=todays_date)  #date__gte => greater or equal

        final = {}
        categories = list(set(map(self.get_category, expenses)))

        for expense in expenses:
            for category in categories:
                final[category] = self.get_amount_for_category(
                    expenses, category
                )

        return response.Response({'category_data': final}, status=status.HTTP_200_OK)
