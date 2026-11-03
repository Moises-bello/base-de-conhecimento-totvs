---
article_id: 360029130031
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: baf414c14d1a291091bc672ba00c54b3869095768d1cdb2e0e64ec4ee73bfb6b
fetched_at: '2026-06-28T22:42:40.932119+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Cálculo da previsão de entrega ou previsão
  inicial de um produto na geração da OP
type: support-article
updated_at: '2021-08-16T13:56:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360029130031-Manufatura-Linha-Protheus-SIGAPCP-C%C3%A1lculo-da-previs%C3%A3o-de-entrega-ou-previs%C3%A3o-inicial-de-um-produto-na-gera%C3%A7%C3%A3o-da-OP
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:01:05 min****Dúvida**Como o Sistema calcula a **previsão de entrega** ou **previsão inicial** de um produto na geração da **OP - Ordem de Produção**?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**A data de **previsão de entrega** ou **previsão inicial** pode ser calculada por meio do roteiro de operações ou do campo **B1\_PE** - **Prazo de Entrega** do **MATA010 - Produtos** na aba **MRP.**  
Para isso o programa valida a informação contida no parâmetro **MV\_PEOPERA - O prazo de entrega dos produtos fabricados deve ser calculado pelo roteiro de operações?.**

* Caso parâmetro esteja com valor **T**, é calculado o prazo de entrega pelo roteiro de operações.
* Caso parâmetro esteja com valor **F**, ou não exista o roteiro é considerado o campo **B1\_PE** do cadastro de produto. Além disso, será verificado o conteúdo do parâmetro **MV\_CALCPRZ - Define os dias da semana a considerar no Prazo de Entrega**.

**Saiba mais**Para mais informações sobre o parâmetro **MV\_CALCPRZ** acesse o *link*: [Manufatura - Linha Protheus - SIGAPCP - Conceito do parâmetro MV\_CALCPRZ](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028914751-MP-SIGAPCP-C%C3%A1lculo-da-previs%C3%A3o-inicial-ou-previs%C3%A3o-de-entrega-da-ordem-de-produ%C3%A7%C3%A3o?source=search)
