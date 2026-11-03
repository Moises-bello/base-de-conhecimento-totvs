---
content_hash: e9d3c2c679db1749ebe7bf1bf260bc5558b9d7cbd2da9b1e6c8c063f816c47d7
fetched_at: '2026-06-29T00:08:28.337094+00:00'
page_id: '271675330'
product: rm
source: tdn-rm
title: ER SAUHRM02-791 - Movimentos de CME
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+SAUHRM02-791+-+Movimentos+de+CME
version: 4
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### (Obrigatório)

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Estoque |
| **Segmento Executor** | RM | | |
| **Projeto1** | SAUHRM02 | **IRM/EPIC1** | SAUHRM02-792 |
| **Requisito/Story/Issue1** | SAUHRM02-791 | **Subtarefa1** | SAUHRM02-793 |
| **Chamado/Ticket2** | 198174 | | |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### (Obrigatório)

## Objetivo

 

O objetivo deste documento é definir o funcionamento do módulo do CME através de tipos de movimento de Requisição para o Centro de Custo CME e o movimento de Devolução para o Centro de Custo CME.

 

### (Obrigatório)

## Definição da Regra de Negócio

A implementação se restringe à funcionalidade de Movimentações de Estoque, no menu Estoque/Movimentação de Estoque.

Serão  criados dois novos tipos de movimento para suportar e diferenciar as movimentações relacionadas ao CME. A funcionalidade trata somente as entradas e saídas dos itens entre os locais de estoque do CME e dos setores de enfermagem.

**RN 01:** Criação do tipo de movimento Requisição para o CME

 Criação do novo tipo de movimento no menu Opções/Parâmetros/Parâmetros RM Nucleus, página “**Tipos de Mov. Estoque**”, campo **Tipo**. Com este novo tipo, deve-se informar os tipos de movimento relacionados ao movimento do Nucleus para se movimentar o estoque.

Tabela: SZTIPOMOV

Campo: TIPO à O novo valor deve ser 10 para o tipo Requisição para o CME

**RN 02:** Criação do tipo de movimento Devolução para o CME

 Criação do novo tipo de movimento no menu Opções/Parâmetros/Parâmetros RM Nucleus, página “**Tipos de Mov. Estoque**”, campo **Tipo**. Com este novo tipo, deve-se informar os tipos de movimento relacionados ao movimento do Nucleus para se movimentar o estoque.

Tabela: SZTIPOMOV

Campo: TIPO à O novo valor deve ser 11 para o tipo Devolução para o CME

**RN 03:** Parametrização do local de estoque envolvidos no processo do CME

 Criação de uma nova página na tela de Parâmetros RM Nucleus com a descrição “Locais de estoque específicos do CME”. Estes locais de estoque não deverão aparecer nos demais tipos de movimento, somente nos definidos nas regras 01 e 02.

**RN 04:** Funcionamento do tipo de movimento Requisição para o CME

 Na funcionalidade Movimentação de Estoque, ao selecionar o tipo Requisição para o CME, o sistema deve solicitar o campo Local de Estoque (que é o local do CME) e o campo “Local de estoque destino” (que é o local da enfermagem). O centro de custo deverá ser informado como sendo o da enfermagem. Somente os locais definidos na regra 03 é que deverão ser exibidos nesses dois locais de estoque.

Somente itens parametrizados como material esterilizável no menu Cadastros / Estoque / Produto / Anexo Informações RM Saúde, campo “Tipo de material esterilizável”, serão permitidos de ser movimentados.

**RN 05:** Funcionamento do tipo de movimento Devolução para o CME

Na funcionalidade Movimentação de Estoque, ao selecionar o tipo Requisição para o CME, o sistema deve solicitar o campo Local de Estoque (que é o local da enfermagem) e o campo “Local de estoque destino” (que é o local do CME). Somente os locais definidos na regra 03 é que deverão ser exibidos nesses dois locais de estoque.

O processamento deste tipo de movimento implicará a execução automática do fluxo “Entrada de materiais” no módulo do CME. A parte de conferência também ocorrerá de forma automática.

Neste tipo de movimento, será disponibilizado o campo da “Requisição Associada”, para que o sistema traga automaticamente os itens solicitados na mesma.

Somente itens parametrizados como material esterilizável no menu Cadastros / Estoque / Produto / Anexo Informações RM Saúde, campo “Tipo de material esterilizável”, será permitidos de ser movimentados.

**RN 06: Fluxo já existente**

O módulo do CME já existente possui processos e fluxos já definidos. Caso o mesmo seja utilizado, será necessário seguir os procedimentos deste módulo. A funcionalidade a ser implementada, somente distingue dos demais tipos de movimento, pela configuração dos movimentos do Nucleus. Possui o mesmo comportamento do movimento de transferência.

O resultado do processamento do movimento de devolução para o CME, no módudo do CME, será a execução do primeiro estágio que é a “Entrada do material” e da “Conferência”.  Os demais processos deverão ser realizados no módulo já existente do CME.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Parâmetros RM Nucleus | Evolução | Opções -> Parâmetros | RN01, RN02, RN03 |
| Movimentação de Estoque | Evolução | Estoque -> Movimentação de Estoque | RN04, RN05 |
| Processamento da Requisição | Evolução | Estoque -> Movimentação de Estoque | - |

***Tabelas Utilizadas***

* *SZTIPOMOV – Tipos de movimento*
* *SZMOVIESTOQUE – Movimentação de estoque*
* *SZCMELOCALESTOQUE - Locais de estoque utilizados com o CME*
* *SZCMEMOV - Movimentação no CME*
* *SZCMEHISTORICO - Histórico do movimentação do cme*

### Opcional

## Dicionário de Dados

**Arquivo ou Código do Script:** SZLOCALESTCME – Locais de estoque específicos do CME / \*Versao=SA.2017.02\_06\*/

 

|  |  |  |
| --- | --- | --- |
| **Índice** | **Chave** | Referência |
| **01** | CODCOLIGADA + SEQ (PK) |  |
| **02** | CODCOLIGADA + CODFILIAL + CODLOC (FK) | TLOC |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| SZLOCALESTCME | CODCOLIGADA | DCODCOLIGADA |  |  | Sim (X) Não ( ) | Código da Coligada |
| SZLOCALESTCME | SEQ | Inteiro |  |  | Sim (X) Não ( ) | Sequencial |
| SZLOCALESTCME | CODFILIAL | Inteiro |  |  | Sim (X) Não ( ) | Código da Filial |
| SZLOCALESTCME | CODLOC | VARCHAR | 15 |  | Sim (X) Não ( ) | Código do local de estoque |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
