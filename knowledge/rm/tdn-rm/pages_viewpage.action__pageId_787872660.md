---
content_hash: 871875e15da9e67192b89e1a92a97473cba40fb381c6734c5f85847e1b5e515c
fetched_at: '2026-06-29T00:11:39.123659+00:00'
page_id: '787872660'
product: rm
source: tdn-rm
title: Utilizando o Visual Studio para auxiliar na criação de suas Atividades C# para
  o TOTVS Automação de Testes - Linha RM
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=787872660
version: 25
---

Este documento irá ajudá-lo a usar o **Visual Studio** para criar o código da sua **Atividade C#**, aproveitando todos os seus recursos, como o compilador integrado e o **IntelliSense**, que facilita a escrita e a correção do código.

Recomendamos o uso das versões 2019 em diante do Visual Studio.

### 1 - Criando  um novo projeto:

1.1 - Abra o Visual Studio e clique em "*Criar novo projeto*".

1.2 - Selecione o template buscando por standard e clicando na opção de "*Class Library*".

1.3 - Nomeie o seu projeto à sua preferência, aqui vamos chamá-lo de "*HelpAutomacaodeTestes*"

1.4 - Selecione o Framework .NET Core 2.1 (Versão homologada)

### 2 - Importando as dependências:

2.1 - Clique com o botão direito nas Dependências do projeto e clique em "*Adicionar Referência de Projeto.*"

2.2 - Um modal irá se abrir e você deverá clicar na opção "*Browse*" ao lado dos botões "*OK*" e "*Cancel*"

2.3 - Navegue até a pasta "*Agent*" do TOTVS Automação de Testes e selecione os arquivos .dll "*TestFlow.Domain*", "*TestFlow.Engine.Activities*" e "*TestFlow.Engine.Rdb*", depois clique em "*Add*"

2.4 - Pronto! Agora é possível utilizar as interfaces que disponibilizamos, como por exemplo o "*ICSharpCodeAction*" e o "*IActivityContext*":

### Usings

c#RDark

### Namespace

c#RDark

### Classe

c#RDark

### 3 - Utilizando os Templates

3.1 - Ao criar um novo código C# selecione um template:

3.2 - Copie todo o código carregado pelo Template e cole em uma nova classe do seu projeto "*TotvsAutomacao*":

3.3 - Construa seu código no Visual Studio, copie todo o código e cole-o substituindo todo o conteúdo presente no editor da ferramenta. Também faça o teste de compilação, clicando no botão "*Verificar compilação*":
