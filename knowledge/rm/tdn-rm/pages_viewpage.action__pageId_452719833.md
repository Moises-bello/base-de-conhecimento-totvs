---
content_hash: dc106aef3ee3db5f779a95a2162d894559671a86a88e5d4d667cb6b9fe193be0
fetched_at: '2026-06-29T00:10:10.418215+00:00'
page_id: '452719833'
product: rm
source: tdn-rm
title: Código de Cálculo 4 - IRRF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719833
version: 2
---

Desconto do tipo valor com incidência no líquido. O cálculo de IRRF poderá ser feito de duas maneiras, conforme opção do módulo Opções | Parâmetros | RM Labore | pasta Identificação.   
 *Não Usando Regime Caixa:*

As empresas que não usam o regime caixa são aquelas que utilizam uma única tabela de IR para todos os pagamentos do mês-competência. O sistema somará os proventos do mês que "incidem IRRF" e encontrará o valor de INC. IRRF.

Será guardado o valor calculado de INSS no mês.

O número de dependentes (conforme Cadastros | Funcionários | pasta Base de Cálculo) será multiplicado pelo valor "por dependente", informado na Tabela de IRRF (Tabelas de Cálculo).

O sistema buscará o total já descontado de IRRF no mesmo mês em envelopes anteriores e encontrará o valor de "JÁ DESCONTOU".

O cálculo será feito da seguinte forma:

(((INC. IRRF - INSS (mês caixa) - DED. DEP. - DEDUT. DE IRRF) \* TAXA)/ 100) DED. CONF. FAIXA - JÁ DESC.

O sistema calculará (INC. IRRF - INSS - DED. DEP - DEDUTÍVEL DE IRRF). Ao valor encontrado será aplicada a Tabela de IRRF, sendo multiplicado pela taxa da faixa encontrada. O resultado será dividido por 100 e, então, será subtraído o valor a deduzir conforme faixa e subtraído o valor de "JÁ DESCONTOU".

*Usando Regime Caixa*

O regime caixa será utilizado para pagamentos da mesma competência em 2 (dois) meses distintos, como, por exemplo, o pagamento do adiantamento com tabela do mês competência e pagamento de salário com tabela de IRRF do mês posterior.

O cálculo efetuado será o mesmo, porém o sistema soma os proventos que incidem IRRF somente do mês caixa, ou seja, mês do efetivo pagamento.

**Exemplo**

A empresa paga adiantamento de salário no dia 20 (vinte) e efetua o pagamento mensal no dia 5 (cinco) do mês seguinte. Neste caso, deve utilizar o regime caixa, pois está efetuando pagamento do mês competência em caixas diferentes (meses do efetivo pagamento diferentes, tabelas de IRRF diferentes).

Pagamento de abril - 05/05

Adiantamento de maio - 20/05

Pagamento de maio - 05/06

Adiantamento de junho - 20/06

A base de cálculo para IRRF será:

PAGAMENTO DE ABRIL (CAIXA MAIO):

Valor do pagamento de abril - adiantamento de abril (20/04) = base de cálculo para pagamento de abril.

ADIANTAMENTO DE MAIO (CAIXA MAIO): Base de cálculo para pagamento de abril + adiantamento de maio = base de cálculo mês caixa de maio.

PAGAMENTO DE MAIO (CAIXA JUNHO): Valor do pagamento de maio - adiantamento de maio (20/05) = base de cálculo para pagamento de maio.

ADIANTAMENTO DE JUNHO (CAIXA JUNHO): Base de cálculo para pagamento de maio + adiantamento de junho = base de cálculo mês caixa de junho.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

Códigos de Cálculo
