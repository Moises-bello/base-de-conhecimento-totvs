---
article_id: 21822563515799
category: Financeiro - Aplicação / Emprestimos
content_hash: 665d7c388af04e74ff5829d1bcf243a58af0976f1cafe098aac9b1212f374c0e
fetched_at: '2026-06-28T22:37:59.532386+00:00'
product: protheus
section_id: 1500001550542
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA716 - Help: Contrato
  já existe na base de dados'
type: support-article
updated_at: '2024-03-07T21:54:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21822563515799-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA716-Help-Contrato-j%C3%A1-existe-na-base-de-dados
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21822563498263) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Ao incluir um empréstimo e apresentado Help: Contrato já existe na base de dados..  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA716 - A partir da versão 2210  
  
**Solução**A rotina pega a sequencia pelo o controle de numeração mas para saber qual realmente é a próxima no seu banco faça *select* no seu e veja com foi o ultimo numero.   
   
**SELECT MAX(EH\_*****NUMERO) MAXNUMPR FROM SEH010 WHERE D\_*****E\_*****L\_*****E\_*****T\_*****= ' '**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/21822563499543)

Ajuste o controle de numeração para que o help não seja mais apresentado.

**Saiba mais:**

<https://tdn.totvs.com/pages/releaseview.action?pageId=680254799>
