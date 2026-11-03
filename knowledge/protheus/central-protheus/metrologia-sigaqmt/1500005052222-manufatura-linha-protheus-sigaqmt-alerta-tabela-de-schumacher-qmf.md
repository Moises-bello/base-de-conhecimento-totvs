---
article_id: 1500005052222
category: Metrologia (SIGAQMT)
content_hash: 68de0f41f8ac00aef3760484c4c18eafccfbf9ba329a264edae29497f164abb0
fetched_at: '2026-06-28T22:42:24.746781+00:00'
product: protheus
section_id: 360005876694
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQMT - Alerta Tabela de Schumacher (QMF)
type: support-article
updated_at: '2025-12-04T19:03:13Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005052222-Manufatura-Linha-Protheus-SIGAQMT-Alerta-Tabela-de-Schumacher-QMF
---

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36786635165975) Tempo aproximado para leitura: **00:00:30 min**  
  
**Ocorrência**  
No módulo **SIGAQMT - Metrologia**, ao acessar a rotina **QMTA140 - Medições** ocorre a mensagem **Atenção - Problemas na tabela de Schumacher (QMF). Provavelmente a tabela foi perdida. Consulte Suporte Microsiga informando esta mensagem. As medições não poderão ser gravadas.**  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Metrologia (SIGAQMT) - Todas as versões  
  
**Causa**  
A mensagem de atenção é apresentada na rotina **QMTA140** quando a tabela **QMF - Tabela de Schumacher** foi perdida ou quando a mesma não existe no banco de dados.  
  
**Solução**  
Para solucionar essa ocorrência será preciso importar via **APSDU** a tabela **QMF** que segue anexo, e acessar novamente a rotina **QMTA140**.   
  
**Anexo**  
Segue arquivo para importação:
