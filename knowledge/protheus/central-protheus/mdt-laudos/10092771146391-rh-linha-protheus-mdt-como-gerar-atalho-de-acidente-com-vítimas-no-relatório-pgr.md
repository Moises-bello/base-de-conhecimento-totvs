---
article_id: 10092771146391
category: MDT - Laudos
content_hash: a3f98afca8a861fb6c85a7607d76699473cfa1acd448faa2a13524c311c97d6d
fetched_at: '2026-06-28T22:44:26.247756+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar atalho de Acidente com vítimas no relatório
  PGR
type: support-article
updated_at: '2023-12-06T17:13:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10092771146391-RH-Linha-Protheus-MDT-Como-gerar-atalho-de-Acidente-com-v%C3%ADtimas-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19607114193431) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar atalho de Acidente com vítimas no relatório PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações > Laudos > Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10085422018839)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10085525958295)  
  
Na rotina Acidente, no menu **Atualizações - Acidente Trabalho - Acidentes** *(MDTA640)* deve ter o cadastro com os campos preenchido:

**Vítima (TNC\_VITIMA) = 1-Sim ou 3-Fatal,****Ficha Médica (TNC\_NUMFIC)** e **Centro Custo (TNC\_CC).  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10092769172119)**Obs.: A data do acidente deve estar dentro do período definido pelo laudo e o campo **Observações** é um campo livre de informação.  
  
Ao gerar o relatório PGR, será apresentado o atalho no formato abaixo:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10093256930583)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
