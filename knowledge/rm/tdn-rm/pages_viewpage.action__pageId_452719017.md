---
content_hash: c49bf6867bcbfe59464052302fc9618f3c1da11631907b209062f34fbd3aae88
fetched_at: '2026-06-29T00:10:03.123176+00:00'
page_id: '452719017'
product: rm
source: tdn-rm
title: Código de Cálculo 6 - Vale Transporte
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719017
version: 2
---

Desconto do tipo valor.

Este cálculo será efetuado sobre o "código de cálculo 32 - Total Entregue de Vale".

O sistema somará os proventos do mês que "incidem vale-transporte" e encontrará o valor de INC. VALE.

O sistema aplicará o valor total que "inc. vale" sobre a porcentagem informada no campo % Desconto (Cadastros | Sindicatos | pasta Identificação) e, se ultrapassar o valor calculado no código de cálculo 032, o sistema irá considerar o valor deste último.

Caso o usuário não habilite o campo "Usa 30 Dias" (Cadastros | Sindicatos | pasta Identificação), o cálculo será feito da seguinte forma:

INC. VALE / 30 \* Nº DIAS UTEIS \* PORCENTAGEM

Em que:

INC. VALE: Total de proventos que "incidem vale-transporte".

30: Dias do mês.

No. DIAS UTEIS: Informado na pasta Vale-Transporte do cadastro de Funcionários. PORCENTAGEM: Informada em Cadastros | Sindicatos | pasta Identificação (campo % desconto).

Se o usuário confirmar o campo "Usa 30 Dias", o cálculo será feito da seguinte forma:

INC. VALE \* PORCENTAGEM

O valor encontrado será comparado com o total entregue de vale-transporte (código de cálculo 032) e será descontado o menor valor.

**Atenção**

Este código não deve ser confundido com o código de cálculo 032. Este último controla o total entregue, enquanto o 006 calcula o valor efetivo a descontar 263.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
