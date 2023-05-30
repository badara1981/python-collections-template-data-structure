
menu_item_var = {'name': "Menu Item", 'ing': "ingredients"}

class Recipe:
    def __init__(self,name,ingredients):
        self.name = name
        self.ingredients = ingredients
    def __str__(self):
        return "{name}: {ingredients}".format(name=self.name,ingredients=self.ingredients)

toast = Recipe("toast",("bread"))
sandwich = Recipe("sandwich",("bread","butter","ham","cheese","butter","bread"))

##

context = {
  'navigation': [
    'Home',
    'Explore',
    'Notification',
    'Messages',
  ],'Information':[
      'Name',
     'Twitter Name',
     'Description',
     'Date',
     'Followers number',
     'Following'],
      'Who to follow':[
          {'name':['tweet_name','about']}]
}

context = {
  'navigation': [
    'Home',
    'Explore',
    'Notification',
    'Messages',
  ],'Information':[
      'Name',
     'Twitter Name',
     'Description',
     'Date',
     'Followers number',
     'Following'],
      'Who to follow':[
          {'name':['tweet_name','about']}]
}
print(context)
