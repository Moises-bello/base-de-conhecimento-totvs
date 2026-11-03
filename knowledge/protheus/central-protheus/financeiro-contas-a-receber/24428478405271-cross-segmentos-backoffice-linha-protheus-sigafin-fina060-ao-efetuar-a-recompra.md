---
article_id: 24428478405271
category: Financeiro - Contas a Receber
content_hash: 3970fb1d7c44f31832e9f1428436b59899f643c0763fe64299d3bce23e0a31be
fetched_at: '2026-06-28T22:38:13.963954+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA060 - Ao efetuar
  a recompra do título (fazendo a transferência da situação de carteira de 2-desconta
  para 0-simples) como gerar um valor a maior da recompra por causa das taxas?
type: support-article
updated_at: '2024-06-26T20:56:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24428478405271-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA060-Ao-efetuar-a-recompra-do-t%C3%ADtulo-fazendo-a-transfer%C3%AAncia-da-situa%C3%A7%C3%A3o-de-carteira-de-2-desconta-para-0-simples-como-gerar-um-valor-a-maior-da-recompra-por-causa-das-taxas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24428470541719) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**Ao efetuar a recompra do título (fazendo a transferência da situação de carteira de 2-desconta para 0-simples) como gerar um valor a maior da recompra por causa das taxas?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas versões

**Solução**

Neste caso no padrão do sistema não seria possível acrescentar valor no momento da recompra deste titulo.

Como é feita a recompra do título.

Acessando a rotina "FINA060 - Transferência"  posicionando em cima do título, e clicando em "Transferir"  
Neste momento da empresa poderá alterar a situação da carteira

De: **2-Situação descontadas**

Para: **0-Situação Carteira**

E neste cenário será possível através do P.E. "Ponto de entrada" F060DGV que é chamado ao transferir para situação 0, alterar o valor da recompra do seu título.

Segue documentação do mesmo.

[F060DGV - Permite alterar o valor da transferência](https://tdn.totvs.com/pages/releaseview.action?pageId=829308092)

**Saiba mais:**

[Transferências - FINA060 - Financeiro - P12](https://tdn.totvs.com/pages/releaseview.action?pageId=271405699)
