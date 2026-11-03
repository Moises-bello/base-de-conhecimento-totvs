---
content_hash: e653cc1e63965f8f3e5d38f629ff13409ea776361bab926683b6c7e6ad19e0ad
fetched_at: '2026-06-29T00:10:10.050172+00:00'
page_id: '452719805'
product: rm
source: tdn-rm
title: Código de Cálculo 21 - Arredondamento Desconto
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719805
version: 4
---

Desconto do tipo valor. O sistema lançará o evento "arredondamento" (código de cálculo 021) na movimentação do mês, diminuindo o saldo devedor do funcionário, sempre respeitando o valor do arredondamento informado no campo Arrendond. do cadastro de Funcionários, pasta Base de Cálculo, e observando que o total líquido deverá ser múltiplo deste arredondamento.

Foi inserida uma melhoria no Log de Cálculo, para que passe a exibir a origem dos valores e o período considerado no código de cálculo 21. Mais informações: [DT - Códigos de Cálculo 21/314/419 - Melhoria do Log de Cálculo](https://tdn.totvs.com/pages/viewpage.action?pageId=917132275)

*Exemplo da melhoria no Código de Cálculo 21*                                                       

**Observação**

Para o correto cálculo dos arredondamentos, é necessário que os períodos sejam processados em ordem crescente.
