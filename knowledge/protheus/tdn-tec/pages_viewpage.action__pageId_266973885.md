---
content_hash: 44717292865626cc073dc3e61b896717780d2562c9277ec9d0f2670a6a657763
fetched_at: '2026-07-02T19:24:21.334718+00:00'
page_id: '266973885'
product: protheus
source: tdn-tec
title: Crescimento do consumo de memória ao utilizar a função Directory
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=266973885
version: 2
---

Crescimento do consumo de memória ao utilizar a função Directory

|  |  |
| --- | --- |
| Situação | Crescimento do consumo de memória ao utilizar a função Directory |
| Ocorrência | Ao utilizar a função Directory em diretórios com mais de 10000 arquivos a memória do AppServer ficava extremamente alta |
| Melhoria | Proteção na função Directory para que só permita diretórios com até 10000 arquivos. |
| Informações adicionais | * Referente ao chamado: SSIM-974 * Referente à ocorrência: TTEC-616 * Disponível em builds superiores a 7.00.131227A - 1.0.3 |
