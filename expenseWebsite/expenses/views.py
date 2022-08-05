from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'E:/Sanchay/Coding/1 Repositories/Geek_O_Engineers-Money/expenseWebsite/expenseWebsite/templates/expenses/index.html')

def add_expense(request):
    return render(request, 'expenseWebsite/expenseWebsite/templates/expenses/add_expense.html')