---
content_hash: ace48c49f51270a51b510bbf33045165c7b5996c0bd01c6072b7c1e57c68ac14
fetched_at: '2026-07-02T19:24:19.705117+00:00'
page_id: '243657157'
product: protheus
source: tdn-tec
title: Problema na função CpyS2TW
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=243657157
version: 1
---

<Resumo do que foi contemplado na alteração associada a essa nota de release> 

|  |  |
| --- | --- |
| Ocorrência | Ao utilizar a função CpyS2TW para copiar um arquivo do servidor para o client estava ocorrendo o erro "500 (Internal Server Error)" no console do browser.  Com isso, o download do arquivo não é realizado. |
| Correção | Ajuste no JSON enviado para realizar o download do arquivo |
| Informações adicionais | * Referente ao chamado: não há chamado associado * Referente à ocorrência: BAS-1031 * Disponível a partir da build 7.00.131227A - 2.3.4 |
