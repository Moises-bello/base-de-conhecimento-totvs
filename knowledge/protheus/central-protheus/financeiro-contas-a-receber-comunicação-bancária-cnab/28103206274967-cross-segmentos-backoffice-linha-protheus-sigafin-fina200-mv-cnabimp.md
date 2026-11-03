---
article_id: 28103206274967
category: Financeiro - Contas a Receber - Comunicação Bancária CNAB
content_hash: 494ee5c19ecb0c6a079eec421eea53eda6af7125269881c8dd7245e3b9dcd2b6
fetched_at: '2026-06-28T22:37:48.012970+00:00'
product: protheus
section_id: 26656449081111
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA200 - MV_CNABIMP
type: support-article
updated_at: '2026-03-25T19:44:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/28103206274967-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA200-MV-CNABIMP
---

![relogio_tempo_leitura_2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/28103206267287) Tempo aproximado para leitura: **00:03:00 min**  
  
**Dúvida**

Qual é a finalidade do parâmetro **MV\_CNABIMP**?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA200 - Todas as versões.

**Solução**

O parâmetro **MV\_CNABIMP** determina se a rotina de Retorno de Cobranças (FINA200) deve gerar e baixar os impostos, conforme definidos no pagamento, ao realizar a baixa do título principal, ou se deve apenas registrar o lançamento do título principal, comportamento padrão.

**Este parâmetro pode ser configurado com as seguintes opções:**

**.T.** (True/Verdadeiro) para gerar e baixar os impostos na baixa CNAB, e

**.F.** (False/Falso) para não gerar os impostos. Por padrão, o parâmetro é inicializado com **.F.**

**Saiba mais**

[MV\_CNABIMP - Geração de impostos no processamento do CNAB - Contas a Receber](https://tdn.totvs.com/pages/releaseview.action?pageId=152802224)
