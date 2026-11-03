---
article_id: 360019196851
category: Originação de Grãos (OG)
content_hash: 37aeb521427219a5d64d9c977d13b5acc7b539223e92781e861992f1393d85c4
fetched_at: '2026-06-28T22:45:44.748215+00:00'
product: protheus
section_id: 360005717833
source: central-protheus
title: Agro - Linha Protheus - AGR - Reabertura de Romaneio de saída já confirmado
type: support-article
updated_at: '2025-06-26T11:14:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019196851-Agro-Linha-Protheus-AGR-Reabertura-de-Romaneio-de-sa%C3%ADda-j%C3%A1-confirmado
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20642116488727)**Tempo aproximado para leitura: **00:00:35 min  
  
Dúvida**Como efetuar e reabertura de OGA250 - Romaneio com Pesagem e OGA251 - Romaneio sem Pesagem, de saída já confirmado?  
  
 **Ambiente**TOTVS Agro - TOTVS Agro - Comercialização (Linha Protheus) - Originação de Grãos (OG) - Versão 12  
  
**Solução**  
Para que seja possível reabrir um romaneio de Saída já confirmado realize os seguintes passos:

**1.** Acesse o romaneio que necessita ser reaberto e verifique a numeração da **Nota Fiscal** e a numeração do **Pedido de Venda**na aba de **Comercialização**;

**2.** Acesse a rotina **MATA521A** - **Exclusão de Documento de Saída** e exclua a **Nota Fiscal de Saída** gerada pelo romaneio;

**3.** Acesse a rotina **MATA410** - **Pedidos de Venda**e exclua o Pedido de Venda gerado pelo romaneio;

**4.** Acesse novamente o registro de romaneio que necessita ser reaberto e por meio das **Outras** **Ações** selecione a opção **Reabrir**. O romaneio será reaberto e as alterações necessárias poderão ser efetuadas.
