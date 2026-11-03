---
content_hash: a63a808e053261a7bf560c592e257796b8cacdbe5c697a640dbd977a06f3b53a
fetched_at: '2026-06-29T00:12:10.739509+00:00'
page_id: '953003537'
product: rm
source: tdn-rm
title: Grupo W01 – Total da NF-e / ISSQN
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003537
version: 1
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo W01 – Total da NF-e / ISSQN** | | | | | | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 342 | W17 | ISSQNtot | Grupo Totais referentes ao ISSQN | G | W01 | - | 0-1 | - |  |  |  | Grupo e tag filhas gerados somente considerando os produtos do tipo serviço. |
| 343 | W18 | vServ | Valor total dos Serviços sob não-incidência ou não tributados pelo ICMS | E | W17 | N | 0-1 | 13v2 |  | Se parâmetro "EditaPrecoTotalItem" estiver marcado e valor total do item > 0 então TITMMOV.VALORTOTALITEM senão (TITMMOV.QUANTIDADE \* TITMMOV.PRECOUNITARIO) |  |  |
| 344 | W19 | vBC | Valor total Base de Cálculo do ISS | E | W17 | N | 0-1 | 13v2 |  |  |  | Totaliza o valor do vBC do ISS dos itens. |
| 345 | W20 | vISS | Valor total do ISS | E | W17 | N | 0-1 | 13v2 |  |  |  | Totaliza o valor do vISSQN do ISS dos itens. |
| 346 | W21 | vPIS | Valor total do PIS sobre serviços | E | W17 | N | 0-1 | 13v2 |  |  |  | Totaliza o valor do vPIS de qualquer grupo de PIS gerado nos itens. |
| 347 | W22 | vCOFINS | Valor total da COFINS sobre serviços | E | W17 | N | 0-1 | 13v2 |  |  |  | Totaliza o valor do vCOFINS de qualquer grupo de COFINS gerado nos itens. |
| 347a | W22a | dCompet | Data da prestação do serviço | E | W01 | N | 1-1 | 8 | Formato: “AAAA-MM-DD” | TMOV.DATASAIDA |  |  |
| 347b | W22b | vDeducao | Valor total dedução para redução da Base de Cálculo | E | W17 | N | 0-1 | 13v2 |  |  |  | Totaliza o valor de vDeducao preenchido no grupo de ISSQN dos itens. |
| 347c | W22c | vOutro | Valor total outras retenções | E | W17 | N | 0-1 | 13v2 | Valor declaratório | TTRBMOV.VALOR |  | Será gerado com os valores dos tributos CONTRIBSOCIALRF ou COSIRF do movimento. |
| 347d | W22d | vDescIncond | Valor total desconto incondicionado | E | W17 | N | 0-1 | 13v2 |  |  |  | Totaliza o valor de vDescIncond preenchido no grupo de ISSQN dos itens. |
| 347e | W22e | vDescCond | Valor total desconto condicionado | E | W17 | N | 0-1 | 13v2 |  |  |  | Totaliza o valor de vDescCond preenchido no grupo de ISSQN dos itens. |
| 347f | W22f | vISSRet | Valor total retenção ISS | E | W17 | N | 0-1 | 13v2 |  |  |  | Totaliza o valor de vISSRet preenchido no grupo de ISSQN dos itens. |
| 347g | W22g | cRegTrib | Código do Regime Especial de Tributação | E | W17 | N | 0-1 | 2 | 1=Microempresa Municipal; 2=Estimativa; 3=Sociedade de Profissionais; 4=Cooperativa; 5=Microempresário Individual (MEI); 6=Microempresário e Empresa de Pequeno Porte (ME/EPP) |  |  | Se Porte da Empresa igual Micro Empresa Entao 1=Microempresa Municipal; Senao Se Porte da Empresa igual Empresa de Pequeno Porte Entao 6=Microempresário e Empresa de Pequeno Porte (ME/EPP) Senao Se Regime de ISS da empresa igual Estimativa Entao 2=Estimativa; Senao Se Regime de ISS da empresa igual sociedade Profissional Entao 3=Sociedade de Profissionais; Senao Se Regime de ISS da empresa igual Cooperativa Entao 4=Cooperativa; Senao Não gera a TAG |
