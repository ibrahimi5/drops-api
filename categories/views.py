from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from posts.models import Post
from .serializers.common import CategorySerializer
from posts.serializers.populated import PopulatedPostSerializer
from rest_framework.exceptions import NotFound

class CategoryIndexView(APIView):
    def get(self, request):
        category = Category.objects.all()              
        serializer = CategorySerializer(category, many=True)  
        return Response(serializer.data) 


class PostByCategoryView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)  # fetch single Category
        except Category.DoesNotExist:
            raise NotFound(detail="Category not found.")
    
        posts = Post.objects.filter(category=category)
        serializer = PopulatedPostSerializer(posts, many=True)
        return Response(serializer.data)