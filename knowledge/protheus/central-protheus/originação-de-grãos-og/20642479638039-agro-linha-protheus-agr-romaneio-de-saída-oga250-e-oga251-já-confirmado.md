---
article_id: 20642479638039
category: Originação de Grãos (OG)
content_hash: fc7cc853761041cda9d2be6e7792eba428d4b29eb916d07b343e2c92aa11927b
fetched_at: '2026-06-28T22:45:44.830067+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Romaneio de saída OGA250  e OGA251 já confirmado
type: support-article
updated_at: '2025-06-24T11:39:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/20642479638039-Agro-Linha-Protheus-AGR-Romaneio-de-sa%C3%ADda-OGA250-e-OGA251-j%C3%A1-confirmado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20642479617559) Tempo aproximado para leitura: **00:00:45 min****Ocorrência**  
No módulo Faturamento, ao realizar o processo para reabrir um romaneio de saída **com pesagem** ou **sem pesagem** é apresentada a ocorrência **Romaneio de saída OGA250  e OGA251 já confirmado**.  
**Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Causa**  
Esse incidente ocorre, pois é preciso realizar o processo para reabrir um romaneio de saída **com pesagem** ou **sem pesagem** no Sistema.  
  
**Solução**  
Para solucionar essa ocorrência, será preciso reabrir um romaneio de Saída já confirmado, realize os seguintes passos:

**1.** Acesse o romaneio que necessita ser reaberto e verifique a numeração da **Nota Fiscal** e a numeração do **Pedido de Venda**na aba de **Comercialização**;

**2.** Acesse a rotina **MATA521A** - **Exclusão de Documento de Saída** e exclua a Nota Fiscal de Saída gerada pelo romaneio;

**3.** Acesse a rotina **MATA410** - **Pedidos de Venda**e exclua o Pedido de Venda gerado pelo romaneio;

**4.** Acesse novamente o registro de romaneio que necessita ser reaberto e por meio das **Outras** **Ações** selecione a opção **Reabrir**. O romaneio será reaberto e as alterações necessárias poderão ser efetuadas.
