---
content_hash: f31c9bdf43d1f0478b308fd54a87de2ee24c3854bc504f105bb6eddf2f27385e
fetched_at: '2026-07-02T19:24:27.029624+00:00'
page_id: '655644893'
product: protheus
source: tdn-tec
title: d - Identificador Customizado
type: documentation
url: https://tdn.totvs.com/display/tec/d+-+Identificador+Customizado
version: 5
---

O **PROBAT** permite que na execução dos testes um identificador customizado possa ser enviado através da função RUN, assim esse identificar ficará gravado na tabela [PROBAT\_TEST\_EXECUTION] e no campo [CUSTOM].

O campo [CUSTOM] é do tipo "character" e de tamanho 255 posições.

Esse recurso é interessante pois ele flexibiliza a forma de identificar diferentes execuções dos testes.

Por exemplo, em um cenário onde existem múltiplas execuções de testes, tais como: unitários, integrados e funcionais, todos são executados em momentos distintos e portanto terão códigos de execução diferentes, esse recurso possibilita agrupá-los pois todos eles irão possuir o mesmo Identificador Customizado, dessa forma os resultados serão agrupados em uma única exportação.

Para enviar um identificador customizado, execute a função RUN da seguinte forma:

```
tlpp.probat.run('custom:123456789')  
​// ou  
​tlpp.probat.run('param:123456789')  
​  
// Ambas as opções farão o PROBAT gravar 123456789 no campo CUSTOM
```

> Saiba mais em:
