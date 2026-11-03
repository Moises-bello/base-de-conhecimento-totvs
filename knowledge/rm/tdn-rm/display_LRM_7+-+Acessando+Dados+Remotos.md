---
content_hash: b3b92682029c5677924f74d57504bd5151a0580a3e36016cb3985f6d3efca62f
fetched_at: '2026-06-29T00:11:28.479344+00:00'
page_id: '731881780'
product: rm
source: tdn-rm
title: 7 - Acessando Dados Remotos
type: documentation
url: https://tdn.totvs.com/display/LRM/7+-+Acessando+Dados+Remotos
version: 6
---

Branch de Referência

Compare rest\_api com pub\_sub

REST

Representational State Transfer (REST) é um estilo de arquitetura para a construção de sistemas distribuídos baseados em hipermídia. Uma vantagem principal do modelo REST é que ele é baseado em padrões abertos e não vincula a implementação do modelo ou dos aplicativos cliente que o acessam a nenhuma implementação específica. Portanto, um serviço Web REST pode ser implementado usando o Microsoft ASP.NET Core e os aplicativos cliente podem ser desenvolvidos usando qualquer linguagem e conjunto de ferramentas que possam gerar solicitações HTTP e analisar respostas HTTP.

O modelo REST usa um esquema de navegação para representar objetos e serviços em uma rede, referidos como recursos. Os sistemas que implementam REST normalmente usam o protocolo HTTP para transmitir solicitações de acesso a esses recursos. Nesses sistemas, um aplicativo cliente envia uma solicitação na forma de um URI que identifica um recurso e um método HTTP (como GET, POST, PUT ou DELETE) que indica a operação a ser executada nesse recurso. O corpo da solicitação HTTP contém todos os dados necessários para executar a operação.

REST define um modelo de solicitação sem estado. Portanto, as solicitações HTTP devem ser independentes e podem ocorrer em qualquer ordem.

A resposta de uma solicitação REST usa códigos de status HTTP padrão. Por exemplo, uma solicitação que retorna dados válidos deve incluir o código de resposta HTTP 200 (**`OK`**), enquanto uma solicitação que falha ao localizar ou excluir um recurso especificado deve retornar uma resposta que inclua o código de status HTTP 404 (**`Not Found`**).

Uma API Web RESTful expõe um conjunto de recursos conectados e fornece as principais operações que permitem que um aplicativo manipule esses recursos e navegue facilmente entre eles. Por esta razão, as URIs que constituem uma típica API web RESTful são orientadas para os dados que ela expõe, e usam as facilidades fornecidas pelo HTTP para operar sobre esses dados.

Solicitação GET

A classe `FormAnswerService` é usada para gerenciar o processo de recuperação de dados do domínio **FormAnswer**. No método **`RegisterAppServices`** da classe **`MauiProgram`**, a classe `FormAnswerService` é registrada como um mapeamento de tipo em relação ao tipo **`IFormAnswerService`** com o contêiner de injeção de dependência. Então, quando uma instância da classe **`FormAnswerViewModel`** é criada, seu construtor aceita um tipo **`IFormAnswerService`**, que o contêiner de injeção de dependência resolve, retornando uma instância da classe `FormAnswerService`. 

A imagem abaixo mostra a interação de classes que leem dados do domínio **FormAnswer**.

O ViewModel chama o método **`GetFormAnswers`** da instância `FormAnswerService` que foi injetada no ViewModel pelo contêiner de injeção de dependência. O exemplo de código a seguir mostra o método **`GetFormAnswers`**:

c#RDarkC#> GetFormAnswers(FormParamsApiClass paramApi)
{
string paramsFixed = SyncParamsHelper.GetSyncParams(paramApi, 1);
if (paramApi.Status.HasValue)
{
string condStatus = paramApi.IgnoreStatus ? "ne" : "eq";
paramsFixed += (paramsFixed.Contains("$filter") ? " and " : (string.IsNullOrEmpty(paramsFixed) ? string.Empty : "&") + "$filter=") +
$"statusId {condStatus} {(int)paramApi.Status.Value}";
}
string apiResource = $"{ApiUrlBase}formanswers" + (string.IsNullOrEmpty(paramsFixed) ? string.Empty : $"?{paramsFixed}");
return await \_requestProvider.GetAsync>(apiResource);
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui/Services/FormAnswer/FormAnswerService.cs)

Esse método cria o URI que identifica o recurso para o qual a solicitação será enviada e usa a classe **`RequestProvider`** para invocar o método GET HTTP no recurso, antes de retornar os resultados para o  **`ViewModel`**. A classe **`RequestProvider`** contém a funcionalidade que envia uma solicitação na forma de um URI que identifica um recurso, um método HTTP que indica a operação a ser executada nesse recurso e um corpo que contém todos os dados necessários para executar a operação. 

O exemplo de código a seguir mostra o método **`GetAsync`** na classe **`RequestProvider`**:

c#RDarkC# GetAsync(string uri, string token = "")
{
HttpClient httpClient = GetOrCreateHttpClient(token);
HttpResponseMessage response = await httpClient.GetAsync(uri).ConfigureAwait(false);
await HandleResponse(response).ConfigureAwait(false);
TResult result = await response.Content.ReadFromJsonAsync();
return result;
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/RequestProvider/RequestProvider.cs)

Esse método chama o método **`GetOrCreateHttpClient`**, que retorna uma instância da classe **`HttpClient`** com os cabeçalhos apropriados definidos. Em seguida, ele envia uma solicitação **`GET`** assíncrona ao recurso identificado pelo URI, com a resposta sendo armazenada na instância **`HttpResponseMessage`**. O método **`HandleResponse`** é invocado, o que lança uma exceção se a resposta não incluir um código de status HTTP de sucesso. Em seguida, a resposta é lida como uma string, convertida de JSON para um objeto `RMSApiListagem` e retornada ao `FormAnswerService`.

Dica

É altamente recomendável armazenar em cache e reutilizar instâncias do **`HttpClient`** para obter melhor desempenho do aplicativo. Criar um novo **`HttpClient`** para cada operação pode levar a um problema de esgotamento do soquete.

Solicitação POST

A classe `FormAnswerService` é usada para gerenciar o processo de recuperação e atualização de dados do domínio **FormAnswer**. No método **`RegisterAppServices`** na classe **`MauiProgram`**, a classe `FormAnswerService` é registrada como um mapeamento de tipo em relação ao tipo **`IFormAnswerService`** com o contêiner de injeção de dependência. Então, quando uma instância da classe **`FormAnswerViewModel`** é criada, seu construtor aceita um tipo **`IFormAnswerService`**, que o contêiner de injeção de dependência resolve, retornando uma instância da classe `FormAnswerService`.

A imagem abaixo mostra a interação das classes que enviam os dados do domínio **FormAnswer**.

O ViewModel chama o método **`PostFormAnswer`** da instância `FormAnswerService` que foi injetada no ViewModel pelo contêiner de injeção de dependência. O exemplo de código a seguir mostra o `GetCatalogAsync`método:

c#RDarkC# PostFormAnswer(string userCodeSync, string systemCode, int appId, FormResposta formResposta)
{
string apiResource = $"{ApiUrlBase}formanswers";
return await \_requestProvider.PostAsync(apiResource, formResposta);
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui/Services/FormAnswer/FormAnswerService.cs)

Esse método cria o URI que identifica o recurso para o qual a solicitação será enviada e usa a classe **`RequestProvider`** para invocar o método POST HTTP no recurso, antes de retornar os resultados ao ViewModel.  
O exemplo de código a seguir mostra um dos métodos **PostAsync** na classe **`RequestProvider`**:

c#RDarkC# PostAsync(string uri, TResult data, string token = "", string header = "")
{
HttpClient httpClient = GetOrCreateHttpClient(token);
if (!string.IsNullOrEmpty(header))
{
AddHeaderParameter(httpClient, header);
}
var content = new StringContent(JsonSerializer.Serialize(data));
content.Headers.ContentType = new MediaTypeHeaderValue("application/json");
HttpResponseMessage response = await httpClient.PostAsync(uri, content).ConfigureAwait(false);
await HandleResponse(response).ConfigureAwait(false);
TResult result = await response.Content.ReadFromJsonAsync();
return result;
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/RequestProvider/RequestProvider.cs)

Esse método chama o método **GetOrCreateHttpClient**, que retorna uma instância da classe **HttpClient** com os cabeçalhos apropriados definidos. Em seguida, ele envia uma solicitação **POST** assíncrona para o recurso identificado pelo URI, com os dados serializados da cesta sendo enviados no formato JSON e a resposta sendo armazenada na instância **HttpResponseMessage**. O método **HandleResponse** é invocado, o que lança uma exceção se a resposta não incluir um código de status HTTP de sucesso. Em seguida, a resposta é lida como uma string, convertida de JSON para um objeto **FormResposta** e retornada ao `FormAnswerService`.
