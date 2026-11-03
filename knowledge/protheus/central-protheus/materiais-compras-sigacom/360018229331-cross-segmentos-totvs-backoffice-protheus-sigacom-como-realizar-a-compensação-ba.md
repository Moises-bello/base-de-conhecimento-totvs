---
article_id: 360018229331
category: Materiais - Compras (SIGACOM)
content_hash: 1f30d02d5f4b852e9545afb2b027636c212ad91124d6dd439e9fda0e7b87c302
fetched_at: '2026-06-28T22:41:08.659941+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Como realizar a compensação
  / baixa do título de forma automática em uma NF de devolução ?
type: support-article
updated_at: '2026-03-09T15:31:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018229331-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Como-realizar-a-compensa%C3%A7%C3%A3o-baixa-do-t%C3%ADtulo-de-forma-autom%C3%A1tica-em-uma-NF-de-devolu%C3%A7%C3%A3o
---

**Dúvida**  
Como realizar a compensação / baixa do título numa devolução automática?

**Ambiente**  
Protheus  – Compras – A partir da versão 11.80

**Solução**

Para que o sistema realize a baixa automática por compensação na inclusão de um documento de entrada, entre os títulos NCC (gerado pela nota de devolução) e a Nota Fiscal (utilizando a função retornar ou incluída manualmente pela opção Incluir) é necessário que o parâmetro **MV\_CMPDEVV** esteja habilitado.

***Obs**:*

1-) Caso o parâmetro esteja ativado o sistema sempre compensará a NCC com o título da venda referente a nota de origem. Se esse título já estiver baixado, o sistema deixará a NCC em aberto para posterior utilização manualmente nas rotinas do financeiro de compensação.

2-) Não há como efetuar a escolha do título NF (receber) no momento da compensação automática, sempre será a origem (NF) com a NCC (devolução).

3-) O sistema padrão sempre efetuará a compensação automática quando o parâmetro **MV\_CMPDEVV** estiver habilitado, seja na devolução total ou parcial de uma venda. E ele verificará também o conteúdo do parâmetro MV\_CHECKNF, para verificar a carteira do título a receber. Caso haja uma devolução parcial de uma venda e, não deseje que o sistema efetue a compensação automaticamente, temos o Ponto de Entrada abaixo para este tratamento.

[**MT103BXCR**](https://tdn.totvs.com/pages/releaseview.action?pageId=583763834)

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
