---
content_hash: 2fbc74e19a1ff5222d069ca1800a6d8fac329c18d254dba1dc910dafcf0de55f
fetched_at: '2026-06-29T00:10:10.069859+00:00'
page_id: '452719817'
product: rm
source: tdn-rm
title: Código de Cálculo 20 - Arredondamento Provento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719817
version: 2
---

Provento do tipo valor.

**Observações**

Após o cálculo geral de proventos e descontos, o sistema irá comparar o líquido com o valor de arredondamento que foi informado no campo Arredondamento em Cadastros | Funcionários | pasta Base de Cálculo. Quando o líquido for negativo, o sistema irá gerar um arredondamento suficiente para zerar o líquido. Quando o funcionário estiver recebendo salário-família, o sistema irá gerar o arredondamento com margem para deixar o líquido igual ou maior que o salário-família.

O total líquido deverá ser múltiplo do valor do arredondamento informado no campo Arredondamento.

Para o correto cálculo dos arredondamentos, é necessário que os períodos sejam processados em ordem crescente.

**Atenção**

Sempre que o líquido do funcionário for negativo, ou seja, o total de descontos for maior que o total de proventos, o sistema lançará, automaticamente, o provento Arredondamento", para ser descontado no mês seguinte no "código de cálculo 021, respeitando, primeiramente, as observações descritas acima.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
