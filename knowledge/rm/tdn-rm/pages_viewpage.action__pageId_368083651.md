---
content_hash: 2eddb5b478e1386e2986edc53171d0437344c6da478556405252702121581167
fetched_at: '2026-06-29T00:09:00.415602+00:00'
page_id: '368083651'
product: rm
source: tdn-rm
title: Utilizando a atividade "Executar Requisição REST"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=368083651
version: 14
---

## **Índice**

1. Visão Geral
2. Especificação
3. Exemplo de utilização

**01. VISÃO GERAL**

Este documento tem por objetivo especificar a atividade “Executar Requisição REST” disponível na Fórmula Visual.

 A atividade “Executar Requisição REST” permite que a fórmula visual execute uma requisição utilizando o protocolo HTTP(S) e o padrão REST com formato JSON. Esta requisição de ser feita utilizando qualquer método HTTP (GET, POST, ETC) e permite que os dados retornados pela requisição sejam consumidos pela fórmula.  
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
| *User-Agent* | É o *Client* no Header da requisição que será enviada. Se ficar vazio, o padrão é "RM/{versão do RM} ({versão do .NET})". |

## Definição da Requisição

|  |  |
| --- | --- |
| **Nome** | **Descrição** |
| JSON (Requisição) | Informe um texto no formato JSON que será utilizado para fazer a requisição ao servidor. Este texto poderá conter parâmetros para montagem do JSON que deverão ser informados entre <>.    Propriedades dinâmicas geradas: |
| JSON (Resposta) | Informe um texto no formato JSON, contendo um exemplo de JSON que é retornado pelo servidor, que será utilizado para gerar a estrutura de tabelas e campos do retorno da requisição.  O Json informado neste campo pode ser utilizado como um schema.  Como exemplo:  Para valores do tipo moeda e com casas decimais, caso neste schema ela seja informado como um valor inteiro (5), a resposta vai converter para inteiro e arredondar o valor. Caso neste schema seja informado um valor do tipo moeda/decimal, com casa decimal (5.20), a resposta será convertida para um valor decimal.  Dessa forma a resposta vai seguir o que for informado no schema. |

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
| Tipo de Conteúdo da Requisição | Informe o tipo de conteúdo MIME que será enviado nos dados da requisição (Header HTTP Content-Type). Por padrão o sistema irá utilizar o tipo “application/json”.  Para mais informações consulte:  <https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers/Content-Type> |

## Resposta

As propriedades de resposta contêm os dados retornados pela execução da requisição.

|  |  |
| --- | --- |
| **Nome** | **Descrição do Parâmetro** |
| Resposta (Código) | Contém o código HTTP da resposta do servidor. |
| Resposta (Texto) | Contém o conteúdo da resposta da requisição no formato de texto, caso o tipo da resposta (Content-Type: “text”), em formato texto. |
| Dados da Leitura | Contém uma fonte de dados com os dados do retorno da requisição, caso a tipo da resposta (Content-Type: “application/json”), em formato de tabelas/colunas. A propriedade JSON (Retorno) será utilizada para geração da estrutura da fonte de dados.  Dica: Utilize a atividade de Transformar Registro em XML e gere um erro com a estrutura de tabelas da requisição).     Importante Advertimos que a transformação automática do resultado de uma requisição Json em XML pode não ser completamente satisfatória, tendo em vista alguns conceitos de tipos complexos e schemas do xml. Ou seja, provavelmente, jsons simples terão pouca intervenção e jsons complexos terão muita intervenção, podendo com isso não serem convertidos através da atividade Transformar Registro em XML. |
| Tabelas | Provê acesso aos dados retornados pela requisição no formato de tabela/coluna. |
| Campos | Provê acesso aos dados da tabela principal retornada pela requisição. |
| Coleção de cookies da resposta da requisição | Caso a requisição possua algum cookie no response, o mesmo será armazenado nesta propriedade. |

Informação

Ao utilizar essa atividade com HTTPS é necessário que o certificado ofereça uma conexão segura. 

**02. EXEMPLO DE UTILIZAÇÃO**

      Uma requisição REST em resumo é uma chamada web, na qual enviamos ou consultamos os dados de um sistema. 

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

javaO que será enviado

**Obs.:** Exemplo de resposta em texto puro.

javaA resposta a ser exibida

* **Configuração da Requisição:**

Similar ao primeiro exemplo, configuramos o endereço e o tempo limite. A grande diferença nesse exemplo é que utilizamos o verbo GET para apenas pegar a mensagem, não necessitando enviar dados ao servidor.

Como mostrado no primeiro exemplo, fizemos o vinculo do campo ResponseText ao texto do e-mail, então esse é o conteúdo/texto do e-mail que será enviado.

Apesar do vinculo ser feito com o campo do texto, o vinculo poderia ter um ou mais campos.

* **Configurando Iteração nos Códigos da Resposta:**

  Inicialmente para podermos utilizar no foreach, vamos voltar na atividade da requisição REST e colocar uma resposta de exemplo no campo JSON de resposta, como mostra imagem abaixo:

           Feito isso, podemos criar nosso foreach e fazer o vinculo de items ao campo códigos da nossa resposta. Isso é feito utilizando um Dataset que será gerado pela atividade REST que é representação em dados da resposta.

           Então da atividade de REST selecionamos o campo Tables[“códigos”] e em seguida escolhemos a propriedade Rows. Assim estaremos interagindo entre cada um dos códigos do JSON.

             Para ilustrarmos, está sendo colocada uma atividade de LOG, para registrar cada um dos valores dos códigos.

             Após configurado, vamos limpar o valor de exemplo do campo de resposta JSON da atividade REST e executar. nas imagens abaixo está sendo mostrado o resultado de como ficou o log e também uma exemplificação gráfica do resultado final da formula.

falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20 ou Superior

false

**Processo:** Atividade "Executar Requisição REST" da Fórmula Visual

falsefalse

**Status:** **Finalizado**

false

**Data:**

false

**Autores:**

false
