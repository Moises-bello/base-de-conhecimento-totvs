---
content_hash: 3f74a975cf52654878c10415fd9f23636baf8d969ca0f8b27c5853030ece8e0d
fetched_at: '2026-06-29T00:05:52.066943+00:00'
page_id: '1056144344'
product: rm
source: tdn-rm
title: Totais monetários e alíquotas aplicadas ao documento (TPF)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=1056144344
version: 4
---

### Voltar para [Layout único de integração da NFS-e com o TPF](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143731)

| Nome | Pai | Tipo Elemento | Ocorrência | Descrição | Campo no RM | Observações |
| --- | --- | --- | --- | --- | --- | --- |
| valores | **[rps](https://tdn.totvs.com/pages/viewpage.action?pageId=1056143860)** | G | 1-1 | Tag raíz para os valores totais do documento. |  |  |
| iss | valores | E | 1-1 | Valor total de ISS do documento. | SOMA(Servico.valiss de todos os itens da nota) | Para o município de Brasília é possível cadastrar ISS devido e retido simultaneamente na mesma nota, por tanto para o tributo ISS o valor considerado será apenas os valores de ISS cujo tipo de retenção seja "Devido" ou "Depósito Juízo". |
| issret | valores | E | 1-1 | Valor total de ISS retido do documento. | SOMA(Servico.valissret de todos os itens da nota) |  |
| outrret | valores | E | 1-1 | Valor total de outras retenções do documento. | SOMA(Servico.valoutasret de todos os itens da nota) |  |
| pis | valores | E | 1-1 | Valor total de PIS do documento. | SOMA(Servico.valpis de todos os itens da nota) |  |
| dJustificaDeducao | valores | E | 0-1 | Discriminação da dedução sobre o serviço | TMOVCOMPL.DISCRDEDUCOES | Gerado apenas para Totvs Colaboração |
| cofins | valores | E | 1-1 | Valor total de COFINS do documento. | SOMA(Servico.valcof de todos os itens da nota) |  |
| inss | valores | E | 1-1 | Valor total de INSS do documento. | SOMA(Servico.valinss de todos os itens da nota) |  |
| ir | valores | E | 1-1 | Valor total de IR do documento. | SOMA(Servico.valir de todos os itens da nota) |  |
| csll | valores | E | 1-1 | Valor total de CSLL do documento. | SOMA(Servico.valcsll de todos os itens da nota) |  |
| aliqiss | valores | E | 1-1 | Alíquota de ISS do documento. | TTRBMOV.ALIQUOTA | Aliquota do ISS |
| aliqpis | valores | E | 1-1 | Alíquota de PIS do documento. | TTRBMOV.ALIQUOTA | Aliquota do PIS |
| aliqcof | valores | E | 1-1 | Alíquota de COFINS do documento. | TTRBMOV.ALIQUOTA | Aliquota do COFINS |
| aliqinss | valores | E | 1-1 | Alíquota de INSS do documento. | TTRBMOV.ALIQUOTA | Aliquota do INSS |
| aliqir | valores | E | 1-1 | Alíquota de IR do documento. | TTRBMOV.ALIQUOTA | Aliquota do IR |
| aliqcsll | valores | E | 1-1 | Alíquota de CSLL do documento. | TTRBMOV.ALIQUOTA | Aliquota do CSLL |
| valtotdoc | valores | E | 1-1 | Valor total do documento. |  | SOMA(servico.valtotal de todos os itens da nota) |
| valcartri | valores | E | 0-1 | Valor da carga tributaria | TITMMOVFISCAL.VLRTOTTRIB |  |
| valpercartri | valores | E | 0-1 | Percentual da carga tributaria |  | Soma dos campos do serviço utilizado:  TPRDCODFISCAL.ALIQIBPTFEDERAL,   TPRDCODFISCAL.ALIQIBPTESTADUAL,                                          TPRDCODFISCAL.ALIQIBPTMUNICIPAL |
| valfoncartri | valores | E | 0-1 | Fonte da carga tributaria |  | Informação Fixa : IBPT |
| percentualDeducoes | valores | E | 0-1 | Valor percentual padrão para dedução/redução do valor do serviço | **Não Será Gerado** |  |
| valorTotalRecebido | valores | E | 0-1 | Valor da base de cálculos das outras retenções | **Não Será Gerado** |  |
| baseCalculoOutrasRet | valores | E | 0-1 | Valor da aliquota das outras informações | **Não Será Gerado** |  |
| codigoTribNacional | valores | E | 0-1 | Código de tributação municipal | Cadastro do Produto, Anexo "Tributo do Produto Por Município", Campo "Código do Serviço no Município"  DTRBMUNICIPIOPRD.CODIGOSERVICO | **Obs.**:  Será gerado somente com o TPF. |
| aliquotaOutrasRet | valores | E | 0-1 | Valor da aliquota das outras informações | **Não Será Gerado** |  |
| tributosfederais | valores | G | 0-1 | Grupo de valores relacionados a Tributos Federais |  |  |
| aliquotaRetencoes | tributosfederais | E | 0-1 | Valor percentual total aproximado dos tributos federais | TPRDCODFISCAL.ALIQIBPTFEDERAL | **Obs.**:  Será gerado somente com o TPF. |
| tributosmunicipais | valores | G | 0-1 | Grupo de valores relacionados a Tributos Municipais |  |  |
| valorTotal | tributosmunicipais | E | 0-1 | Valor monetário total aproximado dos tributos municipais | TITMMOVFISCAL.VALORIBPTMUNICIPAL  *(Soma dos valores dos Tributos Municipais do Movimento)* | **Obs.:** Será gerado somente com o TPF. |
| aliquotaRetencoes | tributosmunicipais | E | 0-1 | Valor percentual total aproximado dos tributos municipais | TPRDCODFISCAL.ALIQIBPTMUNICIPAL | **Obs.:** Será gerado somente com o TPF. |
| tributosestaduais | valores | G | 0-1 | Grupo de valores relacionados a Tributos Estaduais |  |  |
| aliquotaRetencoes | tributosestaduais | E | 0-1 | Valor percentual total aproximado dos tributos estaduais | TPRDCODFISCAL.ALIQIBPTESTADUAL | **Obs.:** Será gerado somente com o TPF. |
| valorTotal | tributosestaduais | E | 0-1 | Valor monetário total aproximado dos tributos estaduais | TITMMOVFISCAL.VALORIBPTESTADUAL  *(Soma dos valores dos Tributos Estaduais do Movimento)* | **Obs.:** Será gerado somente com o TPF. |
| ibscbs | valores | G | 0-1 |  |  |  |
