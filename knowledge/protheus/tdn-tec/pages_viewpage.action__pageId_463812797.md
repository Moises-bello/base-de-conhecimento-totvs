---
content_hash: 3b9574ba71020eb60b8961ad94d7d50c7d91baefbd36817e5d334c1efdf2c138
fetched_at: '2026-07-02T19:24:24.179622+00:00'
page_id: '463812797'
product: protheus
source: tdn-tec
title: TMSPrinter e FWMSPrinter não conseguem criar arquivo temporário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=463812797
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Quando tem muita concorrência pra gerar impressão seja na FWMSPrinter como na TMSPrinter, elas falham ao tentar gerar o arquivo temporário. |
| Correção | O algoritmo de geração do arquivo temporário foi melhorado pra que tenha menos chance de acontecerem conflitos devido a nomes iguais por dois processos diferentes. |
| Informações adicionais | * Referente ao chamado: MTEC-2407 * Disponível em builds iguais ou superiores a [13.1.3.42](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.42) e [13.2.3.42](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.42). |
