---
article_id: 360024982271
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: f8126d415585d6bf17a5eb1d08f773fc4f2193ca3bdbf913a36c35c702b3daa0
fetched_at: '2026-06-28T22:42:45.783765+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Qual o critério para empenhar o produto
  alternativo
type: support-article
updated_at: '2021-05-27T10:51:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024982271-Manufatura-Linha-Protheus-SIGAPCP-Qual-o-crit%C3%A9rio-para-empenhar-o-produto-alternativo
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:01:00 min****Dúvida**Qual o critério para empenhar o produto alternativo?  
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12  
  
**Solução**  
Segue como o Sistema se comportará para realizar o empenho quando há alternativos cadastrados:

* **Se o produto principal tiver saldo:** será empenhado o produto principal;
* **Se o produto principal não tiver saldo suficiente:** será empenhado o saldo que o produto principal possui para depois empenhar os alternativos;
* **Se tiver mais de um produto alternativo:** será verificado na ordem que os produtos estão cadastrados para realizar o empenho;
* **Se produto principal tiver saldo de entrada prevista:** será empenhado o produto principal;
* **Se nenhum produto tiver saldo porém o alternativo tiver quantidade prevista para entrada:** será empenhado o produto que tiver saldo de entrada prevista, caso não seja suficiente será empenhado o produto principal.
