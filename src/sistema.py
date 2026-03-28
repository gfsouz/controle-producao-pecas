import os
import json
import datetime

# ==========================================
# 1. CONFIGURAÇÕES GLOBAIS (REGRAS DA FÁBRICA)
# ==========================================
PESO_MIN, PESO_MAX = 95.0, 105.0
CORES_PERMITIDAS = ["azul", "verde"]
COMP_MIN, COMP_MAX = 10.0, 20.0
CAPACIDADE_CAIXA = 10
ARQUIVO_DADOS = "dados_fabrica.json"

# Estruturas de dados em memória
pecas = []
caixas = []
relatorio = {
    "aprovadas": 0,
    "reprovadas_peso": 0,
    "reprovadas_cor": 0,
    "reprovadas_comp": 0,
    "total_caixas": 0
}

# ==========================================
# 2. FUNÇÕES DE PERSISTÊNCIA (SALVAR/CARREGAR)
# ==========================================
def carregar_dados():
    """Restaura os dados do arquivo JSON se ele existir."""
    global pecas, caixas, relatorio
    if not os.path.exists(ARQUIVO_DADOS):
        return
    try:
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            dados = json.load(f)
            pecas = dados.get("p", [])
            caixas = dados.get("c", [])
            relatorio = dados.get("r", relatorio)
    except Exception:
        print("Erro ao carregar dados. Iniciando do zero.")

def salvar_dados():
    """Grava o estado atual no arquivo JSON."""
    dados = {"p": pecas, "c": caixas, "r": relatorio}
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

# ==========================================
# 3. FUNÇÕES AUXILIARES DE ENTRADA
# ==========================================
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def pedir_numero(mensagem):
    """Solicita um número até que o usuário digite um valor válido."""
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("❌ Inválido! Digite apenas números.")

def pedir_cor():
    """
    Solicita a cor e aceita QUALQUER entrada.
    A validação (se é azul/verde ou não) será feita depois pela função validar_peca().
    Isso permite cadastrar peças de cor 'preto', 'amarelo', etc., e marcá-las como reprovadas.
    """
    cor = input("Cor (azul ou verde): ").strip().lower()
    return cor

# ==========================================
# 4. LÓGICA DE NEGÓCIO PRINCIPAL
# ==========================================
def validar_peca(peso, cor, comp):
    """Verifica se a peça atende aos critérios de qualidade."""
    # 1. Verifica Peso
    if not (PESO_MIN <= peso <= PESO_MAX):
        return False, "peso"
    
    # 2. Verifica Cor (Se não estiver na lista permitida, reprova)
    if cor not in CORES_PERMITIDAS:
        return False, "cor"
    
    # 3. Verifica Comprimento
    if not (COMP_MIN <= comp <= COMP_MAX):
        return False, "comprimento"
    
    return True, ""

def organizar_na_caixa(id_peca):
    """Adiciona a peça à caixa atual ou cria uma nova se estiver cheia."""
    if not caixas or len(caixas[-1]) >= CAPACIDADE_CAIXA:
        caixas.append([])
        relatorio["total_caixas"] += 1
    caixas[-1].append(id_peca)

def cadastrar_peca():
    """Fluxo completo de cadastro: entrada, validação e registro."""
    limpar_tela()
    print("📝 CADASTRAR NOVA PEÇA\n")
    
    id_peca = input("ID da peça: ").strip()
    if not id_peca:
        print("❌ ID não pode ser vazio.")
        input("\nEnter para continuar..."); return

    peso = pedir_numero("Peso (g): ")
    cor = pedir_cor()  # Agora aceita qualquer cor digitada
    comp = pedir_numero("Comprimento (cm): ")
    
    aprovada, motivo = validar_peca(peso, cor, comp)
    data_hora = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # Registro da peça com timestamp
    registro = {
        "id": id_peca, "peso": peso, "cor": cor, "comp": comp,
        "aprovada": aprovada, "motivo": motivo, "data": data_hora
    }
    pecas.append(registro)
    
    if aprovada:
        relatorio["aprovadas"] += 1
        organizar_na_caixa(id_peca)
        print(f"\n✅ Peça APROVADA! Registrada em {data_hora}")
    else:
        # Atualiza contador específico do erro
        if motivo == "peso": 
            relatorio["reprovadas_peso"] += 1
        elif motivo == "cor": 
            relatorio["reprovadas_cor"] += 1
        elif motivo == "comprimento": 
            relatorio["reprovadas_comp"] += 1
        
        print(f"\n❌ Peça REPROVADA! Motivo: {motivo.upper()}")
        if motivo == "cor":
            print(f"   (A cor '{cor}' não é permitida. Apenas azul ou verde são aceitos.)")
    
    input("\nEnter para continuar...")

def listar_pecas():
    """Exibe todas as peças separadas por status."""
    limpar_tela()
    print("📋 LISTAGEM DE PEÇAS\n")
    if not pecas:
        print("Nenhuma peça cadastrada.")
    else:
        print("🟢 APROVADAS:")
        for p in [x for x in pecas if x["aprovada"]]:
            print(f"  ID:{p['id']} | {p['peso']}g | {p['cor']} | {p['comp']}cm | {p['data']}")
        
        print("\n🔴 REPROVADAS:")
        for p in [x for x in pecas if not x["aprovada"]]:
            print(f"  ID:{p['id']} | Cor: {p['cor']} | Motivo: {p['motivo'].upper()} | {p['data']}")
    input("\nEnter para continuar...")

def remover_peca():
    """Remove uma peça e ajusta caixas/contadores consistentemente."""
    limpar_tela()
    print("🗑️ REMOVER PEÇA\n")
    id_busca = input("ID da peça: ").strip()
    
    for i, p in enumerate(pecas):
        if p["id"] == id_busca:
            if p["aprovada"]:
                relatorio["aprovadas"] -= 1
                # Remove da caixa correspondente
                for caixa in caixas:
                    if id_busca in caixa:
                        caixa.remove(id_busca)
                        if not caixa: # Se esvaziou, remove a caixa
                            caixas.remove(caixa)
                            relatorio["total_caixas"] -= 1
                        break
            else:
                # Decrementa contador do motivo específico
                if p["motivo"] == "peso": relatorio["reprovadas_peso"] -= 1
                elif p["motivo"] == "cor": relatorio["reprovadas_cor"] -= 1
                elif p["motivo"] == "comprimento": relatorio["reprovadas_comp"] -= 1
            
            pecas.pop(i)
            print("✅ Removido com sucesso!")
            input("\nEnter para continuar..."); return
    
    print("❌ Peça não encontrada.")
    input("\nEnter para continuar...")

def listar_caixas():
    """Mostra o conteúdo de cada caixa."""
    limpar_tela()
    print("📦 STATUS DAS CAIXAS\n")
    if not caixas:
        print("Nenhuma caixa utilizada.")
    else:
        for idx, c in enumerate(caixas, 1):
            conteudo = ", ".join(c) if c else "Vazia"
            print(f"Caixa {idx}: [{len(c)}/{CAPACIDADE_CAIXA}] -> {conteudo}")
    input("\nEnter para continuar...")

def gerar_relatorio():
    """Exibe métricas consolidadas da produção."""
    limpar_tela()
    print("📊 RELATÓRIO GERENCIAL\n")
    total_rep = (relatorio["reprovadas_peso"] + relatorio["reprovadas_cor"] + 
                 relatorio["reprovadas_comp"])
    print(f"Aprovadas:           {relatorio['aprovadas']}")
    print(f"Reprovadas (Total):  {total_rep}")
    print(f"  - Peso:            {relatorio['reprovadas_peso']}")
    print(f"  - Cor:             {relatorio['reprovadas_cor']}")
    print(f"  - Comprimento:     {relatorio['reprovadas_comp']}")
    print(f"Caixas Utilizadas:   {relatorio['total_caixas']}")
    input("\nEnter para continuar...")

# ==========================================
# 5. MENU PRINCIPAL
# ==========================================
def menu():
    carregar_dados()
    while True:
        limpar_tela()
        print("🏭 GESTÃO INDUSTRIAL")
        print("1.📝 Cadastrar Peça")
        print("2.📋 Listar Peças")
        print("3.🗑️  Remover Peça")
        print("4.📦 Listar Caixas")
        print("5.📊 Relatório Final")
        print("6.🚪 Salvar e Sair")
        
        op = input("\nOpção: ").strip()
        
        if op == '1': cadastrar_peca()
        elif op == '2': listar_pecas()
        elif op == '3': remover_peca()
        elif op == '4': listar_caixas()
        elif op == '5': gerar_relatorio()
        elif op == '6':
            salvar_dados()
            print("Dados salvos. Até logo!")
            break
        else:
            print("❌ Opção inválida.")
            input("Enter para continuar...")

if __name__ == "__main__":
    menu()