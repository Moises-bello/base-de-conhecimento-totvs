---
article_id: 10120780002583
category: MDT - Laudos
content_hash: 5cd16065d588315bbe7484b0ae1f89ce02f6d047e69b10c96cfc81078e8ac3e9
fetched_at: '2026-06-28T22:44:26.256767+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar atalho de Controle no relatório PGR
type: support-article
updated_at: '2023-12-06T17:13:19Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10120780002583-RH-Linha-Protheus-MDT-Como-gerar-atalho-de-Controle-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19606979513623) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar atalho de Controle no relatório PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações - Laudos - Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19606990255383)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10120373869079)  
  
Na rotina Medida Controle, no menu **Atualizações - PPRA - Medidas Controles** *(MDTA135)* e incluir um registro:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10120471631255)

Na rotina Relacionamentos, no menu **Atualizações - Laudos - Relacionamentos** *(MDTA232)*, vincular a Medida de Controle na aba **Medidas de** **Controle** preenchendo o campo **Descrição**:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10120776754327)  
  
Ao gerar o relatório PGR, será apresentado o atalho no formato abaixo:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10120778075287)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
