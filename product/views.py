from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import Product ,voted_product

from django.utils import timezone

import json


# Create your views here.
def ajax(request):
    product = Product.objects

    return render(request, 'ajax.html', {'product': product})


def home(request):
    product = Product.objects
    return render(request, 'products/home.html', {'product': product})


@login_required(login_url='/accounts/signup')
def addp(request):
    if request.method == 'POST':
        if request.POST['title'] and request.POST['body'] and request.POST['url'] and request.FILES['icon'] and \
                request.FILES['image']:
            product = Product()
            product.title = request.POST['title']
            product.body = request.POST['body']

            if request.POST['url'].startswith('http://') or request.POST['url'].startswith('https://'):
                product.url = request.POST['url']
            else:
                product.url = 'http://' + request.POST['url']
            product.image = request.FILES['image']
            product.icon = request.FILES['icon']
            product.pub_date = timezone.datetime.now()
            product.hunter = request.user
            product.save()
            return redirect('/products/' + str(product.id))

        else:
            return render(request, 'products/home.html', {'error': 'all fields are required !'})
    return render(request, 'products/add_product.html')


def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'products/detail.html', {'product': product})


@login_required(login_url='/accounts/signup')
def upvote(request):
    if request.method == 'POST':
        # id = request.POST.get('product_id')
        ans_id = json.loads((request.body.decode('utf-8')))
        id = ans_id["product_id"]

        user = request.user.id
        print('userid is =')


        product = get_object_or_404(Product, pk=id)
        object = voted_product.objects



        if   object.filter(user_id=user).exists():
         voted_object = object.get(user_id=user)
         delete(request,product, voted_object)
         return JsonResponse({'likes': product.votes_total, 'string': 'like'})
        else:
          create(request,user, product,id)
          return JsonResponse({'likes': product.votes_total, 'string': 'dislike'})



def homeupvote(request, product_id):
    product = Product.objects
    return render(request, 'home', {'product:product'})



def delete(request,product,voted_object):
    if product:
                if voted_object:
                 product.votes_total -= 1
                 if product.votes_total < 0:
                     product.votes_total+=1
                 voted_object.delete()
                 product.save()
                 return JsonResponse({'likes': product.votes_total, 'string': 'like'})



def create(request,user,product,id):
    voted = voted_product()
    product.votes_total += 1
    product.string = "liked"
    product.save()
    voted.vote_number = product.hunter
    voted.user_id = user
    voted.product_id = id
    voted.string = "liked"
    voted.save()
    return JsonResponse({'likes': product.votes_total, 'string':'liked'})