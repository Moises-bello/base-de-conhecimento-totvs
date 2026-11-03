---
content_hash: 862ba46078ff33b571b4499d9e1a035945af15b067aea66c630e340e47adc6a6
fetched_at: '2026-06-29T00:08:28.010079+00:00'
page_id: '271652605'
product: rm
source: tdn-rm
title: ER SAUHRM02-592 MATMED vinculado a exames
type: documentation
url: https://tdn.totvs.com/display/LRM/ER+SAUHRM02-592+MATMED+vinculado+a+exames
version: 28
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Hospitalar | **Módulo** | Unidade de Diagnóstico |
| **Segmento Executor** | RM | | |
| **Projeto1** | SAUHRM02 | **IRM/EPIC1** | SAUHRM02-346 |
| **Requisito/Story/Issue1** | SAUHRM02-592 | **Subtarefa1** | SAUHRM02-625 |
| **Chamado/Ticket2** | 197777 | | |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

### Objetivo

 Permitir realizar o vínculo de materiais e medicamentos ao cadastro de exames para solucionar a questão de requisitar os itens na farmácia ou somente cobrar na conta do paciente quando um exame for solicitado.

### Definição da Regra de Negócio

```
Ao solicitar exames para um paciente, o sistema deve verificar se existem MATMED associados a ele e dependendo da configuração deverá criar uma movimentação de estoque e
```

```
incluir os materiais e medicamentos associados.
```

Caso o MATMED não deve gerar movimentação de estoque, o mesmo somente deve ser lançado na conta do paciente.

**RN01: Associando materiais e medicamentos ao exame**

No menu Cadastros -> Unidades de Diagnóstico -> Exames e Serviços, criar um cadastro anexo para associar itens de estoque ao exame.

Para este cadastro, deve-se criar a tabela SZEXAMEMATMED com o seguintes campos:

* CODCOLIGADA, que vai conter a coligada corrente
* CODEXAME, que corresponde ao exame selecionado
* IDPRD, que corresponde ao material ou medicamento associado ao exame
* QTD, que é a quantidade do produto a ser solicitado ou lançado na conta do paciente. Esta quantidade corresponde a quantidade na unidade de controle do produto.
* OPCAO, que pode ter duas opções: Gera movimentação de estoque ou Somente lança na conta do paciente

**RN02: Pedido de exames**

Na funcionalidade de Pedido de Exames para paciente, menu Unidades Diagnóstico e no menu Prontuário, Avaliações Complementares, ao incluir itens no pedido de exames,criar uma rotina que verifica (VerificaMatmedAssociado) se o exame possui MATMED associado.

Se existir, deve verificar se o item é somente para cobrança (criar a rotina LancaMatmedNaConta) ou para gerar movimentação de estoque (classe TMovEstoque).

A  rotina LancaMatmedNaConta deve inserir na tabela SZATENDMATMED e gravar a referência na tabela SZRELEXAMEMATMEDCONTA. É nesta tabela que se encontra qual item foi lançado na conta do paciente.

A classe TMovEstoque deve possuir os métodos CriaCabecalho() que corresponde a inclusão na tabela SZMOVIESTOQUE e o método InsereItem(), que corresponde a inclusão na tabela SZMOVIESTOQUEITEM.

Após incluir o item na movimentação de estoque, deve-se incluir a referência na tabela SZRELEXAMEMOVIESTOQUE. É nesta tabela que se encontra qual item foi lançado na movimentação de estoque.

**RN03: Cancelamento do exame**

Ao se cancelar um exame, chamar a rotina VerificaMatmedAssociado() e verificar se existem matmed associados.

Caso exista, verificar nas tabelas SZRELEXAMEMATMEDCONTA e SZRELEXAMEMOVIESTOQUE se existem registros. Se existir na tabela SZRELEXAMEMATMEDCONTA,

o registro na tabela SZATENDMATMED deverá ser estornada (SZATENDMATMED.ESTORNADO = 'T'). Se existir na tabela SZRELEXAMEMOVIESTOQUE, o registro da tabela

SZMOVIESTOQUEITEM deverá estar com status de suspenso (SZMOVIESTOQUEITEM.STATUS = 'S').

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [SauLabExameAction – MATMED associado a Exames] | [Alteração] | [Cadastros -> Unidades de Diagnósticos -> Exames e Serviçõs] | RN01 |
| [PSARC023 – Pedido de Exames] | [Alteração] | [Unidades de Diagnóstico -> Pedido de Exames] | RN02, RN03 |
| [SadPedidoExamePEP – Exames Compelementares] | [Alteração] | [Prontuário -> Avaliações Complementares] | RN02, RN03 |

```
 
```

```
Tabelas Utilizadas
```

* SZEXAMEMATMED – Cadastro de MATMED associado a exames

* SZRELEXAMEMATMEDCONTA – relacionamento do exame e o MATMED lançados na conta do paciente
* SZATENDMATMED - Lançamento de matmed na conta do paciente
* SZMOVIESTOQUEITEM - Item da requisição
* SZRELEXAMEMOVIESTOQUE  - relacionamento do exame e MATMED relacionados à movimentação de estoque

### Dicionário de Dados

**Arquivo ou Código do Script:**

Tabela: SZEXAMEMATMED

|  |  |  |
| --- | --- | --- |
| **Índice** | **Chave** | Tabela de Referência |
| **01** | <CODCOLIGADA + CODEXAME + IDPRD>  (PK) |  |
| **02** | <CODCOLIGADA + CODEXAME>  (FK) | SZLABEXAME |
| **03** | <CODCOLIGADA + IDPRD> (FK) | SZPRD |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| SZEXAMEMATMED | CODCOLIGADA | DCODCOLIGADA |  |  | Sim (X) Não ( ) | Código da Coligada |
| SZEXAMEMATMED | IDPRD | Inteiro |  |  | Sim (X) Não ( ) | Id. do produto |
| SZEXAMEMATMED | CODEXAME | Inteiro |  |  | Sim (X) Não ( ) | Código do Exame |
| SZEXAMEMATMED | QTD | RMDVALOR4 |  |  | Sim (X) Não ( ) | Quantidade na unidade de controle |
| SZEXAMEMATMED | OPCAO | CHAR | 1 |  | Sim (X) Não ( ) | Opção entre Gera movimentação de estoque   ou Somente lança na conta do paciente |

Tabela: SZRELEXAMEMOVIESTOQUE

|  |  |  |
| --- | --- | --- |
| **Índice** | **Chave** | Tabela de Referência |
| **01** | <CODCOLIGADA + SEQ> (PK) |  |
| **02** | <CODCOLIGADA + ORDEMSERVICO + CODEXAME + SEQEXAME> (FK) | SZPEDEXAMEITEM |
| **03** | <CODCOLIGADA + CODREQUISICAO + SEQUENCIAL> (FK) | SZMOVIESTOQUEITEM |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| SZRELEXAMEMOVIESTOQUE | CODCOLIGADA | DCODCOLIGADA |  |  | Sim (X) Não ( ) | Código da Coligada |
| SZRELEXAMEMOVIESTOQUE | SEQ | Inteiro |  |  | Sim (X) Não ( ) | Sequencial |
| SZRELEXAMEMOVIESTOQUE | ORDEMSERVICO | Inteiro |  |  | Sim (X) Não ( ) | Ordem de Serviço |
| SZRELEXAMEMOVIESTOQUE | CODEXAME | Inteiro |  |  | Sim (X) Não ( ) | Código do Exame |
| SZRELEXAMEMOVIESTOQUE | SEQEXAME | Inteiro |  |  | Sim (X) Não ( ) | Sequencial do exame |
| SZRELEXAMEMOVIESTOQUE | CODREQUISICAO | Inteiro |  |  | Sim (X) Não ( ) | Código da requisção |
| SZRELEXAMEMOVIESTOQUE | SEQUENCIAL | Inteiro |  |  | Sim (X) Não ( ) | Sequencial do item requisitado |

Tabela: SZRELEXAMEMATMEDCONTA

|  |  |  |
| --- | --- | --- |
| **Índice** | **Chave** | Tabela de Referência |
| **01** | <CODCOLIGADA + SEQ> (PK) |  |
| **02** | <CODCOLIGADA + ORDEMSERVICO + CODEXAME + SEQEXAME> (FK) | SZPEDEXAMEITEM |
| **03** | <CODCOLIGADA + NUMEROCONTA+ SEQUENCIALCONTA + SEQPACIAL + SEQDEBITO> (FK) | SZATENDMATMED |

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Tabela** | **Campo** | **Tipo** | **Tamanho** | **Valor Inicial** | **Mandatório** | **Descrição** |
| SZRELEXAMEMATMEDCONTA | CODCOLIGADA | DCODCOLIGADA |  |  | Sim (X) Não ( ) | Código da Coligada |
| SZRELEXAMEMATMEDCONTA | SEQ | Inteiro |  |  | Sim (X) Não ( ) | Sequencial |
| SZRELEXAMEMATMEDCONTA | ORDEMSERVICO | Inteiro |  |  | Sim (X) Não ( ) | Ordem de Serviço |
| SZRELEXAMEMATMEDCONTA | CODEXAME | Inteiro |  |  | Sim (X) Não ( ) | Código do Exame |
| SZRELEXAMEMATMEDCONTA | SEQEXAME | Inteiro |  |  | Sim (X) Não ( ) | Sequencial do exame |
| SZRELEXAMEMATMEDCONTA | NUMEROCONTA | VARCHAR | 14 |  | Sim (X) Não ( ) | Número da conta |
| SZRELEXAMEMATMEDCONTA | SEQUENCIALCONTA | Inteiro |  |  | Sim (X) Não ( ) | Sequencial da conta |
| SZRELEXAMEMATMEDCONTA | SEQPARCIAL | Inteiro |  |  | Sim (X) Não ( ) | Sequencial da parcial |
| SZRELEXAMEMATMEDCONTA | SEQDEBITO | Inteiro |  |  | Sim (X) Não ( ) | Sequencial do débito |

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
