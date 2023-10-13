import random
#preguiça de colocar os gostos do zumbi
class Zumbi:
    def __init__(self, força, velocidade, inteligencia):
        self.força = força
        self.velocidade = velocidade
        self.inteligencia = inteligencia

class Pato:
    def __init__(self, nome):
        self.nome = nome
        self.força = random.randint(1, 100)
        self.velocidade = random.randint(1, 100)
        self.inteligencia = random.randint(1, 100)
#qual e o zumbi?
def identificar_zumbi():
    força = random.randint(1, 100)
    velocidade = random.randint(1, 100)
    inteligencia = random.randint(1, 100)
    return Zumbi(força, velocidade, inteligencia)
#periculosidade? o que e isso? ;)
def avaliar_periculosidade(zumbi):
    return zumbi.força + zumbi.velocidade + zumbi.inteligencia
#pontos fracos?
def identificar_pontos_fracos(zumbi):
    pontos_fracos = []
    if zumbi.força < 40:
        pontos_fracos.append("Força fraca")
    if zumbi.velocidade > 70:
        pontos_fracos.append("Velocidade alta")
    if zumbi.inteligencia < 50:
        pontos_fracos.append("Inteligência baixa")
    return pontos_fracos
#tentativa de sistema de defesa e ataque
def sistema_de_defesa_e_ataque(pato, zumbi):
    periculosidade = avaliar_periculosidade(zumbi)
    pontos_fracos = identificar_pontos_fracos(zumbi)

    print(f"{pato.nome} se depara com um zumbi perigoso!")
    print(f"Avaliação da periculosidade do zumbi: {periculosidade}")
    print(f"Pontos fracos do zumbi: {', '.join(pontos_fracos)}")

    if periculosidade > 150:
        print(f"{pato.nome} decide alçar voo para evitar o confronto.")
    else:
        print(f"{pato.nome} ataca o zumbi nos pontos fracos!")

patos = [Pato("Pato1"), Pato("Pato2"), Pato("Pato3")]
#simulaçao se o pato iria ganhar
for pato in patos:
    zumbi = identificar_zumbi()
    sistema_de_defesa_e_ataque(pato, zumbi)
    print()
