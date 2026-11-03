---
article_id: 5252943584535
category: MDT - Laudos
content_hash: 2af1265a05188993ee94d49d66f0bdfe520cf2a8b2e50e98df9a374f25266ba1
fetched_at: '2026-06-28T22:44:26.182761+00:00'
product: protheus
section_id: 360012070273
source: central-protheus
title: RH - Linha Protheus - MDT - Ao incluir Laudo (MDTA210) e selecionar o tipo
  laudo PCMAT o campo "Centro Custo" não aparece as opções para selecionar.
type: support-article
updated_at: '2023-12-06T17:13:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5252943584535-RH-Linha-Protheus-MDT-Ao-incluir-Laudo-MDTA210-e-selecionar-o-tipo-laudo-PCMAT-o-campo-Centro-Custo-n%C3%A3o-aparece-as-op%C3%A7%C3%B5es-para-selecionar
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19607128360727) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Ao incluir Laudo (MDTA210), e selecionar o tipo laudo PCMAT o campo "Centro Custo" não aparece as opções para selecionar.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Quando tem um laudo do tipo PCMAT é importante ter o cadastro de Obras, no módulo SIGAMDT entre na rotina **Atualizações - Obras PCMAT - Obras (MDTA730)**, pois é deste cadastros que apontamos no campo TO0\_CC (Laudos) e o sistema irá buscar os dados do campo TLL\_CC (Obras).  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5268645787543)  
  
Após este cadastro, você poderá apontar no cadastro do Laudo para o tipo PCMAT e apontar o C.C. previamente cadastrado como Obra, entre no menu **Atualizações - Laudos - Laudos**.  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/5252568303127)  
  
**Saiba Mais**  
[Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Consulte os atalhos disponíveis no relatório PGR](https://tdn.totvs.com/pages/viewpage.action?pageId=667375614)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
