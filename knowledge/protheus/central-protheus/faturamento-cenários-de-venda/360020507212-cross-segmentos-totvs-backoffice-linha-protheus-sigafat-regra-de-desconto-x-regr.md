---
article_id: 360020507212
category: Faturamento - Cenários de Venda
content_hash: 4981638fe97f0496f691375b5eb46bdad280763cf9683f3b4ef08ffb7531ba9a
fetched_at: '2026-06-28T22:38:34.071742+00:00'
product: protheus
section_id: 1500001550382
source: central-protheus
title: Cross Segmentos - TOTVS Backoffice (linha Protheus) - SIGAFAT - Regra de Desconto
  X Regra de Negócio
type: support-article
updated_at: '2022-12-12T15:02:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360020507212-Cross-Segmentos-TOTVS-Backoffice-linha-Protheus-SIGAFAT-Regra-de-Desconto-X-Regra-de-Neg%C3%B3cio
---

**Dúvida**

Qual a hierarquia da regra de negócio e regra de desconto?  
  
**Ambiente**

Cross Segmentos - TOTVS Backoffice (linha Protheus) - SIGAFAT - Todas as versões  
  
**Solução**

Entre a Regra de Negócio e a Regra de Desconto não há hierarquia, pois elas tem funções diferentes.

A Regra de Desconto tem a função de **sugerir** um valor de desconto.  
A Regra de Negócio tem a função de **bloquear** o pedido se entrar nas condições da regra.

**Exemplo**:

Se você tem uma regra de desconto de 10% e uma regra de negocio de 9%.  
O sistema ira preencher os 10% sugerido, porem ira bloquear na regra de negócio pois ultrapassa os 9%.

**Saiba Mais:** [Precificação no módulo Faturamento](https://tdn.totvs.com/x/GkNyFw)
