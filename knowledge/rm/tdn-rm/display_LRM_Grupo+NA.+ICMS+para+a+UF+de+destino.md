---
content_hash: 978604bcdcb81149a6e26b831f06068fc42f54b595d8a117d462de7877581362
fetched_at: '2026-06-29T00:12:10.603634+00:00'
page_id: '953002600'
product: rm
source: tdn-rm
title: Grupo NA. ICMS para a UF de destino
type: documentation
url: https://tdn.totvs.com/display/LRM/Grupo+NA.+ICMS+para+a+UF+de+destino
version: 4
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo NA. ICMS para a UF de destino** | | | | | | | | | | | | |
| # | ID | Campo | Descrição | Ele | Pai | Tipo | Ocorrência | Tamanho | Observação | Campo Origem | Campo na Aplicação | Mais Informações |
| 245a.01 | NA01 | ICMSUFDest | Informação do ICMS Interestadual | G | M01 |  | 0-1 |  | Grupo a ser informado nas vendas interestaduais para consumidor final, não contribuinte do ICMS. Observação: Este grupo não deve ser utilizado nas operações com veículos automotores novos efetuadas por meio de faturamento direto para o consumidor (Convênio ICMS 51/00), as quais possuem grupo de campos próprio (ICMSPart) 245a | - | - | O grupo é gerado nas seguintes condições: - Operação Interestadual; - Operação com Consumidor Final; - Destinatário Contribuinte; - Não gerar para Nota Fiscal de Ajuste e Nota Complementar; - Gerar somente se Natureza de Diferencial de Alíquota; |
| 245a.03 | NA03 | vBCUFDest | Valor da BC do ICMS na UF de destino | E | NA01 | N | 1-1 | 13v2 | Valor da Base de Cálculo do ICMS na UF de destino | TTRBMOV.BASEICMSDIFALIQ | Base de Cálculo do ICMS Diferencial | - |
| 245a.04 | NA04 | vBCFCPUFDest | Valor da BC FCP na UF de destino |  |  |  | 0-1 | 13v2 | Valor da Base de Cálculo do FCP na UF de destino. | TTRBMOV.BASEICMSDIFALIQ | - | - |
| 245a.05 | NA05 | pFCPUFDest | Percentual do ICMS relativo ao Fundo de Combate à Pobreza (FCP) na UF de destino | E | NA01 | N | 0-1 | 3v2-4 | Percentual adicional inserido na alíquota interna da UF de destino, relativo ao Fundo de Combate à Pobreza (FCP) naquela UF. | TPRDCODFISCAL.PERFECP | - | - |
| 245a.07 | NA07 | pICMSUFDest | Alíquota interna da UF de destino | E | NA01 | N | 1-1 | 3v2-4 | Alíquota adotada nas operações internas na UF de destino para o produto / mercadoria. A alíquota do Fundo de Combate à Pobreza, se existente para o produto / mercadoria, deve ser informada no campo próprio (pFCPUFDest) não devendo ser somada a essa alíquota interna. | DREGRAICMS.ALIQSUBST | Alíquota da Substituição Tributária | - |
| 245a.09 | NA09 | pICMSInter | Alíquota interestadual das UF envolvidas | E | NA01 | N | 1-1 | 2v2 | Alíquota interestadual das UF envolvidas: - 4% alíquota interestadual para produtos importados; - 7% para os Estados de origem do Sul e Sudeste (exceto ES), destinado para os Estados do Norte, Nordeste, Centro-Oeste e Espírito Santo; - 12% para os demais casos. | DREGRAICMS.ALIQICMS | Alíquota do ICMS Próprio | - |
| 245a.11 | NA11 | pICMSInterPart | Percentual provisório de partilha do ICMS Interestadual | E | NA01 | N | 1-1 | 3v2-4 | Percentual de ICMS Interestadual para a UF de destino: - 40% em 2016; - 60% em 2017; - 80% em 2018; - 100% a partir de 2019. | DREGRAICMS.PERICMSESTDESTINO | ICMS UF Destinatário | - |
| 245a.13 | NA13 | vFCPUFDest | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino | E | NA01 | N | 0-1 | 13v2 | Valor do ICMS relativo ao Fundo de Combate à Pobreza (FCP) da UF de destino. | Calculado automaticamente (pFCPUF(pFCPUFDest)  \* VBC(vBCUFDest)) | - | - |
| 245a.15 | NA15 | vICMSUFDest | Valor do ICMS Interestadual para a UF de destino | E | NA01 | N | 1-1 | 13v2 | Valor do ICMS Interestadual para a UF de destino (sem o valor do ICMS relativo ao FCP). | Calculado automaticamente (pICMSInter(pICMSInterPart) \* ValorDifal) | - | - |
| 245a.17 | NA17 | vICMSUFRemet | Valor do ICMS Interestadual para a UF do remetente | E | NA01 | N | 1-1 | 13v2 | Valor do ICMS Interestadual para a UF do remetente. Nota: A partir de 2019, este valor será zero. | Calculado automaticamente (ValorDifal - vICMSUFDest) | - | - |
