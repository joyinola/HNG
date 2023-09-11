from rest_framework import serializers
from datetime import datetime, timezone

class SlackTrackSerializer(serializers.Serializer):
    utc_time= serializers.SerializerMethodField()
    github_file_url= serializers.SerializerMethodField()
    github_repo_url= serializers.SerializerMethodField()
    current_day = serializers.SerializerMethodField()

    slack_name = serializers.CharField(max_length=255)
    # current_day = serializers.CharField(max_length=255)
    # utc_time = serializers.DateTimeField()
    track=serializers.CharField(max_length=255)
    # github_file_url=serializers.URLField(max_length=255)
    # github_repo_url=serializers.URLField(max_length=255)
    status_code=serializers.CharField(max_length=255,default=200)

    def get_utc_time(self,obj):
       utc_time=  datetime.now(timezone.utc)
       return getattr(obj, 'utc_time', utc_time)

        
    def get_github_file_url(self,obj):
        file_url= "https://github.com/joyinola/HNG/tree/master/HNG1/stage_one"
        return getattr(obj, 'github_file_url', file_url)

    def get_github_repo_url(self,obj):
        repo_url= "https://github.com/joyinola/HNG.git"
        return getattr(obj, 'github_repo_url', repo_url)
    
    def get_current_day(self,obj):
        current_day= datetime.now().strftime('%A')
        return getattr(obj, 'github_repo_url', current_day)
