---
content_hash: 9ba623ae65c1bc93888cb3e5e80a8fda524ad43a77dc7f34a1778a0d32d1e46b
fetched_at: '2026-06-29T00:09:20.002614+00:00'
page_id: '422545628'
product: rm
source: tdn-rm
title: Lei da Transparência Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545628
version: 15
---

[Conforme Lei 12.741/2012](http://www.planalto.gov.br/ccivil_03/_Ato2011-2014/2012/Lei/L12741.htm), a partir de 10/06/2013 todas as empresas que vendem produtos ou serviços ao consumidor estão obrigadas a informar em cupons e notas fiscais o valor aproximado de tributos que estão embutidos no preço final.

Para tanto, as empresas vendedoras devem fazer o cálculo conforme descrito na lei, ou alternativamente, podem utilizar as alíquotas tributárias disponibilizadas por entidades especializadas em análise de dados econômicos (Art. 2º da Lei):  
*\[...\] Art. 2º Os valores aproximados de que trata o art. 1º serão apurados sobre cada operação e poderão, a critério das empresas vendedoras, ser calculados e fornecidos, semestralmente por instituição de âmbito nacional reconhecidamente idônea, voltada primordialmente à apuração e análise de dados econômicos \[...\]*

A TOTVS optou por utilizar a tabela disponibilizada pelo IBPT - Instituto Brasileiro de Planejamento Tributário denominada IBPTax, que contém as alíquotas tributárias por produtos e serviços, de modo minimizar o impacto operacional e financeiro dos clientes.

Com a importação da tabela IBPTax serão preenchidos ou atualizados os dados fiscais do Produtos com a alíquota aproximada da tributação incidente no mesmo. A correspondência entre a Tabela e a lista de alíquotas importadas será feita pelo NCM do Produto.

Quando se tratar de serviço a correspondência será feita pelo código NBS do produto. Estas informações serão gravadas no movimento de venda e posteriormente na TAG "vTotTrib" da Nota Fiscal Eletrônica e impresso no DANFE correspondente.

Verifique as alíquotas importadas no cadastro dos produtos em [<span style="color: #0000ee"><span style="text-decoration: underline; ">Anexos | Dados Fiscais do Produto</span></span>|/WikiHelp/EST/Est.DadosFiscaisProduto] através do TOTVS Gestão de Estoques, Compras e Faturamento.

Maiores Informações

* [Processo de Importação da Tabela IBPTax](http://tdn.totvs.com/pages/viewpage.action?pageId=235325554)
* [Tabela IBPTax](https://deolhonoimposto.ibpt.org.br/)
* [Campo Valor Aproximado do Tributo](http://tdn.totvs.com/pages/viewpage.action?pageId=235325554)
