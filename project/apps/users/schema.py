import graphql_jwt
from graphql_jwt.decorators import login_required
from graphene_django  import DjangoObjectType
from graphene import List, Field, String, ObjectType

from .models import User

class UserType(DjangoObjectType):
    class Meta:
        model = User
        exclude_fields = ['password']


class Query(ObjectType):
    me = Field(UserType)
    all = List(UserType)
    user_by_id = Field(UserType, id = String(required=True))

    def resolve_all(self, info):
        return User.objects.all()

    def resolve_user_by_id(self, info, id):
        return User.objects.get(pk=id)

    @login_required
    def resolve_me(self, info):
        return info.context.user

class Mutation(ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()