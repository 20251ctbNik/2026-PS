'''
==================================================
# ARQUIVO   : pet.py
# Diciplina : Programação de Sistemas
# Aula      : Aula 20 - Por que POO?
# Auotor    : Nickolas Kinceski Martins
# Conceitos : Classe, objeto, atributos, métodos, encapsulamento
# Atividade : Classe Pet
==================================================
'''

class Pet:
    '''
    Esta classe representa um Pet em um sistema simples de hotel para 
    pets.

    Em vez de guardar os dados do pet em um dicionário solto, como
    fazíamos
    na programação estruturada, agora agrupamos os dados e comportamentos
    dentro de uma classe.
    '''

    def __init__(self, nome, especie, idade, raca, vacinado, observacoes, nome_dono, telefone_dono, peso):
        '''
        Método construtor

        Ele é executado automaticamente quando criamos um novo objeto
        Pet.

        Exemplo:
        pet1 = Pet("Rex", "Cachorro", 5, "SRD", True, "Sem observações", "João", "123456789", 10.0)

        Parâmetros:
        - nome: nome do pet
        - especie: espécie do pet
        - idade: idade do pet
        - raca: raça do pet
        - vacinado: booleano indicando se está vacinado
        - observacoes: observações sobre o pet
        - nome_dono: nome do responsável pelo pet
        - telefone_dono: telefone do dono
        - peso: peso do pet em kg
        '''

        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.raca = raca
        self.peso = peso
        self.nome_dono = nome_dono
        self.telefone_dono = telefone_dono
        self.hospedado = False
        self.vacinado = vacinado
        self.observacoes = observacoes

        # ===========================================
        # ATIVIDADE 1:
        # adicione pelo menos 3 novos atributos para o pet.
        #
        # Esta implementação inclui: raca, peso, nome_dono,
        # telefone_dono, vacinado e observacoes.
        # ===========================================

    def exibir_dados(self):
        '''
        Exibe os dafos principaisd do pet.

        Atualmente, mostra apenas o nome, espécie, idade e status de 
        hospedagem.

        ATIVIDADE:
        Modifique este métodod para exibir também os novos atributos
        que você adicionou no __init__.
        '''

        print("\n=== Dados do Pet ===")
        print(f"Nome: {self.nome}")
        print(f"Espécie: {self.especie}")
        print(f"Idade: {self.idade} anos")
        print(f"Raça: {self.raca}")
        print(f"Peso: {self.peso if self.peso is not None else 'Não informado'}")
        print(f"Nome do dono: {self.nome_dono or 'Não informado'}")
        print(f"Telefone do dono: {self.telefone_dono or 'Não informado'}")
        print(f"Vacinado: {'Sim' if self.vacinado else 'Não'}")
        print(f"Observações: {self.observacoes}")
        print(f"Hospedado: {'Sim' if self.hospedado else 'Não'}")

    def registrar_entrada(self):
        '''
        Registra a entrada do pet no hotel.
        
        Se o pet ainda não estiver hospedado, muda o atributo hospedado
        para True.

        ATIVIDADE:
        Melhore este método para verificar se o pet já está hospedado.
        Se já estiver, mostre uma mensage avisando.
        '''

        if not self.hospedado:
            self.hospedado = True
            print(f"{self.nome} entrou no hotel.")
        else:
            print(f"{self.nome} já está hospedado.")

    def registrar_saida(self):
        '''
        Registra a saída do pet do hotel.

        Se o pet estiver hospedado, muda o atributo hospedado para False.

        ATIVIDADE:
        Melhore este método para verificar se o pet já está hospedado.
        Se não estiver, mostre uma mensage avisando.
        '''

        if self.hospedado:
            self.hospedado = False
            print(f"{self.nome} saiu do hotel.")
        else:
            print(f"{self.nome} não está hospedado.")

    def calcular_diaria(self):

        if self.idade <= 3:
            return 50.00
        elif 4 <= self.idade <= 10:
            return 60.00
        elif self.idade > 30:
            return ("Pet velho demais para ser real.")
        else:
            return 75.00

    def verificar_vacinacao(self):
        '''
        Verifica se o pet está vacinado.

        ATIVIDADE:
        Para este método funcionar, você precisa criar um atributo
        chamado self.vacinado no __init__.

        Se o pet estiver vacinado, exiba:
        "Vacinação em dia."

        Caso contrário, exiba:
        "Atenção: vacinação pendente."
        '''

        if self.vacinado:
            print("Vacinação em dia.")
        else:
            print("Atenção: vacinação pendente.")

    def adicionar_observacao(self, nova_observacao):
        if self.observacoes:
            self.observacoes += f" | {nova_observacao}"
        else:
            self.observacoes = nova_observacao
        print("Observação adicionada.")

    def atualizar_peso(self, novo_peso):
        self.peso = novo_peso
        print(f"Peso atualizado para {self.peso} kg.")

    def emitir_resumo(self):
        '''
        Exibe um resumo geral do pet.
        
        ATIVIDADE:
        Cre uma mensagem organizada contendo:
        - nome do pet
        - espécie
        - idade
        - nome do dono
        - peso
        - status de vacinação
        - status hospedagem
        - valor da diária

        Este método deve usar informaçoes dos atributps e também pode
        chamar outros métodos, como calcular_diaria().
        '''
        resumo = f"Resumo do Pet:\n"
        resumo += f"Nome: {self.nome}\n"
        resumo += f"Espécie: {self.especie}\n"
        resumo += f"Idade: {self.idade} anos\n"
        resumo += f"Nome do dono: {self.nome_dono or 'Não informado'}\n"
        resumo += f"Peso: {self.peso if self.peso is not None else 'Não informado'}\n"
        resumo += f"Raça: {self.raca}\n"
        resumo += f"Vacinado: {'Sim' if self.vacinado else 'Não'}\n"
        resumo += f"Hospedado: {'Sim' if self.hospedado else 'Não'}\n"
        resumo += f"Valor da diária: R$ {self.calcular_diaria():.2f}\n"
        print(resumo)

'''
# =================================
# TESTE DA CLASSE
# =================================
# Deposi de completar a classe, crie pelo menos 3 objetos Pet.
#
# Exemplo:
# pet1 = Pet("Rex", "Cachorro", 5)
#
# Atenção:
# Se você adicionou novo parâmetros no __init__, será necessário
# informar esses dados na criação do objeto.
# =================================
'''

pet1 = Pet("Rex", "Cachorro", 5, "SRD", True, "Sem observações", "João", "123456789", 10.0)
# Meus pets
pet2 = Pet("Dia", "Cachorro", 14, "Pastor Alemão", False, "Sem observações.", "Nickolas", "987654321", 30.0)
pet3 = Pet("Lila", "Gato", 5, "Siamês", True, "Sem observações.", "Nickolas", "555555555", 5.0)

pet1.exibir_dados()
pet1.registrar_entrada()
pet1.verificar_vacinacao()
pet1.calcular_diaria()
pet1.emitir_resumo()

pet2.exibir_dados()
pet2.registrar_entrada()
pet2.verificar_vacinacao()
pet2.calcular_diaria()
pet2.emitir_resumo()

pet3.exibir_dados()
pet3.registrar_entrada()
pet3.verificar_vacinacao()
pet3.calcular_diaria()
pet3.emitir_resumo()