---
content_hash: e62dc110854be53fcfcfc5ea463f5723c78dbc297ff0a7cdd0271988868365b6
fetched_at: '2026-07-02T19:24:27.557424+00:00'
page_id: '656073818'
product: protheus
source: tdn-tec
title: d - Warning
type: documentation
url: https://tdn.totvs.com/display/tec/d+-+Warning
version: 3
---

Ao utilizar o **tlpp.probat.assertWarning()**, o motor registrará a mensagem de aviso solicitada porém não irá gerar resultado, nem positivo e nem negativo.

Exemplo:

c#

```
Os avisos serão registrados na tabela [PROBAT_TEST_WARNING].
```

No momento da exportação dos resultados, quando houver mensagens de avisos registradas, será gerado um arquivo XML apartado do arquivo dos resultados.

O nome do arquivo deverá manter o padrão:  
*{nome\_arquivo\_definido}\_warning.xml*

Seu conteúdo deverá ser parecido com:

xml



Desc: Gera mensagem de aviso, mas nao gera resultados nem positivo, nem negativo
]]>

```

```

> Veja o exemplo completo no GitHub.
