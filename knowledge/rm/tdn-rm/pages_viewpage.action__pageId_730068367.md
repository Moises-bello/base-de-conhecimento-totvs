---
content_hash: 7bc37e2365df90988ec5b721606948d0f0212df73d4b1b36056057aebb532c9c
fetched_at: '2026-06-29T00:11:28.112215+00:00'
page_id: '730068367'
product: rm
source: tdn-rm
title: 5 - Validação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=730068367
version: 6
---

Branch de Referência

Compare validation com navigation

Visão Geral

Qualquer aplicativo que aceite entrada de usuários deve garantir que a entrada seja válida. Um aplicativo pode, por exemplo, verificar se a entrada que contém apenas caracteres em um intervalo específico, tem um determinado comprimento ou corresponde a um formato específico. Sem validação, um usuário pode fornecer dados que causam falha no aplicativo. A validação adequada impõe regras de negócio e pode ajudar a impedir que um invasor injete dados maliciosos.

No contexto do padrão Model-View-ViewModel (MVVM), um Model ou ViewModel geralmente será necessário para executar a validação de dados e sinalizar quaisquer erros de validação para a View para que o usuário possa corrigi-los. A imagem abaixo mostra as classes envolvidas no processo de validação.

As propriedades do ViewModel que requerem validação são do tipo **`ValidatableObject<T>`**, e cada instância **`ValidatableObject<T>`** tem regras de validação adicionadas à sua propriedade **`Validations`**. A validação é chamada do ViewModel chamando o método **`Validate`** da instância **`ValidatableObject<T>`**, que recupera as regras de validação e as executa na propriedade **`ValidatableObject<T>.Value`**. Quaisquer erros de validação são colocados na propriedade **`Errors`** da instância **`ValidatableObject<T>`** e a propriedade **`IsValid`** da instância **`ValidatableObject<T>`** é atualizada para indicar se a validação foi bem-sucedida ou falhou. O código a seguir mostra a implementação do **`ValidatableObject<T>`**:

c#RDarkC# : ObservableObject, IValidity
{
private IEnumerable \_errors;
private bool \_isValid;
private T \_value;
public List> Validations { get; } = new();
public IEnumerable Errors
{
get => \_errors;
private set => SetProperty(ref \_errors, value);
}
public bool IsValid
{
get => \_isValid;
private set => SetProperty(ref \_isValid, value);
}
public T Value
{
get => \_value;
set => SetProperty(ref \_value, value);
}
public ValidatableObject()
{
\_isValid = true;
\_errors = Enumerable.Empty();
}
public bool Validate()
{
Errors = Validations
?.Where(v => !v.Check(Value))
?.Select(v => v.ValidationMessage)
?.ToArray()
?? Enumerable.Empty();
IsValid = !Errors.Any();
return IsValid;
}
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/Validations/ValidatableObject.cs)

A notificação de alteração de propriedade é fornecida pela classe **`ObservableObject`** e, portanto, um controle **`Entry`** pode se vincular à propriedade **`IsValid`** da instância **`ValidatableObject<T>`** na classe do ViewModel para ser notificado se os dados inseridos são válidos ou não.

Regras de Validação

As regras de validação são especificadas criando uma classe que deriva da interface **`IValidationRule<T>`**, que é mostrada no exemplo de código a seguir:

c#RDarkC#
{
string ValidationMessage { get; set; }
bool Check(T value);
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/Validations/IValidationRule.cs)

Essa interface especifica que uma classe de regra de validação deve fornecer ummétodo**`Check`** booleano que é usado para executar a validação necessária e uma propriedade **`ValidationMessage`** cujo valor é a mensagem de erro de validação que será exibida se a validação falhar.

O exemplo de código a seguir mostra a regra **`IsNotNullOrEmptyRule<T>`** de validação, que é usada para realizar a validação do nome de usuário e senha inseridos pelo usuário na `RMSLoginPage`:

c#RDarkC# : IValidationRule
{
public string ValidationMessage { get; set; }
public bool Check(T value) =>
value is string str && !string.IsNullOrWhiteSpace(str);
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/Validations/IsNotNullOrEmptyRule.cs)

O método **`Check`** retorna um booleano indicando se o argumento de valor é nulo, vazio ou consiste apenas em caracteres de espaço em branco.

Às vezes, a validação pode envolver propriedades dependentes. Um exemplo de propriedades dependentes é quando o conjunto de valores válidos para a propriedade A depende do valor específico que foi definido na propriedade B. Verificar se o valor da propriedade A é um dos valores permitidos envolveria a recuperação do valor da propriedade B. Além disso, quando o valor da propriedade B fosse alterado, a propriedade A precisaria ser revalidada.

Adicionando Regras

No aplicativo multiplataforma MinhaQualidadeMaui, as propriedades do ViewModel que requerem validação são declaradas como sendo do tipo **`ValidatableObject<T>`**, onde `T` é o tipo do dado a ser validado. O exemplo de código a seguir mostra um exemplo de duas dessas propriedades:

c#RDarkC# Login { get; private set; }
public ValidatableObject Senha { get; private set; }]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/ViewModels/RMSLoginViewModel.cs)

Para que a validação ocorra, as regras de validação devem ser adicionadas à coleção **Validations** de cada instância **`ValidatableObject<T>`**, conforme demonstrado no exemplo de código a seguir:

c#RDarkC# { ValidationMessage = "O campo Usuário é obrigatório." });
Senha.Validations.Add(new IsNotNullOrEmptyRule { ValidationMessage = "O campo Senha é obrigatório." });
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/ViewModels/RMSLoginViewModel.cs)

Este método adiciona a regra de validação **`IsNotNullOrEmptyRule<T>`** à coleção **`Validations`** de cada instância **`ValidatableObject<T>`**, especificando valores para a propriedade **`ValidationMessage`** da regra de validação, que especifica a mensagem de erro de validação que será exibida se a validação falhar.

Validação Automática

A validação também é acionada automaticamente sempre que uma propriedade vinculada é alterada. Por exemplo, quando uma ligação bidirecional na **`RMSLoginPage`** define a propriedade **`Login`** ou **`Senha`**, a validação é acionada. O exemplo de código a seguir demonstra como isso ocorre:

xmlRDarkXML



]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/RMLib/Views/RMSLoginPage.xaml)

O controle **`CustomEntry`** é vinculado à propriedade **`Login.Value`** da instância **`ValidatableObject<T>`** e a coleção **`Behaviors`** do controle tem uma instância **`EventToCommandBehavior`** adicionada a ela. Esse comportamento executa o **`ValidateCommand`** em resposta ao disparo do evento **`TextChanged`** no **`CustomEntry`**, que é gerado quando o texto no **`CustomEntry`** é alterado. Por sua vez, o **`ValidateCommand`** executa o método `OnValidate`, que executa o método **`Validate`** na instância **`ValidatableObject<T>`**. Portanto, toda vez que o usuário insere um caractere no controle **`CustomEntry`** para o nome de usuário, é realizada a validação dos dados inseridos.

Exibindo Erros

O aplicativo multiplataforma MinhaQualidadeMaui notifica o usuário sobre quaisquer erros de validação, destacando o controle que contém os dados inválidos com uma borda vermelha e exibindo uma mensagem de erro que informa ao usuário por que os dados são inválidos abaixo do controle que contém os dados inválidos. Quando os dados inválidos são corrigidos, a borda volta ao estado padrão e a mensagem de erro é removida. A imagem abaixo mostra a `RMSLoginPage` quando há erros de validação.
