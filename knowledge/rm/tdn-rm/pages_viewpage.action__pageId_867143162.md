---
content_hash: 29fb70061309bdb363f5856293036f783a764b5cdd75cd246083781327df1050
fetched_at: '2026-06-29T00:11:56.532874+00:00'
page_id: '867143162'
product: rm
source: tdn-rm
title: Aumentar o nível de segurança do portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=867143162
version: 2
---

O portal do aluno, permite que a instituição realize a configuração do headers da forma que desejar. **Para saber mais acesse**

## **01.** **VISÃO GERAL**

O objetivo desta documentação é auxiliar os nossos clientes na parametrização para **aumentar o nível de segurança** do portal do aluno. Através de Pentest realizado internamente, chegamos em uma orientação que deve ser seguida para aumentar o nível de segurança do ambiente exposto na internet.

## **02.** **CONFIGURAÇÕES**

Configurações do headers do portal do aluno

Para realizar as **configurações do headers** abaixo será necessário acessar o arquivo **web.config** da pasta **FrameHTML\Web\App\Edu\PortalDoProfessor**

As configuração mencionadas abaixo são apenas uma **sugestão de parametrização**, pois dependerá da configuração do ambiente de cada cliente.

Todas as informações sugeridas foram checadas e testadas em um ambiente controlado com o apoio do nosso time de segurança e com resultados de Pentests executados internamente. No entanto, **é recomendado que as configurações sejam realizadas inicialmente em um ambiente de homologação**, devido à variedade e complexidade das configurações e especificidades dos servidores de cada cliente.

| Atributo | Valores possíveis | Descrição | Referência |
| --- | --- | --- | --- |
| Content Security Policy (CSP) | default-src  script-src  style-src  img-src  font-src  frame-src  frame-ancestors | A diretiva Content-Security-Policy (CSP) é um cabeçalho de segurança importante que ajuda a mitigar os riscos de ataques como XSS (Cross-Site Scripting) e outros tipos de ataques baseados em injeção de código. Ela permite que os desenvolvedores controlem quais recursos são carregados em uma página web e de onde eles podem ser carregados. | [Content Security Policy (CSP) - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) |

Sugestão de configuração


  
]]>

Esse atributo está disponível a partir da release: 12.1.2410.

A tag "**<remove name="Content-Security-Policy" />**", deve ser **mantida** mesmo que a instituição queira **customizar** o atributo **"Content Security Policy (CSP)"**.

Atributos obrigatórios

Os atributos abaixo **são obrigatórios devido a exigência do funcionamento da aplicação** nas diretivas relacionadas

* **'unsafe-inline':** script-src e style-src
* **'unsafe-eval':** script-src

Todas as **customizações do cliente**, exemplo imagens, fontes, url, entre outros, **devem ser incluídas no atributo** "Content Security Policy (CSP)", pois são necessáriopara o funcionamento da aplicação.

O elemento **HttpProtocol**deve ser incluído no nó **<system.webServer>**
