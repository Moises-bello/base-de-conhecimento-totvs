---
article_id: 10111358701847
category: MDT - Laudos
content_hash: 1c18c71a98c40a81990627118845349bf9672bb96cc2387088d39cf0e376e2f2
fetched_at: '2026-06-28T22:44:26.243970+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar atalho Bem no relatório PGR
type: support-article
updated_at: '2023-12-06T17:12:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10111358701847-RH-Linha-Protheus-MDT-Como-gerar-atalho-Bem-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19606902218135) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como gerar atalho Bem no relatório PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho – Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações - Laudos - Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**.  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19606902231575)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10116219591447)  
  
Na rotina EPC BEM, no menu **Atualizações - EPC - EPC (Bem)** *(MNTA080)* deve incluir um registro e preencher os campos:

**Nome do Bem (T9\_NOME),** **Família (T9\_CODFAMI),** **Data Compra (T9\_DTCOMPR) e** **Ult. Acomp. (T9\_DTULTAC).**![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10117165412503)  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10117168253463)

Na rotina Laudos x Equipamentos, no menu **Atualizações - Laudos - Laudos x Equipamentos** *(MDTA220),* na aba **Bem** vincular o equipamento ao laudo:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10117300373655)  
  
Ao gerar o relatório PGR, será apresentado o atalho no formato abaixo:  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10117630017303)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
