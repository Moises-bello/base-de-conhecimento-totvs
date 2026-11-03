---
article_id: 17723026209175
category: Financeiro - Reinf
content_hash: fc13ef3b23b265d9e2c03dad034af0b319bddd725d72cfc21ef4361e9141d08e
fetched_at: '2026-06-28T22:37:51.793127+00:00'
product: protheus
section_id: 17886892336407
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - REINF - Como enviar
  os rendimentos sem retenção de tributos, lucros e dividendos
type: support-article
updated_at: '2023-09-29T14:24:24Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/17723026209175-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-REINF-Como-enviar-os-rendimentos-sem-reten%C3%A7%C3%A3o-de-tributos-lucros-e-dividendos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/17723041932183) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como enviar os rendimentos sem retenção de tributos, lucros e dividendos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro – A partir da release 12.1.33  
  
**Solução**

Temos casos previstos na legislação em que há a obrigatoriedade da prestação de informação de rendimentos sem **retenção de imposto de renda na EFD-REINF bloco 40**. Deve ser enviada a informação do valor do pagamento e sua respectiva classificação de **Natureza de Rendimento**.

Por exemplo, caso haja pagamento de **lucros e dividendos**, o contribuinte deverá informar a **natureza de rendimento** “**12001**” no **título a pagar** ou **documento de entrada**, os registros não deveram estar configurado para **reter imposto**.

Como o **fato gerador** para esses casos é o pagamento, o **título a pagar** deve estar **baixado** e a data de envio para o **TAF** será a **data da baixa** (será gerado os dados no **layout T158** do **TAF**).
