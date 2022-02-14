from graphene_django import DjangoObjectType
import graphene

from apps.users.models import User as UserModel
from apps.cards.models import Card as CardModel
from apps.decks.models import Deck as DecksModel

class User(DjangoObjectType):
  class Meta:
    model = UserModel
    fields = ('email', 'id', 'is_active', 'is_admin', 'last_login')


class Card(DjangoObjectType):
  class Meta:
    model = CardModel

class Decks(DjangoObjectType):
  class Meta:
    model = DecksModel

class Query(graphene.ObjectType):
  users = graphene.List(User)
  cards = graphene.List(Card)
  decks = graphene.List(Decks)

  def resolve_users(self, info):
    return UserModel.objects.all()

  def resolve_cards(self, info):
    return CardModel.objects.all()

  def resolve_decks(self, info):
    return DecksModel.objects.all()


class CreateDeck(graphene.Mutation):
  deck = graphene.Field(Decks)
  class Arguments:
    title = graphene.String()
    description = graphene.String()
  
  def mutate(self, info, title, description):
    print(title, description)
    d = DecksModel(
      title=title, description=description
    )
    d.save()
    return CreateDeck(deck=d)

class CreateCard(graphene.Mutation):
  card = graphene.Field(Card)

  class Arguments:
    question = graphene.String()
    answer = graphene.String()
    deck = graphene.String()

  def mutate(self, info, deck, question, answer):
    c = CardModel(
      question=question, answer=answer, deck_id=deck
    )
    c.save()

    return CreateCard(card=c)


class Mutation(graphene.ObjectType):
  create_card = CreateCard.Field()
  create_deck = CreateDeck.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)