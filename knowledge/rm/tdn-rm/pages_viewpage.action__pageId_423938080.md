---
content_hash: 996bf05a57c60e1c1d4a0785e52525e22743c2e4d2dd3bccc3e7b99d2f905599
fetched_at: '2026-06-29T00:09:25.253546+00:00'
page_id: '423938080'
product: rm
source: tdn-rm
title: Cotação com Margem de Lucro ICMS ST
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938080
version: 2
---

Para que os campos "Margem de Lucro ICMS ST" e "% ICMSST" sejam apresentados no item do Orçamento, deve ser habilitado o parâmetro "Usar ICMS no Item de Orçamento" nos Parâmetros de [Cotação em Definições Gerais 2/4](http://tdn.totvs.com/pages/viewpage.action?pageId=423938121).  
O campo "Margem de Lucro ICMS ST" quando habilitado no Item de Orçamento é carregado com o valor do Campo "Margem S.T (%)" ([Cadastro do Produto | Anexos | Dados Fiscais por UF](http://tdn.totvs.com/display/LRM/Dados+Fiscais+por+UF)) que pode ser cadastrado por Estado. No momento do registro de orçamento esse campo pode ser editado.  
    
 **Cálculo Melhor Oferta**

Quando informados os campos "% ICMSST" e "Margem de Lucro do ICMS ST", ao calcular o Quadro Comparativo o valor da melhor oferta será de acordo com o seguinte cálculo:

* **Valor Bruto ICMSST** = (Valor Equalizado do Produto + Margem de Lucro ICMS ST) x %ICMSST
* **Valor do ICMS** = Valor Equalizado do Produto x %ICMSST
* **Valor Líquido do ICMSST** = Valor Bruto ICMSST - Valor do ICMS
* **Valor do Calculado para Melhor Oferta** = Valor Equalizado do Produto + Valor Líquido do ICMSST.

**Dica!**No Quadro Comparativo, para visualizar os valores de ICMSST e Margem ICMSST, e também outras informações complementares do cálculo, pressione CTRL e clique no quadro sobre algum valor calculado para o produto.  
***Observações******:***

* Quando é informada a Margem de Lucro ICMS ST o sistema não realiza o cálculo padrão de diferencial de alíquota de ICMS/ICMSST.
* O campo Margem de Lucro ICMSST não é levado para o Movimento de Ordem de Compra gerado a partir da Cotação. Isto implica que caso o valor da Margem de Lucro, buscado do default do produto na criação da cotação, seja alterado, o calculo da melhor oferta na Cotação poderá ser diferente do gerado na Ordem de Compra.
