---
article_id: 5325947203735
category: Controle de Auditorias (SIGAQAD)
content_hash: 7e4024d33b97f1edba561f6cc66a5d80c8541cd6dc277b5a812cb74cc207031c
fetched_at: '2026-06-28T22:42:30.868729+00:00'
product: protheus
section_id: 360005876634
source: central-protheus
title: Manufatura - Linha Protheus - SIGAQAD - Parâmetro MV_QADININ
type: support-article
updated_at: '2022-04-12T13:35:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/5325947203735-Manufatura-Linha-Protheus-SIGAQAD-Par%C3%A2metro-MV-QADININ
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:00:20 min** **Dúvida**Qual a função do parâmetro **MV\_QADININ - Especifica nota que uma questão não respondida terá como valor padrão na rotina**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Controle de Auditorias (SIGAQAD) - Todas as versões.  
  
**Solução**O parâmetro **MV\_QADININ** é utilizado na rotina **QADA130 - Cadastros de Resultados**. Quando uma questão não está respondida, o campo **QUD - NOTA - Nota Questão** será preenchido automaticamente na abertura da tela de resultados, conforme o conteúdo do parâmetro **MV\_QADININ** que poderá ser **1 - Sim**, **2 - Não** ou **3 - Não informado**.
