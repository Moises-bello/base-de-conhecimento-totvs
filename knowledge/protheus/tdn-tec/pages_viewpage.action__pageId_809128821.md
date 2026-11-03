---
content_hash: a6f4487606143ab41b2604dde4f991f11dad169ef94708c395c965711be261eb
fetched_at: '2026-07-02T19:24:28.703577+00:00'
page_id: '809128821'
product: protheus
source: tdn-tec
title: Correção - Imagens em formato JPEG não aparecem em impressões via SPOOL
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=809128821
version: 1
---

Correção feita para que imagens em formato JPEG apareçam corretamente nas impressões via SPOOL (direto no driver de impressão).

|  |  |
| --- | --- |
| Situação | Em situações específicas as imagens em formato JPEG não saem na impressão. |
| Ocorrência | Devido a um outro tratamento específico para imagens JPEG, ocorria uma falha ao carregar as informações da imagem. |
| Correção | Os dados da imagem são carregados corretamente. |
| Informações adicionais | * Referente ao chamado: #18398116 * Referente à ocorrência: DTCLIENT01-4387 * Disponível em builds superiores a 2.2.1 |
