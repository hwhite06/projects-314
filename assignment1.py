import random 
D20 = random.randint(1,20)
Hit1 = random.randint (1,6)
Hit2 = random.randint (1,6)
Hit3 = random.randint (1,6)
Hit4 = random.randint (1,6)
Hit5 = random.randint (1,6)
Hit6 = random.randint (1,6)
Hit7 = random.randint (1,6)
Hit8 = random.randint (1,6)
print ("I cast fireball")
print("Dexterity saving throw:")
print(D20)

if (D20>=14):
    Damage = ((Hit1+Hit2+Hit3+Hit4+Hit5+Hit6+Hit7+Hit8)/2)
    print ("saved! enemy takes half damage.")
else:
    Damage = (Hit1+Hit2+Hit3+Hit4+Hit5+Hit6+Hit7+Hit8)
    print ("failed! enemy takes full damage.")
print("Damage dealt:")
print(Damage)
      