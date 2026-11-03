---
content_hash: 90e892411404d6e3b545bbe8f3e87bf7c40cf596f88c2d878e567787db7de0de
fetched_at: '2026-06-29T00:06:20.920355+00:00'
page_id: '223159321'
product: rm
source: tdn-rm
title: Querystring Muito Longa
type: documentation
url: https://tdn.totvs.com/display/LRM/Querystring+Muito+Longa
version: 118
---

# QUERYSTRING MUITO LONGA

|  |  |
| --- | --- |
| **Produto:** | TOTVS Portal - Configurações Globais - Web.Config |
| **Versões:** | 11.82.x, 12.1.x |
| **Ocorrência:** | Exceção é levantada, quando a quantidade de caracteres passada, através da barra de endereço do navegador, é muito grande. |
| **Ambiente:** | TOTVS Portal - Configurações Globais - Web.Config |
| **Passo a passo:** | Ao utilizar processos, onde a quantidade de caracteres passado através da barra de endereço do navegador **(querystring)**, **ultrapasse** o limite imposto pela configuração padrão do site web **(web.config),** uma exceção é levantada: "**The length of the query string for this request exceeds the configured maxQueryStringLength value.**".  Para que a quantidade padrão de caracteres aceitos na barra de endereço do browser seja aumentado, deve-se:  1) Adicionar as tags **system.webServer** (caso não exista), **security** (caso não exista), **requestFiltering** (caso não exista), **requestLimits** (caso não exista) e adicionar o atributo  **maxQueryString**.  **Exemplo:**  <system.webServer>  <security>  <requestFiltering>  <requestLimits maxQueryString="2048" />  </requestFiltering>  </security> <system.webServer/>   | Nome Atributo | Valor Padrão | Valor Mínimo | Valor Máximo | Valor Recomendado | | --- | --- | --- | --- | --- | | maxQueryString | 2048 | 0 | ``` 2097151 ``` | ``` 2097151 ``` |     2) Adicionar a tag **httpRuntime** (caso não exista), e então adicionaro atributo **maxQueryStringLength**.  **Exemplo:**  <httpRuntime requestValidationMode="2.0" maxRequestLength="100000" maxQueryStringLength="2048"/>   | Nome Atributo | Valor Padrão | Valor Mínimo | Valor Máximo | Valor Recomendado | | --- | --- | --- | --- | --- | | maxQueryStringLength | 2048 | 0 | 2097151 | 2097151 | |
| **Observações:** |  |

divs
