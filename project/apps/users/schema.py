import graphene_django
from graphene_django.types import DjangoObjectType

from .models import User

class UserNode(DjangoObjectType):
  class Meta:
    model = User
    interface = (Node,)
    fields = "__all__"

class Query(object):
  all_users = Node.Field(UserNode)