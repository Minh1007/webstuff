from django.db.models import Q
from django.shortcuts import render, HttpResponse
from django.conf import settings
from .models import *
# Create your views here.

def get_contents():
    categories = get_top_menu()

    n_categories = []
    for item in categories:
        contents_by_category_id = list(Content.objects.filter(category=item['id']).values())
        item['contents'] = contents_by_category_id
        item['has_contents'] = True if len(contents_by_category_id) > 0 else False
        n_categories.append(item)
    return n_categories

def get_subcategory_contents(cg_id, sub_cg_id):
    contents = list(Content.objects.filter(category=cg_id, subcategory=sub_cg_id).values())
    has_contents = True if len(contents) > 0 else False
    category = Category.objects.get(id=cg_id)
    sub_category = SubCategory.objects.get(id=sub_cg_id)
    n_contents = {
        'category': category,
        'sub_category': sub_category,
        'contents': contents,
        'has_contents': has_contents
    }

    return n_contents

def get_top_menu():
    categories = list(Category.objects.all().values())
    for item in categories:
        sub_categories_by_category_id = list(SubCategory.objects.filter(category=item['id']).values())
        item['sub_categories'] = sub_categories_by_category_id
    return categories

def subcategory(request, cg_id, sub_cg_id):
    data = {
        "categories": get_top_menu(),
        "data": get_subcategory_contents(cg_id, sub_cg_id),
        "site_url": settings.SITE_URL
    }
    return render(request, 'home_category.html', data)

def home(request):
    data = {
        "categories": get_top_menu(),
        "contents": get_contents(),
        "site_url": settings.SITE_URL
    }
    return render(request, 'home_page.html', data)

def contact_us(request):
    data = {
        "categories": get_top_menu(),
        "site_url": settings.SITE_URL
    }
    return render(request, 'contact.html', data)

def contact(request):
    param = request.POST

    # todo
    # add code here to receive email
    return HttpResponse('success')

def search(request):
    param = request.GET
    keyword = param['keyword']

    contents = list(Content.objects.filter(Q(subcategory__name__icontains=keyword) | Q(category__name__icontains=keyword)).values())
    n_contents = []
    for ct in contents:
        ct['category'] = Category.objects.get(id=ct['category_id'])
        ct['sub_category'] = SubCategory.objects.get(id=ct['subcategory_id'])
        n_contents.append(ct)
    data = {
        "categories": get_top_menu(),
        'contents': n_contents,
        'keyword': keyword
    }
    return render(request, 'searchresults.html', data)

def contentview(request, content_id):
    content_by_id = list(Content.objects.filter(id=content_id).values())[0]
    category = Category.objects.get(id=content_by_id['category_id'])
    sub_category = SubCategory.objects.get(id=content_by_id['subcategory_id'])
    data = {
        "categories": get_top_menu(),
        "content": content_by_id,
        "site_url": settings.SITE_URL,
        "category": category,
        "sub_category": sub_category,
    }

    return render(request, 'content.html', data)