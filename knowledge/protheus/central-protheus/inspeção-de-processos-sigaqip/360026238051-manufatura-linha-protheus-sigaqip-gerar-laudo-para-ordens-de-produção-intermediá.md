---
article_id: 360026238051
category: Inspeção de Processos (SIGAQIP)
content_hash: f9f3815821c63c48e1a1b1add638756e3ba7f1ac65cd244e316f90056bb11990
fetched_at: '2026-06-28T22:42:25.748094+00:00'
product: protheus
section_id: 360005906153
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQIP - Gerar laudo para Ordens de Produção
  Intermediárias
type: support-article
updated_at: '2021-10-01T13:14:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026238051-Manufatura-Linha-Protheus-SIGAQIP-Gerar-laudo-para-Ordens-de-Produ%C3%A7%C3%A3o-Intermedi%C3%A1rias
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**Ao utilizar a integração entre os módulos **SIGAPCP - Planejamento e Controle da Produção** e **SIGAQIP - Inspeção de Processos**, as **Ordens de Produção - OPs** são enviadas para inspeção na rotina **QIPA215 - Resultados**. Qual a parametrização necessária para que as **OPs intermediárias** também sejam enviadas para inspeção?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Inspeção de Processos (SIGAQIP) - Versão 12  
  
**Solução**Para gerar inspeção para as **OPs intermediárias** é necessário configurar o parâmetro **MV\_QPOPINT - Identifica se o usuário deseja inspecionar OPs intermediárias** como **.T.**.
