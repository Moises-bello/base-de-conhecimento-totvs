---
article_id: 360024411712
category: Ativo Fixo - Aquisição por Transferência
content_hash: 4681de2cab9ec3f9e63d6d103c4a958033b85f47b9b87d7eb29a39de448021f0
fetched_at: '2026-06-28T22:41:56.943829+00:00'
product: protheus
section_id: 1500001535341
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA251 - Help: AF250DATAT'
type: support-article
updated_at: '2023-11-20T16:12:40Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024411712-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA251-Help-AF250DATAT
---

***Dúvida***

*Ao processar a rotina de Aquisição por transferência o sistema apresenta a mensagem abaixo:*

*AF250DATAT*

*"A transferência deve ser feita no dia do cálculo da depreciação após a execução, ou no mês posterior a data do último cálculo de depreciação."*

*![](https://centraldeatendimento.totvs.com/hc/article_attachments/360022974752)*

**Ambiente**  
Microsiga Protheus – ativo fixo  – A partir da versão 11.80  
  
  
**Solução**

Para que a situação não seja apresentada deve ser analisado quando foi feito o último calculo de depreciação  mensal.

Ao acessar a rotina ATFA050 verifique a última data de processamento (Controle feito pelo parâmetro MV\_ULTDEPR). A movimentação só será permitida, à partir do primeiro dia, do mês seguinte.
