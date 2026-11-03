---
content_hash: 1d4b349b47b7c5cc8dcd6f815996aaee3064ad8c85724455031167fadb6d1519
fetched_at: '2026-06-29T00:11:28.541130+00:00'
page_id: '731902985'
product: rm
source: tdn-rm
title: 1 - Configurando o Projeto para Testes
type: documentation
url: https://tdn.totvs.com/display/LRM/1+-+Configurando+o+Projeto+para+Testes
version: 6
---

Branch de Referência

Compare unit\_test\_config com initial

Projeto de Teste

Crie um novo projeto na mesma solução do aplicativo .NET MAUI. Isso pode ser feito clicando com o botão direito do mouse na solução. 

Vá para **Add** > **New Project**. Na caixa de diálogo, selecione **"xUnit Test Project"** e clique em **Next**.

Nomeie o projeto de teste e clique em **Next**.

Selecione o Framework e clique em **Create**.

O Framework deve corresponder ao projeto .NET MAUI.

Depois que o projeto é criado, ele terá uma classe padrão **UnitTest1**.

c#RDarkC#

Ao compilar e executar o projeto de teste, ele deve passar, pois nenhuma validação foi implementada.

Este procedimento pode ser feito clicando com o botão direito do mouse no projeto de teste e selecionando **"Run Tests"**.

Adicionando Referência

Agora, devemos adicionar uma referência ao projeto .NET MAUI que precisa de teste.

No projeto de teste, vá para **Dependencies**. Clique com o botão direito do mouse e selecione **Add Project Reference**.

Marque o check e clique em **OK**.

Ao acessar o arquivo de projeto do .NET MAUI (também conhecido como .csproj), aparecerá os Frameworks de destino:

xmlRDarkXMLnet6.0-android;net6.0-ios]]>

E assim no projeto de teste:

xmlRDarkXMLnet6.0]]>

Ao tentar compilar dessa forma o Visual Studio exibirá uma mensagem de erro, pois o projeto .NET MAUI e os Frameworks de destino do projeto de teste não estão alinhadas.

Para solucionar esse problema abra o arquivo .csproj do projeto .NET MAUI e adicione o **net6.0** como destino.

xmlRDarkXMLnet6.0;net6.0-android;net6.0-ios]]>

Também será necessário uma condição para setar o tipo de saída como **Exe** sempre que o Framework de destino for diferente de **net6.0**.

xmlRDarkXMLExe]]>

Recarregue o projeto .NET MAUI. Também pode ser necessário reiniciar o Visual Studio. Com tudo configurado corretamente, o projeto de teste estará apto para executar sem problemas.
