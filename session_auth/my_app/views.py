
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Article
from .serializers import ArticleSerializer

from rest_framework.authentication import (
   SessionAuthentication,
   BasicAuthentication,
   )

from rest_framework.permissions    import (
   AllowAny,
   IsAdminUser,
   IsAuthenticated,
   IsAuthenticatedOrReadOnly,
   DjangoModelPermissions,
   DjangoObjectPermissions,
    
)

class ArticleAPIView(APIView):
   
   authentication_classes = [SessionAuthentication]
   permission_classes     = [IsAuthenticated]
   # permission_classes     = [IsAuthenticatedOrReadOnly]
   # permission_classes     = [AllowAny]
   # permission_classes     = [IsAdminUser]
   # permission_classes     = [DjangoModelPermissions]
   # permission_classes     = [DjangoObjectPermissions]
   
   
   def get(self, request, format=None):
      id = request.data.get('id')
      
      if not id: # if id does exists
         all_articles = Article.objects.all().order_by('-id')
         serializer = ArticleSerializer(all_articles, many=True)
         res = {'detail': serializer.data}
         return Response(res, status=status.HTTP_200_OK)
      
      else:
         try:
            article = Article.objects.get(pk=id)
         except Article.DoesNotExist:
            error = {'detail': 'Sooorry! Article Does Not Exist that you looking for'}
            return Response(error, status=status.HTTP_204_NO_CONTENT)
         except:
            error = {'detail': 'Request is not valid'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
         else:
            serializer = ArticleSerializer(article)
            res = {'detail': serializer.data}
            return Response(res, status=status.HTTP_200_OK)
         
   def post(self, request, format=None):
      """post request to insert data into db"""
      
      serializer = ArticleSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save()
         msg = {'Success': 'Data inserted successfuly', 'data': serializer.data}
         return Response(msg, status=status.HTTP_201_CREATED)
      
      return Response(serializer.errors)
   
   def patch(self, request, format=None):
      """patch request for partial update"""
      id  = request.data.get('id')
      
      if not id: # id does not exist
         msg = {
            'detail': 'Id is required'
         }
         return Response(msg, status=status.HTTP_400_BAD_REQUEST)   
      else:
         try:
            article = Article.objects.get(pk=id)
         except Article.DoesNotExist:
            error = {'Does Not Exist': 'Sooorry! Article Does Not Exist that you looking for'}
            return Response(error, status=status.HTTP_204_NO_CONTENT)
         except:
            error = {'Invalid request': 'Request is not valid'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
         else:
            serializer = ArticleSerializer(article, data=request.data, partial=True)
            if serializer.is_valid():
               serializer.save()
               res = {
                  'msg': 'Data Successfuly Updated', 'data':serializer.data
               }
               return Response(res, status=status.HTTP_200_OK)
               
            else:
               return Response(serializer.errors, status=status.HTTP_BAD_REQUEST)
   
   def put(self, request, format=None):
      """put request for complete update"""
      id  = request.data.get('id')
      
      if not id: # id does not exist
         msg = {
            'detail': 'Id is required'
         }
         return Response(msg, status=status.HTTP_400_BAD_REQUEST)   
      else:
         try:
            article = Article.objects.get(pk=id)
         except Article.DoesNotExist:
            error = {'detail': 'Sooorry! Article Does Not Exist that you looking for'}
            return Response(error, status=status.HTTP_204_NO_CONTENT)
         
         except:
            error = {'detail': 'Request is not valid'}
            return Response(error, status=status.HTTP_400_BAD_REQUEST)
         
         else:
            serializer = ArticleSerializer(article, data=request.data)
            if serializer.is_valid():
               serializer.save()
               res = {
                  'detail': 'Data Successfuly Updated', 'data':serializer.data
               }
               return Response(res, status=status.HTTP_200_OK)
            
            else:
               return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
   
   def delete(self, request, format=None):
      """delete request to delete objects"""
      
      id  = request.data.get('id')
      
      if not id: # id is none
         error = {'detail': 'Id required for deletion'}
         return Response(error, status=status.HTTP_400_BAD_REQUEST)
      else:
         try:
            article = Article.objects.get(pk=id)
         except Article.DoesNotExist:
            error = {'detial': 'Article does not found'}
            return Response(error, status.HTTP_400_BAD_REQUEST)
         
         except:
            error = {'detial': 'Invalid request'}
            return Response(error, status.HTTP_400_BAD_REQUEST)
         
         else:
            article.delete()
            msg = {'detail': 'Article Deleted Successfuly'}
            return Response(msg, status=status.HTTP_200_OK)
            
         
      