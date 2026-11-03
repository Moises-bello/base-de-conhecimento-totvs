---
content_hash: f33d9594f3ebd589efb08cbb2be16ee250364f0c8d86b085d95f89fa17fd932c
fetched_at: '2026-06-29T00:11:28.549174+00:00'
page_id: '731904034'
product: rm
source: tdn-rm
title: 8 - Aplicando Teste Unitário
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=731904034
version: 6
---

Branch de Referência

Compare unit\_testing com rest\_api

Introdução

Um teste unitário pega uma pequena unidade do aplicativo, normalmente um método, isola-o do restante do código e verifica se ele se comporta conforme o esperado. Seu objetivo é verificar se cada unidade funciona conforme o esperado, para que os erros não se propaguem por todo o aplicativo. Detectar um bug onde ele ocorre é mais eficiente do que observar o efeito de um bug indiretamente em um ponto secundário de falha.

O teste unitário tem um efeito mais significativo na qualidade do código quando é parte integrante do fluxo de trabalho de desenvolvimento de software. Os testes unitários podem atuar como documentação de design e especificações funcionais para um aplicativo. Assim que um método for escrito, seus testes devem ser escritos para verificar o comportamento do método em resposta ao padrão, limite e casos de dados de entrada incorretos e também verifique quaisquer suposições explícitas ou implícitas feitas pelo código.

Os testes unitários são muito eficazes contra a regressão. Ou seja, rotina que funcionava, mas foi prejudicada por uma atualização com bug.

MVVM

Testar Models e ViewModels de aplicativos MVVM é idêntico a testar qualquer outra classe e usa as mesmas ferramentas e técnicas; isso inclui recursos como teste unitário e simulação. No entanto, alguns padrões que são típicos para modelar e exibir classes de modelo podem se beneficiar de técnicas específicas de teste unitário.

Dica

Teste uma coisa com cada teste unitário. À medida que a complexidade de um teste se expande, torna-se mais difícil a verificação desse teste. Ao limitar um teste unitário a uma única preocupação, podemos garantir que nossos testes sejam mais repetíveis, isolados e tenham um tempo de execução menor.

Não tente fazer um teste unitário expressar mais de um aspecto do comportamento da unidade. Isso leva a testes que são difíceis de ler e atualizar. Também pode ser confuso para interpretar uma falha.

O aplicativo MinhaQualidadeMaui usa [xUnit](https://xunit.net/) para realizar testes unitários, que suporta dois tipos diferentes de teste:

| Tipo de teste | Atributo | Descrição |
| --- | --- | --- |
| Fatos | `Fact` | Testes que são sempre verdadeiros, que testam condições invariantes. |
| Teorias | `Theory` | Testes que são verdadeiros apenas para um determinado conjunto de dados. |

Os testes unitários incluídos no aplicativo MinhaQualidadeMaui são testes de fato, portanto, cada método de teste é criado com o atributo **`Fact`**.

Testando a Funcionalidade Assíncrona

Ao implementar o padrão MVVM, os ViewModels geralmente invocam operações em serviços de forma assíncrona. Os testes de código que invocam essas operações normalmente usam simulações como substitutos dos serviços reais. O exemplo de código a seguir demonstra o teste da funcionalidade assíncrona passando um serviço fictício para um modelo de exibição:

c#RDarkC#

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui.Tests/Services/UserLoginServiceTests.cs)

Este teste unitário verifica se a propriedade **`login`** da instância `UserLoginService` terá o mesmo valor criado no inicio do teste depois que o método **`GetAsync`** for invocado. 

Testando Implementações de INotifyPropertyChanged

A implementação da interface **`INotifyPropertyChanged`** permite que as Views reajam às alterações originadas de Models e ViewModels. Essas alterações não estão limitadas aos dados mostrados nos controles -- elas também são usadas para controlar a View, como os estados do ViewModel que fazem com que as animações sejam iniciadas ou os controles sejam desabilitados.

As propriedades que podem ser atualizadas diretamente pelo teste unitário podem ser testadas anexando um manipulador de eventos ao evento **`PropertyChanged`** e verificando se o evento é gerado após definir um novo valor para a propriedade. O exemplo de código a seguir mostra esse teste:

c#RDarkC#
{
if (e?.PropertyName?.Equals(nameof(LoginViewModel.MensagemErroLogin)) ?? false)
{
invoked = true;
}
};
loginViewModel.IsMock = true;
loginViewModel.Login.Value = "error";
loginViewModel.Senha.Value = "error";
loginViewModel.LoginCommand.Execute(null);
Assert.True(invoked);
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui.Tests/ViewModels/LoginViewModelTests.cs)

Este teste unitário invoca o comando **`LoginCommand`** da classe **`LoginViewModel`**, que faz com que sua propriedade **`MensagemErroLogin`** seja atualizada. O teste será aprovado, desde que o evento **`PropertyChanged`** seja gerado para a propriedade **`MensagemErroLogin`**.

Testando a Comunicação Baseada em Mensagens

Os ViewModels que usam a classe **`MessagingCenter`** para se comunicar entre classes fracamente acopladas podem ser testados na unidade, assinando a mensagem enviada pelo código em teste, conforme demonstrado no exemplo de código a seguir:

c#RDarkC#(this, MessageKeys.LoginShowPass, (sender) =>
{
messageReceived = true;
});
loginViewModel.ShowPassCommand.Execute(null);
Assert.True(messageReceived);
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui.Tests/ViewModels/LoginViewModelTests.cs)

Este teste unitário verifica se o `LoginViewModel` publica a mensagem `LoginShowPass` em resposta à sua execução do comando `ShowPassCommand`. Como a classe **`MessagingCenter`** oferece suporte a assinaturas de mensagem multicast, o teste de unidade pode assinar a mensagem `LoginShowPass` e executar uma rotina de callback em resposta ao recebimento dela. Essa rotina de callback, especificada como uma expressão lambda, define um campo booleano usado pela instrução **`Assert`** para verificar o comportamento do teste.

Testando Tratamento de Exceção

Testes de unidade também podem ser escritos para verificar se exceções específicas são lançadas para ações ou entradas inválidas, conforme demonstrado no exemplo de código a seguir:

c#RDarkC#(async () => await userLoginService.GetAsync(login));
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui.Tests/Services/UserLoginServiceTests.cs)

Este teste unitário lançará uma exceção porque o objeto `MockUserLoginService` espera um parâmetro diferente de nulo e vazio. O método **`Assert.Throws<T>`** é um método genérico onde `T` é o tipo da exceção esperada. O argumento passado para o método **`Assert.Throws<T>`** é uma expressão lambda que lançará a exceção. Portanto, o teste de unidade será aprovado, desde que a expressão lambda lance um **`Exception`**.

Dica

Evite escrever testes que comparem strings de mensagens de exceção. As cadeias de caracteres de mensagens de exceção podem mudar com o tempo e, portanto, os testes de unidade que dependem dessa comparação são considerados frágeis.
