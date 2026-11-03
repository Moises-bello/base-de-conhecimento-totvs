---
article_id: 11484337859863
category: MDT - Laudos
content_hash: bbf58de0efeae169a8cc6d469556391ce8af767d6d40928dbc2613333a3d2761
fetched_at: '2026-06-28T22:44:26.266425+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar atalho de Dosimetria por Ambiente Físico
  no relatório PGR
type: support-article
updated_at: '2024-07-30T11:57:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/11484337859863-RH-Linha-Protheus-MDT-Como-gerar-atalho-de-Dosimetria-por-Ambiente-F%C3%ADsico-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25269678757911) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como gerar atalho de Dosimetria por Ambiente Físico no relatório PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações - Laudos - Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**. **![](https://centraldeatendimento.totvs.com/hc/article_attachments/25269678759703)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11483818015767)**Na rotina Ambiente Físico, no menu Atualizações - PPRA - Ambiente Físico *(MDTA165),* incluir registro:  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11484064137623)  
  
Na rotina Medição Dosimetro, no menu Atualizações - PPRA - Medição Dosimetro *(MDTA997)*, incluir registro e preencher o campo Registro (TJ7\_TIPREG) igual a Ambiente Físico e vincular o Ambiente cadastrado.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11484148306583)  
  
Vincular o local ao laudo pela rotina Relacionamentos, no meu Atualizações - Laudos - Relacionamentos *(MDTA232)*, na aba **Locais.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11484286892183)**Ao gerar o relatório PGR, será apresentado o atalho no formato abaixo: **![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/11484273014423)  
  
Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
