---
article_id: 235078488
category: SIGAEST - MOVIMENTAÇÕES
content_hash: 44dd996dd5b034fc3a8dc78d5618541f205d7f13543d8ec7c85854f0c45439ae
fetched_at: '2026-06-28T22:38:53.967249+00:00'
product: protheus
section_id: 1500001550102
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Como são gravados
  dados de Movimentos e Saldos de Lotes e Sublotes?
type: support-article
updated_at: '2025-11-14T16:56:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235078488-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-s%C3%A3o-gravados-dados-de-Movimentos-e-Saldos-de-Lotes-e-Sublotes
---

No Protheus, os dados de movimentação e saldo de lotes e sublotes são gravados principalmente nas tabelas SB8 (Saldo por Lote/Sublote) e SD5 (Movimentações por Lote). Produtos com controle por lote atualizam o campo Lote, e os com controle por sublote atualizam Lote e Sublote. O controle de rastreabilidade é ativado pelo parâmetro MV\_RASTRO e configurado no cadastro do produto. Movimentos fiscais e internos são registrados simultaneamente nas tabelas principais (SD1, SD2, SD3) e em SD5 para rastreabilidade detalhada.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36340615889047) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida:**

Como são gravados os dados de movimentação e saldo de lotes e sublotes? Qual a funcionalidade das tabelas SD5 e SB8?

**Ambiente:**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução:**

A partir da implantação do controle de Rastreabilidade no Protheus, existem algumas tabelas exclusivas para tratar o controle de rastreabilidade de lotes e sublotes, sendo elas: **SB8 - Saldo por Lote/Sublote** e **SD5 - Movimentações de Lote/Sublote**.

Por isso, sempre são gravados os campos **Lote** (**\_LOTCTL**) e **Sublote** (**\_NUMLOTE**), este segundo quando o tipo de rastreabilidade do produto é por Sublote.

Nas demais tabelas de dados utilizadas (**SD1**, **SD2**, **SD3**, etc.), o Sistema adota a seguinte regra:

* Produtos com controle de rastreabilidade por lote, somente é atualizado o campo **Lote** (**??\_LOTCTL**).
* Produtos com controle de rastreabilidade por sublote, são atualizados os campos **Lote** (**??\_LOTCTL**) - e **Sublote** (**??\_NUMLOT**)*.*

**Tipos de Saldos e Movimentos:**

* **Saldos e Movimentos Físicos**

O controle para este tipo de saldo, controla a quantidade física disponível no armazém.  
Seu saldo é alimentado pelos Documentos de Entrada/Saída e pelos Movimentos  
Internos.

Tabelas envolvidas:

* SB9 – Saldos Iniciais
* SB2 – Saldos Físico e Financeiro
* SD1 – Itens da NF de Entrada
* SD2 – Itens da NF de Saída
* SD3 – Movimentos Internos
* SD4 - Bloqueios/Empenhos

* **Saldo e Movimentos por Rastreabilidade**

Utiliza-se o controle para este tipo de saldo (Lote/SubLote) para controlar a rastreabilidade e a data de validade de seus produtos dentro do armazém. Para ativar o Controle de Saldos por rastreabilidade, configure o parâmetro ***MV\_RASTRO***com o conteúdo igual a **S** pelo Configurador e após esse procedimento, pela rotina Cadastro de Produtos (MATA010) altere o campo Rastro (B1\_RASTRO) para o conteúdo Lote ou SubLote.

Tabelas (e campos) envolvidos:

* SBJ – Saldos Iniciais por Lote
* SB8 – Saldos por Lote
* SD5 – Requisições por Lote
* SDD - Lotes Vencidos ou Bloqueados
* B8\_EMPENHO - Quantidade empenhada do Lote

**Detalhando os movimentos por Lote (relação entre SD1/SD2/SD3 e SD5)**

Quando o produto tem o controle de Lote/Sublote, o Sistema trata em uma tabela diferenciada todas as movimentações internas e fiscais feitas para o lote. Portanto, quando o produto tem movimento de Nota Fiscal de Entrada ou Saída ou qualquer Movimento Interno, além de gerar os registros nas tabelas "principais" destes movimentos (SD1/SD2/SD3), também gera um registro do movimento na tabela SD5, conforme exemplo abaixo:

**SD5 contendo dois registros de movimentação, um de quantidade 5 e outro de quantidade 1**

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411196594839)

**SD1 contendo o registro da movimentação de 5 (a primeira da tabela SD5)**

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411203548439)**

**SD3 contendo o registro da movimentação de 1 (a segunda da tabela SD5)**

**![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4411203564439)**

**Como gravar a informação no campo D5\_NUMLOTE no Protheus:**

É necessário ter um produto cadastrado como **SUBLOTE** no campo **B1\_RASTRO** e o campo **B1\_LOCALIZ** para o produto controlar endereço.

Ao incluir um saldo inicial para o produto (**MATA220**) e informar o **SubLote** e o **Lote** em outras ações.

O campo **D5\_NUMLOTE** é preenchido, segue a imagem abaixo com um exemplo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36340592101911)

Esse controle é realizado somente quando o produto controla SUBLOTE o campo **B1\_RASTRO** igual **S**.

Quando faça um Documento de Entrada com os campos do Lote e SubLote sem preenchimento, o sistema preenche automaticamente o campo **D5\_NUMLOTE** .

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36340592103191)

O seu produto por padrão tem que tem o controle por **SUBLOTE** e **Endereçamento** para gerar os dados no campo**D5\_NUMLOTE**.

**Saiba mais:**

[Backoffice (Linha Protheus) - SIGAEST - Conceito e tabelas de controle de Lote e Endereço no Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018454332-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Conceito-e-tabelas-de-controle-de-Lote-e-Endere%C3%A7o-no-Protheus)

[SIGAEST - Como descobrir a origem dos saldos na consulta com comando [F4] no Produto?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020380572-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Como-descobrir-a-origem-dos-saldos-na-consulta-com-comando-F4-no-Produto#:~:text=9%20%2D-,Quantidade%20empenhada%20(B2_QEMP),-%3A%20Empenhos%20a)

[Clique aqui e veja mais artigos sobre Movimentações no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001550102-SIGAEST-MOVIMENTA%C3%87%C3%95ES)
