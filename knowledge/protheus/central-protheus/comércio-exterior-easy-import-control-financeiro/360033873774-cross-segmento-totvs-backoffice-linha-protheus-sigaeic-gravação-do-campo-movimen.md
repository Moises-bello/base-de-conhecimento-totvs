---
article_id: 360033873774
category: Comércio Exterior - Easy Import Control - Financeiro
content_hash: 5d8d176d6c8d0f5241240cc95e6dd2c284b91e8516a87488a1733b32bb73ea08
fetched_at: '2026-06-28T22:39:44.369193+00:00'
product: protheus
section_id: 1500001549642
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Gravação do campo
  movimento gerado (E5_TIPODOC)
type: support-article
updated_at: '2022-02-10T21:53:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033873774-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Grava%C3%A7%C3%A3o-do-campo-movimento-gerado-E5-TIPODOC
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**O campo movimento gerado (E5\_TIPODOC) ao efetuar um liquidação no controle de cambio algumas vezes grava como VL ou BA?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – *Easy Import Control* – Todas versões  
  
**Solução**Verifique o motivo de baixa que esta sendo utilizado, na rotina controle de câmbio (EICAP100) , clique F12 e será apresentado a tela abaixo:  
![](https://totvssuporte.zendesk.com/attachments/token/mCmJeofemVZnNhiEbsGUbOuYF/?name=inline-1834434162.png)​  
Se o Motivo da Baixa estiver configurado como **"Mov.Bancaria" = N (Não)**, o campo **E5\_TIPODOC** é gravado "**BA**".  
Se o Motivo da Baixa estiver configurado como **"Mov.Bancaria" = S (Sim),** o campo **E5\_TIPODOC** é gravado **"VL**".  
Sobre **E5\_TIPODOC**: [Descrição E5\_TIPODOC](http://tdn.totvs.com/pages/releaseview.action?pageId=207357394)  
  
![](https://totvssuporte.zendesk.com/attachments/token/mayTYgKDcLKVXdVcW8FUS3kdM/?name=inline-1724343623.png)

Ao realize a liquidação do título será verificado o tipo de movimentação verificado no F12.   
Para que o processo já liquidado seja alterado é necessário realizar o estorno e liquidar novamente, após alteração do F12.
