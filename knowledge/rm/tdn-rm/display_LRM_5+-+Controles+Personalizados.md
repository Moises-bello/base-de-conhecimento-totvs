---
content_hash: f6f60f44b66dc248ea140e2271d29ab3a56969cf083f00cdeefcf9e1d9f4f13d
fetched_at: '2026-06-29T00:11:25.636885+00:00'
page_id: '714225318'
product: rm
source: tdn-rm
title: 5 - Controles Personalizados
type: documentation
url: https://tdn.totvs.com/display/LRM/5+-+Controles+Personalizados
version: 3
---

O .NET MAUI **Entry** é um controle de entrada de texto, que implementa a interface **IEntry**.

No iOS, o **EntryHandler** mapeia o **Entry** para o controle nativo **UITextField**.

No Android, o **Entry** é mapeado para um **AppCompatEditText**, e no Windows o **Entry** é mapeado para um **TextBox**.

O mapeador de propriedades do **Entry**, na classe **EntryHandler**, mapeia as propriedades de controle multiplataforma para a API de visualização nativa.

Isso garante que, quando uma propriedade for definida em um **Entry**, a exibição nativa seja atualizada conforme necessário.

c#RDarkExemplo
{
#if ANDROID
handler.PlatformView.SetBackgroundColor(Colors.Transparent.ToPlatform());
#elif IOS
handler.PlatformView.BorderStyle = UIKit.UITextBorderStyle.None;
#elif WINDOWS
handler.PlatformView.FontWeight = Microsoft.UI.Text.FontWeights.Thin;
#endif
});
}]]>Reutilizando um Controle Customizado do Xamarin.Forms

* Crie um arquivo correspondente ao controle na pasta de sua plataforma:

* Altere os namesapces correspondentes e comente ou remova o assembly **ExportRenderer**:

  c#RDarkExemplo e)
  {
  base.OnElementChanged(e);
  Control?.SetBackgroundColor(global::Android.Graphics.Color.Transparent);
  }
  }
  }]]>

* Inclua o trecho de código a seguir no arquivo **MauiProgram.cs** (linhas 13-19):

  c#RDarkCódigotrue()
  .UseMauiCompatibility()
  .ConfigureMauiHandlers(handlers =>
  {
  #if ANDROID
  handlers.AddCompatibilityRenderer(typeof(RMSCustomEntry), typeof(RMSCustomEntryRenderer));
  #endif
  })
  .ConfigureEffects(effects =>
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
