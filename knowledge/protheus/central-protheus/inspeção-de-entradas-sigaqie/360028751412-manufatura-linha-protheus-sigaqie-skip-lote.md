---
article_id: 360028751412
category: Inspeção de Entradas (SIGAQIE)
content_hash: 3a34678d97d86e4c3074e9c650609d0995a099802842a8fc2d490301a5e0fc90
fetched_at: '2026-06-28T22:42:27.169573+00:00'
product: protheus
section_id: 360005876674
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIE - Skip-lote
type: support-article
updated_at: '2026-06-02T17:24:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028751412-Manufatura-Linha-Protheus-SIGAQIE-Skip-lote
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24294510943767)**Tempo aproximado para leitura: **00:02:30 min****Dúvida**Como configurar o **Skip-lote**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Entradas (SIGAQIE) - Todas as versões  
  
**Solução**Para iniciar a utilização do **Skip-lote** no módulo **SIGAQIE - Inspeção de Entradas**, seguir os tópicos abaixo:

* No **SIGACFG - Configurador**, informar um conteúdo para o parâmetro **MV\_QSKLENT - No. de entregas iniciais para a aplicacao do Skip-lote**. Por exemplo, se o parâmetro estiver com conteúdo igual à **3**, indica que é necessário possuir 3 entradas de inspeção para ser considerado no **Skip-lote**. Se estiver como **0**, indica que a cada entrada de inspeção será considerada no **Skip-lote**;
* Na rotina **MATA010 - Atualização de Produtos**, cadastrar um novo produto, e na aba **C.Q.** informar o campo **Tipo de C.Q.** como **SigaQuality**;
* Na rotina **QIEA010 - Especificação de Produtos**, cadastrar uma especificação para este produto;
* Na rotina **MATA061 - Atualização Produto x Fornecedor**, relacionar um fornecedor para este produto, preenchendo os seguintes campos:
  + **Situação****:**Situação do fornecedor para este produto, indicando o nível de qualidade do mesmo.
  + **Skip-lote:** Regime de **Skip-lote**, que determina a quantidade de entradas controladas.
  + **Tempo Limite:** Tempo limite máximo em meses, entre duas entregas consecutivas para que o regime de **Skip-lote** definido ao fornecedor e produto seja mantido.
  + **Fab/Rev/Perm:** Indica se o fornecedor é o fabricante, revendedor ou somente faz a permuta do produto.
  + **Atualiza:** Indica se o produto e fornecedor terá a situação e o **Skip-lote** atualizados automaticamente pelo Sistema.
  + ****Tipo Atualiz:**** Todos, **Skip-lote** ou situação.
* Na rotina **MATA103 - Documento de Entrada**, incluir um documento de entrada para este produto e fornecedor. No campo **Tipo Entrada** deve ser informada uma **TES - Tipo de Entrada e Saída** que movimente estoque, ou seja, que o campo **Atu. Estoque** esteja como **Sim**;
* Acessar a rotina **QIEA215 - Cadastro de Resultados** e verificar que é gerado um registro para inspeção com a legenda na cor **verde** - **Laudo Aprovado**. Esta cor de legenda indica que o registro entrou no conceito de **Skip-lote**, caso contrário, a legenda estaria na cor **cinza** - **Entrada sem medições cadastradas**.

**Importante**Para que seja permitido informar a situação do fornecedor na rotina **MATA061** é necessário que o parâmetro **MV\_QASSIQS - Situacao do Produto X Fornecedor pode ter categoria Skip-Lote Total se o Fornecedor nao tiver nota de IQS?** esteja com conteúdo igual à **S - Sim**.
