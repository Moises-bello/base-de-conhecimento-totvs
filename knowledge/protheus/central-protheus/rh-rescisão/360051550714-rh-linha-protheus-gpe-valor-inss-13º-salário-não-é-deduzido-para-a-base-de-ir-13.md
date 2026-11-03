---
article_id: 360051550714
category: RH - Rescisão
content_hash: a268774b103cacebdf250bc81d5179df6b5e4e46f3c3b22a24be5abdab0dfafa
fetched_at: '2026-06-28T22:43:50.943196+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Valor INSS 13º salário não é deduzido para a base
  de IR 13º salário em rescisão
type: support-article
updated_at: '2025-06-13T11:50:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360051550714-RH-Linha-Protheus-GPE-Valor-INSS-13%C2%BA-sal%C3%A1rio-n%C3%A3o-%C3%A9-deduzido-para-a-base-de-IR-13%C2%BA-sal%C3%A1rio-em-rescis%C3%A3o
---

**Ocorrência**Valor INSS 13º salário não é deduzido para a base de IRRF 13º salário em rescisão.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - GPE Gestão de Pessoal - Todas as versões.  
  
**Causa**O incidente ocorre, pois o id 0169 não está configurado corretamente.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Entre na rotina Verbas pelo caminho >Atualizações >Definições de Cálculo >Verbas;  
2, Na aba incidências, para os campos RV\_IR e campo RV\_REF13 deixe com Sim;  
3. Exclua a rescisão e calcule novamente, o valor INSS será deduzido corretamente para a base 13º salário.
