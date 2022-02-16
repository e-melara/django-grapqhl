import graphene
from graphene_django import DjangoObjectType

import apps.users.schema
import apps.ingredients.schema

class Query(
  apps.users.schema.Query,
  apps.ingredients.schema.Query,
  graphene.ObjectType
):
  pass

class Mutation(
  apps.users.schema.Mutation,
  graphene.ObjectType
):
  pass

schema = graphene.Schema(query=Query, mutation=Mutation)