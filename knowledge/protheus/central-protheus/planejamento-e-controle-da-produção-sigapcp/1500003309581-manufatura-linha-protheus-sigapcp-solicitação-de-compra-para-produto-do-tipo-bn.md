---
article_id: 1500003309581
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 827ba855bcfa4b5000e2cda09de80f3ff2c31081be30b3141886bb5491bb11bd
fetched_at: '2026-06-28T22:42:47.031948+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Solicitação de compra para produto
  do tipo BN
type: support-article
updated_at: '2021-10-22T14:02:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500003309581-Manufatura-Linha-Protheus-SIGAPCP-Solicita%C3%A7%C3%A3o-de-compra-para-produto-do-tipo-BN
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)***Tempo aproximado para leitura: **00:00:45 min**  
**Dúvida**Por que o componente do tipo **BN -****Beneficiamento**, ao abrir uma **OP - Ordem de produção**, não está gerando **SC - Solicitação de Compra** mesmo quando não possuindo saldo em estoque ?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**Para que o produto do tipo **BN** possa gerar solicitação de compra é necessário que os parâmetros abaixo estejam configurados da seguinte forma:

* **MV\_EMPBN - Indica se devem ser gerados empenhos de Ordens de Produção para componentes do tipo BN** igual a **T**
* **MV\_GERASC - Gera Solicitação de Compras a partir da inclusão da Ordem de Produção** igual a **T**
* **MV\_COMPRBN - Indica se produtos do tipo BN devem ser comprados** igual a **.T.**
