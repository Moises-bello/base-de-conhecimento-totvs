---
content_hash: 48afa3fd1a7155d49c5e2b95f399b7d271abeeb82b3ba4458c4d012140d11dd8
fetched_at: '2026-06-29T00:12:02.754770+00:00'
page_id: '904056730'
product: rm
source: tdn-rm
title: Recomendações de Segurança do Portal do Paciente
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=904056730
version: 6
---

## **CONTEÚDO**

1. **Visão Geral**
2. **Configurações Iniciais**
3. **Configurações no web.config**

PainelVisão Geral

## **01**.**VISÃO GERAL**

A partir da versão **12.1.2502**, o Portal do Paciente incorporará novas configurações de segurança e recomendará práticas adicionais. Este artigo visa apresentar recomendações para aprimorar a segurança, integridade e confidencialidade dos dados no Portal do Paciente, assegurando um ambiente operacional mais protegido.

Configurações Iniciais

## **02**. **CONFIGURAÇÕES INICIAIS**

* Utilizar um certificado SSL válido (Recomendado)

Para garantir que a comunicação com o portal seja segura, habilite o SSL para a sua aplicação no IIS. Isso é recomendado principalmente quando o portal é exposto em uma DMZ ou servidor com acesso via rede pública:

Para isso é necessário adquirir um certificado através de uma autoridade certificadora confiável e seguir as documentações. Para mais informações acesse:

<https://en.wikipedia.org/wiki/SSL>

<https://www.digicert.com/ssl-certificate-installation-microsoft-iis-7.htm>

<https://www.digicert.com/ssl-certificate-installation-microsoft-iis-8.htm>

* Configurar bloqueio de usuário ao inserir senha incorreta no login (Recomendado)

[CONFIGURAÇÃO DE BLOQUEIO POR ERRO AO LOGAR NO SISTEMA - Linha RM - TDN](https://tdn.totvs.com/pages/releaseview.action?pageId=243662499)

* Habilitar SSL/TLS no Host (Opcional)

A comunicação com o HOST já é feita com segurança e os dados não são trafegados em “plain text” por padrão. Porém para aumentar a segurança e fazer com que as informações trafeguem criptografadas e com ainda mais segurança, sugerimos que habilitem o SSL no HOST.  Ver: [Habilitar SSL/TLS no Host - Linha RM - TDN](https://tdn.totvs.com.br/pages/releaseview.action?pageId=244911449)

Configurações no web.config

## **03**. **CONFIGURAÇÕES NO Web.Config**

### Desabilitar o VERB TRACE

Para realizar as configurações abaixo será necessário acessar o arquivo web.config da pasta do portalpaciente em FrameHTML

O trecho de código abaixo deve ser incluído no nó <system.webServer>

Desabilitar o VERB TRACE





]]>

Ou a configuração pode ser feita pelo IIS:

### 

### Desabilitar o Debug: "[ASP.NET](https://asp.net/) DEBUG Method Enabled"

No***web.config***, no nó ***<system.web>***

Adicionar a tag debug false no compilation nó <system.web>]]>

Referência: [Disable debugging for ASP.NET application - ASP.NET | Microsoft Learn](https://learn.microsoft.com/en-us/troubleshoot/developer/webapps/aspnet/development/disable-debugging-application)

**Remover do cabeçalho de resposta HTTP dos seguintes itens**

* **Server**  
  Esse cabeçalho de resposta pode ser removido com uma configuração no arquivo **web.config**, no nó **<system.webServer>** adicione:

]]>

* **X-Powered-By**  
  Esse cabeçalho de resposta pode ser removido com uma configuração no arquivo **web.config**, no nó **<system.webServer>** adicione:

]]>

* **X-AspNet-Version**  
  Esse cabeçalho de resposta pode ser removido com uma configuração no arquivo **web.config**, no nó **<system.web>** adicione:

]]>

* ### Criptografar o *ViewState*

O *ViewState*, caso não esteja criptografado, pode abrir brechas para roubo de informações sensíveis.

Para criptografá-lo, no ***web.config***, no nó ***<system.web>***, adicionar a opção **viewStateEncryptionMode="Always"** ao final da *tag **pages***:

]]>

Referência: <https://learn.microsoft.com/en-us/dotnet/api/system.web.ui.page.viewstateencryptionmode?view=netframework-4.8>

### Configurando os Headers

| Atributo | Valores possíveis | Descrição | Referência |
| --- | --- | --- | --- |
| X-Content-Type-Options | nosniff | ``` Para evitar o sniffing do tipo MIME, você pode adicionar o cabeçalho X-Content-Type-Options.  Isso torna mais difícil para os hackers adivinharem o tipo certo de mime, inspecionando o conteúdo. ``` | <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Content-Type-Options> |
| X-Xss-Protection | ``` 0 1 0; mode=block 1; mode=block ``` | ``` O X-Xss-Protection é um recurso implementado no navegador mais moderno, que interrompe o carregamento da página quando um ataque de script entre sites é detectado. ``` | <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-XSS-Protection> |
| X-Frame-Options | ``` X-Frame-Options: DENY X-Frame-Options: SAMEORIGIN X-Frame-Options: ALLOW-FROM https://example.com/ ``` | ``` O cabeçalho X-Frame-Options garante que os hackers não cX-Content-Type-Optionsriem iframe para o seu site, a fim de induzi-lo a clicar em links que você nunca quis. ``` | <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options> |
| Content Security Policy (CSP) | default-src  script-src  style-src (Obrigatório incluir 'unsafe-inline')  img-src  object-src  base-uri  connect-src (incluir a api do host, a mesma configurada no config.json)  font-src  frame-src  img-src | A diretiva Content-Security-Policy (CSP) é um cabeçalho de segurança importante que ajuda a mitigar os riscos de ataques como XSS (Cross-Site Scripting) e outros tipos de ataques baseados em injeção de código. Ela permite que os desenvolvedores controlem quais recursos são carregados em uma página web e de onde eles podem ser carregados. | <https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP> |

Sugestão de configuração:

]]>

Onde tiver o {HOST\_API\_URL} ou {<http://localhost:8051>}, substituir pelo endereço da api do host, o mesmo apontado no arquivo config.json

ATENÇÃO!

Todas as informações sugeridas acima foram checadas e testadas em um ambiente controlado com o apoio do nosso time de segurança e com resultados de Pentests executados internamente ou externamente pelos nossos clientes. No entanto, é recomendado que as configurações sejam realizadas inicialmente em um ambiente de homologação, devido à variedade e complexidade das configurações e especificidades dos servidores de cada cliente.
