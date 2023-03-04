from django.db.models import Avg
from rest_framework import mixins, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from viva_translate.competitions.models import Competition
from viva_translate.competitions.serializers import (
    CompetitionSerializer,
    YearFilterSerializer,
)


class CompetitionViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    serializer_class = CompetitionSerializer
    queryset = Competition.objects.all()

    @action(
        detail=False,
        methods=["get"],
        url_path=r"year-result/(?P<year>\w+)",
        url_name="year_result",
    )
    def year_result(self, request, year=None):
        year_result_data = Competition.objects.filter(year=year)
        if year_result_data:
            year_result_data = (
                Competition.objects.filter(year=year)
                .values("instance")
                .order_by("instance")
                .annotate(total_score=Avg("score"))
            )
            serializer_class = YearFilterSerializer(year_result_data, many=True)

            return Response(data=serializer_class.data, status=status.HTTP_202_ACCEPTED)
        return Response({"Error": f"Year {year} doesn't have data related"})

    @action(
        detail=False,
        methods=["get"],
        url_path=r"instance-result/(?P<instance>\w+)",
        url_name="instance_result",
    )
    def instance_result(self, request, instance=None):
        instance_result_data = Competition.objects.filter(
            instance=str(instance).upper()
        )
        if instance_result_data:
            instance_result_data = (
                Competition.objects.filter(instance=str(instance).upper())
                .values("instance")
                .order_by("instance")
                .annotate(total_score=Avg("score"))
            )
            serializer_class = YearFilterSerializer(instance_result_data, many=True)

            return Response(data=serializer_class.data, status=status.HTTP_202_ACCEPTED)
        return Response({"Error": f"Instance {instance} doesn't exist"})
