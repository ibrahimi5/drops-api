from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utils.permissions import IsOwnerOrReadOnly
from .models import Post
from .serializers.common import PostSerializer
from .serializers.populated import PopulatedPostSerializer
from rest_framework.exceptions import NotFound

class PostShowView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    def get(self, request):
        posts = Post.objects.all()              
        serializer = PopulatedPostSerializer(posts, many=True)  
        return Response(serializer.data) 

    def post(self, request):
      request.data['owner'] = request.user.id
      serializer = PostSerializer(data=request.data)
      serializer.is_valid(raise_exception=True) 
      serializer.save() 
      return Response(serializer.data, status=201)      
    
class PostDetailView(APIView):
    permission_classes = [IsOwnerOrReadOnly]
    
    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise NotFound(detail="post not found.")
        
        #SHOW route
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PopulatedPostSerializer(post)
        return Response(serializer.data)

    #UPDATE route
    def put(self, request, pk):
        post = self.get_object(pk)
        self.check_object_permissions(request, post)
        serializer = PostSerializer(post, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
        
    #DELETE route
    def delete(self, request, pk):
        post = self.get_object(pk)
        self.check_object_permissions(request, post)
        post.delete()
        return Response(status=204)