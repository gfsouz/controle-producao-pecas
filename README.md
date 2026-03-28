# Sistema de Gestão Industrial: Guia Completo de Execução

O Sistema de Gestão Industrial foi desenvolvido com o propósito de automatizar, controlar e otimizar os processos de produção em ambientes industriais. A solução tecnológica implementada permite realizar o controle de qualidade, o registro e a organização de peças produzidas, garantindo que todas as peças atendam aos padrões de qualidade estabelecidos pela empresa. Ao adotar esse sistema, as organizações conseguem reduzir significativamente os erros humanos, aumentar a eficiência operacional e padronizar os processos de produção.

O funcionamento do Sistema de Gestão Industrial é baseado em critérios de validação rigorosos, que incluem a verificação do peso, da cor e do comprimento de cada peça produzida. Cada peça cadastrada passa por um processo de validação automática, onde são verificados os seguintes parâmetros:

- **Peso**: Cada peça deve estar dentro da faixa de peso estabelecida para ser considerada apta.
- **Cor**: A cor da peça deve estar entre as cores permitidas, que são pré-definidas de acordo com os padrões de qualidade.
- **Comprimento**: O comprimento da peça deve estar dentro dos limites estabelecidos para ser aprovada.

As peças que atendem a todos os critérios de qualidade são aprovadas e organizadas em caixas de armazenamento, enquanto as peças que não atendem a um ou mais critérios são reprovadas e registradas com o motivo específico da rejeição. Esse processo garante que apenas peças que atendem aos padrões de qualidade sejam encaminhadas para as etapas seguintes da produção.

Além do controle de qualidade, o Sistema de Gestão Industrial oferece funcionalidades adicionais que permitem um gerenciamento completo e detalhado de todo o processo de produção. Entre essas funcionalidades, destacam-se:

- **Cadastro de Peças**: Permite o registro de novas peças no sistema, com validação automática dos critérios de qualidade.
- **Listagem de Peças**: Exibe todas as peças cadastradas, separando-as em aprovadas e reprovadas, com informações detalhadas.
- **Remoção de Peças**: Permite a remoção de peças específicas, ajustando automaticamente as caixas e contadores.
- **Listagem de Caixas**: Mostra o conteúdo de cada caixa de armazenamento, facilitando o controle logístico.
- **Geração de Relatórios**: Fornece métricas consolidadas sobre a produção, permitindo uma análise detalhada do desempenho.
- **Salvamento e Saída**: Garante que todos os dados sejam salvos de forma segura antes de encerrar o programa.

O Sistema de Gestão Industrial é uma ferramenta essencial para empresas que buscam melhorar a qualidade dos produtos, aumentar a eficiência operacional e reduzir custos associados a erros de produção.

---

## Estrutura do Projeto

A estrutura do projeto foi organizada de maneira clara e objetiva, facilitando a localização e o entendimento dos arquivos e documentos que compõem o sistema. A estrutura é composta pelos seguintes diretórios e arquivos:

```
GESTAO-INDUSTRIAL/
│
├── docs/
│   └── Analise_e_Discussao.pdf
│
├── src/
│   ├── sistema.py
│   └── dados_fabrica.json
```

- **docs/Analise_e_Discussao.pdf**: Documento que contém a análise técnica detalhada do sistema, incluindo os requisitos, a arquitetura, os casos de uso e as especificações técnicas.
- **src/sistema.py**: Arquivo principal do sistema, responsável por iniciar o menu interativo e executar as funcionalidades do sistema. Este é o arquivo que deve ser executado para iniciar o Sistema de Gestão Industrial.
- **src/dados_fabrica.json**: Arquivo de dados persistentes, gerado automaticamente durante a execução do sistema. Este arquivo armazena todas as informações relacionadas às peças, caixas e relatórios gerados pelo sistema.

---

## Como Rodar o Programa

Para executar o Sistema de Gestão Industrial, é necessário seguir os passos detalhados abaixo. Esses passos garantem que o sistema seja iniciado corretamente e que todas as funcionalidades estejam disponíveis para uso.

---

### Pré-requisitos

Antes de iniciar a execução do sistema, é fundamental verificar se os seguintes pré-requisitos estão atendidos:

1. **Python versão 3.11 ou superior** instalado no computador.
  - Para verificar a versão do Python instalada, abra o terminal ou prompt de comando e digite o seguinte comando:
  - Caso o Python não esteja instalado, é necessário realizar o download e a instalação a partir do site oficial: [python.org](https://www.python.org/downloads/).
2. **Permissão para leitura e escrita de arquivos** na pasta "src".
  - Certifique-se de que o usuário possui as permissões adequadas para acessar e modificar arquivos na pasta "src".
3. **Ambiente de execução**:
  - O sistema pode ser executado em qualquer sistema operacional (Windows, macOS, Linux) que possua o Python instalado.

---

### Passos para Execução

1. **Acessar a pasta "src"**:
  - Abra o terminal ou prompt de comando do sistema operacional.
  - Navegue até a pasta "src" utilizando o comando:
    ```bash
    cd caminho/para/a/pasta/GESTAO-INDUSTRIAL/src/
    ```
  - Substitua "caminho/para/a/pasta/" pelo caminho real onde o projeto foi salvo.
2. **Executar o sistema**:
  - O arquivo `sistema.py` é o responsável por iniciar o menu interativo do Sistema de Gestão Industrial.
  - Execute o seguinte comando para iniciar o sistema:
    ```bash
    python sistema.py
    ```
  - Após a execução do comando, o sistema será iniciado e exibirá o seguinte menu interativo no terminal:
    ```
    🏭 GESTÃO INDUSTRIAL
    ```
  1. 📝 Cadastrar Peça
  2. 📋 Listar Peças
  3. 🗑️ Remover Peça
  4. 📦 Listar Caixas
  5. 📊 Relatório Final
  6. 🚪 Salvar e Sair
    `
    Opção 1: 📝 Cadastrar Peça**  
    Permite registrar uma nova peça no sistema.  
    Durante o cadastro, são solicitadas as informações: ID, peso, cor e comprimento.  
    O sistema realiza a validação automática das informações e exibe uma mensagem informando se a peça foi aprovada ou reprovada, além do destino (caixa ou não).
    Opção 2: 📋 Listar Peças**  
    Exibe todas as peças cadastradas, separando-as em aprovadas e reprovadas.  
    Para cada peça, são exibidas informações detalhadas, como ID, peso, cor, comprimento, status e data de registro.
    Opção 3: 🗑️ Remover Peça**  
    Permite remover uma peça específica pelo seu ID.  
    Ao remover uma peça aprovada, o sistema ajusta automaticamente as caixas e contadores para manter a consistência dos dados.
    Opção 4: 📦 Listar Caixas**  
    Mostra o conteúdo de cada caixa, incluindo o número da caixa, a quantidade de peças armazenadas e os IDs das peças.
    Opção 5: 📊 Relatório Final**  
    Exibe métricas consolidadas sobre a produção, como total de peças aprovadas e reprovadas, quantidade de caixas utilizadas e motivos de rejeição.
    Opção 6: 🚪 Salvar e Sair**  
    Salva todos os dados no arquivo "dados_fabrica.json" e encerra o programa de forma segura.
3. **Utilizar o menu interativo**:
  - Selecione a opção desejada digitando o número correspondente e pressionando Enter.
  - O sistema executará a funcionalidade escolhida e retornará ao menu principal após a conclusão.

---

## Exemplos de Entradas e Saídas para Todas as Funcionalidades

A seguir, são apresentados exemplos detalhados de entradas e saídas para cada uma das funcionalidades do sistema.

---

### 1. 📝 Cadastrar Peça

**Exemplo 1: Peça Aprovada**

```
Opção: 1
ID da peça: P001
Peso (g): 100
Cor (azul ou verde): azul
Comprimento (cm): 15

✅ Peça APROVADA! Registrada em 25/03/2026 10:30:45
Vai para Caixa 1 (1/10)
```

**Exemplo 2: Peça Reprovada (Cor Inválida)**

```
Opção: 1
ID da peça: P011
Peso (g): 100
Cor (azul ou verde): rosa
Comprimento (cm): 15

❌ Peça REPROVADA! Motivo: COR
(A cor 'rosa' não é permitida. Apenas azul ou verde são aceitos.)
Não vai para caixa
```

**Exemplo 3: Peça Reprovada (Peso Inválido)**

```
Opção: 1
ID da peça: P012
Peso (g): 110
Cor (azul ou verde): azul
Comprimento (cm): 15

❌ Peça REPROVADA! Motivo: PESO
Não vai para caixa
```

**Exemplo 4: Peça Reprovada (Comprimento Inválido)**

```
Opção: 1
ID da peça: P013
Peso (g): 100
Cor (azul ou verde): verde
Comprimento (cm): 25

❌ Peça REPROVADA! Motivo: COMPRIMENTO
Não vai para caixa
```

---

### 2. 📋 Listar Peças

**Exemplo:**

```
Opção: 2

📋 LISTAGEM DE PEÇAS

🟢 APROVADAS:
ID:P001 | 100g | azul | 15cm | 25/03/2026 10:30:45
ID:P002 | 98g | verde | 12cm | 25/03/2026 10:35:22

🔴 REPROVADAS:
ID:P011 | Cor: rosa | Motivo: COR | 25/03/2026 10:40:10
ID:P012 | Peso: 110g | Motivo: PESO | 25/03/2026 10:45:30
ID:P013 | Comprimento: 25cm | Motivo: COMPRIMENTO | 25/03/2026 10:50:15
```

---

### 3. 🗑️ Remover Peça

**Exemplo 1: Remover Peça Aprovada**

```
Opção: 3
ID da peça: P001

✅ Removido com sucesso!
```

**Exemplo 2: Remover Peça Inexistente**

```
Opção: 3
ID da peça: P999

❌ Peça não encontrada.
```

---

### 4. 📦 Listar Caixas

**Exemplo 1: Caixa com Peças**

```
Opção: 4

📦 STATUS DAS CAIXAS

Caixa 1: [2/10] -> P001, P002
```

**Exemplo 2: Nenhuma Caixa Utilizada**

```
Opção: 4

📦 STATUS DAS CAIXAS

Nenhuma caixa utilizada.
```

**Exemplo 3: Caixa Cheia**

```
Opção: 4

📦 STATUS DAS CAIXAS

Caixa 1: [10/10] -> P001, P002, P003, P004, P005, P006, P007, P008, P009, P010
```

---

### 5. 📊 Relatório Final

**Exemplo:**

```
Opção: 5

📊 RELATÓRIO GERENCIAL

Aprovadas:           2
Reprovadas (Total):  3
  - Peso:            1
  - Cor:             1
  - Comprimento:     1
Caixas Utilizadas:   1
```

---

### 6. 🚪 Salvar e Sair

**Exemplo:**

```
Opção: 6

Dados salvos. Até logo!
```

---

## Resumo dos Exemplos


| Funcionalidade  | Exemplo de Entrada                               | Exemplo de Saída                                                               |
| --------------- | ------------------------------------------------ | ------------------------------------------------------------------------------ |
| Cadastrar Peça  | ID: P001, Peso: 100, Cor: azul, Comprimento: 15  | ✅ Peça APROVADA! Registrada em [data e hora], Vai para Caixa 1 (1/10)          |
| Cadastrar Peça  | ID: P011, Peso: 100, Cor: rosa, Comprimento: 15  | ❌ Peça REPROVADA! Motivo: COR, Não vai para caixa                              |
| Cadastrar Peça  | ID: P012, Peso: 110, Cor: azul, Comprimento: 15  | ❌ Peça REPROVADA! Motivo: PESO, Não vai para caixa                             |
| Cadastrar Peça  | ID: P013, Peso: 100, Cor: verde, Comprimento: 25 | ❌ Peça REPROVADA! Motivo: COMPRIMENTO, Não vai para caixa                      |
| Listar Peças    | -                                                | Lista de peças aprovadas e reprovadas com detalhes                             |
| Remover Peça    | ID: P001                                         | ✅ Removido com sucesso!                                                        |
| Remover Peça    | ID: P999                                         | ❌ Peça não encontrada.                                                         |
| Listar Caixas   | -                                                | Caixa 1: [2/10] -> P001, P002                                                  |
| Listar Caixas   | -                                                | Nenhuma caixa utilizada.                                                       |
| Listar Caixas   | -                                                | Caixa 1: [10/10] -> P001, P002, P003, P004, P005, P006, P007, P008, P009, P010 |
| Relatório Final | -                                                | Aprovadas: 2, Reprovadas: 3, Caixas Utilizadas: 1                              |
| Salvar e Sair   | -                                                | Dados salvos. Até logo!                                                        |


---

## Observações Finais

- **Peças Aprovadas**: São organizadas em caixas com capacidade máxima de 10 peças. Quando uma caixa atinge a capacidade máxima, é fechada automaticamente e uma nova caixa é iniciada.
- **Peças Reprovadas**: Não são organizadas em caixas e são registradas com o motivo específico da rejeição (cor, peso ou comprimento).
- **Critérios de Validação**: Peso (95g a 105g), Cor (azul ou verde), Comprimento (10cm a 20cm).
- **Arquivo de Execução**: O arquivo `sistema.py` é o responsável por iniciar o menu interativo do sistema.