from rest_framework import serializers

from viva_translate.competitions.models import Competition


def error_message(previous_score, new_score):
    message = (
        f"You can not register the new score {previous_score} "
        + f"because in the past competition the team scored {new_score}"
    )
    return message


class CompetitionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Competition
        fields = [
            "id",
            "year",
            "instance",
            "team",
            "score",
        ]

    def validate(self, attrs):
        if str(attrs["instance"]).upper() == "NA":
            past_result = Competition.objects.filter(
                team=attrs["team"], year=attrs["year"], instance="LO"
            )
            if past_result:
                if past_result.first().score > 65:
                    return attrs
                else:
                    raise serializers.ValidationError(
                        error_message(attrs["score"], past_result.first().score)
                    )
        elif str(attrs["instance"]).upper() == "RE":
            past_result = Competition.objects.filter(
                team=attrs["team"], year=attrs["year"], instance="NA"
            )
            if past_result:
                if past_result.first().score > 65:
                    return attrs
                else:
                    raise serializers.ValidationError(
                        error_message(attrs["score"], past_result.first().score)
                    )
        elif str(attrs["instance"]).upper() == "IN":
            past_result = Competition.objects.filter(
                team=attrs["team"], year=attrs["year"], instance="RE"
            )
            if past_result:
                if past_result.first().score > 65:
                    return attrs
                else:
                    raise serializers.ValidationError(
                        error_message(attrs["score"], past_result.first().score)
                    )
        elif str(attrs["instance"]).upper() == "LO":
            return attrs


class YearFilterSerializer(serializers.Serializer):
    total_score = serializers.IntegerField()
    instance = serializers.CharField()
