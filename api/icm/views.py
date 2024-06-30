from rest_framework import views, generics
from rest_framework.response import Response

from .serializers import ICMSerializer, ICMResponseSerializer
from .calculator import Calculator

class ICMView(generics.CreateAPIView):
    serializer_class = ICMSerializer
    iterations = 100000

    def post(self, request):
        data = request.data
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        icmResponse = {"chance":Calculator.sicm(data["stacks"],data["payouts"],self.iterations)}
        results = ICMResponseSerializer(icmResponse).data
        print(results)
        return Response(results)
