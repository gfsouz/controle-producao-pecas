# 🏭 Sistema de Gestão Industrial de Peças

Sistema de controle de qualidade para peças industriais desenvolvido em Python puro, sem dependências externas. O sistema valida componentes por peso, cor e comprimento, distribui as peças aprovadas em caixas com capacidade definida e emite relatórios com os resultados por categoria. Todos os dados ficam salvos em arquivo JSON e são restaurados automaticamente na próxima execução.

---

## 📁 Estrutura do Projeto

```
GESTAO-INDUSTRIAL/
├── docs/
│   └── Análise e Discussão.pdf
├── src/
│   ├── sistema.py
│   └── dados_fabrica.json
└── README.md
```

---

## ⚙️ Critérios de Aprovação

| Atributo    | Valor aceito             |
|-------------|--------------------------|
| Peso        | Entre 95g e 105g         |
| Cor         | `azul` ou `verde`        |
| Comprimento | Entre 10cm e 20cm        |
| Caixa       | Máximo 10 peças por caixa |

A validação é sequencial: **peso → cor → comprimento**. A primeira falha encerra a checagem e define o motivo de rejeição da peça.

---

## 🚀 Como Executar

**Requisito:** Python 3.8 ou superior. Nenhuma biblioteca externa necessária.

```bash
# 1. Entre na pasta do projeto
cd GESTAO-INDUSTRIAL/src

# 2. Execute o programa
python sistema.py
```

> O arquivo `dados_fabrica.json` é criado automaticamente na primeira execução. Para salvar os dados, use sempre a **Opção 6 – Salvar e Sair**. Fechar o terminal sem salvar descarta as alterações da sessão.

---

## 🖥️ Menu Principal

```
🏭 GESTÃO INDUSTRIAL
1.📝 Cadastrar Peça
2.📋 Listar Peças
3.🗑️  Remover Peça
4.📦 Listar Caixas
5.📊 Relatório Final
6.🚪 Salvar e Sair

Opção:
```

---

## 📌 Exemplos de Uso

Todos os exemplos correspondem exatamente aos dados do `dados_fabrica.json`.

---

### ✅ P001 — Aprovada

**Entrada:**
```
ID da peça: P001
Peso (g): 100.0
Cor (azul ou verde): azul
Comprimento (cm): 15.0
```
**Saída:**
```
✅ Peça APROVADA! Registrada em 27/03/2026 19:53:18
```

---

### ✅ P002 — Aprovada

**Entrada:**
```
ID da peça: P002
Peso (g): 98.0
Cor (azul ou verde): verde
Comprimento (cm): 12.0
```
**Saída:**
```
✅ Peça APROVADA! Registrada em 27/03/2026 19:53:53
```

---

### ✅ P003 — Aprovada

**Entrada:**
```
ID da peça: P003
Peso (g): 102.0
Cor (azul ou verde): azul
Comprimento (cm): 18.0
```
**Saída:**
```
✅ Peça APROVADA! Registrada em 27/03/2026 19:54:25
```

---

### ✅ P004 — Aprovada

**Entrada:**
```
ID da peça: P004
Peso (g): 96.0
Cor (azul ou verde): verde
Comprimento (cm): 14.0
```
**Saída:**
```
✅ Peça APROVADA! Registrada em 27/03/2026 20:20:10
```

---

### ✅ P005 — Aprovada

**Entrada:**
```
ID da peça: P005
Peso (g): 104.0
Cor (azul ou verde): verde
Comprimento (cm): 19.0
```
**Saída:**
```
✅ Peça APROVADA! Registrada em 27/03/2026 20:20:38
```

---

### ✅ P006 — Aprovada

**Entrada:**
```
ID da peça: P006
Peso (g): 99.0
Cor (azul ou verde): azul
Comprimento (cm): 11.0
```
**Saída:**
```
✅ Peça APROVADA! Registrada em 27/03/2026 20:21:07
```

---

### ✅ P007 — Aprovada

**Entrada:**
```
ID da peça: P007
Peso (g): 101.0
Cor (azul ou verde): azul
Comprimento (cm): 17.0
```
**Saída:**
```
✅ Peça APROVADA! Registrada em 27/03/2026 20:21:29
```

---

### ❌ P011 — Reprovada (cor)

**Entrada:**
```
ID da peça: P011
Peso (g): 100.0
Cor (azul ou verde): rosa
Comprimento (cm): 15.0
```
**Saída:**
```
❌ Peça REPROVADA! Motivo: COR
   (A cor 'rosa' não é permitida. Apenas azul ou verde são aceitos.)
```

---

### ❌ P012 — Reprovada (peso)

**Entrada:**
```
ID da peça: P012
Peso (g): 110.0
Cor (azul ou verde): verde
Comprimento (cm): 15.0
```
**Saída:**
```
❌ Peça REPROVADA! Motivo: PESO
```

---

### ❌ P013 — Reprovada (comprimento)

**Entrada:**
```
ID da peça: P013
Peso (g): 100.0
Cor (azul ou verde): verde
Comprimento (cm): 25.0
```
**Saída:**
```
❌ Peça REPROVADA! Motivo: COMPRIMENTO
```

---

### ✅ P008 — Aprovada

**Entrada:**
```
ID da peça: P008
Peso (g): 97.0
Cor (azul ou verde): azul
Comprimento (cm): 13.0
```
**Saída:**
```
✅ Peça APROVADA! Registrada em 27/03/2026 20:24:42
```

---

### ✅ P09 — Aprovada

**Entrada:**
```
ID da peça: P09
Peso (g): 103.0
Cor (azul ou verde): verde
Comprimento (cm): 17.0
```
**Saída:**
```
✅ Peça APROVADA! Registrada em 27/03/2026 20:26:03
```

---

### ✅ p10 — Aprovada

**Entrada:**
```
ID da peça: p10
Peso (g): 104.0
Cor (azul ou verde): verde
Comprimento (cm): 15.0
```
**Saída:**
```
✅ Peça APROVADA! Registrada em 27/03/2026 20:27:45
```

---

### 📋 Listagem de peças (Opção 2)

```
📋 LISTAGEM DE PEÇAS

🟢 APROVADAS:
  ID:P001 | 100.0g | azul  | 15.0cm | 27/03/2026 19:53:18
  ID:P002 | 98.0g  | verde | 12.0cm | 27/03/2026 19:53:53
  ID:P003 | 102.0g | azul  | 18.0cm | 27/03/2026 19:54:25
  ID:P004 | 96.0g  | verde | 14.0cm | 27/03/2026 20:20:10
  ID:P005 | 104.0g | verde | 19.0cm | 27/03/2026 20:20:38
  ID:P006 | 99.0g  | azul  | 11.0cm | 27/03/2026 20:21:07
  ID:P007 | 101.0g | azul  | 17.0cm | 27/03/2026 20:21:29
  ID:P008 | 97.0g  | azul  | 13.0cm | 27/03/2026 20:24:42
  ID:P09  | 103.0g | verde | 17.0cm | 27/03/2026 20:26:03
  ID:p10  | 104.0g | verde | 15.0cm | 27/03/2026 20:27:45

🔴 REPROVADAS:
  ID:P011 | Cor: rosa  | Motivo: COR         | 27/03/2026 20:22:48
  ID:P012 | Cor: verde | Motivo: PESO        | 27/03/2026 20:23:12
  ID:P013 | Cor: verde | Motivo: COMPRIMENTO | 27/03/2026 20:23:41
```

---

### 📦 Status das caixas (Opção 4)

```
📦 STATUS DAS CAIXAS

Caixa 1: [10/10] -> P001, P002, P003, P004, P005, P006, P007, P008, P09, p10
```

Uma nova caixa é criada automaticamente ao atingir 10 peças.

---

### 📊 Relatório gerencial (Opção 5)

```
📊 RELATÓRIO GERENCIAL

Aprovadas:           10
Reprovadas (Total):  3
  - Peso:            1
  - Cor:             1
  - Comprimento:     1
Caixas Utilizadas:   1
```

---

## 💾 Arquivo de Dados

Os dados ficam salvos em `dados_fabrica.json`. O conteúdo abaixo é o resultado real da sessão de testes com 13 peças.

```json
{
    "p": [
        {
            "id": "P001",
            "peso": 100.0,
            "cor": "azul",
            "comp": 15.0,
            "aprovada": true,
            "motivo": "",
            "data": "27/03/2026 19:53:18"
        },
        {
            "id": "P002",
            "peso": 98.0,
            "cor": "verde",
            "comp": 12.0,
            "aprovada": true,
            "motivo": "",
            "data": "27/03/2026 19:53:53"
        },
        {
            "id": "P003",
            "peso": 102.0,
            "cor": "azul",
            "comp": 18.0,
            "aprovada": true,
            "motivo": "",
            "data": "27/03/2026 19:54:25"
        },
        {
            "id": "P004",
            "peso": 96.0,
            "cor": "verde",
            "comp": 14.0,
            "aprovada": true,
            "motivo": "",
            "data": "27/03/2026 20:20:10"
        },
        {
            "id": "P005",
            "peso": 104.0,
            "cor": "verde",
            "comp": 19.0,
            "aprovada": true,
            "motivo": "",
            "data": "27/03/2026 20:20:38"
        },
        {
            "id": "P006",
            "peso": 99.0,
            "cor": "azul",
            "comp": 11.0,
            "aprovada": true,
            "motivo": "",
            "data": "27/03/2026 20:21:07"
        },
        {
            "id": "P007",
            "peso": 101.0,
            "cor": "azul",
            "comp": 17.0,
            "aprovada": true,
            "motivo": "",
            "data": "27/03/2026 20:21:29"
        },
        {
            "id": "P011",
            "peso": 100.0,
            "cor": "rosa",
            "comp": 15.0,
            "aprovada": false,
            "motivo": "cor",
            "data": "27/03/2026 20:22:48"
        },
        {
            "id": "P012",
            "peso": 110.0,
            "cor": "verde",
            "comp": 15.0,
            "aprovada": false,
            "motivo": "peso",
            "data": "27/03/2026 20:23:12"
        },
        {
            "id": "P013",
            "peso": 100.0,
            "cor": "verde",
            "comp": 25.0,
            "aprovada": false,
            "motivo": "comprimento",
            "data": "27/03/2026 20:23:41"
        },
        {
            "id": "P008",
            "peso": 97.0,
            "cor": "azul",
            "comp": 13.0,
            "aprovada": true,
            "motivo": "",
            "data": "27/03/2026 20:24:42"
        },
        {
            "id": "P09",
            "peso": 103.0,
            "cor": "verde",
            "comp": 17.0,
            "aprovada": true,
            "motivo": "",
            "data": "27/03/2026 20:26:03"
        },
        {
            "id": "p10",
            "peso": 104.0,
            "cor": "verde",
            "comp": 15.0,
            "aprovada": true,
            "motivo": "",
            "data": "27/03/2026 20:27:45"
        }
    ],
    "c": [
        [
            "P001",
            "P002",
            "P003",
            "P004",
            "P005",
            "P006",
            "P007",
            "P008",
            "P09",
            "p10"
        ]
    ],
    "r": {
        "aprovadas": 10,
        "reprovadas_peso": 1,
        "reprovadas_cor": 1,
        "reprovadas_comp": 1,
        "total_caixas": 1
    }
}
```

| Chave | Conteúdo |
|-------|----------|
| `p`   | Lista de todas as peças com atributos e timestamp |
| `c`   | Caixas com os IDs das peças aprovadas |
| `r`   | Contadores do relatório por categoria |

---

##  Fluxo do Sistema

```
Início
  └─► Carrega dados do JSON
        └─► Menu principal (loop)
              ├─► [1] Cadastrar peça
              │     ├─► Coleta: ID, peso, cor, comprimento
              │     ├─► Valida: peso → cor → comprimento
              │     ├─► Aprovada:  vai para caixa
              │     └─► Reprovada: registra motivo
              ├─► [2] Listar peças
              ├─► [3] Remover peça
              ├─► [4] Listar caixas
              ├─► [5] Relatório
              └─► [6] Salva e encerra
```

---

## Regras do Sistema

- **Validação sequencial** — peso, depois cor, depois comprimento. A primeira falha define o motivo.
- **Remoção consistente** — ao remover uma peça aprovada, ela sai da caixa. Se a caixa ficar vazia, é excluída.
- **Cor aceita qualquer texto** — a validação acontece depois, permitindo registrar e analisar cores fora do padrão.
- **IDs diferenciam maiúsculas** — `P001` e `p001` são peças diferentes.
- **Caixas automáticas** — nova caixa criada automaticamente ao atingir o limite de 10 peças.
- **Contadores separados** — rejeições por peso, cor e comprimento ficam em campos distintos no relatório.

---

## Autor

**Gabriel Alves Ferreira De Souza**  
Desafio de Automação Digital — Gestão de Peças, Qualidade e Armazenamento