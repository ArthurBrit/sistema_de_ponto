from database import BancoDeDados
from repositories import RepositorioFuncionario, RepositorioPonto


class SistemaPonto:
    def __init__(self):
        self.banco = BancoDeDados()
        self.funcionarios = RepositorioFuncionario(self.banco)
        self.pontos = RepositorioPonto(self.banco)

    def ler_texto(self, mensagem):
        while True:
            valor = input(mensagem).strip()

            if valor:
                return valor

            print("Digite um valor válido.")

    def registrar_chegada(self):
        print("\n--- Registrar chegada ---")

        matricula = self.ler_texto("Matrícula/ID do funcionário: ")
        funcionario = self.funcionarios.buscar_por_matricula(matricula)

        if funcionario is None:
            print("Funcionário não encontrado.")
            resposta = input("Deseja cadastrar agora? [s/n]: ").strip().lower()

            if resposta != "s":
                return

            nome = self.ler_texto("Nome do funcionário: ")
            self.funcionarios.cadastrar(matricula, nome)
            funcionario = self.funcionarios.buscar_por_matricula(matricula)

        registro_aberto = self.pontos.buscar_registro_aberto(funcionario.id)

        if registro_aberto:
            print("Este funcionário já possui uma chegada sem saída registrada.")
            return

        self.pontos.registrar_chegada(funcionario.id)

        print(f"Chegada registrada para {funcionario.nome}.")

    def registrar_saida(self):
        print("\n--- Registrar saída ---")

        matricula = self.ler_texto("Matrícula/ID do funcionário: ")
        funcionario = self.funcionarios.buscar_por_matricula(matricula)

        if funcionario is None:
            print("Funcionário não encontrado.")
            return

        registro_aberto = self.pontos.buscar_registro_aberto(funcionario.id)

        if registro_aberto is None:
            print("Nenhuma chegada aberta encontrada para esta matrícula.")
            return

        self.pontos.registrar_saida(registro_aberto.id)

        print(f"Saída registrada para {funcionario.nome}.")

    def listar_registros(self):
        print("\n--- Registros ---")

        registros = self.pontos.listar_todos()

        if not registros:
            print("Nenhum registro encontrado.")
            return

        for registro in registros:
            id_registro, nome, matricula, chegada, saida = registro
            saida_formatada = saida if saida else "Em aberto"

            print(
                f"{id_registro}. {nome} "
                f"(ID: {matricula}) | "
                f"Chegada: {chegada} | "
                f"Saída: {saida_formatada}"
            )

    def listar_presentes(self):
        print("\n--- Funcionários presentes ---")

        presentes = self.pontos.listar_presentes()

        if not presentes:
            print("Nenhum funcionário está com presença em aberto.")
            return

        for presente in presentes:
            id_registro, nome, matricula, chegada = presente

            print(
                f"{id_registro}. {nome} " f"(ID: {matricula}) | " f"Chegada: {chegada}"
            )

    def exibir_menu(self):
        print("\n===== Controle de chegada e saída =====")
        print("1 - Registrar chegada")
        print("2 - Registrar saída")
        print("3 - Listar todos os registros")
        print("4 - Listar funcionários presentes")
        print("0 - Sair")

        return input("Escolha uma opção: ").strip()

    def executar(self):
        while True:
            opcao = self.exibir_menu()

            if opcao == "1":
                self.registrar_chegada()
            elif opcao == "2":
                self.registrar_saida()
            elif opcao == "3":
                self.listar_registros()
            elif opcao == "4":
                self.listar_presentes()
            elif opcao == "0":
                print("Encerrando o sistema.")
                self.banco.fechar()
                break
            else:
                print("Opção inválida. Tente novamente.")
