---
article_id: 24819040138775
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 10bd4f8e63ccfe687560f047c971d074a5a2bb8d2aeafcdfd1b11e6a7bfb2c68
fetched_at: '2026-06-28T22:38:44.087184+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - NF (Nota Fiscal de Venda)
  e NFS (Nota Fiscal de Serviço) no mesmo pedido de venda
type: support-article
updated_at: '2024-07-11T17:44:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24819040138775-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-NF-Nota-Fiscal-de-Venda-e-NFS-Nota-Fiscal-de-Servi%C3%A7o-no-mesmo-pedido-de-venda
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24819051426967) Tempo aproximado para leitura: **00:02:30 min** **Dúvida**É possível emitir NF (Nota Fiscal de Venda) e NFs (Nota Fiscal de Serviço) no mesmo pedido de venda?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**Há como, porém não no mesmo faturamento ou no mesmo item, pois no faturamento, eles irão gerar conteúdos diferentes, um gerará modelo de NFS para a prefeitura local e o outro uma DANFE.

É possível ter duas linhas no pedido de venda:

* Faturar a primeira como nota normal primeiramente.
* Faturar a linha dois em outro faturamento como nota de serviço (com TES de serviço).

Outra opção menos usual:

* Faturar metade do mesma linha de item como nota normal primeiramente.
* Trocar a TES do pedido de venda para uma TES de Serviços, faturar o restante do mesmo item na mesma linha anterior como nota de serviço.

**OBSERVAÇÃO 1:** Em ambas situações, o faturamento dos itens não são ao mesmo tempo, por conta da finalidade, tem de ser um primeiro em seguida, o outro, por exemplo.

**OBSERVAÇÃO 2:** Em casos de rejeição na transmissão, orientamos que contate a Equipe SPED/TSS.

**Saiba mais:**

* [Cross Segmentos-TOTVS Backoffice (Linha Protheus)-SIGAFAT - Configuração básica de nota de serviço](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360063295573-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Configura%C3%A7%C3%A3o-b%C3%A1sica-de-nota-de-servi%C3%A7o)
* [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Nota de débito e crédito - Ambiente Brasil](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044977413-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Nota-de-d%C3%A9bito-e-cr%C3%A9dito-Ambiente-Brasil)
* [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como ter acesso as notas emitidas](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008104422-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-ter-acesso-as-notas-emitidas)
* [Cross Segmentso - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Como fazer liberação parcial do pedido de venda para faturamento](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360036133173-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Como-fazer-libera%C3%A7%C3%A3o-parcial-do-pedido-de-venda-para-faturamento)
* [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Verificar Pedido com Liberação Parcial](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500007495161-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Verificar-Pedido-com-Libera%C3%A7%C3%A3o-Parcial)
* [Cross Segmentos - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Comportamento do campo “Qtd. Liberada” (C6\_QTDLIB)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/10409483539223-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Comportamento-do-campo-Qtd-Liberada-C6-QTDLIB)
