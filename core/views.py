from core.models import Stock, CoffeeBag
from django.shortcuts import get_object_or_404
from serializers import StockSerializer, CoffeeBagSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StockList(APIView):
    """
    List all Stock list, or create a new stock.
    """

    def get(self, request, format=None):
        owner = request.user.is_superuser
        if owner:
            stock = Stock.objects.all()
        else:
            stock = Stock.objects.filter(owner=request.user)
        serializer = StockSerializer(stock, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StockSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockDetail(APIView):
    """
    retrieve, update or delete a stock instance
    """

    def get_object(self, pk):
        try:
            return Stock.objects.get(pk=pk)
        except Stock.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        stock = self.get_object(pk)
        serializer = StockSerializer(stock, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        stock = self.get_object(pk)
        stock.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CoffeeBags(APIView):
    """
    List all CoffeBags list, or create a new stock.
    """

    def get(self, request, format=None):
        owner = request.user.is_superuser
        if owner:
            coffeebags = CoffeeBag.objects.all()    
        else:
            # coffeebags = CoffeeBag.objects.filter(stock=request.stock.owner)
            coffeebags = CoffeeBag.objects.filter(stock=request.user.id)
        serializer = CoffeeBagSerializer(coffeebags, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CoffeeBagSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CoffeeBagDetail(APIView):
    """
    retrieve, update or delete a coffeeBag instance
    """

    # def get_object(self, pk):
    #     try:
    #         return CoffeeBag.objects.get(pk=pk)
    #     except CoffeeBag.DoesNotExist:
    #         raise Http404
    def get_object(self, pk):
        obj = get_object_or_404(self.get_queryset(), pk=self.kwargs["pk"])
        self.check_object_permissions(self.request, obj)
        return obj

    def get(self, request, pk, format=None):
        coffeebag = self.get_object(pk)
        serializer = CoffeeBagSerializer(coffeebag)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        coffeebag = self.get_object(pk)
        serializer = CoffeeBagSerializer(coffeebag, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        coffeebag = self.get_object(pk)
        coffeebag.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
