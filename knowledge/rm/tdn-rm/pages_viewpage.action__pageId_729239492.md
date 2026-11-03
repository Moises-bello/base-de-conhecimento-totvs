---
content_hash: 0300670479230a6db657e9874456864137a428f8e5c7c24a08575d821b194828
fetched_at: '2026-06-29T00:11:27.738656+00:00'
page_id: '729239492'
product: rm
source: tdn-rm
title: 3 - Injeção de Dependência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=729239492
version: 7
---

Branch de Referência

Compare dependency\_injection com unit\_test\_config

Introdução

A injeção de dependência é uma versão especializada do padrão Inversão de Controle (IoC), onde a preocupação que está sendo invertida é o processo de obtenção da dependência necessária. Com a injeção de dependência, outra classe é responsável por injetar dependências em um objeto em tempo de execução. O exemplo de código a seguir mostra como a classe **LoginViewModel** é estruturada ao usar injeção de dependência:

c#RDarkC# \_webApiService;
private IConfigService \_configService;
private INavigationService \_navigationService;
public LoginViewModel(IWebApiService webApiService,
IConfigService configService, IUserLoginService userLoginService, INavigationService navigationService)
: base(configService, userLoginService)
{
\_webApiService = webApiService;
\_configService = configService;
\_navigationService = navigationService;
var config = \_configService.GetConfig();
NomeAplicativo = config.AppName;
if (config.UltimoUsuario != null && config.UltimoUsuario.savePassword && App.loginAutomatico)
{
App.loginAutomatico = false;
this.LoginCommand.Execute(null);
}
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui/ViewModels/LoginViewModel.cs)

O construtor LoginViewModel recebe várias instâncias de objeto de interface como argumentos injetados por outra classe. A única dependência na classe LoginViewModel está nos tipos de interface. Portanto, a classe LoginViewModel não tem conhecimento da classe responsável por instanciar os objetos da interface. A classe responsável por instanciar os objetos de interface e inseri-los na classe LoginViewModel é conhecida como contêiner de injeção de dependência.

Contêiner

Os contêineres de injeção de dependência reduzem o acoplamento entre objetos, fornecendo um recurso para criar instâncias de classes e gerenciar seu tempo de vida com base na configuração do contêiner. Durante a criação do objeto, o contêiner injeta nele quaisquer dependências que o objeto requer. Se essas dependências ainda não foram criadas, o contêiner cria e resolve suas dependências primeiro. Há várias vantagens em usar um contêiner de injeção de dependência:

* Um contêiner elimina a necessidade de uma classe localizar suas dependências e gerenciar seus tempos de vida.
* Um container permite o mapeamento de dependências implementadas sem afetar a classe.
* Um contêiner facilita a testabilidade ao permitir que as dependências sejam simuladas.
* Um contêiner aumenta a capacidade de manutenção ao permitir que novas classes sejam facilmente adicionadas ao aplicativo.

O método **RegisterAppServices** recebe uma instância de **MauiAppBuilder**, e podemos usar a propriedade **Services** para registrar nossos serviços, Views e ViewModels. 

c#RDarkC#, WebApiService>();
builder.Services.AddTransient();
builder.Services.AddTransient();
builder.Services.AddTransient();
#if ANDROID
builder.Services.AddSingleton();
builder.Services.AddSingleton();
#endif
return builder;
}]]>

[Clique para acessar o arquivo](https://totvstfs.visualstudio.com/Construcao-e-Projetos/_git/app-minha-qualidade-maui?path=/MinhaQualidadeMaui/MauiProgram.cs)

Dependendo das necessidades do seu aplicativo, pode ser necessário adicionar serviços com tempos de vida diferentes. A tabela a seguir fornece informações sobre esses diferentes tempos de registro:

| Método | Descrição |
| --- | --- |
| `AddSingleton<T>` | Cria uma única instância do objeto que permanecerá durante o tempo de vida do aplicativo. |
| `AddTransient<T>` | Cria uma nova instância do objeto quando solicitado durante a resolução. Os objetos transitórios não têm um tempo de vida predefinido, mas normalmente seguirão o tempo de vida de seu host. |

Dica

Os contêineres de injeção de dependência nem sempre são adequados. A injeção de dependência apresenta complexidade e requisitos adicionais que podem não ser apropriados ou úteis para aplicativos pequenos. Se uma classe não tiver dependências ou não for uma dependência de outros tipos, pode não fazer sentido colocá-la no contêiner. Além disso, se uma classe tiver um único conjunto de dependências que são parte integrante do tipo e nunca serão alteradas, pode não fazer sentido colocá-la no contêiner.
