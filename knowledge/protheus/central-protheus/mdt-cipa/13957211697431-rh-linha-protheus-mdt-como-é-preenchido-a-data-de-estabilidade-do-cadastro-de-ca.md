---
article_id: 13957211697431
category: MDT - CIPA
content_hash: ab09d570480999f10624723c83d2d51c08d3ee584284d911362ce66c342de60f
fetched_at: '2026-06-28T22:44:23.276430+00:00'
product: protheus
section_id: 360012070553
source: central-protheus
title: RH - Linha Protheus - MDT - Como é preenchido a data de estabilidade do cadastro
  de candidato da cipa
type: support-article
updated_at: '2025-10-03T17:58:14Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13957211697431-RH-Linha-Protheus-MDT-Como-%C3%A9-preenchido-a-data-de-estabilidade-do-cadastro-de-candidato-da-cipa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24726413281175) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**Como é preenchido a data de estabilidade do cadastro de candidato da cipa?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**O Período de estabilidade é apresentado do dia da Candidatura (TNO\_DTCAND) até o dia da eleição (TNN\_ELEICA), ou seja, no cadastro do Mandato veja a configuração do campo "Prev.Eleic." que o sistema irá considerar na Data de Estabilidade.     
  
No módulo MDT, na rotina *Atualizações - Cipa - Mandatos* (MDTA635), o sistema irá considerar o campo "Prev.Eleic."(TNN\_ELEICA) para compor a informação de Data de Estabilidade (TNO\_DTESTB) do cadastro de Candidatos:   
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13957115092247)  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/13957156558231)  
  
Em caso de não gerar Estabilidade, consulte nossa documentação: [O que verificar quando não é gerado Estabilidade para um Funcionário vinculado a CIPA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002954301-RH-Linha-Protheus-MDT-O-que-verificar-quando-n%C3%A3o-%C3%A9-gerado-Estabilidade-para-um-Funcion%C3%A1rio-vinculado-a-CIPA)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
