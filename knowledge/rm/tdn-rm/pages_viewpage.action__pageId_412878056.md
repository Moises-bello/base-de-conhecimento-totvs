---
content_hash: a5dc4e3706dee8929eeb3111af0a79d728aa8df3cf1b55dd70405d3beddc0eed
fetched_at: '2026-06-29T00:09:11.590388+00:00'
page_id: '412878056'
product: rm
source: tdn-rm
title: Utilizando a atividade "Executar Requisição SOAP"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=412878056
version: 13
---

# Índice:

---

* Objetivo
* Especificação

# Objetivo:

---

Este documento tem por objetivo especificar a atividade “Executar Requisição SOAP” disponível na Fórmula Visual.

# Especificação:

---

A atividade “Executar Requisição SOAP” permite que a fórmula visual execute uma requisição utilizando o protocolo SOAP. Esta requisição é feita utilizando o método HTTP (POST) e permite que os dados retornados pela requisição sejam consumidos pela fórmula visual.  
É possível ainda definir o tipo de autenticação da requisição que pode ser básica (informando um usuário e senha) ou baseada em Tokens (informando o schema e token).

Vamos Configurar o Serviço.

**1)** Clique com o botão direito na atividade e selecione a opção **Configurar Web Service**.

**2)**Defina o descritor do Web Service (**WSDL**) que será utilizado e clique em **OK**.

Será apresentado o **XML** do descritor à sua esquerda, e será apresentado os métodos disponíveis à sua direita.

**3)**Escolha o método que será utilizado.

**4)** Após escolher o método à ser utilizado na Fórmula Visual, as propriedades Método, Wsdl e Endereço da Requisição já estarão preenchidas, você deverá preencher então o usuário e senha (caso houver necessidade) e o Pré Autenticar (também se houver necessidade)

## Parâmetros da Requisição

|  |  |
| --- | --- |
| **Nome** | **Descrição** |
| Cabeçalhos HTTP | Se a sua requisição exigir o envio de header, preencha esta propriedade da atividade - Disponível a partir da versão 12.1.24. Os parâmetros devem ser informados um por linha, como no exemplo abaixo. Após clicar em Ok, novas propriedades serão exibidas nos detalhes da atividade, no agrupamento "Cabeçalhos HTTP", para preenchimento dos valores dos campos do header. Exemplo: |
| Endereço da Requisição | Endereço do serviço que deseja executar a requisição.  Exemplo:  [http://10.31.0.155:8051/wsDataServer/IwsDataServer](http://www.totvs.com/IwsDataServer/ReadView) [http://10.31.0.155:8051/wsProcess/IwsProcess](http://www.totvs.com/IwsDataServer/ReadView)  Atenção Para alguns serviços, o WSDL **não atende** **os requisitos da requisição SOAP.**  Caso o WSDL **não atenda** os requisitos, a URL será inserida na propriedade **WSDL** no grupo "Definição da Requisição", automaticamente .  Caso a URL **atenda** os requisitos a mesma será inserida na propriedade **Endereço da Requisição**. |
| Método de Requisição | Método do serviço que será executado. |
| Tempo Limite | Informe um tempo limite para execução da requisição em segundos. Caso este tempo seja ultrapassado será gerado um erro de timeout. |
| Utilizar Proxy do Sistema | Selecione se a requisição deverá utilizar a configuração padrão de proxy do Windows. |
| *User-Agent* | É o *Client* no Header da requisição que será enviada. Se ficar vazio, o padrão é "RM/{versão do RM} ({versão do .NET})". |

## Definição da Requisição

|  |  |
| --- | --- |
| **Nome** | **Descrição** |
| Método | Método do serviço que será executado. |
| Requisição (XML) | XML que será enviado na Requisição.  Este texto poderá conter parâmetros para montagem do XML que deverão ser informados entre chaves { }.  Exemplo: xml     GlbUsuarioData  CODUSUARIO='{CodUsuario}'  CODCOLIGADA=1;CODSISTEMA=G ]]> O Parâmetro será criado como uma propriedade na atividade. |
| WSDL | Neste campo será inserido automaticamente a URL do WSDL caso a mesma **não atenda os requisitos da requisição SOAP.** |

## Segurança/Autenticação

|  |  |
| --- | --- |
| **Nome** | **Descrição** |
| Tipo de Autenticação | Selecione o tipo de autenticação da requisição, que pode ser:   * + None Não utiliza nenhum tipo de autenticação.   + Basic Faz a requisição utilizando autenticação básica através do Header Authorization (autenticação padrão utilizada pelo Host), um usuário e senha devem ser informados através das respectivas propriedades.   + UserName Faz a requisição utilizando autenticação padrão por usuário e senha, que devem ser informados nas propriedades Usuário e Senha. Para mais informações consulte: <https://pt.stackoverflow.com/questions/254503/o-que-%C3%A9-basic-auth>   + Token Faz a requisição utilizando autenticação via Token (através do Header Authorization), que devem ser informados nas propriedades Token e Token Schema. Para mais informações consulte:  <https://pt.wikipedia.org/wiki/OAuth> |
| Usuário | Informe o nome do usuário que será utilizado pela autenticação básica. |
| Senha | Informe a senha do usuário que será utilizado pela autenticação básica. |
| Token | Informe os dados do Token que será utilizado pela autenticação via Token. |
| Token Schema | Informe o Schema do Token que será utilizado pela autenticação via Token. São exemplos de schema BEARER, OASIS e outros. |

## Tipo de Conteúdo

|  |  |
| --- | --- |
| **Nome** | **Descrição do Parâmetro** |
| Codificação do Texto da Requisição | Informe o tipo de codificação utilizado para codificar/decodificar os textos da requisição. Por padrão será utilizado a formato UTF-8.  Para mais informações consulte:  <https://msdn.microsoft.com/pt-br/library/system.text.encoding(v=vs.110).aspx> |
| Tipo de Conteúdo Aceito | Informe o tipo de conteúdo MIME aceito como retorno da requisição. Por padrão será aceito qualquer tipo de conteúdo, porém alguns servidores Web exigem que o tipo de conteúdo aceito seja informado (Header HTTP Accept).  Para mais informações consulte:  <https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Accept> |
| Tipo de Conteúdo da Requisição | Informe o tipo de conteúdo MIME que será enviado nos dados da requisição (Header HTTP Content-Type). Por padrão o sistema irá utilizar o tipo “text/XML”.  Para mais informações consulte:  <https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Content-Type> |

## Resposta

As propriedades de resposta contêm os dados retornados pela execução da requisição.

|  |  |
| --- | --- |
| **Nome** | **Descrição do Parâmetro** |
| Resposta (Código) | Contém o código HTTP da resposta do servidor. |
| Resposta (Texto) | Contém o conteúdo da resposta da requisição no formato de texto, caso o tipo da resposta (Content-Type: “text”), em formato texto. |
| Tabelas | Provê acesso aos dados retornados pela requisição no formato de tabela/coluna. |
| Campos | Provê acesso aos dados da tabela principal retornada pela requisição. |

Informação

Ao utilizar essa atividade com HTTPS é necessário que o certificado ofereça uma conexão segura.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superior

false

**Processo:** Atividade "Executar Requisição SOAP" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
