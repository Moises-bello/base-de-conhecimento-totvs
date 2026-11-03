---
content_hash: 54bf1db5a4b8c23da5470e6a49b7c0f33c05029216034a2540951f7fa68e1bc6
fetched_at: '2026-06-29T00:05:55.364676+00:00'
page_id: '142802978'
product: rm
source: tdn-rm
title: Cadastro de URL’s Externas para acesso no RM Portal.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=142802978
version: 17
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | Portal Web |
| **Subprocesso** | **:** | Cadastro URL’s Externas para acesso no RM Portal. |
| **Data da publicação** | **:** | 07/04/2014 |

      O cadastro de URL´s externas visa permitir ao usuário o acesso a páginas na web via links, dentro da opção Ferramentas > Utilitários no RM Portal.

**Cadastro de Categoria URL’s Externas**

     Para cadastrar as URL’s externas primeiro será preciso cadastrar as categorias das URL’s e associar aos perfis de segurança que terão acessos a esta categoria. Após o cadastro será possível associar uma URL a uma categoria correspondente. 

Isso deverá ser feito dentro do RM, em Globais > Serviços > Categoria 

Defina um nome para a Categoria.

Defina os Perfis de acesso da Categoria.

**Cadastro de URL’s Externas para Web**

      Após cadastrar a Categoria vamos cadastrar as URL’s que serão acessadas pelo o Portal. Neste cadastro deverão ser informados a categoria da URL e a opção de enviar o contexto do sistema para o site externo.

    As URL’s serão por sistema, portanto ao entrar na visão do cadastro o usuário deverá selecionar o sistema que estará cadastrando as URL’s (igual ao cadastro de perfil).

Defina:

* O Nome da URL
* A URL Externa
* A Categoria criada anteriormente
* Envia Contexto

**Página Web de URL’s Externas**

     No portal será exibido para o usuário todas as URL’s do Sistema que esta logado e URL’s Globais, onde ambas sejam das categorias associadas aos perfis de segurança do usuário.

Caso as URL’s estejam cadastradas para enviar o contexto do sistema ao clicar no link será enviado o contexto do sistema junto com a URL.

A página web das URL’s externas terão as seguintes informações:

* Nome
* URL

**Execução segura do site externo**

Ao clicar na url disponibilizada na lista, o usuário será redirecionado para o link em questão. Serão passados dois parâmetros para a url, entre eles:

* *key1* = Valor *string* contendo Identificador da sessão do usuário;
* *key2* = Valor *string* contendo um código criptografado validador de segurança do processo.

**WebService de retorno da sessão do usuário**

**1)** **– Serviço web para retornar a session do usuario:**

Foi disponibilizado um WebService genérico no Portal Corpore.Net chamado “wsCorporeNet”. Ele contém o método “GetXmlSession”.Conforme abaixo:

[WebMethod]

public string GetXmlSession(string idSession, string checkSum)

Esse método deverá receber os parâmetros enviados através do link redirecionado. Se os valores forem passados de forma correta, o mesmo retornará todo o conteúdo da sessão do usuário em um formato xml, conforme figura abaixo:

**2)** **– Informações técnicas para utilização do webService nos sites externos**

**a)** Os parâmetros [key1 e key2] passados na url deverão ser recuperados da seguinte forma (exemplo criados na linguagem *dotNet):*

* string key1 = HttpContext.Current.Request.QueryString["Key1"].ToString();
* string key2 = HttpContext.Current.Request.QueryString["Key2"].ToString();

**b)** Deverá ser criado um *proxy* de webService para comunicação com o serviço web hospedado no portal RM, conforme figura aba

Para criação do *proxy*, o usuário deverá informar a url do endereço de WebService hospedado.

**c)** Após a criação do proxy, o método “*GetXmlSession*” poderá ser chamado. Esse deverá receber os valores de Key1 e Key2 nos parâmetros do método. Se os mesmo forem passados de forma correta, ele retornará uma string contendo o conteúdo das variáveis de sessão do usuário no formato *Xml*, conforme exemplo abaixo:

string sessionId = HttpContext.Current.Request.QueryString["Key1"].ToString();

string checkSum = HttpContext.Current.Request.QueryString["Key2"].ToString();

 wsCorp.wsCorporeNetSoapClient x = new wsCorp.wsCorporeNetSoapClient();

string result = x.GetXmlSession(sessionId, checkSum);

**Consumo de WebService**

                - Ao acionar o link externo, o nosso portal irá enviar na query string, ou seja, via método GET, duas chaves que serão solicitadas pelo nosso método do web service.

                - Em posse dessas chaves, basta acionar nosso web service e chamar o método informado na documentação passando as duas chaves recuperadas anteriormente.

                Na web temos vários exemplos de consumo de WS utilizando linguagem ASP.

                Seguem alguns exemplos:

* <http://www.codeproject.com/Articles/18737/Call-XML-Web-service-from-ASP>
* <http://stackoverflow.com/questions/6781734/how-to-call-a-net-web-service-method-from-classic-asp-using-soap>
* <http://stackoverflow.com/questions/19588294/how-to-call-net-webservice-in-classic-asp>
* <http://forums.asp.net/t/1777845.aspx?Consuming+ASP+Net+webservice+un+exposed+method+through+Classic+ASP>
* <http://weblogs.asp.net/cabhilash/archive/2010/03/18/calling-web-services-in-classic-asp.aspx>
* <http://www.velocityreviews.com/forums/t76035-calling-a-net-web-service-from-classic-asp.html>

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
