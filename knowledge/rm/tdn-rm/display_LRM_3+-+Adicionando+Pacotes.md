---
content_hash: 83e523cf5ebeb09533e1bb03e00b877be0eb40f91253b7dba46a8fadfda65254
fetched_at: '2026-06-29T00:11:25.629329+00:00'
page_id: '714225214'
product: rm
source: tdn-rm
title: 3 - Adicionando Pacotes
type: documentation
url: https://tdn.totvs.com/display/LRM/3+-+Adicionando+Pacotes
version: 3
---

Pacote do SQLite

* Adicione o pacote **`sqlite-net-pcl`** e suas dependências:

* Lista de pacotes após inseridos:

  xmlRDarkCódigo



  ]]>

* No iOS é necessário definir o provedor do SQLite no arquivo **`AppDelegate.cs:`**

  c#RDarkCódigo
Pacote do Firebase

* Adicione o pacote Plugin.Firebase ( >= 1.2.0) no nuget. Depois os arquivos `GoogleService-Info.plist` e **`google-services.json`** à pasta raiz do projeto e inclua-os no arquivo .csproj dessa forma:

  xmlRDarkCódigo



  ]]>

* Coloque a chamada de inicialização no arquivo `MauiProgram.cs (linha 15)`:

  c#RDarkCódigotrue()
  ...
  .RegisterFirebaseServices()
  .Build();
  }
  private static MauiAppBuilder RegisterFirebaseServices(this MauiAppBuilder builder)
  {
  builder.ConfigureLifecycleEvents(events => {
  #if IOS
  events.AddiOS(iOS => iOS.FinishedLaunching((app, launchOptions) => {
  CrossFirebase.Initialize(app, launchOptions, CreateCrossFirebaseSettings());
  return false;
  }));
  #else
  events.AddAndroid(android => android.OnCreate((activity, state) =>
  CrossFirebase.Initialize(activity, state, CreateCrossFirebaseSettings())));
  #endif
  });
  builder.Services.AddSingleton(\_ => CrossFirebaseAuth.Current);
  return builder;
  }
  private static CrossFirebaseSettings CreateCrossFirebaseSettings()
  {
  return new CrossFirebaseSettings(isAuthEnabled: true);
  }
  }]]>

* Adicione o seguinte `ItemGroup` ao arquivo `.csproj` para evitar erros de compilação:

  xmlRDarkCódigo


  ]]>
