---
article_id: 360052751274
category: Comércio Exterior - Easy Import Control - Desembaraço
content_hash: d593f28a0cd662b510f6c5dcbdc677dcd50d1559ec8645ef1f0ab509bc9cf698
fetched_at: '2026-06-28T22:39:50.113914+00:00'
product: protheus
section_id: 1500001549442
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Mensagem: Processo
  possui Nota Fiscal Unica, despesas diferentes de 902 e 903 não podem serem lançadas.'
type: support-article
updated_at: '2022-04-27T20:48:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052751274-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Mensagem-Processo-possui-Nota-Fiscal-Unica-despesas-diferentes-de-902-e-903-n%C3%A3o-podem-serem-lan%C3%A7adas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Como corrigir a mensagem: Processo possui Nota Fiscal Única, despesas diferentes de 902 e 903 não podem serem lançadas. , ao incluir uma despesa?  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087656533/mceclip0.png)  
   
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**No Desembaraço , ao incluir uma despesa para a nota Única com o parâmetro **MV\_AVG0160** habilitado, a rotina apresentará a mensagem:   
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360087656533/mceclip0.png)  
Permitindo apenas inserir despesas 902 e 903. Sendo assim, para incluir despesas é necessário desabilitar o parâmetro **MV\_AVG0160**.
