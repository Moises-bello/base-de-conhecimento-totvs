---
content_hash: d759a4bd39b1e4ea83c239ebcfc65e3c683403208aa9d7ab19a3252fc2760ab6
fetched_at: '2026-07-02T19:24:24.984738+00:00'
page_id: '493639164'
product: protheus
source: tdn-tec
title: Correção do componente tMediaPlayer, para evitar queda do SmartClient.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=493639164
version: 1
---

Proteção no destrutor da classe TMediaPlayer, para deletar os ponteiros criados.

|  |  |
| --- | --- |
| Situação | SmartClient fecha ao fechar rotina com componente tMediaPlayer. |
| Ocorrência | Ao utilizar a classe TMediaPlayer, gera queda do Smartclient |
| <Tipo de alteração (correção, implementação, melhoria, homologação)> | Proteção no destrutor da classe TMediaPlayer, para deletar os ponteiros criados.<Descrição da alteração> |
| Informações adicionais | * Referente ao chamado: 5392711 * Referente à ocorrência: MTEC-2502 * Disponível em builds superiores a 13.2.3.41 |
