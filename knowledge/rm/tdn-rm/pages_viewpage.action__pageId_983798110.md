---
content_hash: cb5a3345028178a8ca1693cd32895c26bf9e18d4b0bdbaa69a2cd51fdfcbc659
fetched_at: '2026-06-29T00:12:16.266756+00:00'
page_id: '983798110'
product: rm
source: tdn-rm
title: Nível de segurança nos Portais Educacionais
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=983798110
version: 81
---

Recurso disponível **a partir da release 12.1.2510**

## **1.****VISÃO GERAL**

Com o objetivo de **aumentar o nível de segurança** dos ambientes expostos na internet para todos os portais educacionais sem instabilizar os recursos presentes atualmente nos mesmos, criaremos o arquivo **configuração web** (conforme imagem abaixo) para atender todos portais educacionais de forma geral.

A instituição poderá realizar a configuração dos headers da forma que desejar. **Para saber mais acesse** [Aumentar a segurança de sua aplicação](https://tdn.totvs.com.br/pages/viewpage.action?pageId=284462425)

 

## **2.****CONFIGURAÇÕES**

 O arquivo **configuração web** será criado na pasta **"FrameHTML\Web\App\Edu**" conterá, nesse primeiro momento, as regras mínimas com valores do atributo **Content Security Policy (CSP)** para não gerar instabilidade nos recursos presentes nos portais educacionais.

Esse arquivo será criado **a partir da release 12.1.2510.**

Desta forma, caso o arquivo não exista na pasta "**FrameHTML\Web\App\Edu**", o instalador irá criar o arquivo. Caso contrário, o mesmo não será criado novamente, ou seja, será ajustado nesse primeiro momento.

Nesse arquivo terá as regras padrões do atributo **Content Security Policy (CSP).**

| Atributo | Descrição | Referência |
| --- | --- | --- |
| Content Security Policy (CSP | A diretiva Content-Security-Policy (CSP) é um cabeçalho de segurança importante que ajuda a mitigar os riscos de ataques como XSS (Cross-Site Scripting) e outros tipos de ataques baseados em injeção de código. Ela permite que os desenvolvedores controlem quais recursos são carregados em uma página web e de onde eles podem ser carregados. | [Content Security Policy (CSP) - HTTP | MDN](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP) |

Regra padrão




]]>

Se o cliente tiver alguma regra presente no atributo "**Content Security Policy (CSP)**" do arquivo **configuração web** de um determinado portal do TOTVS Educacional, será necessário ajustar este arquivo para que tais regras personalizadas não sejam afetadas.

Uma sugestão é a inclusão da tag "**<remove name="Content-Security-Policy" />**", antes da linha do atributo "**Content Security Policy (CSP)**" **para manter as regras personalizadas da instituição, customizações do cliente e url parametrizadas no sistema**.

## **3.****CONFIGURAÇÕES DO CONFIG.JSON DO PORTAL**

Recomenda-se configurar o arquivo **config.json** dos portais web com o parâmetro **apiServer** vazio, conforme orientado na documentação  (item 3).

Essa configuração evita a exposição desnecessária da URL da API no frontend, permitindo que o endereço seja resolvido de acordo com as definições do ambiente em que a aplicação está sendo executada.
