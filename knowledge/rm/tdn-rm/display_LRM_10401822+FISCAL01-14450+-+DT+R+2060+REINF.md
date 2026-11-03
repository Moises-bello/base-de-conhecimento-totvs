---
content_hash: 8adcebfb3a4e6935846a44ec81ef8db6aede1b970530c7e39e80a501b20032cf
fetched_at: '2026-06-29T00:10:53.930044+00:00'
page_id: '590020655'
product: rm
source: tdn-rm
title: 10401822 FISCAL01-14450 - DT R 2060 REINF
type: documentation
url: https://tdn.totvs.com/display/LRM/10401822+FISCAL01-14450+-+DT+R+2060+REINF
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS Backoffice |
| Linha de Produto: | DistribuiçãoConstrução ProjetosLinha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF;  Período de Apuração. |
| Ticket: | 10401822 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-14450 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o REINF, evento R-2060 o sistema está desconsiderando o valor da exclusão e não gerando o valor correto da base de calculo da Contribuição Previdenciária. 

## **03. SOLUÇÃO**

Os dados do Registro 2060 da REINF vem diretamente do período de apuração, este qual utilizava o código da conta contábil como chave graças ao obsoleto bloco P da EFD Contribuições.

Este não é o caso da REINF ocasionando erro de cálculo em casos onde houvessem exclusões e saídas com contas contábeis distintas.

Em consequência do defeito e a inutilização do bloco P, todos os períodos de apuração do CPRB com o ano maior ou igual a 2020 passam a **não agrupar** por conta contábil.
