from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def ecommerce_index_view(request):
    '''This function render index page of ecommerce views'''
    
    return HttpResponse('Welcome to 6410742230 Chaibancha Raengklang views!')

def home_view(request, item_id):

    context_data = {
        "item_id": item_id   
        }
       
    return render(request, 'HomePage.html',context= context_data)

def category_view(request, item_id):

    context_data = {
        "category_id": item_id   
        }
       
    return render(request, 'CategoryPage.html',context= context_data)

def product_view(request, item_id):

    context_data = {
        "product_id1": item_id,
        "product_name1": "Chaibancha Raengklang",
        "product_description1": "translation to 'Chaibancha Raengklang'",
        "product_price1": "9,999.99",

        "product_id2": "XXX",
        "product_name2": "XXXX XXXX",
        "product_description2": "translation to 'X'",
        "product_price2": "X,XXX",
        }
       
    return render(request, 'ProductPage.html',context= context_data)

def checkout_view(request, item_id):

    context_data = {
        "checkout_id": item_id   
        }
       
    return render(request, 'CheckoutPage.html',context= context_data)

def contact_view(request, item_id):

    context_data = {
        "contact_id": item_id   
        }
       
    return render(request, 'ContactPage.html',context= context_data)