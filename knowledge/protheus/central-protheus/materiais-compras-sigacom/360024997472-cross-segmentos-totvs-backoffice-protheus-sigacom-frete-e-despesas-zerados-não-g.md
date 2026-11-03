---
article_id: 360024997472
category: Materiais - Compras (SIGACOM)
content_hash: a7ae3f1e2b516f8821d3cfa1ecf0936e82b27098f8c4d30fa1a5d0d0bf15c277
fetched_at: '2026-06-28T22:41:08.885339+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Frete e Despesas Zerados
  - Não gravam valores digitados o Documento de Entrada / Pedido
type: support-article
updated_at: '2026-02-18T18:32:02Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024997472-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Frete-e-Despesas-Zerados-N%C3%A3o-gravam-valores-digitados-o-Documento-de-Entrada-Pedido
---

Tempo aproximado para leitura:**00:03 min**  
  
**Dúvida**

Em quais condição os campos frete/despesa não acatam o valor digitado, deixando o conteúdo zero na inclusão do Documento de Entrada / Pedido de Compras ?

**Ambiente**  
Microsiga Protheus – Compras– A partir da versão 11.80  
  
**Solução**

Ao digitar valores nos campos da aba **Desconto**/**Frete**/**Despesas**, os campos **Frete** ou **Despesa** são zerados quando informado zero no campo **Cálculo** **de** **ISS** (**F4\_ISS**), tendo o **TES** com conteúdo igual a **SIM**.

Esta configuração não permite digitar **Despesas** e **Fretes**, pois entende que a nota já é uma despesa e impede a informação de outros valores nesta aba.

Para permitir, utilize **TES** cujo campo **Cálculo** **de** **ISS** (**F4\_ISS**) esteja com o conteúdo **NÃO**.

![20211215_155856.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4416035085591)

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
