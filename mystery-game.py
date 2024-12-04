import random
import time

class MysteryGame:
    def __init__(self):
        self.cases = [
            {
                "title": "O Roubo no Museu",
                "description": "Uma valiosa pintura desapareceu do museu local durante uma exposição especial. Você precisa descobrir o culpado entre 4 suspeitos.",
                "suspects": [
                    {"nome": "Carlos Silva", "profissao": "Zelador do Museu", "alibi": "Estava fazendo limpeza no andar de baixo"},
                    {"nome": "Laura Mendes", "profissao": "Curadora", "alibi": "Estava em reunião com diretores"},
                    {"nome": "Ricardo Santos", "profissao": "Segurança", "alibi": "Fazia ronda no corredor principal"},
                    {"nome": "Amanda Oliveira", "profissao": "Visitante", "alibi": "Estava no café do museu"}
                ],
                "evidencias": [
                    "Câmera de segurança com falha no horário do roubo",
                    "Pegadas próximas à vitrine",
                    "Chave mestra do sistema de alarme desativada",
                    "Bilhete misterioso encontrado no local"
                ],
                "solucao": "Ricardo Santos"
            },
            {
                "title": "Mistério na Mansão Abandonada",
                "description": "Um grupo de jovens encontra um corpo estranho em uma mansão antiga. Quem é o assassino?",
                "suspects": [
                    {"nome": "João Pedro", "profissao": "Explorador Urbano", "alibi": "Estava fotografando os cômodos"},
                    {"nome": "Marina Rocha", "profissao": "Historiadora", "alibi": "Estudando a história da mansão"},
                    {"nome": "Lucas Ferreira", "profissao": "Advogado", "alibi": "Verificando documentos da propriedade"},
                    {"nome": "Helena Costa", "profissao": "Jornalista", "alibi": "Investigando histórias locais"}
                ],
                "evidencias": [
                    "Pegadas diferentes no chão empoeirado",
                    "Carta antiga escondida em um livro",
                    "Relógio parado com hora específica",
                    "Marca de sangue na escada"
                ],
                "solucao": "Lucas Ferreira"
            },
            {
                "title": "O Desaparecimento no Cruzeiro",
                "description": "Uma passageira misteriosamente some durante um cruzeiro de luxo. Descubra o culpado.",
                "suspects": [
                    {"nome": "Roberto Lima", "profissao": "Capitão", "alibi": "Na cabine de comando"},
                    {"nome": "Suzana Almeida", "profissao": "Camareira", "alibi": "Organizando os quartos"},
                    {"nome": "André Costa", "profissao": "Barman", "alibi": "Preparando bebidas no bar"},
                    {"nome": "Paula Rodrigues", "profissao": "Passageira", "alibi": "No convés principal"}
                ],
                "evidencias": [
                    "Cartão-chave do quarto encontrado no corredor",
                    "Câmera de segurança com imagem borrada",
                    "Maletinha deixada para trás",
                    "Registro de chamadas telefônicas"
                ],
                "solucao": "Roberto Lima"
            },
            {
                "title": "Assassinato na Empresa",
                "description": "O diretor financeiro é encontrado morto em seu escritório. Quem cometeu o crime?",
                "suspects": [
                    {"nome": "Eduardo Souza", "profissao": "Contador", "alibi": "Em reunião com auditores"},
                    {"nome": "Carla Pereira", "profissao": "Secretária", "alibi": "Na recepção"},
                    {"nome": "Rafael Oliveira", "profissao": "Vendedor", "alibi": "Em visita a clientes"},
                    {"nome": "Mônica Santos", "profissao": "Recursos Humanos", "alibi": "Entrevistando candidatos"}
                ],
                "evidencias": [
                    "Documento rasgado na lixeira",
                    "Vidro da janela quebrado",
                    "Sangue em uma gaveta entreaberta",
                    "E-mail com ameaças anônimas"
                ],
                "solucao": "Eduardo Souza"
            },
            {
                "title": "Mistério na Escola",
                "description": "O laboratório de informática foi vandalizado. Descubra quem foi o responsável.",
                "suspects": [
                    {"nome": "Pedro Henrique", "profissao": "Aluno", "alibi": "Na aula de educação física"},
                    {"nome": "Ana Clara", "profissao": "Professora", "alibi": "Em reunião pedagógica"},
                    {"nome": "Carlos Alberto", "profissao": "Técnico de Informática", "alibi": "Em manutenção no auditório"},
                    {"nome": "Juliana Reis", "profissao": "Coordenadora", "alibi": "Em visita administrativa"}
                ],
                "evidencias": [
                    "Marca de tênis no chão",
                    "Pendrive deixado para trás",
                    "Câmera de segurança com sinal de interferência",
                    "Mensagem de texto no celular apreendido"
                ],
                "solucao": "Pedro Henrique"
            },
            {
                "title": "Roubo na Joalheria",
                "description": "Uma coleção de joias raras desapareceu durante a noite. Quem é o ladrão?",
                "suspects": [
                    {"nome": "Fernando Rocha", "profissao": "Segurança Noturno", "alibi": "Fazendo ronda externa"},
                    {"nome": "Mariana Costa", "profissao": "Proprietária", "alibi": "Em viagem de negócios"},
                    {"nome": "Bruno Silva", "profissao": "Vendedor", "alibi": "Em casa com família"},
                    {"nome": "Daniela Oliveira", "profissao": "Funcionária", "alibi": "Trabalhando no turno da manhã"}
                ],
                "evidencias": [
                    "Alarme desarmado sem disparar",
                    "Impressão digital parcial na vitrine",
                    "Cópia da chave do cofre",
                    "Registro de chamada telefônica suspeita"
                ],
                "solucao": "Fernando Rocha"
            },
            {
                "title": "Assassinato na Fazenda",
                "description": "O fazendeiro é encontrado morto em seu escritório. Investigue o assassino.",
                "suspects": [
                    {"nome": "José Dias", "profissao": "Capataz", "alibi": "Cuidando do gado"},
                    {"nome": "Maria Aparecida", "profissao": "Cozinheira", "alibi": "Preparando o almoço"},
                    {"nome": "João Miguel", "profissao": "Filho do Fazendeiro", "alibi": "Na cidade"},
                    {"nome": "Pedro Oliveira", "profissao": "Vizinho", "alibi": "Em sua propriedade"}
                ],
                "evidencias": [
                    "Marca de bota próxima ao corpo",
                    "Carta de ameaça escondida",
                    "Arma do crime próxima à janela",
                    "Registro de ligação interurbana"
                ],
                "solucao": "João Miguel"
            },
            {
                "title": "O Mistério do Teatro",
                "description": "A estrela principal do espetáculo é encontrada desmaiada nos bastidores. O que aconteceu?",
                "suspects": [
                    {"nome": "Carlos Eduardo", "profissao": "Diretor", "alibi": "Na sala de produção"},
                    {"nome": "Juliana Santos", "profissao": "Atriz Secundária", "alibi": "Se preparando para o espetáculo"},
                    {"nome": "Ricardo Mendes", "profissao": "Técnico de Som", "alibi": "Ajustando equipamentos"},
                    {"nome": "Amanda Silveira", "profissao": "Maquiadora", "alibi": "No camarim"}
                ],
                "evidencias": [
                    "Frasco de água com substância estranha",
                    "Bilhete amassado no lixo",
                    "Maquiagem derramada no chão",
                    "Celular com mensagem de ameaça"
                ],
                "solucao": "Juliana Santos"
            },
            {
                "title": "Desaparecimento no Metrô",
                "description": "Uma passageira desaparece misteriosamente em uma estação movimentada. Encontre a verdade.",
                "suspects": [
                    {"nome": "Paulo Cesar", "profissao": "Segurança", "alibi": "Monitorando câmeras"},
                    {"nome": "Ana Luiza", "profissao": "Bilheteira", "alibi": "No guichê de atendimento"},
                    {"nome": "Roberto Santos", "profissao": "Motorista do Metrô", "alibi": "Conduzindo o trem"},
                    {"nome": "Marcia Oliveira", "profissao": "Faxineira", "alibi": "Limpando a plataforma"}
                ],
                "evidencias": [
                    "Câmera de segurança com problema técnico",
                    "Bolsa abandonada na plataforma",
                    "Rastro de sangue próximo à escada rolante",
                    "Bilhete de metrô rasgado"
                ],
                "solucao": "Paulo Cesar"
            },
            {
                "title": "O Enigma da Casa Noturna",
                "description": "Um cliente é encontrado inconsciente no banheiro. Descubra o que aconteceu.",
                "suspects": [
                    {"nome": "André Luiz", "profissao": "Barman", "alibi": "Preparando bebidas"},
                    {"nome": "Camila Rodrigues", "profissao": "Segurança", "alibi": "Controlando a entrada"},
                    {"nome": "Ricardo Almeida", "profissao": "DJ", "alibi": "No console de som"},
                    {"nome": "Fernanda Costa", "profissao": "Garçonete", "alibi": "Atendendo mesas"}
                ],
                "evidencias": [
                    "Copo com resto de bebida",
                    "Chave de quarto de motel",
                    "Marca de agressão no pescoço",
                    "Conversa de WhatsApp comprometedora"
                ],
                "solucao": "Camila Rodrigues"
            }
        ]
        self.pontuacao = 0

    def iniciar_jogo(self):
        print("Bem-vindo ao Clube de Detetives!")
        print("Você irá investigar 10 casos de mistério. Boa sorte, detetive!\n")
        
        casos_jogados = random.sample(self.cases, 10)
        
        for caso in casos_jogados:
            self.jogar_caso(caso)
        
        print(f"\nPontuação Final: {self.pontuacao}/10 casos resolvidos")
        self.gerar_certificado()

    def jogar_caso(self, caso):
        print(f"\n--- {caso['title']} ---")
        print(caso['description'])
        
        time.sleep(2)
        print("\n--- Evidências Encontradas ---")
        for i, evidencia in enumerate(caso['evidencias'], 1):
            print(f"{i}. {evidencia}")
        
        time.sleep(2)
        print("\n--- Suspeitos ---")
        for i, suspeito in enumerate(caso['suspects'], 1):
            print(f"{i}. {suspeito['nome']} - {suspeito['profissao']} (Álibi: {suspeito['alibi']})")
        
        while True:
            try:
                resposta = input("\nQuem você acredita ser o culpado? (Digite o nome completo): ")
                if resposta == caso['solucao']:
                    print("🎉 Parabéns! Você RESOLVEU o caso! 🕵️‍♀️")
                    self.pontuacao += 1
                else:
                    print(f"❌ Ops! O culpado era {caso['solucao']}. Continue investigando!")
                break
            except Exception as e:
                print("Entrada inválida. Tente novamente.")

    def gerar_certificado(self):
        print("\n--- CERTIFICADO DE DETETIVE ---")
        if self.pontuacao == 10:
            print("🏆 DETETIVE MÁSTER!")
        elif self.pontuacao >= 7:
            print("🥇 DETETIVE EXPERIENTE!")
        elif self.pontuacao >= 5:
            print("🥈 DETETIVE INTERMEDIÁRIO!")
        else:
            print("🔍 DETETIVE INICIANTE!")
        
        print(f"\nCasos Resolvidos: {self.pontuacao}/10")
        print("\nPARABÉNS PELA INVESTIGAÇÃO!")

def main():
    jogo = MysteryGame()
    jogo.iniciar_jogo()

if __name__ == "__main__":
    main()
