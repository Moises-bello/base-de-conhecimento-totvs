---
content_hash: bddf4d2dd9483f5d4fc84afb4591a0cddf0fa1aa8fabc9dbd6731ba239769293
fetched_at: '2026-07-02T19:24:23.272114+00:00'
page_id: '301188643'
product: protheus
source: tdn-tec
title: Correção - TSay quando criado sem largura, altura e pai, não aparece
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=301188643
version: 1
---

Mantido o legado de mesmo que um TSay não tenha largura, altura e pai, deve ser apresentado corretamente com seu tamanho conforme seu conteúdo.

|  |  |
| --- | --- |
| Situação | TSay sem largura, altura e pai não aparece. |
| Ocorrência | O problema acontece porque o sistema não está calculando a largura e altura pelo conteúdo. |
| Correção | O cálculo de tamanho foi reimplementado. |
| Informações adicionais | * Referente à ocorrência: MTEC-705 * Disponível em builds superiores a 170117a-20171002 |
