---
content_hash: 407e870defc26d5dd50b2355cca75e316c7dcf508320e267cf792c1266fbdcba
fetched_at: '2026-06-29T00:09:53.483792+00:00'
page_id: '440839571'
product: rm
source: tdn-rm
title: FOPCALCULO01-5355 Diferença Salarial por Dissídio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=440839571
version: 1
---

# Diferença Salário Dissídio

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | Plataforma RH |
| **Módulo:** | Folha de Pagamento |
| **Função:** | Diferença de Salário por Dissídio |
| **Situação/Requisito:** | Ao realizar uma Diferença Salarial por Dissídio de um mês retroativo, em que já houver uma diferença de férias (dissídio não), o produto está recalculando o desconto de INSS incorretamente, as verbas de Diferença de Férias entram em dobro para a base de INSS, consequentemente o funcionário terá um desconto de INSS a maior. |
| **Solução/Implementação:** | Ajuste no cálculo de diferença salarial, para não duplicar a base de INSS quando já existir diferença do mês para o mesmo mês. |
