from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, JsonResponse
from .models import Item

def home(request):
    items = Item.objects.all()

    if not items:
        Item.objects.create(text="cat")
        Item.objects.create(text="dog")
        items = Item.objects.all()

    return render(request,'home.html',{'items': items})

def update_text(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=pk)
        item.text = request.POST.get('text')
        item.save()
        return HttpResponse('Text updated successfully!', status=204)

def update_image(request, pk):
    if request.method == 'POST':
        item = get_object_or_404(Item, pk=pk)
        item.image = request.FILES.get('image')
        item.save()
        return HttpResponse(f'<img id="image-display-{ pk }" src="{item.image.url}" alt="Uploaded Image" class="mb-2 max-w-full h-auto">')
        # return JsonResponse({'imageUrl': item.image.url})
        # return HttpResponse('Image updated successfully!', status=204)
