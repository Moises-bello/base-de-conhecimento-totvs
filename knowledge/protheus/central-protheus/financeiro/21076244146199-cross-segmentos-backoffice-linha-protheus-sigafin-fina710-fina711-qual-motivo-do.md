---
article_id: 21076244146199
category: Financeiro
content_hash: 5c961f233d796b5223c3105f4d55d7230139d838306fb0ba27f47ae945d95f00
fetched_at: '2026-06-28T22:38:03.102485+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice linha Protheus - SIGAFIN - FINA710 FINA711 - Qual
  motivo do job FINA711 excluir um pedido antigo na tabela "F76 Saldos de Pedidos
  por Data" e depois incluir novamente?
type: support-article
updated_at: '2024-02-02T21:09:04Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21076244146199-Cross-Segmentos-Backoffice-linha-Protheus-SIGAFIN-FINA710-FINA711-Qual-motivo-do-job-FINA711-excluir-um-pedido-antigo-na-tabela-F76-Saldos-de-Pedidos-por-Data-e-depois-incluir-novamente
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244116759) Tempo aproximado para leitura: **00:15: min****Dúvida**Qual motivo do job FINA711 excluir um pedido antigo na tabela "F76 Saldos de Pedidos por Data" e depois incluir novamente?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da P12.1.2210

**Solução:**

A rotina FINA710 - Novo Fluxo de Caixa, somente mostra em tela pedidos com data de entrega de hoje para frente, não mostra em tela pedidos com data de entrada anteriores a hoje (data de entrada vencida), por esse motivo nessas condições, ao executar o job FINA711, esse irá atualizar a data na tabela F76 Saldos de Pedidos por Data" para o pedido voltar a ser mostrado no FINA710 - Novo Fluxo de Caixa

**Exemplo 1:**

A database (data do dia de hoje é **02/02/2024**)

E tenho um pedido no valor de R$ 10mil onde o campo da data de entrega é **C6\_ENTREG = 02/02/2024**

Quando for executado o job FINA711 na mesma data base, será levado o conteúdo do campo **C6\_ENTREG** para o campo **F76\_DATA = 02/02/2024**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21076223829527)](https://centraldeatendimento.totvs.com/hc/article_attachments/21076223829527)

FINA710 - Novo Fluxo de Caixa > Movimentação financeira > Geral, será apresentando assim:

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244119447)](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244119447)

FINA710 - Novo Fluxo de Caixa > Movimentação financeira > Consolidado

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21076223831575)](https://centraldeatendimento.totvs.com/hc/article_attachments/21076223831575)

**Exemplo 2:**

A database (data do dia de hoje é **01/02/2024**)

E tenho um pedido no valor de R$ 10mil onde o campo da data de entrega é **C6\_ENTREG = 01/02/2024**

Quando foi executado o job FINA711 na mesma data base, será levado o conteúdo do campo **C6\_ENTREG** para o campo **F76\_DATA****= 01/02/2024**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244121367)](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244121367)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244121879)](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244121879)

O dia atual agora é **02/02/2024**

A database (data do dia de hoje é **02/02/2024**), porém hoje dia **02/02/2024** não foi executado o meu meu job FINA711 ainda.

Veja que esse pedido não será apresentando mais no FINA710 Novo Painel Gestor

FINA710 - Novo Fluxo de Caixa > Movimentação financeira > Geral.

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21076223836567)](https://centraldeatendimento.totvs.com/hc/article_attachments/21076223836567)

FINA710 - Novo Fluxo de Caixa > Movimentação financeira > Consolidado

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244123799)](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244123799)

Para esse pedido antigo ser apresentado (data de entrega vencida) terei que executar o job FINA711 (data do dia de hoje é **02/02/2024**)

Quando o Job for executado, irá deletar o pedido na tabela "F76 Saldos de Pedidos por Data" e criando um novo com um novo conteúdo no campo **F76\_DATA = 02/02/2024**

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244124311)](https://centraldeatendimento.totvs.com/hc/article_attachments/21076244124311)

E esse pedido voltará a ser apresentando no "FINA710 - Novo Painel Gestor" como foi mostrado no **Exemplo 1**

Mais informações sobre o processo acima:

[Gravação da tabela F76 - FINA711](https://tdn.totvs.com/pages/releaseview.action?pageId=709395826)

[![](https://centraldeatendimento.totvs.com/hc/article_attachments/21076223842071)](https://tdn.totvs.com/pages/releaseview.action?pageId=709395826)
