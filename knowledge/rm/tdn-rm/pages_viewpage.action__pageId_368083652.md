---
content_hash: 00dc683efa1cb852881725cca77fc518dac81af4fb98f4a6899961fc856744a5
fetched_at: '2026-06-29T00:09:00.433266+00:00'
page_id: '368083652'
product: rm
source: tdn-rm
title: Utilizando a atividade "Executar Requisição HTTP"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=368083652
version: 22
---

## **Índice**

1. Visão Geral
2. Exemplo de utilização

**01. VISÃO GERAL**

Este documento tem por objetivo especificar a atividade “Executar Requisição HTTP” disponível na Fórmula Visual.

A atividade “Executar Requisição HTTP” permite que a fórmula visual execute uma requisição utilizando o protocolo HTTP(S). Esta requisição de ser feita utilizando qualquer método HTTP (GET, POST, ETC) e permite que os dados retornados pela requisição (em formato binário ou texto) sejam consumidos pela fórmula.  
É possível ainda definir o tipo de autenticação da requisição que pode ser básica (informando um usuário e senha) ou baseada em Tokens (informando o schema e token).

## Parâmetros da Requisição

|  |  |
| --- | --- |
| **Nome** | **Descrição** |
| Cabeçalhos HTTP | Se a sua requisição exigir o envio de header, preencha esta propriedade da atividade - Disponível a partir da versão 12.1.24.  Os parâmetros devem ser informados um por linha, como no exemplo abaixo. Após clicar em Ok, novas propriedades serão exibidas nos detalhes da atividade, no agrupamento "Cabeçalhos HTTP", para preenchimento dos valores dos campos do header. Exemplo: |
| Endereço da Requisição | Informe o endereço do servidor para executar a requisição. O endereço deve ser informado completo inclusive com o protocolo que pode ser HTTP ou HTTPS. É possível criar parâmetros para montagem do endereço, informando os valores entre <>.  Exemplo:  [https://www.google.com/search?q=<texto](https://www.google.com/search?q=%3ctexto)>  Neste caso será criada uma propriedade dinâmica para que seja informado o conteúdo do parâmetro <texto>. |
| Método de Requisição | Selecione o método HTTP que será utilizado para fazer a requisição, os métodos disponíveis são Get, Head, Post, Put, Delete e Patch. |
| Tempo Limite | Informe um tempo limite para execução da requisição em segundos. Caso este tempo seja ultrapassado será gerado um erro de timeout. |
| Utilizar Proxy do Sistema | Selecione se a requisição deverá utilizar a configuração padrão de proxy do Windows. |
| Coleção de cookies do cabeçalho da requisição | Adiciona os cookies informados no cabeçalho da requisição. |
| User-Agent | É o *Client* no Header da requisição que será enviada. Se ficar vazio, o padrão é "RM/{versão do RM} ({versão do .NET})". |

## Conteúdo da Requisição

Informe somente uma das propriedades caso deseje enviar algum conteúdo pela requisição, que pode ser binário, post, texto ou arquivo disponibilizado pela atividade [Executar Relatório](https://tdn.totvs.com/pages/viewpage.action?pageId=463814973). Nesse último caso deverá ser informado Nome chave do arquivo de formulário e Nome do arquivo de formulário.

|  |  |
| --- | --- |
| **Nome** | **Descrição** |
| Dados (Binário) | Informe o conteúdo da requisição em formato binário. Adicionalmente o tipo de conteúdo poderá ser definido através da propriedade “Tipo de Conteúdo da Requisição”. |
| Dados (Post) | Informe os nomes dos parâmetros do Post, normalmente esta opção será utilizada quando o método de requisição for Post. Você deve informar um parâmetro por linha e para cada parâmetro informado será criada uma propriedade dinâmica para que o valor seja informado. |
| Dados (Texto) | Informe o conteúdo da requisição em formato texto. Adicionalmente o tipo de conteúdo poderá ser definido através da propriedade “Tipo de Conteúdo da Requisição”. |
| Nome chave do arquivo de formulário | Informe a chave a ser utilizada no arquivo enviado. Seu valor padrão é file.  Obs: A propriedade *Tipo de Conteúdo da Requisição* deve ser *multipart/form-data*. |
| Nome do arquivo de formulário | Informe o nome do arquivo de formulário (com extensão - Exemplo: nomeDoArquivo.pdf)  Obs: A propriedade *Tipo de Conteúdo da Requisição* deve ser *multipart/form-data*. |

## Segurança/Autenticação

|  |  |
| --- | --- |
| **Nome** | **Descrição** |
| Tipo de Autenticação | Selecione o tipo de autenticação da requisição, que pode ser:   * None Não utiliza nenhum tipo de autenticação. * Basic Faz a requisição utilizando autenticação básica através do Header Authorization (autenticação padrão utilizada pelo Host), um usuário e senha devem ser informados através das respectivas propriedades. * UserName Faz a requisição utilizando autenticação padrão por usuário e senha, que devem ser informados nas propriedades Usuário e Senha. Para mais informações consulte: <https://pt.stackoverflow.com/questions/254503/o-que-%C3%A9-basic-auth> * Token Faz a requisição utilizando autenticação via Token (através do Header Authorization), que devem ser informados nas propriedades Token e Token Schema. Para mais informações consulte:  <https://pt.wikipedia.org/wiki/OAuth> |
| Usuário | Informe o nome do usuário que será utilizado pela autenticação básica. |
| Senha | Informe a senha do usuário que será utilizado pela autenticação básica. |
| Token | Informe os dados do Token que será utilizado pela autenticação via Token. |
| Token Schema | Informe o Schema do Token que será utilizado pela autenticação via Token. São exemplos de schema BEARER, OASIS e outros. |

## Tipo de Conteúdo

|  |  |
| --- | --- |
| Nome | Descrição |
| Codificação do Texto da Requisição | Informe o tipo de codificação utilizado para codificar/decodificar os textos da requisição. Por padrão será utilizado a formato UTF-8.  Para mais informações consulte:  <https://msdn.microsoft.com/pt-br/library/system.text.encoding(v=vs.110).aspx> |
| Tipo de Conteúdo Aceito | Informe o tipo de conteúdo MIME aceito como retorno da requisição. Por padrão será aceito qualquer tipo de conteúdo, porém alguns servidores Web exigem que o tipo de conteúdo aceito seja informado através do Header HTTP Accept.  Para mais informações consulte:  <https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Accept> |
| Tipo de Conteúdo da Requisição | Informe o tipo de conteúdo MIME que será enviado nos dados da requisição. Por padrão o sistema irá utilizar o tipo “application/x-www-form-urlencoded”.  Para mais informações consulte:  <https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Content-Type> |

## Resposta

As propriedades de resposta contêm os dados retornados pela execução da requisição.

|  |  |  |
| --- | --- | --- |
| Nome do Parâmetro | Descrição do Parâmetro | Obrigatório |
| Resposta (Binário) | Contém o conteúdo da resposta da requisição no formato binário. | n/a |
| Resposta (Código) | Contém o código HTTP da resposta do servidor. | n/a |
| Resposta (Texto) | Contém o conteúdo da resposta da requisição no formato de texto, caso o tipo da resposta (Content-Type: “text”), em formato texto. | n/a |
| Coleção de cookies da resposta da requisição | Caso a requisição possua algum cookie no response, o mesmo será armazenado nesta propriedade. | n/a |

Informação

Ao utilizar essa atividade com HTTPS é necessário que o certificado ofereça uma conexão segura. 

Não é possível utilizar a atividade "Requisição HTTP", para percorrer os registros retornados, dentro da atividade "Para cada Interação". Para realizar essa ação é necessário utilizar a atividade "[Executar Requisição REST](https://tdn.totvs.com/x/w4LwFQ)"

**02. EXEMPLO DE UTILIZAÇÃO**

      Uma requisição HTTP em resumo é uma chamada web, na qual enviamos ou consultamos os dados de um sistema. Mais informações sobre [HTTP](https://rockcontent.com/blog/http/). 

* **EXEMPLO 1:**

      Abaixo vamos ver uma simulação onde mandamos uma mensagem em JSON para o endereço: <http://www.mocky.io/v2/5ea9d5b52d00007b0026838a> e ele irá nos retornar uma mensagem, com isso utilizaremos uma exceção para exibir qual foi o resultado.

javaO que será enviadojavaA resposta a ser exibida

* **Configuração da Requisição:**

Como mostrado na imagem acima, definimos:

* **Conteúdo da requisição > Dados (texto):** Conteúdo que desejamos enviar, esse campo pode ser feito relacionamento com outra propriedade de outra atividade para casos mais complexos. Dentro de conteúdo notamos outros dois campos, o preenchimento de cada um deles vai da necessidade, sendo: Binário para envio de arquivos, Post para envio de formulário e o texto para formatos livres como textos em XML ou JSON;
* **Requisição > Endereço da requisição**:  Endereço completo de onde vamos mandar a requisição (incluindo o protocolo http/https);
* **Requisição > Método da requisição**:  Tratamento do verbo HTTP utilizado, o preenchimento vai de cada necessidade, mas em resumo, "POST" são para enviar dados e "GET" são para pegar dados;
* **Requisição > Tempo Limite:** É um simples limite em segundos de quanto tempo estamos dispostos a aguardar o servidor responder nossa requisição;
* **Tipo de Conteúdo > Tipo de conteúdo da requisição:** Esse campo é para informarmos na requisição qual o tipo de conteúdo do nosso texto enviado (Conteúdo da requisição > Dados texto), em nosso caso tratou-se de um JSON;

Com isso temos o preenchimento dos campos base da requisição, como mencionado, o valor de preenchimento varia para cada serviço/sistema e o correto preenchimento deve ser alinhado junto ao mesmo.

* **Utilização da resposta da chamada HTTP**

 Para pegar a resposta da chamada HTTP podemos fazer o relacionamento com o campo ResponseText que é a resposta literal feita para a requisição, nesse caso, temos um json.

Para esse exemplo utilizamos a atividade de "Exceção" para exibir qual foi a resposta do servidor, com isso, a resposta pode ser repassada para outras atividades, para fazer transformações como uma atividade de codificação que faria a transformação do JSON em um DataSet, exemplo abaixo:

* **EXEMPLO 2:**

      Abaixo vamos utilizar uma requisição HTTP para enviar uma mensagem em texto que será encaminhada para uma atividade de "Envio de e-mail". O endereço que irá nos retornar a mensagem é o: <http://www.mocky.io/v2/5ea9e4dd2d000047002683db>

javaO que será enviadojavaA resposta a ser exibida

* **Configuração da Requisição:**

Similar ao primeiro exemplo, configuramos o endereço e o tempo limite. A grande diferença nesse exemplo é que utilizamos o verbo GET para apenas pegar a mensagem, não necessitando enviar dados ao servidor.

Como mostrado no primeiro exemplo, fizemos o vinculo do campo ResponseText ao texto do e-mail, então esse é o conteúdo/texto do e-mail que será enviado.

Apesar do vinculo ser feito com o campo do texto, o vinculo poderia ter um ou mais campos.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superior

false

**Processo:** Atividade "Executar Requisição HTTP" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
