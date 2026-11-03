---
article_id: 360044597173
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: c2543193535bd73b6de8ba6c1bca60a3174cdba94f93093b1b9e7dc9973dda6f
fetched_at: '2026-06-28T22:42:47.082828+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Tempo MOD dobrado
type: support-article
updated_at: '2021-08-09T14:20:48Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360044597173-Manufatura-Linha-Protheus-SIGAPCP-Tempo-MOD-dobrado
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:02 min**  
**Dúvida**  
Por que ao realizar ao realizar o apontamento no **MATA681 - Produção PCP MOD 2** o tempo da **MOD - Mão de Obra** está dobrado?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Isso ocorre pois o Sistema fará a multiplicação do tempo com o conteúdo do campo **G2\_MAOOBRA - Mão-de-Obra** que é definido no roteiro de operações.  
  
**Exemplo**  
Se o tempo calculado pelo Sistema for de 1 hora, porém para a operação em questão o campo **G2\_MAOOBRA** estiver preenchido com 2, significa que para a execução da operação são necessários dois operadores, neste caso o tempo da **MOD** será multiplicado pelo número de operadores, para este exemplo, o tempo requisitado da **MOD** será de 2 e não de 1.
