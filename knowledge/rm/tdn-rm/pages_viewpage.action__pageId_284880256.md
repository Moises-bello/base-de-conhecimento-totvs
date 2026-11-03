---
content_hash: ac0302c7d4eb6933bfeb76bb31cb52fa024b7583eef2b6e2dd39b99a19a5519b
fetched_at: '2026-06-29T00:08:37.633353+00:00'
page_id: '284880256'
product: rm
source: tdn-rm
title: Customização Externa
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=284880256
version: 35
---

Foram desenvolvidos dois serviços REST para que o cliente possa customizar sua aplicação de acordo com o contexto educacional atual do portal do aluno. Abaixo detalharemos cada um desses serviços.

### **GetKeySession – Retorna a chave para obter o contexto**

O primeiro serviço chamado de *GetKeySession*, irá retornar uma chave criptografada do contexto atual do usuário no portal do aluno e deverá ser usada como parâmetro do segundo serviço (*GetSession*). O serviço *GetKeySession* utiliza o verbo de requisição GET e pode ser útil quando for necessário uma customização que não possa ser feita através de um cadastro de Url Externa de Globais e necessite das informações do contexto do usuário logado no portal.

O endereço para acessar o endpoint GetKeySession:

http://<nome\_do\_servidor\_ou\_ip>/rm/api/TOTVSEducacional/GetKeySession

O serviço GetKeySession necessita da sessão em que o usuário está logado, por isso, só funcionará se for executado dentro do ambiente do portal.

Exemplo de uma requisição do endpoint *GetKeySession* através do Swagger:

## **GetSession – Retorna o contexto atual do aluno**

O segundo serviço chamado de *GetSession*, irá retornar um objeto Json com os dados de contexto do aluno. Esse serviço utiliza o verbo de requisição GET e recebe como parâmetro uma chave criptografada de nome *key* obtida pelo primeiro serviço *GetKeySession*.

O endereço para acessar o endpoint GetSession:

http://<nome\_do\_servidor\_ou\_ip>/rm/api/TOTVSEducacional/GetSession?key=<chave\_criptografada>

Alias do contexto

O alias do banco de dados utilizado para consultar o contexto do aluno no serviço GetSession é o alias parametrizado no arquivo ...\FrameHTML\Web.Config, no parâmetro **ServiceAlias**.

É obrigatório passar uma chave criptografada para que este serviço retorne os dados. Essa chave é obtida por meio do serviço *GetKeySession*.

É obrigatório configurar a TAG *ServiceAlias* no arquivo Web.config da pasta FrameHTML para que este serviço funcione corretamente.

O serviço *GetSession* deve ser executado de fora do ambiente do portal.

 

Modelo do JSON que é retornado pelo GetSession (lembrando que um dado pode ou não estar preenchido baseado no usuário logado):

{  
"data":[  
{  
"CODCOLIGADA":1,  
"CODFILIAL":1,  
"NOMEFILIAL":"Filial Belo Horizonte",  
"CODTIPOCURSO":1,  
"NOMETIPOCURSO":"Ensino Superior",  
"RA":"ES-00177",  
"NOMEALUNO":"Thiago Enzo Sales",  
"CODUSUARIOPAI":null,  
"NOMEPAI":null,  
"CODUSUARIOMAE":null,  
"NOMEMAE":null,  
"CODUSUARIORACA":null,  
"NOMERACA":null,  
"CODUSUARIORESPFINANCEIRO":null,  
"NOMERESPFINANCEIRO":null,  
"CODUSUARIORESPCONTRATO":null,  
"NOMERESPCONTRATO":null,  
"IDHABILITACAOFILIAL":1,  
"CODCURSO":"1-1",  
"NOMECURSO":"DIREITO",  
"CODHABILITACAO":"1",  
"NOMEHABILITACAO":"DIREITO",  
"NOMEMATRIZ":"Grade Curricular de Direito",  
"NOMETURNO":"MANHÃ",  
"IDPERLET":22,  
"CODPERLET":"2019/1",  
"DTINICIO":"2019-01-01T00:00:00",  
"APRESENTACAO":"1",  
"CODTURMA":null,  
"PERIODO":null,  
"SITMATHABILITACAO":"Matriculado",  
"SITMATPERLET":"Pré-Matricula",  
"CODUSUARIOALUNO":"ES-00177",  
"GUID":"L\\FF\\09\\28B\\FDc\\DF\\A4\\21s\\14\\E75\\40\\E6p\\21\\E8\\D5i\\A8m\\C45\\02\\BDI\\2C\\A2\\5E\\C008\\AAn\\8B\\A9l\.."  
}  
],  
"messages":[

],  
"length":1,  
"HttpStatusCode":200  
}

# **Quando e como usar?**

##### Exemplo 1: Cliente precisa customizar a tela de ocorrência do portal adicionando um link para uma aplicação externa.

Para isso, utilizando a [documentação de customização](http://tdn.totvs.com/pages/viewpage.action?pageId=284880344), podemos alterar esta tela e adicionar um botão que irá redirecionar para a URL de uma aplicação externa. No código abaixo, no evento do click deste botão, o serviço GetKeySession é chamado para recuperar a KeySession e, posteriormente, essa key será repassada para o aplicativo externo via QueryString.

xmlMidnightClique para copiar o HTML adicionado no viewtrue
Abrir aplicativo externo
]]>jsMidnightClique para copiar o código adicionado no controllertruefalseIMPORTANTE!!!

Caso a instalação esteja na versão superior a versão 12.1.27, o caminho da instalação deve ser: url: "[http://**localhost/FrameHTML**/rm/api/TOTVSEducacional/GetKeySession](http://localhost:8025/rm/api/TOTVSEducacional/GetKeySession)",

jsMidnightClique para copiar o código adicionado no controllertrue

Funcionamento do código de exemplo acima:

##### Exemplo 2: Cliente precisa adicionar uma URL externa ao menu do portal do aluno que redireciona para uma aplicativo externo passando o contexto.

Para isto, basta o Cliente realizar o cadastro da URL externa informando a URL do aplicativo externo que receberá o contexto.

Funcionamento:

Para reproduzir os exemplos basta extrair os fontes em um diretório e criar um aplicativo web.

Isto pode ser feito no Gerenciador de Serviços de Informações da Internet (IIS), por exemplo.

No próprio aplicativo já estão descritas as instruções de uso.

A porta padrão utilizada pelo serviço GetSession é a porta 8080.

Aplicação de exemplo para acesso ao Contexto do portal do aluno (ASP.NET)

250

A partir da Versão 12.1.2205

GetKeySession - Retornar e-mail do Aluno

Implementado a funcionalidade para que ao utilizar a API "GetSession", para retornar os dados do Contexto do Aluno, foi incluído também a informação do e-mail do aluno ( caso essa informações esteja preenchida em seu cadastro).

> Aplicação de exemplo para acesso ao Contexto do portal do aluno (ASP.NET) ( com a inclusão do e-mail do Aluno)

250
