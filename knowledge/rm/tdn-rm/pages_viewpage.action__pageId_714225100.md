---
content_hash: 6d308ab45d359c1e76977db70c77aa076722b05bb8760726d3e0d0ca56d4dab1
fetched_at: '2026-06-29T00:11:25.625235+00:00'
page_id: '714225100'
product: rm
source: tdn-rm
title: 2 - Migrando XAML e Códigos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=714225100
version: 6
---

O primeiro passo é trazer o XAML e o código-fonte do aplicativo existente no Xamarin.Forms.

Abaixo está uma lista de todos os arquivos e pastas que foram migrados.

Seria uma boa ideia adicionar o projeto MAUI a um provedor de controle de versão e verificar regularmente as alterações ao longo da migração. 

Isso facilitará a reversão para alterações anteriores ou a execução de algumas tentativas e erros.

Usando o explorador de arquivos, arraste e solte o conteúdo necessário do projeto existente para a pasta raiz do seu novo projeto MAUI. 

O conteúdo ficará semelhante à figura abaixo.

Etapas de Migração de Código do Xamarin.Forms

* Substitua as seguintes informações do Xamarin.Forms pelo equivalente em .NET MAUI:

  | **Valor Antigo** | **Valor Novo** |
  | --- | --- |
  | xmlns="<http://xamarin.com/schemas/2014/forms>" | xmlns="<http://schemas.microsoft.com/dotnet/2021/maui>" |
  | using Xamarin.Forms | using Microsoft.Maui / using Microsoft.Maui.Controls |
  | using Xamarin.Forms.Xaml | using Microsoft.Maui.Controls.Xaml |
  | Rg.Plugins.Popup | Mopups |
  | Plugin.\* | Microsoft.Maui.Devices.\* |
  | Xamarin.Forms.Device.RuntimePlatform | Microsoft.Maui.Devices.DeviceInfo.Platform |
  | Xamarin.Forms.Device.Platform | Microsoft.Maui.Devices.DevicePlatform |
  | CarouselView.FormsPlugin.Abstractions | Microsoft.Maui.Controls.CarouselView |
  | MasterDetailPage | FlayoutPage |
  | Device.BeginInvokeOnMainThread() | Dispatcher.Dispatch() |
  | Xamarin.Forms.Color | Microsoft.Maui.Graphics.Colors |
  | new Rectangle | new Rect |
  | Grid.Children.Add(view, 0, 0) | Grid.SetRow((IView)view, 0)  Grid.SetColumn((IView)view, 0) |

* Exclua ou comente o conteúdo do arquivo **`AssemblyInfo.cs`**.

As propriedades poderão ser reativadas quando o aplicativo compilar e executar sem erros.

A maioria dessas propriedades foram incorporadas como parte do novo .NET MAUI csproj, portanto, verifique quais realmente são necessárias.

* Em **`MauiProgram.cs`**, atualize o objeto **`builder`** para configurar efeitos (linha 11):

  c#RDarkCódigotrue()
  .ConfigureEffects(
  effects =>
  {
  effects.Add();
            })
  .ConfigureFonts(fonts =>
  {
  fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
  fonts.AddFont("OpenSans-Semibold.ttf", "OpenSansSemibold");
  })
  return builder.Build();
  }
  }]]>
Etapas de Migração do Xamarin Community Toolkit

* Adicione o pacote `Maui Community Toolkit` no nuget:

* Substitua as seguintes informações do Xamarin Community Toolkit pelo equivalente ao MAUI Community Toolkit: 

  | Valor Antigo | Valor Novo |
  | --- | --- |
  | `xmlns:xct="http://xamarin.com/schemas/2020/toolkit"` | `xmlns:mct="http://schemas.microsoft.com/dotnet/2022/maui/toolkit"` |
  | `xct:` | `mct:` |
  | `using Xamarin.CommunityToolkit.UI.Views;` | `using CommunityToolkit.Maui.Views;` |
  | `using Xamarin.CommunityToolkit.Extensions;` | Substituir por uma string vazia |
  | `Navigation.ShowPopup` | `this.ShowPopup` |
  | `xct:IsNullOrEmptyConverter` | `mct:IsStringNullOrEmptyConverter` |
  | `xct:ListIsNullOrEmptyConverter` | `mct:IsListNullOrEmptyConverter` |
  | `xct:ListIsNotNullOrEmptyConverter` | `mct:IsListNotNullOrEmptyConverter` |

* Em **`MauiProgram.cs`**, atualize seu construtor para usar o `Maui Community Toolkit (linha 15)`.

  c#RDarkCódigotrue()
  .ConfigureEffects(
  effects =>
  {
  })
  .UseMauiCommunityToolkit()
  .ConfigureFonts(fonts =>
  {
  fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
  fonts.AddFont("OpenSans-Semibold.ttf", "OpenSansSemibold");
  })
  return builder.Build();
  }
  }]]>
