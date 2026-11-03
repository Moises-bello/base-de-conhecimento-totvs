---
content_hash: 54f4bc8c945fcdfcff1357787277c7d3a18402ef8b5def253f5c293c6265c535
fetched_at: '2026-06-29T00:05:51.509477+00:00'
page_id: '1050309255'
product: rm
source: tdn-rm
title: Novo Resíduo - Distribuição
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1050309255
version: 3
---

### Sumário

1. Visão Geral
2. Pré-requisitos Comuns
3. Os 3 Processos Manuais

   * 1. Gerar Parcela de Resíduo
   * 2. Distribuir Resíduos nas Próximas Parcelas
   * 3. Cancelar Parcela/Distribuição de Resíduo
4. Comparativo entre os Processos
5. Regras de Negócio Detalhadas
6. Parametrização
7. Exemplos Práticos
8. Perguntas Frequentes
9. Glossário

01Visão |

### t

## **1. Visão Geral**

O **Resíduo Manual** é uma funcionalidade que permite ao usuário gerenciar de forma flexível os resíduos acumulados em parcelas quitadas. Diferente do resíduo automático (que aguarda 12 meses para gerar uma parcela única), o resíduo manual pode ser acionado **a qualquer momento**, conforme a necessidade do negócio.

**Importante:** Todos os processos são **manuais**. O sistema não executa nenhuma ação automática – o usuário seleciona as parcelas de origem e escolhe a operação desejada.

2Pré-Requisitos |

### t

## **2. Pré-requisitos Comuns**

Para qualquer operação de resíduo manual, as parcelas de origem devem atender:

* Estar **quitadas**
* Possuir **resíduo calculado** (diferença entre valor pago e valor corrigido)
* Pertencer ao mesmo **grupo** de parcelas
* Não terem sido utilizadas em outro processo de resíduo manual anterior
2Processos |

### t

## **3. Os 3 Processos Manuais**

### 3.1 Gerar Parcela de Resíduo {#gerar-parcela}

**Objetivo:** Criar uma parcela nova e exclusiva para cobrar o resíduo de forma concentrada.

**Quando usar:** Quando se deseja uma cobrança separada, facilitando a visualização e o controle do resíduo.

**Passo a passo:**

| Etapa | Ação |
| --- | --- |
| 1 | Acesse: Contratos > Contratos de Vendas e Aluguéis |
| 2 | Selecione o contrato desejado |
| 3 | Clique em: Processos > Gerar Parcela de Resíduo |
| 4 | Na tela, selecione as parcelas quitadas que possuem resíduo |
| 5 | Informe a **data de vencimento** da nova parcela |
| 6 | Confirme a operação |

**Resultado:**

* Uma nova parcela é criada no plano de financiamento
* A parcela pertence a um **novo grupo** específico de resíduo
* O valor é a soma dos resíduos das parcelas selecionadas
* As parcelas de origem **não** entrarão no resíduo automático de 12 meses

---

### 3.2 Distribuir Resíduos nas Próximas Parcelas {#distribuir}

**Objetivo:** Ratear o valor do resíduo entre parcelas futuras, **sem criar uma parcela nova**.

**Quando usar:** Quando se quer diluir o impacto financeiro para o cliente, incorporando o valor nas parcelas existentes.

**Passo a passo:**

| Etapa | Ação |
| --- | --- |
| 1 | Acesse: Contratos > Contratos de Vendas e Aluguéis |
| 2 | Selecione o contrato desejado |
| 3 | Clique em: Processos > Distribuir Resíduos nas Próximas Parcelas |
| 4 | Selecione as parcelas de origem (quitadas, com resíduo) |
| 5 | Escolha o **destino** da distribuição: |
|  | ☐ Próximas 12 parcelas do próximo período |
|  | ☐ Todas as parcelas em aberto a partir do próximo período |
| 6 | Confirme a operação |

**Importante sobre o "próximo período":**

* O próximo período é definido com base no **aniversário da parcela de origem**
* Exemplo: Parcela de FEV/2025 → próximo período = FEV/2026
* Exemplo: Parcela de MAR/2026 → próximo período = MAR/2027
* **Nunca** é calculado com base na data atual

**Resultado:**

* As parcelas de destino têm seu valor **acrescido** proporcionalmente
* Nenhuma parcela nova é criada
* A distribuição ocorre dentro do **mesmo grupo** das parcelas de origem
* O cálculo da distribuição é **automático e proporcional** (sistema rateia o valor)

---

### 3.3 Cancelar Parcela/Distribuição de Resíduo {#cancelar}

**Objetivo:** Desfazer operações anteriores de resíduo manual, seja parcela criada ou distribuição realizada.

**Quando usar:** Quando houve erro na operação, necessidade de ajustes ou refaturamento.

**Passo a passo:**

| Etapa | Ação |
| --- | --- |
| 1 | Acesse: Contratos > Contratos de Vendas e Aluguéis |
| 2 | Selecione o contrato desejado |
| 3 | Clique em: Processos > Cancelar Parcela/Distribuição de Resíduo |
| 4 | Selecione a parcela que deseja cancelar/desfazer |
| 5 | Confirme a operação |

**Regras importantes:**

* Só é possível cancelar se a parcela que recebeu o valor (ou a parcela criada) estiver **em aberto**
* Se a parcela já foi quitada, é necessário **cancelar a baixa primeiro**
* Pode desfazer **parcelas específicas** (não precisa desfazer todas)
* O cancelamento é **total por parcela** (não é possível cancelar parcialmente)

**O que acontece:**

| Cenário | Resultado |
| --- | --- |
| Cancelar parcela de resíduo criada | A parcela é removida do plano |
| Cancelar distribuição | Os valores são estornados das parcelas de destino |

2Comparativos |

### t

## **4. Comparativo entre os Processos**

| Aspecto | Gerar Parcela | Distribuir | Cancelar |
| --- | --- | --- | --- |
| **Cria parcela nova?** | ✅ Sim | ❌ Não | ❌ Não (remove) |
| **Altera parcelas existentes?** | ❌ Não | ✅ Sim | ✅ Sim (estorna) |
| **Exige data de vencimento?** | ✅ Sim | ❌ Não | ❌ Não |
| **Impacto no resíduo automático** | Parcelas de origem são excluídas | Parcelas de origem são excluídas | Reverte a exclusão |
| **Momento da execução** | A qualquer tempo | A qualquer tempo | A qualquer tempo |

2Regras |

### t

## **5. Regras de Negócio Detalhadas**

| Regra | Descrição |
| --- | --- |
| **Seleção de parcelas** | Usuário escolhe manualmente as parcelas de origem |
| **Cálculo da distribuição** | Automático e proporcional |
| **Período de distribuição** | Baseado no aniversário da parcela de origem |
| **Grupo** | Distribuição ocorre dentro do mesmo grupo |
| **Cancelamento** | Só permitido se parcela de destino estiver em aberto |
| **Cancelamento específico** | Pode desfazer por parcela, mas deve ser a parcela completa |
| **Reversão** | Se quitada, precisa cancelar baixa primeiro |

2Parametrização  |

### t

## **6. Parametrização**

A funcionalidade de resíduo é controlada por **dois níveis de parâmetros**:

### Nível 1: Componente de Resíduo

**Onde:** Cadastro do Componente Financeiro  
**Campo:** "Distribuir resíduo sobre as parcelas em aberto do próximo período"  
**Efeito:** Define o comportamento padrão para distribuições

### Nível 2: Parâmetro Geral do Sistema

**Onde:** Parametrização Geral  
**Campo:** "Realizar a distribuição automática de resíduo em todas as parcelas em aberto"  
**Efeito:** Aplica a regra globalmente (quando aplicável)

2Exemplos |

### t

## **7. Exemplos Práticos**

### Exemplo 1: Gerar Parcela de Resíduo

**Cenário:**

* Parcela de FEV/2025 quitada com resíduo de R$ 500
* Parcela de MAR/2025 quitada com resíduo de R$ 300
* Total de resíduo: R$ 800

**Ação:** Usuário seleciona as 2 parcelas e gera parcela de resíduo com vencimento em 15/04/2025

**Resultado:** Nova parcela de R$ 800 criada no plano

---

### Exemplo 2: Distribuir Resíduos

**Cenário:**

* Parcela de FEV/2025 quitada com resíduo de R$ 600
* Próximo período: FEV/2026
* Parcelas em aberto de FEV a DEZ/2026 (11 parcelas)

**Ação:** Usuário escolhe "Distribuir" e seleciona a parcela de origem

**Resultado:** R$ 600 rateado entre as 11 parcelas de destino (cerca de R$ 54,54 a mais em cada)

---

### Exemplo 3: Cancelar Distribuição

**Cenário:** Distribuição foi feita, mas cliente reclamou do valor

**Ação:** Usuário acessa "Cancelar" e seleciona as parcelas que receberam o acréscimo (desde que em aberto)

**Resultado:** Valores são estornados e parcelas voltam ao valor original

2FAG |

### t

## **8. Perguntas Frequentes**

### 1. Posso misturar parcelas de grupos diferentes?

Não. As parcelas de origem precisam pertencer ao **mesmo grupo**.

### 2. O que acontece se eu distribuir e depois gerar parcela?

Não é possível. Uma vez que a parcela de origem é utilizada em um processo manual, ela fica **bloqueada** para outros processos.

### 3. Posso cancelar só parte de uma distribuição?

Não. O cancelamento é **total por parcela**.

### 4. E se a parcela que recebeu distribuição já foi quitada?

É necessário **cancelar a baixa** primeiro, para só então cancelar a distribuição.

### 5. A distribuição considera juros e correção?

Não. A distribuição incorpora apenas o **valor do resíduo** às parcelas de destino.

### 6. Como identificar parcelas que já passaram por resíduo manual?

O sistema mantém **histórico** e as parcelas de origem ficam marcadas como "utilizadas em resíduo manual".

2Glossário |

### t

## **9. Glossário**

| Termo | Definição |
| --- | --- |
| **Resíduo** | Diferença entre valor pago e valor corrigido da parcela |
| **Parcela de origem** | Parcela quitada que possui resíduo e será utilizada no processo |
| **Parcela de destino** | Parcela futura que receberá o acréscimo do resíduo |
| **Próximo período** | Período baseado no aniversário da parcela de origem |
| **Grupo** | Conjunto de parcelas com mesmas características |
| **Cancelar baixa** | Reverter a quitação de uma parcela |
| **Distribuição proporcional** | Rateio automático do valor entre as parcelas de destino |
