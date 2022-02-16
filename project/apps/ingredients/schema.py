import graphene
from graphene_django import DjangoObjectType
from graphql_jwt.decorators import login_required

from .models import Category, Ingredient

class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = ('__all__')


class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ('__all__')


class Query(graphene.ObjectType):
    category_all = graphene.List(CategoryType)
    category_by_id = graphene.Field(CategoryType, id = graphene.Int(required=True))

    ingredients_all = graphene.List(IngredientType)
    ingredient_by_id = graphene.Field(IngredientType, id = graphene.Int(required=True))

    @login_required
    def resolve_category_all(self, info):
        user = info.context.user
        return Category.objects.all()

    @login_required
    def resolve_category_by_id(self, info, id):
        return Category.objects.get(pk=id)

    @login_required
    def resolve_ingredients_all(self, info):
        return Ingredient.objects.all()

    @login_required
    def resolve_ingredients_by_id(self, info, id):
        return Ingredient.objects.get(pk=id)
