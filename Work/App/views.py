from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Item_Page1, Item_Page2, Item_Page3
from .forms import FormAdd

def page_1(request):
    processors = Item_Page1.objects.all()
    return render(request, 'Page_1.html', {'processors': processors})

def page_2(request):
    video_cards = Item_Page2.objects.all()
    return render(request, 'Page_2.html', {'video_cards': video_cards})

def page_3(request):
    RAM = Item_Page3.objects.all()
    return render(request, 'Page_3.html', {'RAM': RAM})

def pageform(request):
    if request.method == "POST":

        caption = request.POST.get("caption", "Undefined")
        price = request.POST.get("price", "Undefined")
        path_img = request.POST.get("path_img", "Undefined")
        input_select = request.POST.get("select", "Undefined")

        if input_select == '1':
            processors.append({"price": price, "caption": caption, "img": path_img})
            Item_Page1.objects.create(caption=caption, price=price, path_img=path_img)

        elif input_select == '2':
            video_cards.append({"price": price, "caption": caption, "img": path_img})
            Item_Page2.objects.create(caption=caption, price=price, path_img=path_img)

        elif input_select == '3':
            RAM.append({"price": price, "caption": caption, "img": path_img})
            Item_Page3.objects.create(caption=caption, price=price, path_img=path_img)

        return HttpResponseRedirect("/")

    else:
        form_add = FormAdd()
        return render(request, 'Page_form.html', {'form_add': form_add})
