---
content_hash: 85bc70ed04c88828c42ab4a7270ccc140421a15cf5c456e988cc8a2509c35bf6
fetched_at: '2026-06-29T00:08:50.326435+00:00'
page_id: '334334136'
product: rm
source: tdn-rm
title: Como separar 1/3 de Férias Proporcionais e Indenizadas?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=334334136
version: 3
---

Devido a necessidade de adaptação de algumas verbas rescisórias às novas regras do eSocial, será necessária a criação de novos eventos com os códigos de cálculo abaixo:

* 365 - FÉRIAS EM DOBRO RESCISÃO
* 366 - ADICIONAL 1/3 FÉRIAS EM DOBRO RESCISÃO
* 367 - ADICIONAL 1/3 FÉRIAS VENCIDAS RESCISÃO
* 368 - DIFERENÇA 1/3 FÉRIAS VENCIDAS RESCISÃO
* 369 - ADICIONAL 1/3 FÉRIAS PROPORCIONAIS RESCISÃO
* 370 - DIFERENÇA 1/3 FÉRIAS PROPORCIONAIS RESCISÃO

As informações de cada um destes códigos de cálculos estão no WikiHelp: <http://wikihelp.totvs.com.br/WikiHelp/FOP/FOP.CodigosCalculo.aspx>

No parametrizador marcar o parâmetro “Separar Médias de Férias Vencidas e Proporcionais na Rescisão”.

Este parâmetro também deve rá ser marcado pois, segundo as regras do eSocial, as verbas rescisórias referentes as férias do período vencido devem ser enviadas separadas das verbas referentes ao período proporcional.

Informar a data em “A partir de: “ - Para marcar a partir de qual data será o marco do cálculo feito separando Médias e 1/3 de férias vencidas e proporcionais na rescisão informe esta data.

**Observação:** É importante informar a data correta na marcação do parâmetro, para evitar inconsistências no caso de uma Rescisão Complementar.

Exemplo de cálculo de rescisão com estes códigos de cálculo:

Observação: O evento adicional de rescisão 0016 – Provento Férias foi considerado no cálculo do 1/3 de férias vencidas.

 Exemplo de cálculo de rescisão complementar com estes códigos de cálculo:

**Para maiores informações:**

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)
