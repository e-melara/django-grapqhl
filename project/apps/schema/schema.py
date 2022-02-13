from graphene_django import DjangoObjectType
import graphene

from apps.users.models import User as UserModel

class User(DjangoObjectType):
  class Meta:
    model = UserModel
    fields = ('email', 'id', 'is_active', 'is_admin', 'last_login')

class Query(graphene.ObjectType):
  users = graphene.List(User)

  def resolve_users(self, info):
    return UserModel.objects.all()

schema = graphene.Schema(query=Query)