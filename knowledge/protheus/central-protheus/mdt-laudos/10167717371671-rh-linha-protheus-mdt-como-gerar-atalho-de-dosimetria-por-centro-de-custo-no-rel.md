---
article_id: 10167717371671
category: MDT - Laudos
content_hash: 02df2b681f91bc0c4c6c6da634ecec34c0d1ce9f4b63436c47c2fdb5f5102300
fetched_at: '2026-06-28T22:44:26.276251+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar atalho de Dosimetria por Centro de Custo
  no relatório PGR
type: support-article
updated_at: '2023-12-06T17:11:47Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10167717371671-RH-Linha-Protheus-MDT-Como-gerar-atalho-de-Dosimetria-por-Centro-de-Custo-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19606801178263) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar atalho de Dosimetria por Centro de Custo no relatório PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações - Laudos - Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19606845327895)  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10166298416791)

Na rotina Centro Custo, no menu **Atualizações - Cadastros Gerais - Centro Custos** *(CTBA030)*, incluir um registro:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10166374654487)

Na rotina Medição Dosimetro, no menu **Atualizações - PPRA - Medição Dosimetro** *(MDTA997)*, incluir registro e preencher o campo **Registro (TJ7\_TIPREG)** igual ao Centro de Custo e vincular o centro de custo incluído.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10166615630231)  
  
Ao gerar o relatório PGR, será apresentado o atalho no formato abaixo:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10167688018071)  
  
**Saiba Mais**

[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
