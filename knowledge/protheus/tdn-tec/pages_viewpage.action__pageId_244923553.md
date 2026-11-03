---
content_hash: 21b1dc6026174a4b3c7a3763827c9b2a9c7530044c37f8fe496268269b8ef168
fetched_at: '2026-07-02T19:24:20.392921+00:00'
page_id: '244923553'
product: protheus
source: tdn-tec
title: Erro ao gerar PDOC de Métodos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244923553
version: 1
---

|  |  |
| --- | --- |
| Situação | Ao exportar os PDOCs para HTML simples, o TDS reclamava da falta de um arquivo |
| Ocorrência | Verificamos que realmente faltava um arquivo, adicionamos o arquivo de acordo com a formatação necessária |
| Correção | Adicionamos o arquivo "method.vm" que é utilizado para exportar PDOC |
| Informações adicionais | * Referente ao chamado: TVRAUO * Referente à ocorrência: SSIM-1188 * Disponível em builds superiores a 11.3.2 |
