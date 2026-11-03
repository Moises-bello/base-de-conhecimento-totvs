---
article_id: 10145032777495
category: MDT - Laudos
content_hash: 8d9d03c11d4aee0c7103317e36d71863e703ec2916b4b4c85f02573ec859ea5b
fetched_at: '2026-06-28T22:44:26.261023+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar atalho de Cronograma no relatório PGR
type: support-article
updated_at: '2023-12-06T17:12:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10145032777495-RH-Linha-Protheus-MDT-Como-gerar-atalho-de-Cronograma-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19606856892311) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar atalho de Cronograma no relatório PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações - Laudos - Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19606850628631)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10144654498199)  
  
Na rotina Plano de Ação, no menu **Atualizações - PPRA - Plano de Ação** *(MDTA615)*, inclui um registro e preenche a aba **Planejamento**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10144771973783)  
  
Na rotina Relacionamentos, no menu **Atualizações - Laudos - Relacionamentos** *(MDTA232),* vincular o plano ao laudo pela rotina de **Relacionamentos (MDTA232)** na aba **Plano de Ação:**  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10144855114391)  
  
Ao gerar o relatório PGR, será apresentado o atalho no formato abaixo:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10144948480023)  
 **Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
