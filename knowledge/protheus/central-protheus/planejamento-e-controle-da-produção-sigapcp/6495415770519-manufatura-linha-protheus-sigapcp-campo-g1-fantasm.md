---
article_id: 6495415770519
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: e4fc486eacff0b09027685bb9ca5a2798773165aaab27e341eb6f3ca631fc4ff
fetched_at: '2026-06-28T22:42:40.996744+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Campo G1_FANTASM
type: support-article
updated_at: '2025-10-15T16:47:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6495415770519-Manufatura-Linha-Protheus-SIGAPCP-Campo-G1-FANTASM
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:01:03 min** **Dúvida**Como é o funcionamento do campo **G1\_FANTASM - Fantasma** do **PCPA200 - Estrutura**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**O campo **G1\_FANTASM** é lido **apenas** para as **OPs - Ordens de Produção** geradas através do **MRP Memória**.  
  
Então:

* Se o campo **G1\_FANTASM**estiver **em branco**, o **MRP Memória** considerará a informação do campo **B1\_FANTASM - Fantasma** do **MATA010 - Cadastro de Produto** para o componente;
* Se o campo **G1\_FANTASM**estiver configurado igual a **Sim** o  **MRP Memória**irá considerar o componente como **fantasma**, para aquela estrutura, **independente** da configuração do campo **B1\_FANTASM** do **MATA010**;
* Se o campo **G1\_FANTASM**estiver configurado igual a **Não** o  **MRP Memória não** irá considerar o componente como **fantasma**, para aquela estrutura, **independente** da configuração do campo **B1\_FANTASM** do **MATA010**;
