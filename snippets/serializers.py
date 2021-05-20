from rest_framework import serializers

from .models import Snippet, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=False, allow_blank=True, max_length=100)
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        instance = Snippet.objects.create(**validated_data)
        return instance
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', validated_data.title)
        instance.code  = validated_data.get('code', validated_data.code)
        instance.linenos = validated_data.get('linenos', validated_data.linenos)
        instance.language = validated_data.get('language', validated_data.language)
        instance.style    = validated_data.get('style', validated_data.style)
        instance.save()

        return instance


