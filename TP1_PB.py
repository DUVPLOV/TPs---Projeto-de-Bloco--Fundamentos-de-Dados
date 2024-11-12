from datetime import date, datetime
lista_de_tarefas = []
lista_de_tarefas_concluidas = []
lista_de_tarefas_pendentes = []
lista_do_historico_dos_status=[]

class Tarefa:
  _id = 1
  def __init__(self, nome, descricao, prioridade, data_inicial, data_limite):
    """
      Inicializa uma nova tarefa com os atributos fornecidos, incluindo nome, descrição,
      prioridade, data inicial e data limite. Cada tarefa recebe um ID único e o status
      inicial é definido como uma string vazia.

      Args:
          nome (str): Nome da tarefa.
          descricao (str): Descrição da tarefa.
          prioridade (int): Prioridade da tarefa (1-5).
          data_inicial (str): Data de início da tarefa no formato "DD/MM/AAAA".
          data_limite (str): Data de término da tarefa no formato "DD/MM/AAAA".
      """

    self.id=Tarefa._id
    Tarefa._id +=1
    self.nome = nome
    self.data_inicial = data_inicial
    self.descricao = descricao
    self.prioridade = prioridade
    self.data_limite = data_limite
    self.status = ""
  def salvar_tarefa(self):
    """
      Salva a instância da tarefa na lista global de tarefas (`lista_de_tarefas`).
    """

    lista_de_tarefas.append(self)
  def alterar_status(self,novo_status):
    """
      Altera o status da tarefa para o novo status fornecido.

      Args:
          novo_status (str): Novo status a ser atribuído à tarefa.
    """

    self.status = novo_status

class HistoricoDeStatus:
    _id = 1
    def __init__(self, id_tarefa, status_atual, status_anterior, data):
      """
        Inicializa um novo registro de histórico de status para uma tarefa específica.
        Cada registro inclui o ID da tarefa, o status atual, o status anterior e a data da alteração.

        Args:
            id_tarefa (int): ID da tarefa associada ao histórico.
            status_atual (str): Status atual da tarefa.
            status_anterior (str): Status anterior da tarefa.
            data (date): Data da alteração de status.
       """

      self.id=HistoricoDeStatus._id
      HistoricoDeStatus._id +=1
      self.id_tarefa = id_tarefa
      self.status_atual = status_atual
      self.status_anterior = status_anterior
      self.data = data

    def salvar_status(self):
       """
        Salva a instância do histórico de status na lista global `lista_do_historico_dos_status`.
       """

       lista_do_historico_dos_status.append(self)

def solicitar_nome():
    """
      Solicita e valida o nome da tarefa, permitindo apenas letras e números com
      um mínimo de 3 caracteres. Continua pedindo a entrada até um nome válido ser fornecido.

      Returns:
          str: Nome válido inserido pelo usuário.
    """

    while True:
        nome = input("Digite o nome (letras e números permitidos, mínimo de 3 caracteres): ").strip()
        
        if nome.isalnum() and len(nome) >= 3:
            return nome
        else:
            print("Nome inválido! Por favor, insira um nome com letras e números e com no mínimo 3 caracteres.")

def solicitar_descricao():
    """
      Solicita e valida a descrição da tarefa, que deve ter entre 1 e 200 caracteres.
      Continua pedindo a entrada até uma descrição válida ser fornecida.

      Returns:
          str: Descrição válida inserida pelo usuário.
    """

    while True:
        descricao = input("Digite a descrição (máximo de 200 caracteres): ").strip()
        if 0 < len(descricao) <= 200:
            return descricao
        else:
            print("Descrição inválida! Deve ter entre 1 e 200 caracteres.")

def solicitar_prioridade():
    """
      Solicita e valida a prioridade da tarefa, que deve ser um número inteiro entre 1 e 5.
      Continua pedindo a entrada até que uma prioridade válida seja fornecida.

      Returns:
          int: Prioridade válida inserida pelo usuário.
    """

    while True:
        try:
            prioridade = int(input("Digite a prioridade (1 a 5): ").strip())
            if 1 <= prioridade <= 5:
                return prioridade
            else:
                print("Prioridade inválida! Deve ser um número entre 1 e 5.")
        except ValueError:
            print("Entrada inválida! Por favor, insira um número entre 1 e 5.")

def verificar_data(dia, mes, ano):
    """
    Verifica se a data fornecida é válida.
    
    Args:
        dia (int): O dia da data.
        mes (int): O mês da data.
        ano (int): O ano da data.
    
    Returns:
        bool: True se a data for válida, False caso contrário.
    """
    if ano < 1:
        return False
    if mes < 1 or mes > 12:
        return False
    dias_por_mes = {
        1: 31, 2: 29 if (ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)) else 28,
        3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31,
        11: 30, 12: 31
    }
    
    if dia < 1 or dia > dias_por_mes[mes]:
        return False
    
    return True

def solicitar_data_usuario(msg):
    """
    Solicita uma data ao usuário e valida manualmente cada parte.
    
    Returns:
        str: A data válida inserida pelo usuário no formato DD/MM/AAAA.
    """
    while True:
        data_entrada = input(f"{msg} no formato DD/MM/AAAA: ")
        try:
            dia, mes, ano = map(int, data_entrada.split("/"))
            if verificar_data(dia, mes, ano):
                return f"{dia:02}/{mes:02}/{ano}"
            else:
                print("Data inválida! Tente novamente.")
        except ValueError:
            print("Formato incorreto! Por favor, use o formato DD/MM/AAAA.")

def adicionar_dados():
    """
    Função principal que solicita nome, descrição, prioridade, data inicial e data final.
    
    Returns:
        dict: Dicionário contendo os dados válidos inseridos pelo usuário.
    """
    dados = {
        "nome": solicitar_nome(),
        "descricao": solicitar_descricao(),
        "prioridade": solicitar_prioridade(),
        "data_inicial" : solicitar_data_usuario("Digite a data inicial"),
        "data_limite" : solicitar_data_usuario("Digite a data final")
    }
    return dados

def listar_tarefas(tabela):
  """
    Lista todas as tarefas contidas na tabela fornecida.

    Args:
        tabela (list): Lista de tarefas a serem exibidas.
  """

  for tarefa in tabela:
    print(
      f"\nID: {tarefa.id}\n"
      f"Tarefa: {tarefa.nome}\n"
      f"Descrição: {tarefa.descricao}\n"
      f"Prioridade: {tarefa.prioridade}\n"
      f"Data Inicial: {tarefa.data_inicial}\n"
      f"Data Limite: {tarefa.data_limite}\n"
      f"Status: {tarefa.status}\n"
    )

def listar_historico_de_status():
  """
    Exibe o histórico de status de todas as tarefas contidas em `lista_do_historico_dos_status`.
  """

  for registro in lista_do_historico_dos_status:
    print(
      f"\nID: {registro.id}\n"
      f"Tarefa ID: {registro.id_tarefa}\n"
      f"Status Anterior: {registro.status_anterior}\n"
      f"Status Atual: {registro.status_atual}\n"
      f"Data: {registro.data}\n"
    )

def criar_tarefa():
    """
    Cria uma nova tarefa após validação dos dados e das datas, atualizando o status e o histórico da tarefa.
    
    Returns:
        Tarefa: A tarefa criada, se bem-sucedida; caso contrário, retorna None.
    """
    try:
        dados = adicionar_dados()
        
        data_inicial = datetime.strptime(dados["data_inicial"], "%d/%m/%Y")
        data_limite = datetime.strptime(dados["data_limite"], "%d/%m/%Y")
        
        if data_limite < data_inicial:
            print(f"Erro: A data limite {dados['data_limite']} é anterior à data inicial {dados['data_inicial']}.")
            return None
        
        nova_tarefa = Tarefa(
            dados["nome"], 
            dados["descricao"], 
            dados["prioridade"], 
            dados["data_inicial"], 
            dados["data_limite"]
        )
        
        nova_tarefa.alterar_status("Tarefa Criada")
        data_atual = date.today()
        
        historico_status = HistoricoDeStatus(
            nova_tarefa.id, 
            nova_tarefa.status, 
            "", 
            data=data_atual
        )
        
        historico_status.salvar_status()
        
    except ValueError as ve:
        print(f"Erro ao processar as datas: {ve}")
        return None
    except Exception as e:
        print(f"Não foi possível criar a tarefa devido a um erro: {e}")
        return None
    else:
        nova_tarefa.salvar_tarefa()
        print("Tarefa criada com sucesso!")
        return nova_tarefa

def excluir_tarefa(id_tarefa, tabela):
  """
    Exclui uma tarefa da tabela fornecida com base em seu ID.

    Args:
        id_tarefa (int): ID da tarefa a ser excluída.
        tabela (list): Lista de onde a tarefa será removida.
  """

  tarefa = pesquisar_tarefa(id_tarefa,tabela)
  if(tarefa):
    try:
      indice = tarefa["índice"]
      del tarefa["tabela"][indice]
    except:
      print("Não foi possível excluir a tarefa.")
    else:
      print("Tarefa deletada com sucesso!")
  else:
    print(f"Não existe nenhuma tarefa com o ID {id_tarefa}")

def atualizar_historico_status(tarefa, novo_status):
    """
      Atualiza o histórico de status de uma tarefa, armazenando o status anterior e
      o status atual junto com a data da alteração.

      Args:
          tarefa (Tarefa): Instância da tarefa a ser atualizada.
          novo_status (str): Novo status a ser atribuído à tarefa.
    """

    status_anterior = tarefa.status
    tarefa.status = novo_status
    data_atual = date.today()
    historico_status = HistoricoDeStatus(tarefa.id,tarefa.status,status_anterior,data_atual)
    historico_status.salvar_status()

def trocar_tarefa_de_tabela(tarefa,tabela_atual,nova_tabela):
  """
    Move uma tarefa de uma tabela (lista) para outra, excluindo-a da tabela atual.

    Args:
        tarefa (Tarefa): Instância da tarefa a ser movida.
        tabela_atual (list): Lista de onde a tarefa será removida.
        nova_tabela (list): Lista para onde a tarefa será adicionada.
  """

  nova_tabela.append(tarefa)
  excluir_tarefa(tarefa.id,tabela_atual)

def pesquisar_tarefa(id_tarefa,tabela):
  """
    Pesquisa uma tarefa pelo ID na tabela fornecida, retornando um dicionário com
    a tarefa e sua posição.

    Args:
        id_tarefa (int): ID da tarefa a ser pesquisada.
        tabela (list): Lista onde a tarefa será pesquisada.

    Returns:
        dict: Dicionário com a tarefa e sua posição, ou False se não for encontrada.
  """

  for tarefa in tabela:
    if(tarefa.id == id_tarefa):
      indice = tabela.index(tarefa)
      return{
        "índice": indice,
        "id_tarefa":id_tarefa,
        "tabela": tabela,
        "tarefa":tarefa
      }
    else:
      print(f"Tarefa com ID {id_tarefa} não encontrada.")
      return False

def concluir_tarefa(id_tarefa):
  """
    Conclui uma tarefa, movendo-a da lista de tarefas pendentes para a lista de tarefas
    concluídas e atualizando seu histórico de status.

    Args:
        id_tarefa (int): ID da tarefa a ser concluída.
  """

  tarefa = pesquisar_tarefa(id_tarefa,lista_de_tarefas_pendentes)
  if(tarefa):
    try: 
      atualizar_historico_status(tarefa["tarefa"],"Concluída")
      trocar_tarefa_de_tabela(tarefa["tarefa"],lista_de_tarefas_pendentes,lista_de_tarefas_concluidas)
    except:
      print("Não foi possível alterar a tarefa para concluída")
    else:
      print("Tarefa adicionada a lista de tarefas concluídas.")
  else:
    print(f"Não existe nenhuma tarefa pendente com o ID {id_tarefa}")

def fazer_tarefa(id_tarefa):
  """
    Marca uma tarefa como "Em andamento", movendo-a da lista de tarefas abertas para a lista
    de tarefas pendentes e atualizando seu histórico de status.

    Args:
        id_tarefa (int): ID da tarefa a ser movida para "Em andamento".
  """

  tarefa = pesquisar_tarefa(id_tarefa,lista_de_tarefas)
  if(tarefa):
      try: 
        atualizar_historico_status(tarefa["tarefa"],"Em andamento")
        trocar_tarefa_de_tabela(tarefa["tarefa"],lista_de_tarefas,lista_de_tarefas_pendentes)
      except:
        print("Não foi possível alterar a tarefa para pendente")
      else:
        print("Tarefa adicionada a lista de tarefas pendentes.")
  else:
    print(f"Não existe nenhuma tarefa em aberto com o ID {id_tarefa}")

def menu_edit():
   """
    Exibe o menu de edição das tarefas, permitindo ao usuário selecionar um atributo
    para editar.

    Returns:
        str: O nome do atributo selecionado pelo usuário para edição, ou "sair" para encerrar.
    """

   print("-----Menu de Edição-----")
   print("[0] - Nome")
   print("[1] - Descricão")
   print("[2] - Prioridade")
   print("[3] - Data inicial")
   print("[4] - Data final")
   print("[5] - Sair")
   try:
    opcao = int(input("Digite o número correspondente a opção desejada: "))
   except:
      print("Erro: digite um número correspondente a uma das opções!")
      return None
   match opcao:
      case 0:
         return "nome"
      case 1:
         return "descricao"
      case 2:
         return "prioridade"
      case 3:
         return "data_inicial"
      case 4:
         return "data_limite"
      case 5:
         return "sair"
      case _:
         return "Opção inválida"
      
def editar_tarefa(id_tarefa, tabela):
    """
      Edita um atributo específico de uma tarefa na tabela fornecida com base no ID
      e na opção de edição selecionada pelo usuário.

      Args:
          id_tarefa (int): ID da tarefa a ser editada.
          tabela (list): Lista onde a tarefa está armazenada.
    """

    while True:
        opcao_edit = menu_edit()
        
        if opcao_edit == "sair":
            print("Edição encerrada.")
            break
        
        if opcao_edit == "Opção inválida" or opcao_edit is None:
            print("Opção inválida. Tente novamente.")
            continue 
        
        tarefa = pesquisar_tarefa(id_tarefa, tabela)
        
        if not tarefa:
            print("Tarefa não encontrada.")
            return
        
        match opcao_edit:
            case "nome":
                novo_valor = solicitar_nome()
            case "descricao":
                novo_valor = solicitar_descricao()
            case "prioridade":
                novo_valor = solicitar_prioridade()
            case "data_inicial":
                novo_valor = solicitar_data_usuario("Digite a nova data inicial")
            case "data_limite":
                novo_valor = solicitar_data_usuario("Digite a nova data final")
            case _:
                print("Opção inválida.")
                continue

        setattr(tarefa["tarefa"], opcao_edit, novo_valor)
        print(f"{opcao_edit.capitalize()} atualizado com sucesso!")


# nova_tarefa = criar_tarefa()
# fazer_tarefa(1)
# listar_tarefas(lista_de_tarefas_pendentes)
# listar_historico_de_status()
# editar_tarefa(1,lista_de_tarefas_pendentes)
# concluir_tarefa(1)
# excluir_tarefa(1,lista_de_tarefas_concluidas)
