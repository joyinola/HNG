from rest_framework import serializers
from datetime import datetime, timezone

class SlackTrackSerializer(serializers.Serializer):
    utc_time= serializers.SerializerMethodField()
    github_file_url= serializers.SerializerMethodField()
    github_repo_url= serializers.SerializerMethodField()

    slack_name = serializers.CharField(max_length=255)
    current_day = serializers.CharField(max_length=255)
    utc_time = serializers.DateTimeField()
    track=serializers.CharField(max_length=255)
    github_file_url=serializers.URLField(max_length=255)
    github_repo_url=serializers.URLField(max_length=255)
    status_code=serializers.CharField(max_length=255)

    def get_utc_time(self,obj):
       utc_time=  datetime.now(timezone.utc)
       return getattr(obj, 'utc_time', utc_time)

        
    def get_github_file_url(self,obj):
        utc_time=  datetime.now(timezone.utc)
        return getattr(obj, 'utc_time', utc_time)

    def get_github_file_url(self,obj):
        utc_time=  datetime.now(timezone.utc)
        return getattr(obj, 'utc_time', utc_time)
