---
article_id: 4421539714583
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 6734aae9c434111099b1d87bbd1062fab5bf6801a13fb3fddd3e1b3d06f316d6
fetched_at: '2026-06-28T22:39:41.084292+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Campo Saldo Qtde
  no Purchase Order
type: support-article
updated_at: '2024-02-02T16:30:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4421539714583-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Campo-Saldo-Qtde-no-Purchase-Order
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21070971972759)Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Qual a função do campo "**Saldo Qtde"** (W3\_SALDO\_Q) no *Purchase Order*?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – Easy Import Control – Todas versões  
  
**Solução**A informação presente neste campo se refere ao saldo disponível do item entre o **PO** (*Purchase Order*) e a **LI** (Licença de Importação).  
Se o item não for anuente, será criada uma **PLI**(Preparação da Licença de Importação) automática e por isso esse campo fica zerado. Caso o item seja anuente, esse campo deve controlar a quantidade do item que não tem **PLI** ainda.
