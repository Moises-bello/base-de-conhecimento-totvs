---
content_hash: aa06273efe49f32c712a8f6f828c695519446e8b9a8c9aa75aa6324171e468c4
fetched_at: '2026-07-02T19:24:20.457755+00:00'
page_id: '249267804'
product: protheus
source: tdn-tec
title: 4GL - Não valida fechamento de chaves de comentario em bloco
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=249267804
version: 3
---

4GL - Não valida fechamento de chaves de comentario em bloco

|  |  |
| --- | --- |
| Situação | 4GL - Não valida fechamento de chaves de comentario em bloco |
| Ocorrência | Ao compilar um fonte que tenha abertura de 2 blocos de comentário e fechamento de apenas um, a compilação é realizada com sucesso, considerando todo o fonte como comentário |
| Correção | Exibir erro de compilação por não encontrar o fechamento do segundo bloco de comentário. |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: TEC-7296 * Disponível em builds superiores a 7.00.131227A - 1.0.3 |
