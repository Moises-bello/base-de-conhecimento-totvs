---
content_hash: e6d94b6c351d4391ea744d1568694afba2c9b2be7f2e649a7ed8e282a9bdc944
fetched_at: '2026-06-29T00:11:27.721824+00:00'
page_id: '729232452'
product: rm
source: tdn-rm
title: Guia de Boas Práticas com .NET MAUI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=729232452
version: 10
---

Visão Geral

Os aplicativos corporativos enfrentam uma série de problemas difíceis de resolver, incluindo requisitos de negócio em constante mudança, a necessidade de tempo de retorno rápido, suporte para várias plataformas e integração com vários sistemas. Devido à natureza variável desses problemas, é importante que a arquitetura de um aplicativo permita que ele seja modular, modificável e extensível ao longo do tempo.

Este guia fornece soluções do mundo real para lidar com esses problemas ao criar um aplicativo corporativo com .NET MAUI. O guia utiliza um aplicativo .NET MAUI, previamente migrado do Xamarin.Forms, que serve como referência e guia para padrões de design corporativo. Este guia aborda tópicos como o padrão MVVM, injeção de dependência, navegação, validação, baixo acoplamento de componentes e outras preocupações corporativas. 

Independentemente da plataforma, os desenvolvedores de aplicativos corporativos enfrentam vários desafios:

* Requisitos do aplicativo que podem mudar com o tempo.
* Novas oportunidades e desafios de negócio.
* Comentários contínuos durante o desenvolvimento que podem afetar significativamente o escopo e os requisitos do aplicativo.

Com isso em mente, é importante criar aplicativos que possam ser facilmente modificados ou estendidos ao longo do tempo. Projetar para tal adaptabilidade pode ser difícil, pois requer uma arquitetura que permita que partes individuais do aplicativo sejam desenvolvidas de forma independente e testadas isoladamente sem afetar o restante do aplicativo.

A abordagem tradicional para projetar e construir um aplicativo resulta no que é chamado de aplicativo *monolítico*, em que os componentes são fortemente acoplados sem uma separação clara entre eles. Normalmente, essa abordagem monolítica leva a aplicativos difíceis e ineficientes de manter, pois pode ser difícil resolver bugs sem quebrar outros componentes do aplicativo e pode ser difícil adicionar novos recursos ou substituir recursos existentes.

Uma solução eficaz para esses desafios é particionar um aplicativo em componentes discretos e fracamente acoplados que podem ser facilmente integrados em um aplicativo. Essa abordagem oferece vários benefícios:

* Ela permite que funcionalidades individuais sejam desenvolvidas, testadas, estendidas e mantidas por diferentes indivíduos ou equipes.
* Ela promove a reutilização e uma clara separação de preocupações entre os recursos horizontais do aplicativo, como autenticação e acesso a dados, e os recursos verticais, como a funcionalidade de negócio específica do aplicativo. Isso permite que as dependências e interações entre os componentes do aplicativo sejam gerenciadas com mais facilidade.
* Ela ajuda a manter uma separação de funções, permitindo que diferentes indivíduos ou equipes se concentrem em uma tarefa ou funcionalidade específica de acordo com sua experiência. Em particular, ela fornece uma separação mais clara entre a interface do usuário e a lógica de negócio do aplicativo.

Segue abaixo alguns itens que merecem atenção e auxiliam na componentização do aplicativo:

Dica

Os itens abaixo foram aplicados ao projeto [MinhaQualidadeMaui](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui) e cada item possui uma **branch** com suas respectivas implementações.

Seria interessante fazer um comparativo entre elas para acompanhar a evolução do projeto e as alterações que foram necessárias.

[Comparando Branches no Visual Studio 2022](https://learn.microsoft.com/en-us/visualstudio/version-control/git-browse-repository?view=vs-2022#compare-branches)

h3title
