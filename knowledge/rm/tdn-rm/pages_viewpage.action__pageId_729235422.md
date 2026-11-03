---
content_hash: ad3424bf274920d793773826a6c2ac293aab0c5469e356a49d334c0646d245a6
fetched_at: '2026-06-29T00:11:27.729886+00:00'
page_id: '729235422'
product: rm
source: tdn-rm
title: 2 - Model-View-ViewModel (MVVM)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=729235422
version: 10
---

Introdução

O padrão MVVM ajuda a separar claramente a lógica de negócio e apresentação de um aplicativo de sua interface de usuário (UI). Manter uma separação clara entre a lógica do aplicativo e a UI ajuda a resolver vários problemas de desenvolvimento e facilita o teste, a manutenção e a evolução de um aplicativo. Ela também pode melhorar significativamente as oportunidades de reutilização de código e permite que desenvolvedores e designers de UI colaborem mais facilmente ao desenvolver suas respectivas partes de um aplicativo.

Além de entender as responsabilidades de cada componente, também é importante entender como eles interagem. Em um alto nível, a **View** conhece o **ViewModel** e o **ViewModel** conhece o **Model**, mas o **Model** não conhece o **ViewModel** e o **ViewModel** não conhece a **View**. Portanto, o **ViewModel** isola a **View** do **Model** e permite que o **Model** evolua independentemente da **View**.

[Saiba mais](https://learn.microsoft.com/en-us/dotnet/architecture/maui/mvvm)

View

A **View** é responsável por definir a estrutura, layout e aparência do que o usuário vê na tela. Idealmente, cada **View** é definida em XAML, com um code-behind limitado que não contém a lógica de negócio. No entanto, em alguns casos, o code-behind pode conter lógica de interface do usuário que implementa um comportamento visual difícil de expressar em XAML, como animações.

Dica

Evite habilitar e desabilitar elementos de interface no code-behind.

View Model

O **ViewModel** implementa propriedades e comandos aos quais a **View** pode vincular dados e notifica-la de quaisquer alterações de estado por meio de eventos de notificação de alteração. As propriedades e comandos que o **ViewModel** fornece definem a funcionalidade a ser oferecida pela interface do usuário, mas a **View** determina como essa funcionalidade deve ser exibida.

Embora seja possível expor a implementação real da interface **ICommand** no **ViewModel** (por exemplo, **Command<T>** ou **RelayCommand**), é recomendável expor seus comandos publicamente como **ICommand**. Dessa forma, se for necessário alterar a implementação posteriormente, ela poderá ser facilmente trocada.

Dicas

* Mantenha a interface de usuário responsiva com operações assíncronas.
* Centralize conversões de dados em uma camada de conversão.
* Para coleções utilize **ObservableCollection<T>**.
Model

As classes de modelo são classes não visuais que encapsulam os dados do aplicativo. Portanto, o **Model** pode ser pensado como a representação do modelo de domínio do aplicativo, que geralmente inclui um modelo de dados juntamente com lógica de negócio e validação. Exemplos: objetos de transferência de dados (DTOs) e Plain Old CLR Objects (POCOs).  
As classes de modelo são normalmente usadas em conjunto com serviços ou repositórios que encapsulam o acesso a dados e o armazenamento em cache.

Importante

Os aplicativos devem ser arquitetados para o uso correto do evento **PropertyChanged**, atendendo aos seguintes requisitos:

* Sempre disparar um evento **PropertyChanged** para quaisquer propriedades calculadas cujos valores sejam usados ​​por outras propriedades no **Model** ou **ViewModel**.
* Sempre disparar um evento **PropertyChanged** no final do método que faz uma alteração de propriedade, ou quando se sabe que o objeto está em um estado seguro. Gerar o evento interrompe a operação invocando os manipuladores do evento de forma síncrona. Se isso acontecer no meio de uma operação, poderá expor o objeto a funções de retorno de chamada quando estiver em um estado não seguro e parcialmente atualizado. Além disso, é possível que mudanças em cascata sejam acionadas por eventos **PropertyChanged**. As alterações em cascata geralmente exigem que as atualizações sejam concluídas antes que a alteração em cascata seja segura para execução.
* Nunca disparar um evento **PropertyChanged** se a propriedade não for alterada. Isso significa que você deve comparar os valores antigos e novos antes de gerar o evento **PropertyChanged**.
* Nunca disparar um evento **PropertyChanged** durante o construtor de um **ViewModel** se você estiver inicializando uma propriedade. Os controles vinculados a dados na **View** não estarão assinados para receber notificações de alteração neste momento.
* Nunca disparar mais de um evento **PropertyChanged** com o mesmo argumento de nome de propriedade em uma única invocação síncrona de um método público de uma classe. Por exemplo, dada uma propriedade **NumberOfItems** cujo armazenamento de apoio é o campo **\_numberOfItems**, se um método incrementa o **\_numberOfItems** cinquenta vezes durante a execução de um loop, ele só deve gerar notificação de alteração de na propriedade **NumberOfItems** uma vez, depois que todo o trabalho estiver concluído. Para métodos assíncronos, gere o evento **PropertyChanged** para um determinado nome de propriedade em cada segmento síncrono de uma cadeia de continuação assíncrona.
