---
content_hash: 0e2d035439b4a68790a1532c4bee16fb37a3d0c649da2d28f51f5992297bbd65
fetched_at: '2026-06-29T00:11:28.090505+00:00'
page_id: '729242006'
product: rm
source: tdn-rm
title: 4 - Navegação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=729242006
version: 7
---

Branch de Referência

Compare navigation com dependency\_injection

Introdução

O .NET MAUI inclui suporte para navegação de página, que normalmente resulta da interação do usuário com a interface do usuário ou do próprio aplicativo como resultado de alterações internas de estado de objetos.

A lógica de navegação pode residir no code-behind de uma View ou em um ViewModel associado a dados. Embora colocar a lógica de navegação em uma View possa ser a abordagem mais direta, ela não é facilmente testável por meio de testes de unidade. Colocar a lógica de navegação em classes de ViewModel significa que a lógica pode ser verificada por meio de testes de unidade. Além disso, o ViewModel pode implementar a lógica para controlar a navegação para garantir que certas regras de negócios sejam aplicadas. Por exemplo, um aplicativo pode não permitir que o usuário saia de uma página sem primeiro garantir que os dados inseridos sejam válidos.

Um serviço de navegação é normalmente invocado a partir de ViewModels, a fim de promover a testabilidade. No entanto, navegar para Views dos ViewModels exigiria que os ViewModels fizessem referência a View e, particularmente, Views às quais o ViewModel ativo não está associado, o que não é recomendado. Portanto, o **MauiNavigationService** apresentado aqui especifica o tipo de ViewModel como o destino para o qual navegar.

O aplicativo multiplataforma **MinhaQualidadeMaui** usa a classe **MauiNavigationService** para fornecer navegação ao ViewModel. Essa classe implementa a interface **INavigationService**, que é mostrada no seguinte exemplo de código:

c#RDarkC# routeParameters = null);
Task PopAsync();
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui/Services/Navigation/INavigationService.cs)

Essa interface especifica que uma classe de implementação deve fornecer os seguintes métodos:

| Método | Propósito |
| --- | --- |
| InitializeAsync | Executa a navegação quando o aplicativo é iniciado. |
| NavigateToAsync | Executa navegação hierárquica para uma página especifica usando uma rota de navegação registrada. Pode, opcionalmente, passar parâmetros de rota nomeados para usar no processamento da página de destino. |
| PopAsync | Remove a página atual da pilha de navegação. |

Solicitação de Navegação

O .NET MAUI fornece várias maneiras de navegar em um aplicativo. A maneira tradicional de navegar é com a classe **`NavigationPage`**, que implementa uma experiência de navegação hierárquica na qual o usuário pode navegar pelas páginas, para frente e para trás, conforme desejar. No aplicativo MinhaQualidadeMaui foi implementado o componente **`Shell`** como contêiner raiz e um host de navegação. 

A navegação é realizada dentro das classes ViewModel invocando um dos métodos **`NavigateToAsync`**, especificando o caminho da rota para a página que está sendo navegada, conforme demonstrado no exemplo de código a seguir:

c#RDarkC#

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui/ViewModels/LoginViewModel.cs)

O exemplo de código a seguir mostra o método **`NavigateToAsync`** fornecido pela classe **`MauiNavigationService`**:

c#RDarkC# routeParameters = null)
{
var shellNavigation = new ShellNavigationState(route);
return routeParameters != null
? Shell.Current.GoToAsync(shellNavigation, true, routeParameters)
: Shell.Current.GoToAsync(shellNavigation, true);
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui/Services/Navigation/MauiNavigationService.cs)

O controle `Shell` já está familiarizado com a navegação baseada em rota, portanto, o método **`NavigateToAsync`** funciona para mascarar essa funcionalidade. O método **`NavigateToAsync`** permite que os dados de navegação sejam especificados como um argumento que é passado para o ViewModel que está sendo navegado, onde normalmente é usado para executar a inicialização.

Passando Parâmetros

O método **`NavigateToAsync`**, especificado pela interface **`INavigationService`**, permite que os dados de navegação sejam especificados como um **`IDictionary<string, object>`** dos dados que são passados ​​para o ViewModel que está sendo navegado, onde normalmente é usado para executar a inicialização.

Por exemplo, a classe **`LoginViewModel`** contém um **`ConfigurationCommand`** que é executado quando o usuário clica no botão de configuração na página **`RMSLoginPage`**. Por sua vez, isso executa o método **`OnConfigurate_ClickedAsync`**, que é mostrado no seguinte exemplo de código:

c#RDarkC# { { "IsBaseExemplo", isExBase } });
}
...
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui/ViewModels/LoginViewModel.cs)

Este método invoca a navegação para a rota **`ReconfigPage`**, passando a propriedade IsBaseExemplo como parâmetro.

O `ReconfigViewModel` possui um atributo adicionado a ele que permite receber dados do serviço de navegação, conforme mostrado no exemplo de código abaixo.

c#RDarkC# CanBackup = !value && !string.IsNullOrEmpty(App.GetContexto().User);
}
...
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui/ViewModels/ReconfigViewModel.cs)

O atributo `QueryProperty` nos permite fornecer um parâmetro para uma propriedade para mapear valores e uma chave para localizar valores do dicionário de parâmetros de consulta. Neste exemplo, a chave "IsBaseExemplo" e o valor dela foram fornecidos durante a chamada **`NavigateToAsync`**. O ViewModel encontrou a chave "IsBaseExemplo" e mapeou o valor para a propriedade `IsBaseExemplo`.
