from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Tutorial
from .serializers import TutorialSerializer

@api_view(['GET', 'POST', 'DELETE'])
def tutorial_list(request):
    if request.method == 'GET':
        tutorials = Tutorial.objects.all()
        title = request.GET.get('title', None)
        if title is not None:
            tutorials = tutorials.filter(title__icontains=title)
        serializer = TutorialSerializer(tutorials, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = TutorialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Tutorial.objects.all().delete()
        return JsonResponse({'message': f'{count[0]} Tutorials were deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def tutorial_detail(request, pk):
    try:
        tutorial = Tutorial.objects.get(pk=pk)  # Find tutorial by pk
    except Tutorial.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        # Serialize the tutorial and return it
        serializer = TutorialSerializer(tutorial)
        return Response(serializer.data)

    elif request.method == 'PUT':
        # Update the tutorial with the data from the request
        serializer = TutorialSerializer(tutorial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        # Delete the tutorial
        tutorial.delete()
        return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    
        
@api_view(['GET'])
def tutorial_list_published(request):
    # Get only published tutorials
    tutorials = Tutorial.objects.filter(published=True)  # Adjust field name if necessary

    serializer = TutorialSerializer(tutorials, many=True)
    return Response(serializer.data)
