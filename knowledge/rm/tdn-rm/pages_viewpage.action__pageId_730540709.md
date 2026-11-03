---
content_hash: 1a46f9934e3ce3c864937de28d1aeefd2812fcb9e282ad2539d39ee84fa8f7be
fetched_at: '2026-06-29T00:11:28.201457+00:00'
page_id: '730540709'
product: rm
source: tdn-rm
title: 6 - Publish/Subscribe
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=730540709
version: 5
---

Branch de Referência

Compare pub\_sub com validation

Introdução

A classe **`MessagingCenter`** implementa o padrão Publish-Subscribe, permitindo a comunicação baseada em mensagens entre componentes com baixo acoplamento. Esse mecanismo permite que publicadores e assinantes se comuniquem sem ter uma referência direta um ao outro, ajudando a reduzir as dependências entre os componentes, além de permitir que os componentes sejam desenvolvidos e testados de forma independente.

A classe **`MessagingCenter`** fornece a funcionalidade de publicação/assinatura multicast. Isso significa que pode haver vários publicadores que publicam uma única mensagem e vários assinantes ouvindo a mesma mensagem. A imagem abaixo ilustra essa relação:

Os publicadores enviam mensagens usando o método **`MessagingCenter.Send`**, enquanto os assinantes escutam as mensagens usando o método **`MessagingCenter.Subscribe`**. Além disso, os assinantes também podem cancelar assinaturas de mensagens, se necessário, com o método **`MessagingCenter.Unsubscribe`**.

Internamente, a classe **`MessagingCenter`** usa referências fracas. Isso significa que ele não manterá os objetos "vivos" e permitirá que eles sejam coletados como lixo. Portanto, só deve ser necessário cancelar a assinatura de uma mensagem quando uma classe não deseja mais recebe-la.

Embora a classe **`MessagingCenter`** permita a comunicação entre classes fracamente acopladas, ela não oferece uma única solução de arquitetura para esse problema. Por exemplo, a comunicação entre um ViewModel e uma View também pode ser obtida pelo mecanismo de **Binding** e por meio de notificações de alteração de propriedade (**NotifyPropertyChanged**). Além disso, a comunicação entre dois ViewModels também pode ser obtida passando dados durante a navegação.

Publicando

Os publicadores notificam os assinantes de uma mensagem com uma das sobrecargas **`MessagingCenter.Send`**. O exemplo de código a seguir demonstra a publicação da mensagem **`LoginShowPass`**:

c#RDarkC#

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/ViewModels/RMSLoginViewModel.cs)

Neste exemplo, o método **Send** especifica dois argumentos:

* O primeiro argumento especifica a classe do remetente. Ela deve ser especificada por qualquer assinante que deseje receber a mensagem.
* O segundo argumento especifica a mensagem.

Se necessário, um terceiro argumento pode especificar os dados de payload a serem enviados ao assinante. Esse payload pode ser de qualquer tipo **`object`**. Será importante que o assinante da mensagem conheça o tipo de payload esperado.

O método Send publicará a mensagem e seus dados usando uma abordagem de fire-and-forget. Portanto, a mensagem é enviada mesmo que não haja assinantes cadastrados para receber a mensagem. Nessa situação, a mensagem enviada é ignorada.

O método **`MessagingCenter.Send`** pode usar parâmetros genéricos para controlar como as mensagens são entregues. Portanto, várias mensagens que compartilham uma identidade de mensagem, mas enviam diferentes tipos de dados de payload, podem ser recebidas por diferentes assinantes.

Assinando

Os assinantes podem se registrar para receber uma mensagem usando uma das sobrecargas. O exemplo de código a seguir demonstra como o aplicativo MinhaQualidadeMaui se inscreve e processa a mensagem **`LoginShowPass`**:

c#RDarkC#(this, MessageKeys.LoginShowPass, (viewModel) =>
{
Dispatcher.Dispatch(() =>
{
ImageShowSenha.Source = entrySenha.IsPassword ? "ImageShowSenhaOn.png" : "ImageShowSenhaOff.png";
entrySenha.IsPassword = !entrySenha.IsPassword;
});
});]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/Views/RMSLoginPage.xaml.cs)

No exemplo anterior, o método **Subscribe** assina a mensagem **`LoginShowPass`** e executa um delegate de retorno de chamada em resposta ao recebimento da mensagem. Esse delegate de retorno de chamada, especificado como uma expressão lambda, executa o código que atualiza a interface do usuário.

Não tente modificar os dados de payload de dentro de um delegate de retorno de chamada, pois vários threads podem estar acessando os dados recebidos simultaneamente. Nesse cenário, os dados de payload devem ser imutáveis para evitar erros de concorrência.

Cancelando Assinatura

Os assinantes podem cancelar a assinatura de mensagens que não desejam mais receber. Isso é obtido com uma das sobrecargas **`MessagingCenter`.Unsubscribe**, conforme demonstrado no exemplo de código a seguir:

c#RDarkC#(this, MessageKeys.LoginShowPass);]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/Views/RMSLoginPage.xaml.cs)

Neste exemplo, a sintaxe do método Unsubscribe reflete os argumentos de tipo especificados ao se inscrever para receber a mensagem **`LoginShowPass`**.
