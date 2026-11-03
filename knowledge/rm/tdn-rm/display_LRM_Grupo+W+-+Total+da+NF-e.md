---
content_hash: 04e4bd67863778cdbf62c623633452e68879ebb87f0a976cf914b47951c39c91
fetched_at: '2026-06-29T00:12:10.726590+00:00'
page_id: '953003493'
product: rm
source: tdn-rm
title: Grupo W - Total da NF-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+W+-+Total+da+NF-e
version: 2
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo W - Total da NF-e** | | | | | | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 326 | W01 | Total | Grupo Totais da NF-e | G | A01 |  | 1-1 | - | O grupo de valores totais da NF-e deve ser informado com o somatório do campo correspondente dos itens |  |  |  |
| 327 | W02 | ICMSTot | Grupo Totais referentes ao ICMS | G | W01 |  | 1-1 | 13v2 |  |  |  | Totaliza o valor do vPIS de qualquer grupo de PIS gerado nos itens. |
| 328 | W03 | vBC | Base de Cálculo do ICMS | E | W02 | N | 1-1 | 13v2 |  |  |  | Totaliza o valor de .vBC de qualquer grupo de ICMS gerado nos itens. |
| 329 | W04 | vICMS | Valor Total do ICMS | E | W02 | N | 1-1 | 13v2 |  | TTRBMOV.VALOR (ICMS) | Valor |  |
| 329.01 | W04a | vICMSDeson | Valor Total do ICMS desonerado | E | W02 | N | 1-1 | 13v2 |  |  | Será preenchido com o valor total do campo **vICMSDeson** dos itens |  |
| 329.03 | W04c | vFCPUFDest | Valor total do ICMS relativo Fundo de Combate à Pobreza (FCP) da UF de destino. | E | W02 | N | 0-1 | 13v2 | Valor total do ICMS relativo ao Fundo de Combate à Pobreza (FCP) para a UF de destino. | (DREGRAICMS.PERICMSFCP/100 )\*  TTRBMOV.BASEDECALCULO | Tag calculada. |  |
| 329.05 | W04e | vICMSUFDest | Valor total do ICMS Interestadual para a UF de destino | E | W02 | N | 0-1 | 13v2 | Valor total do ICMS Interestadual para a UF de destino (sem o valor do ICMS relativo ao FCP). | (((DREGRAICMS.ALIQSUBST/100) \*  TTRBMOV.BASEDECALCULO) - ((DREGRAICMS.ALIQICMS / 100) \* TTRBMOV.BASEDECALCULO))) \* (DREGRAICMS.PERICMSESTDESTINO/100) | Tag calculada. |  |
| 329.07 | W04g | vICMSUFRemet | Valor total do ICMS Interestadual para a UF do remetente | E | W02 | N | 0-1 | 13v2 | Valor total do ICMS Interestadual para a UF do remetente. Nota: A partir de 2019, este valor será zero | ValorICMSDes - (((DREGRAICMS.ALIQSUBST/100) \*  TTRBMOV.BASEDECALCULO) - ((DREGRAICMS.ALIQICMS / 100) \* TTRBMOV.BASEDECALCULO))) | Tag calculada. |  |
| 329.08 | W04h | vFCP | Valor Total do FCP (Fundo de Combate à Pobreza) | E | W02 | N | 1-1 | 13v2 | Corresponde ao total da soma dos campos id: N17c |  |  |  |
| 330 | W05 | vBCST | Base de Cálculo do ICMS ST | E | W02 | N | 1-1 | 13v2 |  | TTRBMOV.BASEDECALCULO (ICMSST) |  |  |
| 331 | W06 | vST | Valor Total do ICMS ST | E | W02 | N | 1-1 | 13v2 |  |  |  | Será totalizado o valor do ICMS ST do cujo a natureza esteja configurada para o ST somar no valor contábil da NF-e. |
| 331.01 | W06a | vFCPST | Valor Total do FCP (Fundo de Combate à Pobreza) retido por substituição tributária | E | W02 | N | 1-1 | 13v2 | Corresponde ao total da soma dos campos id:N23d | Corresponde ao total da soma dos campos id:N23d |  |  |
| 331.02 | W06b | vFCPSTRet | Valor Total do FCP retido anteriormente por Substituição Tributária | E | W02 | N | 1-1 | 13v2 | Corresponde ao total da soma dos campos id:N27d) | Corresponde ao total da soma dos campos id:N27d |  |  |
| 332 | W07 | vProd | Valor Total dos produtos e serviços | E | W02 | N | 1-1 | 13v2 |  | Se parâmetro "EditaPrecoTotalItem" estiver marcado e valor total do item > 0 então TITMMOV.VALORTOTALITEM senão (TITMMOV.QUANTIDADE \* TITMMOV.PRECOUNITARIO) |  |  |
| 333 | W08 | vFrete | Valor Total do Frete | E | W02 | N | 1-1 | 13v2 |  | TITMMOV.RATEIOFRETE |  |  |
| 334 | W09 | vSeg | Valor Total do Seguro | E | W02 | N | 1-1 | 13v2 |  | TITMMOV.RATEIOSEGURO |  |  |
| 335 | W10 | vDesc | Valor Total do Desconto | E | W02 | N | 1-1 | 13v2 |  | TITMMOV.RATEIODESC + TITMMOV.VALORDESC |  |  |
| 336 | W11 | vII | Valor Total do II | E | W02 | N | 1-1 | 13v2 |  | TTRBMOV.VALOR |  | Totaliza o valor de vII preenchido no grupo de imposto de importação dos itens |
| 337 | W12 | vIPI | Valor Total do IPI | E | W02 | N | 1-1 | 13v2 |  |  |  | Totaliza o valor de vIPI do grupo de IPITrib gerado nos itens |
| 337.01 | W12a | vIPIDevol | Valor Total do IPI devolvido | E | W02 | N | 1-1 | 13v2 | Deve ser informado quando preenchido o Grupo Tributos Devolvidos na emissão de nota finNFe=4 (devolução) nas operações com não contribuintes do IPI. Corresponde ao total da soma dos campos id:UA04. | NÃO SERÁ GERADO |  |  |
| 338 | W13 | vPIS | Valor do PIS | E | W02 | N | 1-1 | 13v2 |  |  |  | Totaliza o valor de vPIS de qualquer grupo de PIS gerado nos itens. |
| 339 | W14 | vCOFINS | Valor do COFINS | E | W02 | N | 1-1 | 13v2 |  |  |  | Totaliza o valor de vCOFINS de qualquer grupo de COFINS gerado nos itens. |
| 340 | W15 | vOutro | Outras Despesas acessórias | E | W02 | N | 1-1 | 13v2 |  | TITMMOV.VALORDESP |  |  |
| 341 | W16 | vNF | Valor Total da NF-e | E | W02 | N | 1-1 | 13v2 | Vide validação para este campo na regra de validação W16-xx. | TMOV.VALORLIQUIDO |  |  |
| 341ª | W16a | vTotTrib | Valor aproximado total de tributos federais, estaduais e municipais. | E | W02 | N | 0-1 | 13v2 | (NT 2013/003) |  |  | Totaliza o valor de vTotTrib dos itens. |
