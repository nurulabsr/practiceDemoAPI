from .models import DemoModel
from .serializers import DemoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
from rest_framework import status
# Create your views here.



@api_view(['GET', 'POST'])
def DemoItems(request):
    if request.method == 'GET':
        items = DemoModel.objects.all()
        # -----------same method (start searching) ---------------
        search_variable = request.GET.get('search')  # ?search 
        price = request.GET.get('price')
        description = request.GET.get('description')
        
        if search_variable:
            items = items.filter(title__icontains=search_variable)
        if price:
            items = items.filter(price__icontains=price)
        if description:
            items = items.filter(description__icontains=description)  
        # __________end same method_______________
        # __________start ordering________________
        ordering = request.GET.get('ordering')
        if ordering:
           items = items.order_by(ordering)
        # __________End Ordering__________________
        serializers_item = DemoSerializer(items, many=True)
        return Response(serializers_item.data)
    
    if request.method == 'POST':
        serializers_item = DemoSerializer(data=request.data)
        serializers_item.is_valid(raise_exception=True)
        serializers_item.save()
        return Response(serializers_item.data, status.HTTP_201_CREATED)
        
