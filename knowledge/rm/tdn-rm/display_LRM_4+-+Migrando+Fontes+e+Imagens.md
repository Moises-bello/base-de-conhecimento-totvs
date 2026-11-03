---
content_hash: bcbcc123613794812913352bf8f4d388174864c4fc00a00ee98de5c23212d6fb
fetched_at: '2026-06-29T00:11:25.633650+00:00'
page_id: '714225247'
product: rm
source: tdn-rm
title: 4 - Migrando Fontes e Imagens
type: documentation
url: https://tdn.totvs.com/display/LRM/4+-+Migrando+Fontes+e+Imagens
version: 3
---

Arquivos de Fonte

O registro de fontes foi simplificado no .NET MAUI.

* Copie as fontes do aplicativo existente em Xamarin.Forms para a pasta **`Resources\Fonts`** em seu projeto MAUI.

* Certifique-se de que a propriedade "Build Action" esteja definida como **MauiFont:**

* Atualize o arquivo `MauiProgram.cs` para incluir as fontes migradas:

  c#RDarkCódigo()
  .ConfigureEffects(
  effects =>
  {
  })
  .ConfigureFonts(fonts =>
  {
  fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
  fonts.AddFont("OpenSans-Semibold.ttf", "OpenSansSemibold");
  fonts.AddFont("NunitoSans-Bold.ttf", "NunitoSansBold");
  fonts.AddFont("NunitoSans-ExtraLight.ttf", "NunitoSansExtraLight");
  fonts.AddFont("NunitoSans-Regular.ttf", "NunitoSansRegular");
  fonts.AddFont("Nunito-SemiBold.ttf", "NunitoSemiBold");
  })
  .UseMauiCommunityToolkit();
  return builder.Build();
  }
  }]]>
Imagens, Ícones e Splash

* Copie os arquivos existentes do Xamarin.Forms para as pastas em seu projeto MAUI: 
  + **`Resources\AppIcon`**
  + **`Resources\Images`**
  + **`Resources\Splash`**

Dê preferência para imagens SVG para um melhor desempenho.

No MAUI esse recurso é nativo. Não há necessidade de biblioteca terceira.

* Certifique-se de que a propriedade "Build Action" esteja definida de acordo com o seu tipo de arquivo: **MauiIcon,** **MauiImage, MauiSplash** e etc.
