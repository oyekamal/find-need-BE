from dj_rest_auth.registration.views import RegisterView
from .serializers import (
    GetCustomUserSerializer,
    ListFollowSerializer,
    FollowSerializer,
    CustomRegisterSerializer,
    LanguageSerializer,
    UserLanguageUpdateSerializer,
    UserSerializer,
    CustomUserUpdateSerializer,
    BlockSerializer,
    ChatMessageSerializer,
    NotificationSerializer,
)
from .models import (
    Language,
    CustomUser,
    Country,
    City,
    Follow,
    Block,
    ChatMessage,
    Notification,
)
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from .serializers import CountrySerializer, CitySerializer
from rest_framework import filters
from django_filters import rest_framework as drf_filters
from .serializers import CustomUserSerializer

from dj_rest_auth.serializers import LoginSerializer
from dj_rest_auth.views import LoginView
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.decorators import action
from rest_framework.response import Response


class PageNumberPaginationCustom(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000


class LimitOffsetPaginationCustom(LimitOffsetPagination):
    default_limit = 10
    limit_query_param = "limit"
    offset_query_param = "offset"
    max_limit = 1000


class FollowingListView(ListAPIView):
    serializer_class = CustomUserUpdateSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        user = get_object_or_404(CustomUser, id=user_id)
        following = Follow.objects.filter(follower=user).values_list(
            "following", flat=True
        )
        return CustomUser.objects.filter(id__in=following)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FollowerListView(ListAPIView):
    serializer_class = CustomUserUpdateSerializer

    def get_queryset(self):
        user_id = self.kwargs["user_id"]
        user = get_object_or_404(CustomUser, id=user_id)
        followers = Follow.objects.filter(following=user).values_list(
            "follower", flat=True
        )
        return CustomUser.objects.filter(id__in=followers)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class FollowViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["follower", "following"]
    search_fields = ["follower", "following"]

    def get_serializer_class(self):
        if self.action == "list":
            return ListFollowSerializer
        elif self.action == "retrieve":
            return ListFollowSerializer
        return FollowSerializer


class CustomLoginView(LoginView):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        if not serializer.is_valid():
            return Response(
                {"message": f"Fail to login", "error": serializer.errors},
                status=status.HTTP_404_NOT_FOUND,
            )

        # serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        # try:
        #     user.auth_token.delete()
        # except:
        #     pass
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "key": token.key,
                "message": "Login successful",
                "email": user.email,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "phone_number": user.phone_number,
                "id": user.id,
                "is_staff": user.is_staff,
                "is_active": user.is_active,
                "error": {},
            },
            status=status.HTTP_200_OK,
        )


# class CustomLoginView(LoginView):
#     serializer_class = LoginSerializer
#     def get_response(self):
#         orginal_response = super().get_response()
#         mydata = {"message": "some message", "status": "success"}
#         orginal_response.data.update(mydata)
#         return orginal_response


# def post(self, request, *args, **kwargs):
#     response = super().post(request, *args, **kwargs)
#     user = self.request.user
#     response.data['email'] = user.email
#     response.data['username'] = user.username
#     response.data['first_name'] = user.first_name
#     response.data['last_name'] = user.last_name
#     response.data['phone_number'] = user.phone_number
#     return response
class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            {"message": "User created successfully."}, status=201, headers=headers
        )

    def perform_create(self, serializer):
        user = serializer.save(self.request)
        # Additional logic if needed


class LanguageViewSet(ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class UserLanguageUpdate(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserLanguageUpdateSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        updated_instance = self.get_object()  # Get the updated user instance
        return Response(
            UserSerializer(updated_instance).data, status=status.HTTP_200_OK
        )


class CustomUserDetail(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPaginationCustom
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = [
        "username",
        "email",
        "first_name",
        "last_name",
        "phone_number",
        "is_active",
        "is_staff",
    ]
    search_fields = ["username", "email", "first_name", "last_name", "phone_number"]

    def get_serializer_class(self):
        if self.action == "list":
            return GetCustomUserSerializer
        elif self.action == "retrieve":
            return GetCustomUserSerializer
        return CustomUserSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context["request"] = self.request
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            # Exclude users who are blocked by the current user
            queryset = queryset.exclude(blocking__blocker=self.request.user).order_by(
                "-created_at"
            )
        return queryset


class CustomUserUpdate(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserUpdateSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


class CountryViewSet(ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name"]
    search_fields = ["name"]


class CityViewSet(ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["name", "country"]


class BlockViewSet(ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["blocker", "blocked"]

    def perform_create(self, serializer):
        serializer.save(blocker=self.request.user)

    def get_queryset(self):
        return Block.objects.filter(blocker=self.request.user)


class ChatMessageViewSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ChatMessage.objects.all()
    pagination_class = PageNumberPaginationCustom
    serializer_class = ChatMessageSerializer
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["sender", "receiver"]
    search_fields = ["sender", "receiver"]

    # def get_queryset(self):
    #     user = self.request.user
    #     return ChatMessage.objects.filter(sender=user) | ChatMessage.objects.filter(receiver=user)

    @action(detail=False, methods=["get"], url_path="chat-users")
    def chat_users(self, request):
        user = request.user
        sent_messages = (
            ChatMessage.objects.filter(sender=user)
            .values_list("receiver", flat=True)
            .distinct()
        )
        received_messages = (
            ChatMessage.objects.filter(receiver=user)
            .values_list("sender", flat=True)
            .distinct()
        )
        chat_user_ids = set(sent_messages).union(set(received_messages))
        chat_users = CustomUser.objects.filter(id__in=chat_user_ids)
        serialize = GetCustomUserSerializer(chat_users, many=True)
        return Response(serialize.data)


class NotificationViewSet(ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPaginationCustom
    filter_backends = [filters.SearchFilter, drf_filters.DjangoFilterBackend]
    filterset_fields = ["title", "body", "name", "user", "notification_type"]
    search_fields = [
        "title",
        "name",
        "user",
    ]

    # Custom patch action to mark notifications as read
    @action(detail=False, methods=["patch"], url_path="mark-as-read")
    def mark_as_read(self, request):
        # Extract the list of notification IDs from the request data
        notification_ids = request.data.get("ids", [])

        if not notification_ids:
            return Response(
                {"detail": "No notification IDs provided."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Update notifications where id is in the list
        notifications = Notification.objects.filter(id__in=notification_ids)
        updated_count = notifications.update(is_read=True)

        if updated_count > 0:
            return Response(
                {"detail": f"{updated_count} notifications marked as read."},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"detail": "No notifications were updated."},
                status=status.HTTP_404_NOT_FOUND,
            )

    # Get unread notification IDs for a specific user using a query param
    @action(detail=False, methods=["get"], url_path="unread-ids")
    def get_unread_notification_ids(self, request):
        user_id = request.query_params.get("user")

        if not user_id:
            return Response(
                {"detail": "User identifier is required."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Retrieve unread notifications for the specified user
        unread_notifications = Notification.objects.filter(
            user=user_id, is_read=False
        ).values_list("id", flat=True)

        if unread_notifications:
            return Response(
                {"unread_ids": list(unread_notifications)},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"detail": "No unread notifications."},
                status=status.HTTP_404_NOT_FOUND,
            )
