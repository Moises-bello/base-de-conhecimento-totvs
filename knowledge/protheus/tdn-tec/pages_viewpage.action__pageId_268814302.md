---
content_hash: 5aef7883e77885a36b4760ebd507b90588d1303438ff39b60d04d6b62d29d2de
fetched_at: '2026-07-02T19:24:21.637900+00:00'
page_id: '268814302'
product: protheus
source: tdn-tec
title: Correção - Calendário do campo de data (TGet) no SmartClient em linguagem russa
  deve iniciar a semana na segunda-feira.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=268814302
version: 1
---

Correção - Calendário do campo de data (TGet) no SmartClient em linguagem russa deve iniciar a semana na segunda-feira.

|  |  |
| --- | --- |
| Situação | O calendário do TGet no SmartClient com linguagem russa estava iniciando a semana com o domingo, mas o padrão usado na Rússia é iniciar com a segunda-feira. |
| Ocorrência | Foi solicitado para que quando o SmartClient for executado com a linguagem russa o calendário do TGet seja ajustado para iniciar a linha da semana pela segunda-feira, e não pelo domingo. |
| Correção | O calendário foi ajustado para iniciar a semana com a segunda-feira quando a linguagem do SmartClient for indicada como russa. |
| Informações adicionais | * Referente ao chamado: SSIM-1283 * Referente à ocorrência: TWKOVH * Disponível a partir da build 7.00.131227A 2.3.0 |
