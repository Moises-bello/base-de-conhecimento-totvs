---
article_id: 1500002954541
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: cb47e5779c592c736729d3bcc5d957eff84050797691b71c7a0f6ad100a1cc46
fetched_at: '2026-06-28T22:38:43.863933+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Erro na geração
  da nota fiscal de saída exportação
type: support-article
updated_at: '2023-09-18T17:32:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002954541-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Erro-na-gera%C3%A7%C3%A3o-da-nota-fiscal-de-sa%C3%ADda-exporta%C3%A7%C3%A3o
---

**Ocorrência**

Ao gerar uma nota fiscal de saída exportação, ocorre o erro:

**type mismatch on compare on MAPVL2SD2(MATA461.PRX) 17/09/2020 10:34:00 line : 5361**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**

O erro é causado por que está sendo esperado uma informação numérica para a variável **NPAREEC52**,porém,ela está recebendo uma informação caráter.

A variável **NPAREEC52** recebe a informação do parâmetro **MV\_EEC0052,** este parâmetro é do tipo **numérico**, se ele for criado como caráter gera o erro em questão

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
1. Valide se o parâmetro **MV\_EEC0052** está como **numérico**;  
2. Caso não esteja, altere de carácter para numérico ou recrie o parâmetro via configurador conforme abaixo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360104169073)

**[MTRADE-682 DT Calculo do peso bruto na Nota Fiscal de Saída com lote](https://tdn.totvs.com/pages/releaseview.action?pageId=274855235)**

3. Reinicie o Smartclient após o procedimento e realize a geração da nota fiscal de saída (**MATA461**).
