---
content_hash: d9bce803cbdcab6bdf2b4f985cbc3f357b089fd788c71f431b233e4cbe1884f6
fetched_at: '2026-06-29T00:09:47.676203+00:00'
page_id: '435105044'
product: rm
source: tdn-rm
title: Funções de Fórmula para Contabilização do Aluguel
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=435105044
version: 2
---

---

**Valores referentes ao contrato de locação**

* **VALORFINALDATA**  
  Retorna o valor final do contrato na data processada (período contábil). Considera os reajustes, aditivos e escalonamentos
* **VALORFINALANTERIORDATA**  
  Retorna o valor final do contrato na data anterior à data processada (período contábil anterior). Considera os reajustes, aditivos e escalonamentos
* **VALORTOTALEVENTOFINANCEIROCONTRATO**  
  Retorna o valor total do evento financeiro de aluguel associado ao contrato de locação. O valor total deste evento é mutável, pois varia à medida que os lançamentos financeiros de aluguel são gerados ou excluídos
* **VALORTOTALDOCONTRATODATA**  
  Retorna o valor total do contrato na data processada (período contábil). Considera os reajustes, aditivos e escalonamentos
* **VALORDATAXADEADMINISTRACAODATA**  
  Retorna o valor da taxa de administração na data processada (período contábil), considerando para seu cálculo o valor final do contrato no mesmo período contábil. Leva em consideração o período de carência para seu cálculo
* **VALORDATAXADEINTERMEDIACAODATA**  
  Retorna o valor da taxa de intermediação na data processada (período contábil), considerando para seu cálculo o valor final do contrato no mesmo período contábil. Leva em consideração o período de recorrência para seu cálculo.
* **VALORDEDESCONTODATA**  
  Retorna o valor de desconto do contrato na data processada (período contábil). Considera os reajustes, aditivos e escalonamentos
* **RECEITALINEARDATA**  
  Retorna o valor da receita linear na data processada (período contábil). Considera os reajustes, aditivos e escalonamentos
* **RECEITALIQUIDADATA**  
  Retorna o valor da receita liquida na data processada (período contábil). Considera os reajustes, aditivos e escalonamentos
* **DESCONTOLINEARDATA**  
  Retorna o valor do desconto linearizado na data processada (período contábil). Considera os reajustes, aditivos e escalonamentos
* **PROVISAODELINEARIZACAODATA**  
  Retorna o valor de provisão de linearização na data processada (período contábil). Considera os reajustes, aditivos e escalonamentos
* **PROVISAODERECEITADATA**  
  Retorna o valor de provisão de receita linear na data processada (período contábil). Considera os reajustes, aditivos e escalonamentos
* **VALORRESIDUODATA**  
  Valor de resíduo em uma data
* **VALORORIGINALDATA**  
  Esta função irá retornar o valor final original do contrato, considerando o valor final do momento da efetivação do contrato. Caso haja algum escalonamento nesta data, esta função de fórmula irá retornar o valor original do escalonamento, desconsiderando seus possíveis reajustes
* **VALORACUMULADOADITIVODATA**  
  Esta função irá retornar o valor acumulado de aditivos na data determinada. Este cálculo será feito subtraindo o valor do aditivo do valor anterior a ele (onde o valor anterior poderá ser o valor original, um reajuste ou outro aditivo anterior). Caso haja algum escalonamento nesta data, esta função de fórmula irá retornar 0 (zero)
* **VALORACUMULADOREAJUSTEDATA**  
  Esta função irá retornar o valor acumulado de reajustes na data determinada. Este cálculo será feito subtraindo o valor reajustado do valor anterior a ele (onde o valor anterior poderá ser o valor original, um aditivo anterior ou um outro reajuste anterior). Caso haja algum escalonamento nesta data, esta função de fórmula irá retornar, caso existam, o valor de reajuste do escalonamento acumulado, ignorando entretanto os valores de reajustes do contrato.

**Valores referentes ao imóvel do contrato de locação**

* **VALORDOIMOVELDATA**  
  Retorna o valor do imóvel do contrato na data processada (período contábil). Considera os reajustes, aditivos e escalonamentos
* **VALORANTERIORDOIMOVELDATA**  
  Retorna o valor do imóvel do contrato na data anterior à data processada (período contábil). Considera os reajustes, aditivos e escalonamentos.

**Valores referentes ao rateio por centro de custo do contrato de locação**

* **CODIGOCENTROCUSTORATEIO**  
  Retorna o código do centro de custo do rateio
* **PERCENTUALCENTROCUSTORATEIO**  
  Retorna o percentual do centro de custo do rateio.

**Valores referentes à rescisão**

* **VALORDARESCISAOPROLOCADOR**  
  Valor da Rescisão do Locador
* **VALORFINALDARESCISAOLOCADOR**  
  Valor Final da Rescisão do Locador
* **VALORDEDESCONTOLOCADOR**  
  Valor do Desconto da Rescisão do Locador
* **VALORDARESCISAOPROLOCATARIO**  
  Valor da Rescisão do Locatário
* **VALORFINALDARESCISAOLOCATARIO**  
  Valor Final da Rescisão do Locatário
* **VALORDEDESCONTOLOCATARIO**  
  Valor do Desconto da Rescisão do Locatário.
