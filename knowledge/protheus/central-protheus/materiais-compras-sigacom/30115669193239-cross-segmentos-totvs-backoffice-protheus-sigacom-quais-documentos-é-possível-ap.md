---
article_id: 30115669193239
category: Materiais - Compras (SIGACOM)
content_hash: f422f4dc1e496e91c7e2e8d86732324c1ea49973bfddeee05ee0f8d1646c2861
fetched_at: '2026-06-28T22:41:10.324492+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais documentos é
  possível aprovar através do APP MEU PROTHEUS?
type: support-article
updated_at: '2026-01-22T18:07:23Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/30115669193239-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Quais-documentos-%C3%A9-poss%C3%ADvel-aprovar-atrav%C3%A9s-do-APP-MEU-PROTHEUS
---

**Dúvida**

Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Quais documentos é possível aprovar através do APP MEU PROTHEUS?

**Solução**

Através do APP MEU PROTHEUS é possível realizar a aprovação dos documentos abaixo:

* Solicitação de Compras com alçada por entidade Contábil, CR\_TIPO='SC';
* Pedidos de Compra com alçada Padrão, CR\_TIPO='PC';
* Pedidos de Compra com alçada por Item Pedido, CR\_TIPO='IP';
* Medições de Contrato geradas a partir do GCT com alçada Padrão, CR\_TIPO='MD';
* Medições de Contratos geradas a partir do GCT com alçada por Entidade Contábil, CR\_TIPO='IM';
* Solicitação ao Armazém geradas a partir da rotina MATA105, CR\_TIPO='SA';
* Contratos de Compra/Venda gerados a partir do GCT com alçada Padrão (Sem Entidades Contabeis), CR\_TIPO='CT'

Além dos documentos informados acima é possível também realizar a aprovação/rejeição de Prestação de Contas (Controle de Viagens);

**OBSERVAÇÃO:**

Através do APP MEU PROTHEUS não é possível realizar a aprovação:

* de Revisão de Contratos (CR\_TIPO='RV')
* de Contratos com Alçada por Entidades Contábeis (CR\_TIPO='IC')
* e também não é possível aprovar SC's que possuam o Bloqueio Simples, onde a liberação é realizada na própria rotina MATA110.

***Saiba Mais:***

* [Guia de Usa Meu Protheus](https://tdn.totvs.com/x/uTxZEg)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
