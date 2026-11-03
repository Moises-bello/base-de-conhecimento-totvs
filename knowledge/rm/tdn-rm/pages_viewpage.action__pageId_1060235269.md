---
content_hash: c8cbb5500c0292e0187b48d793c179944605b26ec0b935e9e01344260bd9b781
fetched_at: '2026-06-29T00:05:52.836058+00:00'
page_id: '1060235269'
product: rm
source: tdn-rm
title: Lançamento de Diárias SUS
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1060235269
version: 19
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Formas de Execução**
3. **Regras de Negócio**
4. **Critérios de Identificação**
5. **Processo de Lançamento**

sumarioVisão Geral

## **01. VISÃO GERAL**

Este processo tem como objetivo realizar o **lançamento automático de diárias SUS** em AIHs, contemplando três tipos de diárias:

* **Diárias de Longa Permanência** — quando o tempo de internação excede o limite previsto pelo procedimento principal da AIH.
* **Diárias de Acompanhante** — quando o paciente se enquadra em um dos perfis definidos pelo SUS (Idoso, Criança ou Gestante).
* **Diárias de UTI** — quando o paciente ocupa leito de UTI.

O sistema avalia automaticamente as AIHs elegíveis, identifica o tipo de diária aplicável, calcula a quantidade correta e realiza o lançamento dos procedimentos correspondentes.

Formas de Execução

## **02****. FORMAS DE EXECUÇÃO**

O processo poderá ser executado de três formas:

1. Execução Agendada

* Configura-se um agendamento diário do processo.
* O sistema executa automaticamente no horário definido.
* Todas as AIHs elegíveis são avaliadas.
2. Execução Manual com Seleção de AIHs

* O usuário acessa a tela de **Elaboração de AIH**.
* Seleciona uma ou mais AIHs.
* Executa o processo **"Lançamento de Diária SUS"**.
* Apenas as AIHs selecionadas são processadas.

3. Execução Manual sem Seleção de AIHs

* O usuário acessa a tela de **AIH** sem selecionar nenhum registro.
* Executa o processo **“Lançamento de Diária SUS”**.
* O sistema considerará automaticamente AIHs com status:  
  + **Em Elaboração**
  + **Pendentes**
* Em todos os modos de execução, ambos os tipos de diária (Longa Permanência e Acompanhante) são avaliados e lançados conforme elegibilidade de cada AIH.

Pré-requisitos Gerais

## **03****. PRÉ-REQUISITOS GERAIS**

Independentemente do tipo de diária, são obrigatórios:

* **Convênio SUS** com a opção **"Lançamento Automático de Diária"** habilitada no contrato.

* **Parâmetros SUS** preenchidos em *Ambiente > Configuração > Parâmetros > Gestão Hospitalar > Parâmetros SUS > Editar perfil existente*:
  + Idade Idoso (em anos)
  + Idade Menor — Sexo Masculino (em anos)
  + Idade Menor — Sexo Feminino (em anos)
* **Tipos de Leito UTI** corretamente classificados no cadastro de leitos (necessário para excluir os dias de UTI do cálculo) pelo caminho *Cadastros > Leitos*.
  + No cadastro de leitos a opção para selecionar a diária a ser lançada na AIH fica habilitada quando o tipo de acomodação é UTI.
  + Com a classe de leito selecionada como qualquer um do tipo UTI, a opção ***Lookup Código de Diária UTI SIGTAP***ficara disponível para seleção da diária que será lançada posteriormente na AIH

* **Procedimento principal** preenchido na AIH.

Regras de Negócio

## **04****. REGRAS DE NEGÓCIO**

## 4.1. Diária de Longa Permanência

**Condições para lançamento:**

* + A AIH possui procedimento principal válido.
  + O procedimento principal é classificado pelo SIGTAP como permitindo longa permanência.

**Regra principal:**

> Se **Tempo de Internação > Tempo Permitido**, o sistema lança um registro de diária de longa permanência para cada dia excedente.

**Cálculo:**

* + Tempo de Internação = (Data de Saída ou Data Atual, caso paciente ainda internado) − Data de Início
  + Tempo de UTI **não é considerado** (subtraído do total)
  + Dias Excedentes = Tempo de Internação − Tempo Permitido

**Procedimento utilizado:** `0802010199` — Diária de Longa Permanência

## 4.2. Diária de Acompanhante

O sistema identifica automaticamente o perfil do paciente e lança o procedimento correspondente.

### Perfis suportados

| Perfil | Critério | Código de Procedimento |
| --- | --- | --- |
| **Idoso (com pernoite)** | Idade ≥ Parâmetro SUS Idoso **e** Data Saída diferente de Data Início | `0802010040` |
| **Idoso (sem pernoite)** | Idade ≥ Parâmetro SUS Idoso **e** Data Saída igual a Data Início | `0802010059` |
| **Criança** | Idade ≤ Parâmetro SUS Menor (Masculino ou Feminino, conforme sexo) | `0802010024` |
| **Gestante** | Procedimento principal de Parto Normal ou Cesárea | `0802010032` |

### Cálculo da quantidade de diárias

```

```

Quantidade de Diárias = Dias de Internação − Dias de UTI + Adicional de Óbito

```

```

* + **Dias de Internação:** período entre Data de Início e Data de Saída (ou Data Atual, caso ainda internado)
  + **Dias de UTI:** total de diárias UTI já lançadas no período
  + **Adicional de Óbito:** soma-se **+1 diária** quando o motivo de encerramento da AIH é:
    - 31, 41, 42 ou 43 (motivos de óbito)

### Datas dos lançamentos

* + O sistema lança uma diária por dia, **dentro do período de internação**.
  + Datas já lançadas manualmente **não são duplicadas** — o sistema apenas completa as faltantes.
  + A data de referência inicial é a **Data de Saída** (se houver) ou a **Data Atual** (paciente ainda internado).

## 4.3. Diária de UTI

O sistema identifica automaticamente os períodos em que o paciente ocupou leito de UTI durante o atendimento e gera as diárias correspondentes na AIH, utilizando o código SIGTAP cadastrado no próprio leito de UTI ocupado.

### Identificação do período em UTI

```

```

A apuração é feita a partir do histórico de leitos, filtrando pelo paciente e atendimento da AIH, ordenado por data/hora:  
  
 **Início de um período****:** primeiro registro com status do leito diferente de  ***"ocupado"*** em leito cuja classe de acomodação tem tipo de acomodação = 7 (UTI). Cobre todas as variantes (UTI Adulto, UTI Neonatal etc.).  
**Fim do período****:** próximo registro do mesmo leito com status diferente de "***ocupado***", ou transição para outro leito.  
**Múltiplos períodos****:** o paciente pode entrar e sair da UTI várias vezes no mesmo atendimento; cada janela de ocupação gera um período próprio.  
**Período aberto ao fim do histórico****:** caso o paciente continue ocupando o leito de UTI ao final da apuração, usa-se a Data de Saída da AIH ou a Data Atual (paciente ainda internado).

### Regra geral para lançamento de diária de UTI

* + ***Data da alta/transferência não gera diária.***

Aplicam-se  
as seguintes exceções:  
  
**| Situação | Datas geradas |**  
| Internação de 1 dia (entrada = saída) | 1 diária no dia |  
| Alta / transferência real (status do leito mudou) | do dia da entrada até o dia anterior à saída |  
| Óbito no último período (motivo de cobrança 41, 42 ou 43) | do dia da entrada até o dia da saída (inclusive) |  
| Período aberto até o fim da AIH (sem transição de leito) | do dia da entrada até a Data de Saída AIH / Data Atual |

### Datas dos lançamentos

* + O sistema lança uma diária por dia, **conforme as regras de contagem acima.**
  + Datas já lançadas manualmente **não são duplicadas** — o sistema apenas completa as faltantes.
  + A data de referência inicial é a **Data de Saída** (se houver) ou a **Data Atual** (paciente ainda internado).

Critérios de Identificação

**05****. CRITÉRIOS DE IDENTIFICAÇÃO**

Para cada AIH elegível, o sistema executa em sequência:

1. **Carrega dados da AIH e do paciente** (idade, sexo, procedimento principal, datas).
2. **Verifica elegibilidade do convênio** (parâmetro de lançamento automático ativo).
3. **Carrega dados do leito de UTI**(se aplicável).
4. **Avalia regras de UTI:**
   * Procedimento principal permite UTI?
   * Idade do paciente está dentro de IDADEMIN/IDADEMAX do procedimento da diária?
   * Cada leito UTI ocupado tem Código de diária de UTI SIGTAP cadastrado?
   * Quantidade máxima da diária de uti cadastrada no leito ainda não atingido?
   * Quantidade de diárias de UTI lançadas não excede os dias em UTI nem o total da AIH?
5. **Avalia regras de Longa Permanência:**
   * Procedimento principal permite?
   * Há dias excedentes?
6. **Avalia perfil para Acompanhante:**
   * Idade ≥ parâmetro Idoso → perfil Idoso
   * Idade ≤ parâmetro Menor (por sexo) → perfil Criança
   * Procedimento principal de Parto/Cesárea → perfil Gestante
7. **Calcula quantidade pendente para cada tipo:**
   * Subtrai diárias já lançadas no período da quantidade esperada.
8. **Lança somente o que falta**, respeitando o período de internação.
Processo de Lançamento

## **06****. PROCESSO DE LANÇAMENTO**

Ao identificar que a AIH atende às regras de elegibilidade:

1. O sistema calcula a quantidade de diárias pendentes para cada tipo.
2. Identifica o(s) procedimento(s) aplicável(eis):
   * Diária de Longa Permanência (`0802010199`)
   * Diária de Acompanhante (código conforme perfil — ver tabela em 4.2)
   * Diária de UTI (conforme condições em 4.3)
3. Realiza o lançamento automático:
   * Um registro por dia excedente
   * Quantidade igual a 1 por registro
   * Datas distribuídas de forma regressiva a partir da Data de Saída (ou Data Atual)
   * Datas já preenchidas manualmente são respeitadas e não duplicadas
4. Exibe mensagem de informação para cada lançamento realizado, indicando a data e a AIH.

### Após a execução do lançamento automático de diárias SUS, a tela de procedimentos da AIH passa a identificar a origem de cada item (automático ou manual) facilitando a conferência pelo faturista.

Lançamentos via Evolução Clínica

## **06****. Lançamentos via Evolução Clínica**

Este processo tem como objetivo realizar o **lançamento automático de procedimentos SUS na AIH do paciente**, via evolução clínica no Prontuário Eletrônico.

Para o devido funcionamento é necessário cadastrar um "Tipo de Evolução", cadastro este onde serão informados o procedimento SUS, a especialidade e conselho profissional que um prestador precisa possuir para lançar o procedimento na conta do paciente.

Caminho: Cadastros > Uso Geral > Registro e Controle > Tipo de Evolução.

Uma vez cadastrado o tipo de evolução, ao efetuar uma evolução clínica no prontuário eletrônico, o sistema irá identificar automaticamente quando o membro da equipe multiprofissional que esta efetuando a evolução, possui especialidade e conselho profissional que atendam a regra especificada e, em caso positivo realizará o lançamento do procedimento (SIGTAP) correspondente a este cadastro na **elaboração de AIH do paciente**.

Exemplo de inclusão de Evolução, com a especialidade "Clínica Médica" do prestador, cujo conselho profissional é o CRM:

Ao confirmar a evolução é disparada a regra que adiciona o procedimento cadastrado na AIH do paciente.

As regras de validação para inclusão do procedimento na AIH são: Convênio SUS, AIH com status pendente ou em elaboração, e prestador do serviço com mesma especialidade e conselho profissional previamente cadastrados no "Tipo de Evolução".

Uma vez validada a regra e confirmada a evolução clínica o procedimento é incluído na AIH do paciente.

Excluir ou Suspender Evolução

## **07****. Excluir ou Suspender Evolução**

Ao suspender ou excluir, no Prontuário Eletrônico, evoluções com status **Em Elaboração** ou **Pendente** que possuam procedimentos SUS vinculados, os procedimentos associados à respectiva evolução serão removidos automaticamente.
