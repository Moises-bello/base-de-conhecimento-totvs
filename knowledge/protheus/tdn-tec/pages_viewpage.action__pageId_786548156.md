---
content_hash: bd1d5eb1aa15ae724a70f550fc775f7f1ae7fd25f139936571e7dfc55b7f33ed
fetched_at: '2026-07-02T19:24:28.501832+00:00'
page_id: '786548156'
product: protheus
source: tdn-tec
title: Objetos retornados por referência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=786548156
version: 4
---

Atenção:

Os objetos JSON retornados por métodos de oRest, como por exemplo oRest:getQueryRequest(), são referências ao objeto existente no REST e não uma cópia.

Existem alguns motivos para ser uma referência, são eles:

* Melhorar performance do serviço;
* Economia de memória;
* Evitar que seja necessário limpar o objeto na saída da implementação do serviço REST.

Portanto, é imprescindível que não se manipule diretamente o Objeto, pois isso irá refletir nas próximas requisições, causando problemas difíceis de serem detectados.

Métodos:

cpp
