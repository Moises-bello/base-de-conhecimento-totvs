---
content_hash: a98b4b5daa0997e358869217a5198c467add37c6a04ffefc74804395f3acdf76
fetched_at: '2026-07-02T19:24:29.390321+00:00'
page_id: '866541750'
product: protheus
source: tdn-tec
title: Correção - Tela branca ao abrir páginas que usam o CEF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=866541750
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Situação | Ao abrir um programa que usa o CEF, de forma intermitente, a página não era carregada, ficando com a tela em branco |
| Ocorrência | Tela branca ao abrir um programa que usa o CEF. Reproduzido após chamar o Shift+F6 várias vezes |
| Correção | Bloqueado a operação de "Reload Browser" caso a página corrente seja a do "preindex" (pois esta é responsável  por abrir o WebSocket) |
| Informações adicionais | * Referente ao chamado: [#21160238](https://suporte.totvs.com/portal/p/10098/consulta-tickets?ticket=21160238) * Referente à ocorrência: DTCLIENT01-4987 * Disponível em builds superiores a 20.3.2.9 |
