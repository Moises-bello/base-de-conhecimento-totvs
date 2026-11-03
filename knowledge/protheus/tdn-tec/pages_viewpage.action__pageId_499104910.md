---
content_hash: 2a07bd64dad4c1f887db2aaa7d4d1f46ab52106b5c48e16a0b3f5000461201ce
fetched_at: '2026-07-02T19:24:25.141193+00:00'
page_id: '499104910'
product: protheus
source: tdn-tec
title: Access Violation na edição consulta padrão
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=499104910
version: 1
---

|  |  |
| --- | --- |
| Ocorrência | Erro ocasionado devido a tentativa de concatenção de elemento de array inválido com texto. |
| Correção | Inserido proteção para que em casos de acesso a elemento de array inválido a execução seja interrompida após execução do bloco de códido . |
| Informações adicionais | * Referente ao chamado: MTEC-2644 * Disponível em builds iguais ou superiores a [13.1.3.44](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.1.3.44) e [13.2.3.44](http://tdn.totvs.com.br/display/tec/Application+Server+-+13.2.3.44). |
