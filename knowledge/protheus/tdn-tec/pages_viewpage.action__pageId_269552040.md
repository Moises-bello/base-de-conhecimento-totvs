---
content_hash: 239a872a9466b3be4054046c3f8c7269effb3b336908276f32528917a3649d08
fetched_at: '2026-07-02T19:24:22.439220+00:00'
page_id: '269552040'
product: protheus
source: tdn-tec
title: Invasão de Memória ao Utilizar a Função ADVPL NotBit
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=269552040
version: 2
---

Invasão de Memória ao Utilizar a Função ADVPL NotBit

|  |  |
| --- | --- |
| Situação | Invasão de Memória ao Utilizar a Função ADVPL NotBit |
| Ocorrência | Ao executar a rotina 'Carga Máquina' a função NotBit é utilizada e causa uma invasão de memória decorrente da otimização no compilador gcc. |
| Correção | Remoção da otimização do gcc somente em NotBit. |
| Informações adicionais | * Referente ao chamado: TVRELK * Referente à ocorrência: SSIM-1242 * Disponível em builds superiores a 2.3.0 |
