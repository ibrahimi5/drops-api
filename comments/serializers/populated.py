from .common import CommentSerializer
from users.serializers.common import BasicUserSerializer

class PopulatedPostSerializer(CommentSerializer):
    owner = BasicUserSerializer()
