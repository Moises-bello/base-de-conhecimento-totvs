---
content_hash: 344e59ada9114a8462ede6963d2799e60bdd1566262b69b8909ccfe97c739389
fetched_at: '2026-06-29T00:08:58.603318+00:00'
page_id: '360450387'
product: rm
source: tdn-rm
title: Biblioteca AspNetCore
type: documentation
url: https://tdn.totvs.com/display/LRM/Biblioteca+AspNetCore
version: 6
---

# Índice:

---

.\*ndice:

# Objetivo:

---

       Esta página tem por objetivo demonstrar como é feito o uso Middleware.

# Snowden AspNetCore:

---

       Esta biblioteca fornecida pelo Snowden disponibiliza um meio para que aplicações desenvolvidas em Asp.Net 5 consigam fazer a integração facilitada. Fornecendo operações para gravar qualquer \_Exception\_ não tratada pelos \_controllers\_ e gravando também respostas selecionadas com base em seu status.

       Apesar do nome AspNetCore, ela também funciona no .Net a partir da versão 4.7.1, desde que a mesma esteja utilizando a versão do Asp.Net 5

# Como Funciona:

---

       Esta biblioteca funciona adicionando ***middlewares***na pilha de execução de sua aplicação. Então toda requisição terá uma interação com esses ***middlewares,*** podendo assim capturar ***exceptions***ainda não tratados nos ***controllers***ou mesmo pegar o conteúdo da requisição ou resposta.

# Get Started:

---

       Com uma nova aplicação em AspNetCore, vamos adicionar as dependências e configurar o uso do Snowden, para isso vamos editar o arquivo de Startup.cs gerado.

       Na parte de configuração de serviços (ConfigureServices) vamos adicionar o Snowden no injetor de dependências e configura-lo. Então vamos utilizar o ***namespace***Totvs.Snowden.ClientApi.AspNetCore que contem extensões facilitadoras para isso. Vejamos exemplo abaixo:

c#
{
// ambiente que se encontra a aplicação
config.Environment = EnvironmentDefaultNames.Test;
// Definições da aplicação
config.Application.Name = "snowden-aspnetcore";
config.Application.ProductLine = "snowden-samples";
config.Application.Version = typeof(Startup).Assembly.GetName().Version.ToString();
// authenticação com os servidores do snowden
config.Credentials.Key = "tRaIsWygt2hKAubGk4EjSrGACDsa";
config.Credentials.Secret = "7MpWYUzesrLkAgyoIze3i7rffFYa";
// Definimos um totvsId Padrão
// pode ser resolvido em tempo de execução implementando
// ISnowdenAspNetCoreClientResolver e registrando. ex:
// `config.Services.ClientResolver = typeof(MyType);`
config.TotvsId = "03745af30a384000908D1fc02f6a5240";
// Se desejamos logar qualquer exception enviada pelo sistema
config.Log.Exceptions = true;
// Logar as respostas com os seguintes status
// ALERTA: Esta operação pode degradar o sistema
// pois ela demanda utilizar stream em memoria do
// resultado do objeto.
config.Log.ResponseStatusCode = SnowdenClientApiAspNetCoreOptionsLog.ServerFaultStatuses;
});
services.AddMvc();
}]]>

       Vemos acima que estamos configurando diversas informações do Snowden, incluindo dados da aplicação que está executando; Credenciais de autenticação com o Snowden; Cliente da operação (a seguir será mostrado como resolve-lo dinamicamente); E também onde deve ser gravado;

       Até agora tudo que fizemos foi adicionar as dependências do Snowden e configura-las. Agora vamos adicionar o Snowden na pilha de execução da aplicação. Nas configurações da aplicação (Configure), também utilizando do namespace Totvs.Snowden.ClientApi.AspNetCore, vamos utilizar outro facilitador. Vejamos abaixo:

c#

       Com isso nossa aplicação já se encontra integrada com o Snowden, a partir de agora qualquer Exception não tratada será gravada. Como configurado, também estaremos gravando qualquer resposta que pertença ao grupo de falhas de servidor (faixa 500).

       Observem também que adicionamos o Snowden logo antes do uso do MVC, isso está diretamente ligado ao funcionamento da ***middlewares***para que ela seja capaz de capturar a ele deve ser o primeiro na pilha de tratamento, para isso registramos ele posteriormente a qualquer tratamento de ***exceptions***, assim ele é o primeiro a tratar qualquer exception lançada. Segue abaixo uma leitura sugerida para melhor entendimento:

* <https://www.thomaslevesque.com/2018/03/27/understanding-the-asp-net-core-middleware-pipeline/>

# Identificação do Cliente em Tempo de Execução:

---

       Para identificarmos o cliente em tempo de execução temos que implementar a ***interface*** ISnowdenAspNetCoreClientResolver localizada em Totvs.Snowden.ClientApi.AspNetCore.Services, essa apenas requer a implementação de um único método que recebe o contexto da requisição e deve retornar o TotvsId.

c#

       Após implementar a classe, devemos adicionar nossa implementação no container de injeção de dependências, e configurar para o Snowden utilizar nossa implementação. Para isso dentro das opções do Snowden temos a opção Services, essa possui a propriedade "ClientResolver" que recebe o tipo que irá fazer a resolução do cliente.

c#
{
config.Environment = EnvironmentDefaultNames.Test;
config.Application.Name = "snowden-aspnetcore";
config.Application.ProductLine = "snowden-samples";
config.Application.Version = typeof(Startup).Assembly.GetName().Version.ToString();
config.Credentials.Key = "tRaIsWygt2hKAubGk4EjSrGACDsa";
config.Credentials.Secret = "7MpWYUzesrLkAgyoIze3i7rffFYa";
// Resolver que irá identificar o cliente em tempo de execução
config.Services.ClientResolver = typeof(CustomClientResolver);
});
services.AddMvc();
}]]>falsefalse

**Produto:** Framework

false

**Versão:** 12.1.20

false

**Processo:** Uso do Middleware

falsefalse

**Status:** Finalizado

false

**Data:**

false

**Autores:**
