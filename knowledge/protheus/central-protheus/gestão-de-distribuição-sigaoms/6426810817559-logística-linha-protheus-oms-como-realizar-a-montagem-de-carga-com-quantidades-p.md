---
article_id: 6426810817559
category: Gestão de Distribuição (SIGAOMS)
content_hash: c5d787835eb232cc8b0d9fddc24b0a0674838e3922ea3f1bfcc78c65c506dfef
fetched_at: '2026-06-28T22:45:49.743759+00:00'
product: protheus
section_id: 206957088
source: central-protheus
title: Logística - Linha Protheus - OMS - Como realizar a montagem de Carga com quantidades
  parciais
type: support-article
updated_at: '2022-05-30T20:54:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6426810817559-Log%C3%ADstica-Linha-Protheus-OMS-Como-realizar-a-montagem-de-Carga-com-quantidades-parciais
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Como realizar a **Montagem de Carga com quantidades parciais**?  
  
**Ambiente**TOTVS Logística - TOTVS OMS (Linha Protheus) - Gestão de Distribuição (SIGAOMS) - Todas as versões  
  
**Solução**No **TOTVS OMS - Order Management System**, para criar uma carga, a rotina se baseia na tabela **SC9 -Pedidos Liberados**, onde os pedidos deverão estar totalmente liberados. A rotina **OMSA200 - Montagem de Carga**, possibilita a geração de carga com **quantidades parciais**, ou seja, **utilizar parte das quantidades liberadas no pedido de venda**. Abaixo descrevemos um exemplo de utilização:

* Acesse a rotina **OMSA200 - Montagem de Carga/Carregamento/Montagem de Carga**.  
  Neste momento é possível configurar quais pedidos devem ser apresentados para **Montagem da Carga**, filtrando também por cliente e demais propriedades de acordo com a necessidade.
* Selecione o **Pedido** que deseja gerar **Carga de uma quantidade parcial**.
* Com o **Pedido** selecionado, acesse o botão **Outras Ações/Botão Div. item.** Acionando esse botão poderá **informar a quantidade de quebra do item.**

****![omsa200_1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/6427591184535/omsa200_1.png)****

* Veja que o Sistema passa apresentar as linhas do pedido conforme a quantidade que foi quebrada:

**![omas200_2.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/6427677424919/omas200_2.JPG)**

* Nesse momento, basta **selecionar a sequencia que deseja incluir na Carga**, em seguida poderá seguir fluxo do seu processo até o **Faturamento da Carga**, utilizando quantidades parciais da **Liberação de Pedidos de Venda**.

**Saiba mais**Maiores informações sobre a rotina **OMSA200 - Montagem de Carga**, poderão ser acessadas no *link:*[Montagem de Carga - OMSA200 - SIGAOMS](https://tdn.totvs.com/pages/releaseview.action?pageId=551446517)
