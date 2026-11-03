---
article_id: 235301687
category: Materiais - Compras (SIGACOM)
content_hash: 63961b651177fec56b5f1f73e401bb829e2e2623df4a10575f894e19dcba2569
fetched_at: '2026-06-28T22:41:24.092815+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Procedimentos para
  compra / venda de produtos em consignação
type: support-article
updated_at: '2026-04-17T19:49:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/235301687-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Procedimentos-para-compra-venda-de-produtos-em-consigna%C3%A7%C3%A3o
---

**Dúvida**

Quais os procedimentos para compra/venda de produtos em consignação?

**Ambiente**  
Protheus– Compras – A partir da versão 11.80  
  
**Solução**

Segue abaixo os procedimentos para compra/venda de produtos em consignação.

1. O fornecedor envia a mercadoria para a empresa, para que a mesma seja vendida, porém a mercadoria continua sendo de propriedade do fornecedor.
   * **RECEBIMENTO DA REMESSA** -> **TES**: Poder 3º = Remessa/Atualiza estoque = SIM
2. Quando a mercadoria é vendida, a empresa fatura diretamente para seu cliente a mercadoria consignada.
   * **VENDA DO PRODUTO** -> **TES**: Poder 3º = Não controla / Atualiza estoque = SIM
3. A empresa realiza uma devolução simbólica (somente NF) da mercadoria que antes era consignada, para o fornecedor.
   * **NOTA DE DEVOLUÇÃO SIMBÓLICA PARA O FORNECEDOR** -> **TES**: Poder 3º = Devolução / Atualiza estoque = NÃO
4. Após receber a NF, o fornecedor irá realizar o faturamento efetivo (venda da mercadoria) a empresa, que por sua vez está neste momento comprando a mercadoria.
   * **NOTA DE COMPRA DO PRODUTO CONSIGNADO VENDIDO** -> **TES**: Poder 3º = Não controla / Atualiza estoque = NÃO.

***Saiba Mais :***

[PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)

[Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
