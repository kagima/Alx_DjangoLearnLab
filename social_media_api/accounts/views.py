from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from rest_framework import status
from .models import User
from .serializers import UserSerializer, LoginSerializer, UserProfileSerializer

# User Registration
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.get(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Login
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# User Profile (Authenticated users only)
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

# Follower  user view
class FollowUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        user_to_follow = User.objects.get(pk=pk)
        if user_to_follow == request.user:
            return Response({'error': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.add(user_to_follow)
        return Response({'message': f'You are now following {user_to_follow.username}.'}, status=status.HTTP_200_OK)

# Unfollow user view
class UnfollowUserView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        user_to_unfollow = User.objects.get(pk=pk)
        if user_to_unfollow == request.user:
            return Response({'error': 'You cannot unfollow yourself.'}, status=status.HTTP_400_BAD_REQUEST)
        request.user.following.remove(user_to_unfollow)
        return Response({'message': f'You have unfollowed {user_to_unfollow.username}.'}, status=status.HTTP_200_OK)
    
            
