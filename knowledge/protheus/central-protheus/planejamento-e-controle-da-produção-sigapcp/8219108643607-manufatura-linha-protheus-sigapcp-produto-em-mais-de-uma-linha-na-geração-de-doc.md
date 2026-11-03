---
article_id: 8219108643607
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 83978d139664f85b3619d095f791f64186dcdee00d96dca997bba181feffb2ee
fetched_at: '2026-06-28T22:42:45.757144+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Produto em mais de uma linha na geração
  de Documentos MRP
type: support-article
updated_at: '2022-08-17T11:31:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8219108643607-Manufatura-Linha-Protheus-SIGAPCP-Produto-em-mais-de-uma-linha-na-gera%C3%A7%C3%A3o-de-Documentos-MRP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:40 min  
  
Dúvida**Por que o **produto** está sendo apresentado em mais de uma linha no **PCPA144 - Geração de Documentos MRP**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Essa situação pode ocorrer quando o **produto** possui **configuração de opcionais**, e está selecionado **opcionais** diferentes para **estoque**, **entradas** ou **saídas**.  
O **MRP - Manufacturing Resource Planning** considera cada **produto** com uma seleção de **opcionais** diferentes como um **produto** diferente.  
O Sistema somente consegue agrupar no mesmo **produto** ao realizar o cálculo aquele que tiver a mesma **configuração de opcionais**.
