---
article_id: 10754531817111
category: MDT - Laudos
content_hash: 7f5181fc42b6b62fff4e4f869ff7ea14637968888138dbf98e8bc4987d317dd0
fetched_at: '2026-06-28T22:44:26.285806+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Como gerar atalho de Quadro Riscos no relatório
  PGR
type: support-article
updated_at: '2025-03-03T18:19:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/10754531817111-RH-Linha-Protheus-MDT-Como-gerar-atalho-de-Quadro-Riscos-no-relat%C3%B3rio-PGR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372871494679) Tempo aproximado para leitura: **00:04:00 min** **Dúvida**Como gerar atalho de Quadro Riscos no relatório PGR, rotina MDTR851?  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Incluir um Laudo, através da rotina **Atualizações - Laudos - Laudos** *(MDTA210)* onde o campo de **Tipo Laudo (TO0\_TIPREL)** seja igual a **6-PGR** e deve incluir o atalho em questão na pasta de **Conteúdo**. **![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/30372871497111)**  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10753306233495)  
  
Na rotina Agentes, no menu **Atualizações - PPRA - Agentes** *(MDTA180)*, incluir um registro preenchendo os campos necessário e o campo **Meio Propag.** **(TMA\_PROPAG)**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10753808905623)  
  
Na rotina Risco, no menu **Atualizações - PPRA - Riscos** *(MDTA180)*, incluir o risco e vincular ao Agente.  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10753886622615)  
  
Vincular o Risco ao Laudo através da rotina Relacionamentos, no menu **Atualizações - PPRA - Relacionamentos** *(MDTA232)* na aba **Laudos**.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10754004430743)  
  
Ao gerar o relatório PGR, será apresentado o atalho no formato abaixo:  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/10754473160087)  
  
**Saiba Mais**[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6961760300311-EC-Assistente-Carolina-Segmentos-Funcionalidades-da-Carolina)
