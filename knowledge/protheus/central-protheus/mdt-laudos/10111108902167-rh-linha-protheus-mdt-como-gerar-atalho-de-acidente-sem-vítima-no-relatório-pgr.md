---
article_id: 10111108902167
category: MDT - Laudos
content_hash: 5f83a3bd91955ebf0065209f868648ae3108257dca392084b0093bc37454e169
fetched_at: '2026-06-28T22:44:26.252224+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar atalho de Acidente sem vítima no relatório
  PGR
type: support-article
updated_at: '2024-07-30T17:04:37Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10111108902167-RH-Linha-Protheus-MDT-Como-gerar-atalho-de-Acidente-sem-v%C3%ADtima-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25279227546775) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como gerar atalho de Acidente sem vítima no relatório PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações - Laudos - Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25279257431319)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10109864904087)  
  
Na rotina Acidente, no menu **Atualizações - Acidente Trabalho - Acidentes** *(MDTA640)* deve incluir uma despesa material e preencher os campos:

**Vítima (TNC\_VITIMA) = 2-Não** e **Centro Custo (TNC\_CC).  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10111096451607)**Obs.: A data do acidente deve estar dentro do período definido pelo laudo e o campo Observações é um campo livre de informação.  
  
Ao gerar o relatório PGR, será apresentado o atalho no formato abaixo:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10111192071703)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
