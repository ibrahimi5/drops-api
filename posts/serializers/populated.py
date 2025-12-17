from .common import PostSerializer
from users.serializers.common import BasicUserSerializer

class PopulatedPostSerializer(PostSerializer):
    owner = BasicUserSerializer()
