---
article_id: 24631492211095
category: Financeiro
content_hash: f1aee96846cc506b4fba862db2809be31d2c9e5ca47bb2d45c78305c65123f57
fetched_at: '2026-06-28T22:38:03.136908+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Nosso Número
  Santander
type: support-article
updated_at: '2024-07-08T18:22:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24631492211095-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Nosso-N%C3%BAmero-Santander
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24631492192407) Tempo aproximado para leitura: **01:00 min** **Dúvida**Diferença entre o nosso número gerado no Protheus e o registrado no banco Santander?  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - Todas as versões  
  
**Solução**Deve ser observado a seguinte regra: Na transmissão da comunicação via XML do banco Santander:

Nosso Número: será enviado ao banco um sequencial de 13 posições, composto pela seguinte regra: sequencial (12 posições) + digito verificador do sequencial (1 posição)

Ex.: Nosso Número com sequencial 999999999999 será enviado como 9999999999996 sendo o número 6 o digito verificador.

**Saiba Mais**

**[JOB e Transmissão via E-mail - FINA713](https://tdn.totvs.com/pages/releaseview.action?pageId=619130482)**

**[Santander - Comunicação Bancária](https://tdn.totvs.com/pages/releaseview.action?pageId=653588365)**
