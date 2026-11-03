---
article_id: 10760868982295
category: MDT - Laudos
content_hash: 461b3e734c5de5539ae477b56b9557b4f758a78b981bc1007ec95769b2e8587c
fetched_at: '2026-06-28T22:44:26.280724+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar atalho de Quadro Medida de Controle
  no relatório PGR
type: support-article
updated_at: '2024-07-30T11:55:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10760868982295-RH-Linha-Protheus-MDT-Como-gerar-atalho-de-Quadro-Medida-de-Controle-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25269647383703) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como gerar atalho de Quadro Medida de Controle no relatório PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações - Laudos - Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**. **![](https://centraldeatendimento.totvs.com/hc/article_attachments/25269647390999)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10760951945495)**Na rotina Medida Controle, no menu **Atualizações - PPRA - Medida Controle** *(MDTA135)*, incluir registro.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10761129895319)  
  
Vincular a medida ao Laudo pela rotina de Relacionamentos, no menu **Atualizações - PPRA - Relacionamentos** *(MDTA232)* na aba **Medidas de Controle**.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10761336026519)  
  
Ao gerar o relatório PGR, será apresentado o atalho no formato abaixo:  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10761369322263)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
