from .views import ExpenseSummaryStats, IncomeSourcesSummaryStats
from django.urls import path


urlpatterns = [
    path('expense-category-data', ExpenseSummaryStats.as_view(), name="expense_category_summary"),
    path('income-sources-data', IncomeSourcesSummaryStats.as_view(), name="income_sources_summary"),
]
