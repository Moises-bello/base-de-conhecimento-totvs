---
content_hash: 5230a4e99ab8ea41eac8afdafa52a37327b012ec6f34a99510208e7a99f7c88f
fetched_at: '2026-07-02T19:24:27.069991+00:00'
page_id: '656073816'
product: protheus
source: tdn-tec
title: c - tlpp.probat.export()
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=656073816
version: 3
---

É possível solicitar a exportação sempre que desejar, e para isso é preciso fazer uso da Main Function:

c#

Como parâmetro, devemos informar o tipo de códigos para busca das execuções e claro, a lista de códigos desejados:

Os tipos disponíveis para uso são:

| Tipo | Como informar | Descrição |
| --- | --- | --- |
| code | "type:code" | Código de execução dos testes (\*1) |
| custom | "type:custom" | Identificador customizado enviado para a execução (\*2) |

> (\*1) - Para obter um código de execução, utilize o retorno das funções RUN do **PROBAT**.
>
> (\*2) - Veja informações detalhadas em: (Identificador Customizado)

Exemplos:

c#

```

```

> Pode-se enviar mais de um código para unificar os resultados no momento da exportação.
