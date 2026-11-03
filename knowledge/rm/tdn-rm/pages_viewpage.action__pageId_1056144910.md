---
content_hash: 7b4dd81492fcd5d932f565adb88df7d564d9b6631fe997052fb8cab402673448
fetched_at: '2026-06-29T00:05:52.116584+00:00'
page_id: '1056144910'
product: rm
source: tdn-rm
title: Grupo de valores relacionados a IBS e CBS (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056144910
version: 3
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

Grupo gerado apenas quando a Base do Tributo IBS/CBS está maior que zero ou quando a mesma for igual a zero e o Valor Total do Serviço do Item for igual a zero.

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| ibscbs | [valores](https://tdn.totvs.com/pages/viewpage.action?pageId=1056144344) | G | 1-1 | Grupo de valores relacionados a IBS e CBS |  |  |
| valorTotalNotaFiscal | ibscbs | N | 1-1 | Valor Total da NF considerando os impostos por fora: IBS e CBS | TTRBMOV.BASEDECALCULO do tributos (IBS +CBS) + TTRBMOV.VALOR IBS e CBS | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| baseCalculo | ibscbs | N | 1-1 | Valor da base de cálculo (BC) do IBS/CBS antes das reduções para cálculo do tributo bruto | TTRBMOV.VALOR | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| valorRepRes | ibscbs | N | 1-1 | Valor monetário (R$) total relativo ao fornecimento | TITMMOV.VALORBRUTOITEM | Soma do valor bruto (quando parametrizado: Edita Preço Total Item) ou líquido de todos os itens. **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| percentualRedutor | ibscbs | N | 1-1 | Percentual de redução compras governamentais | TTRBMOV.PCTREDUCAOALIQUOTA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| valMulta | ibscbs | N | 0-1 | Valor da multa | **Não Será Gerado** |  |
| valJuros | ibscbs | N | 0-1 | Valor dos juros | **Não Será Gerado** |  |
| valInicialCobrado | ibscbs | N | 0-1 | Valor inicial cobrado pela prestação do serviço | **Não Será Gerado** |  |
| valFinalCobrado | ibscbs | N | 0-1 | Valor total cobrado pela prestação do serviço | **Não Será Gerado** |  |
| valIPI | ibscbs | N | 0-1 | Valor do IPI | **Não Será Gerado** |  |
| tributacaoregular | ibscbs | G | 1-1 | Grupo de valores relacionados a IBS e CBS |  |  |
| aliqEfetivaRegIbsUf | tributacaoregular | N | 1-1 | Alíquota efetiva de tributação regular do IBS estadual | TTRBMOV.ALIQUOTACHEIA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| tributacaoIbsUf | tributacaoregular | N | 1-1 | Valor da tributação regular do IBS estadual | ibscbs.baseCalculo \* aliqEfetivaRegIbsUf | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| aliqEfetivaIbsMunicipio | tributacaoregular | N | 1-1 | Alíquota efetiva de tributação regular do IBS municipal | TTRBMOV.ALIQUOTACHEIA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| tributacaoIbsMunicipio | tributacaoregular | N | 1-1 | Valor da tributação regular do IBS municipal | ibscbs.baseCalculo \* aliqEfetivaIbsMunicipio | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| aliqEfetivaCbs | tributacaoregular | N | 1-1 | Alíquota efetiva de tributação regular da CBS | TTRBMOV.ALIQUOTACHEIA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| valTribRegCBS | tributacaoregular | N | 1-1 | Valor da tributação regular da CBS | Base de cálculo CBS \* aliqEfetivaCbs | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| ibs | ibscbs | G | 1-1 | Grupo que agrupará as Informações Relativas às Totalizações do IBS |  |  |
| valorTotal | ibs | N | 1-1 | Valor total do IBS(UF + Mun) | TTRBMOV.VALOR do IBS Mun + TTRBMOV.VALOR DO IBS UF | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| valorCreditoPresumido | ibs | N | 1-1 | Valor do tributo bruto da Operação para a CBS. | TTRBMOV.VALORCREDPRESUMIDO | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| percentualCreditoPresumido | ibs | N | 0-1 | Percentual do Crédito Presumido do IBS. | TTRBMOV.PCCREDPRESUMIDO | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| valorTotalUf | ibs | N | 1-1 | Total valor do IBS estadual. | TTRBMOV.VALOR para o IBS UF | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| valorTotalDesUf | ibs | N | 1-1 | Total valor desonerado municipal | **Não Será Gerado** |  |
| valorTotalDiferimentoUf | ibs | N | 1-1 | Total do Diferimento estadual | TTRBMOV.TRIBUTODIFERIDO | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| percentualDiferimentoUF | ibs | N | 1-1 | Percentual de diferimento estadual. | TTRBMOV.PCTDIFERIMENTO | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| valorTributacaoOperacaoUf | ibs | N | 1-1 | Valor do tributo bruto da Operação para IBS Estadual | TTRBMOV.VALOR para o IBS UF | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| percentualRedAliqUF | ibs | N | 1-1 | Percentual de redução de alíquota estadual. | TTRBMOV.PCTREDUCAOALIQUOTA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| aliquotaEfetivaUf | ibs | N | 1-1 | Valor da alíquota efetiva UF | TTRBMOV.ALIQUOTA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| aliquotaIBSMunicipio | ibs | N | 0-1 | Alíquota do IBS de competência do Município | TTRBMOV.ALIQUOTACHEIA do IBS Mun | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| valorIbsMunicipio | ibs | N | 1-1 | Total valor do IBS municipal | TTRBMOV.VALOR | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| valorDifMunicipal | ibs | N | 1-1 | Total de diferimento Municipal | TTRBMOV.TRIBUTODIFERIDO | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| percDifMunicipio | ibs | N | 1-1 | Percentual de diferimento municipal | TTRBMOV.PCTDIFERIMENTO | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| aliqMunDes | ibs | N | 1-1 | Valor da alíquota municipal de desoneração do IBS | **Não Será Gerado** |  |
| devTribMun | ibs | N | 1-1 | Devolução personalizada do IBS municipal | **Não Será Gerado** |  |
| tributacaoOpMun | ibs | N | 1-1 | Valor do tributo bruto da Operação para o IBS Municipal | **Não Será Gerado** |  |
| percAliqEfetMun | ibs | N | 1-1 | Percentual de alíquota efetiva municipal | TTRBMOV.ALIQUOTA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| percRedAliqMun | ibs | N | 1-1 | Percentual de redução de alíquota Municipal | TTRBMOV.PCTREDUCAOALIQUOTA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| cbs | ibscbs | G | 1-1 | Grupo que agrupará as Informações Relativas às Totalizações do CBS |  |  |
| valorTotal | cbs | N | 1-1 | Total valor da CBS da União | TTRBMOV.VALOR | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| valorCreditoPresumido | cbs | N | 1-1 | Valor do Crédito Presumido da CBS. | TTRBMOV.VALORCREDPRESUMIDO | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| aliquotaCreditoPresumido | cbs | N | 0-1 | Alíquota do crédito presumido para a CBS | TTRBMOV.PCCREDPRESUMIDO | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| valorDesonerado | cbs | N | 1-1 | Total do valor desonerado CBS | **Não Será Gerado** |  |
| aliqDes | cbs | N | 1-1 | Valor da alíquota Desoneração da CBS | **Não Será Gerado** |  |
| valorDiferimento | cbs | N | 1-1 | Total do Diferimento CBS | TTRBMOV.TRIBUTODIFERIDO | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| percentualDiferimento | cbs | N | 1-1 | Percentual de diferimento da CBS | TTRBMOV.PCTDIFERIMENTO | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| valorTributacaoOperacao | cbs | N | 1-1 | Valor do tributo bruto da Operação para a CBS | TTRBMOV.VALOR | **Obs:** Caso o parâmetro 'Não Agrupa Itens NFSE' esteja marcado, será considerado sempre o primeiro item da nota. Caso contrário, será feito o somatório. |
| percentualAliquotaEfetiva | cbs | N | 1-1 | Percentual da alíquota efetiva do CBS | TTRBMOV.ALIQUOTA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| percRedAliq | cbs | N | 1-1 | Percentual da redução de alíquota CBS | TTRBMOV.PCTREDUCAOALIQUOTA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
| devolucaoTributo | cbs | N | 1-1 | Devolução personalizada da CBS | **Não Será Gerado** |  |
| valorPercentual | cbs | N | 0-1 | Alíquota da UF para CBS da localidade de incidência | TTRBMOV.ALIQUOTACHEIA | **Obs:** Caso a nota tenha mais de um item, será considerado sempre o primeiro item da nota. |
