---
content_hash: 73cde9e4f1bd64e03cacdc803af4e659f45f1ab954035cd9b70eace46f46e486
fetched_at: '2026-06-29T00:09:04.055335+00:00'
page_id: '382545298'
product: rm
source: tdn-rm
title: 2637172 EDUCACIONAL01-4671 DT Importação de arquivo MARC 21
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=382545298
version: 83
---

# IMPORTACAO DE ARQUIVO MARC 21

|  |  |
| --- | --- |
| **Linha de Produto:** | RM. |
| **Segmento:** | Educacional. |
| **Módulo:** | TOTVS Educacional |
| **Função:** | Importação de arquivo MARC 21 |
| **Situação/Requisito:** | Ao importar um arquivo com padrão MARC 21 o sistema está apresentando a mensagem: "String or binary data would be truncated" |
| **Solução/Implementação:** | Foi identificado que a informação do ISBN da publicação possuía um texto maior que o campo da base de dados.  Um script foi criado para o aumento do tamanha do campo na base de dados, de forma a receber o texto importado pelo arquivo MARC 21. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A. |

divs
