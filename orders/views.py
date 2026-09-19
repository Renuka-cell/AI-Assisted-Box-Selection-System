from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Order
from .serializers import OrderSerializer
from .services import recommend_box


class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class RecommendBoxView(APIView):

    def post(self, request, pk):
        order = get_object_or_404(Order, pk=pk)

        try:
            result = recommend_box(order)

        except ValueError as error:
            return Response(
                {
                    "error": str(error)
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        if result is None:
            return Response(
                {
                    "order_id": order.id,
                    "recommended_box": None,
                    "message": (
                        "No suitable box is available "
                        "for this order."
                    ),
                },
                status=status.HTTP_200_OK,
            )

        box = result["box"]

        packed_dimensions = result["packed_dimensions"]

        return Response(
            {
                "order_id": order.id,
                "recommended_box": {
                    "id": box.id,
                    "name": box.name,
                    "length": str(box.length),
                    "width": str(box.width),
                    "height": str(box.height),
                    "max_weight": str(box.max_weight),
                    "cost": str(box.cost),
                },
                "total_weight": str(
                    result["total_weight"]
                ),
                "packed_dimensions": {
                    "length": str(packed_dimensions[0]),
                    "width": str(packed_dimensions[1]),
                    "height": str(packed_dimensions[2]),
                },
                "wasted_volume": str(
                    result["wasted_volume"]
                ),
            },
            status=status.HTTP_200_OK,
        )