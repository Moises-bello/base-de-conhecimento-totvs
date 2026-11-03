---
article_id: 360047230174
category: Comércio Exterior - Easy Export Control - Financeiro
content_hash: 385dc9e99683481a6dae0c9f1ea7949c5cd5fa972b5a95a22bfc1c5ade0cc1d4
fetched_at: '2026-06-28T22:36:58.149623+00:00'
product: protheus
section_id: 1500001538221
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEEC - Preenchimento
  do campo EEQ_DESCON
type: support-article
updated_at: '2022-06-10T21:22:41Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047230174-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEEC-Preenchimento-do-campo-EEQ-DESCON
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Ao preencher o campo EEQ\_DESCON o valor é considerado no E1\_VALOR?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Export Control* – A partir da versão 11.80  
  
**Solução**Ao informar o campo EEQ\_DESCON este não irá modificar o valor da parcela no campo E1\_VALOR. O valor de desconto (EEQ\_DESCON) será preenchido ao realizar a liquidação do título.   
Verifique que o Vl. a Receber será alterado de acordo com o Desconto informado:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069903593/mceclip0.png)

Ao verificar a posição do título no SIGAFIN, o valor do desconto será preenchido na SE5:  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360069903713/mceclip1.png)
