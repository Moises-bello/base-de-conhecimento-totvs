---
content_hash: 100667c50d4a98d88370854e0f1c7632f4cca699999f9f11851ed1eb64ba8eb6
fetched_at: '2026-07-02T19:24:24.184856+00:00'
page_id: '464951789'
product: protheus
source: tdn-tec
title: TCBrowse aparece vazio no SmartClient quando dentro de um FWWizardControl
type: documentation
url: https://tdn.totvs.com/display/tec/TCBrowse+aparece+vazio+no+SmartClient+quando+dentro+de+um+FWWizardControl
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Quando criado um TCBrowse em mais de um passo de um FWWizardControl, a partir do segundo não aparece informação nenhuma. |
| Correção | Força o envio de informações de colunas pro SmartClient pra este caso específico onde o TCBrowse é criado em tempo de execução em uma TDialog já ativada. |
| Informações adicionais | * Referente ao chamado: MTEC-2306 * Disponível em builds iguais ou superiores a [13.1.3.42](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.42) e [13.2.3.42](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.42). |
