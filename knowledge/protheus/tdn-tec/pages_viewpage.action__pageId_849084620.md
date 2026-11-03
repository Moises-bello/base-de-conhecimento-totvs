---
content_hash: 2c680c8e7042c4f5723177be95a91fb417c545f8be665ca781d432c11493d2b3
fetched_at: '2026-07-02T19:24:28.739178+00:00'
page_id: '849084620'
product: protheus
source: tdn-tec
title: Seção [general], chave buildKillUsers
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=849084620
version: 2
---

buildKillUsers

## Valores válidos

| Valores válidos |  | Descrição |
| --- | --- | --- |
| 0 | Padrão | Não inicia a compilação enquanto existirem conexões abertas com a instância atual do true |
| 1 |  | Derruba todas as conexões abertas com a instância atual do true para permitir a compilação. |

Atenção

Caso existam outros processos em execução no TOTVS Application Server onde o IDE / TDS está conectado, todos serão derrubados, inclusive aqueles que não pertencem ao ambiente que você está compilando. Este recurso foi desenvolvido para facilitar a compilação em ambientes onde são utilizadas "Working Threads", como WEB Services Server em AdvPL, onde para cada nova compilação era necessário finalizar e iniciar novamente o TOTVS Application Server.

## Exemplos
