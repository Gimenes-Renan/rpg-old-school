import random

class classeBase:
    forca = 0
    agilidade = 0
    vitalidade = 0
    energia = 0
    hp = vitalidade*1
    mp = energia*1
    skills=[]


class Arqueiro(classeBase):
    skills=["Shot","Triple Shot","Critical"]
    forca = 2
    agilidade = 4
    vitalidade = 1
    energia = 2
    hp = vitalidade*60
    mp = energia*80
    skill1 = agilidade*1
    skill2 = agilidade*energia*forca*1
    skill3 = energia*(agilidade)*3

class Guerreiro(classeBase):
    skills=["Swing","Triple Swing","Strenght"]
    forca = 4
    agilidade = 2
    vitalidade = 2
    energia = 1
    hp = vitalidade*100
    mp = energia*40
    skill1 = forca*1
    skill2 = vitalidade*energia*forca*1
    skill3 = energia*(forca)*3
class Ladino(classeBase):
    skills=["Steal","Triple Stars","Evade"]
    forca = 1
    agilidade = 4
    vitalidade = 2
    energia = 2
    hp = vitalidade*60
    mp = energia*80
    skill1 = agilidade*1
    skill2 = agilidade*energia*forca*1
    skill3 = energia*(agilidade)*3
class Mago(classeBase):
    skills=["Magic Ball","Triple Comets","Mana Regen"]
    forca = 1
    agilidade = 2
    vitalidade = 2
    energia = 4
    hp = vitalidade*40
    mp = energia*100
    skill1 = energia*1
    skill2 = energia*agilidade*vitalidade*1
    skill3 = energia*energia*3
def usarSkill():
    for item in classe.skills:
        print(item)

    while True:
        skill = input ("Selecione sua Skill:")
        if (skill.lower() == classe.skills[0].lower()) or (skill == "1"):
            return (random.random()+1)*classe.skill1
        elif (skill.lower() == classe.skills[1].lower()) or (skill == "2"):
            return (random.random()+1)*classe.skill2
        elif (skill.lower() == classe.skills[2].lower()) or (skill == "3"):
            return (random.random()+1)*classe.skill3


classe = classeBase()
classeStr = str

print ("Qual sua classe? \n Arqueiro, Guerreiro, Ladino, Mago")
while True:
    classeStr=input()
    if classeStr.lower() == "arqueiro":
        classe = Arqueiro
        break
    elif classeStr.lower() == "guerreiro":
        classe = Guerreiro
        break
    elif classeStr.lower() == "ladino":
        classe = Ladino
        break
    elif classeStr.lower() == "mago":
        classe = Mago
        break

print ("A classe escolhida foi " + classeStr)
print ("Você tem 10 pontos para gastar em Força, Vitalidade, Agilidade, Energia")
classe.forca += int(input("Força: "))
classe.vitalidade += int(input("Vitalidade: "))
classe.agilidade += int(input("Agilidade: "))
classe.energia += int(input("Energia: "))
classe.hp += classe.vitalidade*10
classe.mp += classe.energia*10
print ("Seus Status são:")
print ("\nForça: ",classe.forca,"\nAgilidade: ",classe.agilidade,"\nVitalidade:",classe.vitalidade,"\nEnergia:",classe.energia)

exp = 0
level = 1

while True:
    dificuldade = int(input("Qual o nivel que quer jogar? (1 a 5)"))
    mobHp = dificuldade*80
    mobExp = dificuldade*1
    print ("O Nível selecionado foi: ",dificuldade, "\nA vida do MOB é:", mobHp)
    print ("Vamos lutar!")


    while classe.hp>0 and mobHp>0:
        playerAtt = usarSkill()
        print("]Seu dano: ", playerAtt)
        mobHp -= playerAtt
        print("Vida do MOB ",mobHp)
        if mobHp <=0:
            break
        mobAtt = (random.random()+1)*dificuldade
        print("Dano do MOB ",mobAtt)
        classe.hp -= mobAtt
        print ("Seu HP ",classe.hp)

    if classe.hp<=0:
        print("Você Morreu")
        break

    expToLevel = (level**3)
    if mobHp<=0:
        print("Você Venceu!")
        exp += mobExp
        print ("EXP Atual: ",exp, "A EXP necessário para o próximo nível é ", expToLevel)

    if (exp >= expToLevel):
        level += 1
        print ("*****************************'\n' Você passou de Nível, seu novo Nível é: ", level,'\n *****************************')
        classe.forca += 2
        classe.vitalidade += 2
        classe.agilidade += 2
        classe.energia += 2
        classe.hp += classe.vitalidade*10
        classe.mp += classe.energia*10
        print ("Status Atuais:",'\n',"Força: ",classe.forca,'\n',"Agilidade: ",classe.agilidade,'\n',"Vitalidade:",classe.vitalidade,'\n',"Energia:",classe.energia,'\n')
