---
content_hash: 3d59296efd728eb42157d1fec17626f65a5f442e4ebb9694aeca9afbae932601
fetched_at: '2026-06-29T00:11:26.859694+00:00'
page_id: '721006785'
product: rm
source: tdn-rm
title: 'FISCAL01-18149 - Ticket #15549341 - DT - Na IN 2.083/22 Meses do cálculo foram
  alterados, passando de abril a setembro e de Outubro a março.'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=721006785
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Apuração de Tributos |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-18942, FISCAL01-18926 |

## **02. SITUAÇÃO/REQUISITO**

Temos no sistema, em obrigações principais – Eventos Tributários - POEB, o cadastro para o usuário incluir manualmente o mês e o % da POEB.

Estas informações são utilizadas na apuração da POEB somente os valores dos meses de março e setembro, estes meses são tratados internamente.

A IN 2.083/22 alterou os meses, passando de abril a setembro e de outubro a março.

<http://normas.receita.fazenda.gov.br/sijut2consulta/link.action?visao=anotado&idAto=124142>

## **03. SOLUÇÃO**

Ajuste no cálculo do POEB que a partir do mês 06/2022 deve considerar os meses 4 e 10 para realizar o cálculo.

Disponível a partir da biblioteca 12.1.33
