class Cat:
    def __init__(self, life = 'boring', satiety = 'none', height = 80, owner='angry'):
        self.life = life
        self.satiety = satiety
        self.height = height
        self.owner = owner

class Dog:
    def __init__(self, life1='happy', satiety1='true', height1=70, owner1='kind'):
        self.life1 = life1
        self.satiety1 = satiety1
        self.height1 = height1
        self.owner1 = owner1

cat=Cat()
dog=Dog()
print("cat's life:")
print('life was-', cat.life )
print('satiety was-', cat.satiety)
print('hieght was-', cat.height)
print('owner was-', cat.owner)
print("dog's life:")
print('life was-', dog.life1)
print('satiety was-', dog.satiety1)
print('hieght was-', dog.height1)
print('owner was-', dog.owner1)
