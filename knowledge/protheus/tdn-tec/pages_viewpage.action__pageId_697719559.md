---
content_hash: 130821ab4da30c36eda236337e75ec60b96ad79bdcf12eb6983170945038dd85
fetched_at: '2026-07-02T19:24:27.948543+00:00'
page_id: '697719559'
product: protheus
source: tdn-tec
title: Correção - TMenu popup aparece na tela que a aplicação não está sendo apresentada
  - 19
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=697719559
version: 1
---

Foi corrigido o posicionamento do TMenu popup que aparecia na tela principal se a aplicação estivesse sendo exibida em outra tela.

|  |  |
| --- | --- |
| Situação | O TMenu popup aparece na tela errada. |
| Ocorrência | Se a aplicação estiver sendo exibida em uma tela que não seja a primária, qualquer TMenu popup aparece na posição errada na tela primária. |
| Correção | O posicionamento foi corrigido para que o TMenu popup apareça na posição devida na tela que a aplicação está sendo exibida. |
| Informações adicionais | * Referente ao chamado: #14605491 * Referente à ocorrência: DTCLIENT01-3478 DTCLIENT01-3432 * Disponível em builds superiores a 19.3.1.9 |
