---
content_hash: 290dafc00920502300d65d337bb5a720c0a3113183723595f3bdf02199d8ab7b
fetched_at: '2026-06-29T00:08:54.768568+00:00'
page_id: '346491540'
product: rm
source: tdn-rm
title: Integracao com o WebService do Totvs Mashups - Integração com Recaptcha
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=346491540
version: 4
---

### Introdução

A utilização cada vez mais crescente do reCaptcha 2, serviço do Google que impossibilita que robôs sejam utilizados, para extrair dados de páginas da Web fez com que o mecanismo do TOTVS Mashup fosse aprimorado para tratar este tipo controle. Para isso foram feitas alterações no Web Service do Mashup para contemplar esta integração.

Como o mecanismo do reCaptcha 2 não pode ser tratado diretamente no servidor de Mashups, foram feitas alterações na API e nos Web Services do Mashup para permitir que o cliente do Mashup faça os devidos tratamentos necessários para a execução.

### Pré-requisitos

O reCaptcha tem um mecanismo de controle baseado na Url do site que utiliza o serviço, com uma chave da API específica para esta Url. Com está combinação é possível simular a execução do reCaptcha como se estivesse no próprio site. Para isso é necessária a utilização de um web browser embutido que permita a injeção de HTML simulando uma Url específica. Como por exemplo o CEF (Chromium Embeeded Framework)  - <https://en.wikipedia.org/wiki/Chromium_Embedded_Framework>.

### Parâmetro do Mashup (SOAData)

Foram criadas duas novas propriedades para a classe SOAData da API do Mashup. Estas propriedades quando estiverem preenchidas deverão ser utilizadas para a resolução do reCaptcha pelo cliente.

#### RecaptchaKey

Baseado no valor da propriedade RecaptchaKey, o cliente deverá gerar um HTML para executar o reCaptcha utilizando o browser embutido. Este HTML irá conter basicamente a chamada para o reCaptcha. O seguinte código pode ser utilizado como base para o HTML que será gerado, substituindo o valor [SITEKEY] pelo valor da propriedade retornado pelo Mashup.

Neste exemplo, quando o reCaptcha for resolvido a função recaptchaCallback será executada pela API do Google, devolvendo o valor da resposta do reCaptcha, que por sua vez, deverá ser devolvido como valor do parâmetro do Mashup.

xmlHTML


TOTVS Mashups Recaptcha
]]>

#### RecaptchaUrl

Esta propriedade irá conter o endereço (Url) que deverá ser simulado pelo browser no momento da carga do HTML gerado utilizando o valor do RecaptchaKey.

### Integração utilizando a biblioteca CEFSharp

A biblioteca CEFSharp permite a utilização da API do CEF na plataforma .NET. Ela possui implementações para Windows Forms, WPF e aplicação sem tela e está disponível no GitHub também como um pacote NuGet. O seguinte código cria um UserControl WindowsForms para resolução do reCaptcha em uma aplicação C#.

c#C#
/// Controle do Recaptcha
///
public partial class SOARecaptchaControl : UserControl
{
/// 
/// Componente do navegador
/// 
private ChromiumWebBrowser Browser;
/// 
/// Callback do Javascript
/// 
private RecaptchaCallback RecaptchaCallback;
/// 
/// Html base para chamar o recaptcha
/// 
private const string Html =
"
" +
"" +
"" +
" " +
" " +
" " +
" " +
" " +
" Recaptcha Test" +
" " +
" " +
"" +
"" +
"" +
"" +
"";
public SOARecaptchaControl()
{
InitializeComponent();
}
/// 
/// Chave do Recaptcha (RecaptchaKey)
/// 
public string SiteKey = "6LeP2TQUAAAAACab2AAHziJUCqPwLmBILdrjhJ54";
/// 
/// Url do Site (RecaptchaUrl)
/// 
public string SiteUrl = "https://www.receita.fazenda.gov.br/Aplicacoes/SSL/ATCTA/CPF/ConsultaSituacao/ConsultaPublica.asp";
/// 
/// Resposta do Recaptcha
/// 
public string RecaptchaResponse = null;
private static void InitializeCefSharp()
{
if (!Cef.IsInitialized)
LoadCefSharp();
}
[MethodImpl(MethodImplOptions.NoInlining)]
private static void LoadCefSharp()
{
// inicializa as configurações do chromium...
CefSettings settings = new CefSettings();
settings.BrowserSubprocessPath = Path.Combine(AppDomain.CurrentDomain.SetupInformation.ApplicationBase,
Environment.Is64BitProcess ? "x64" : "x86",
"CefSharp.BrowserSubprocess.exe");
// inicializa...
Cef.Initialize(settings, performDependencyCheck: false, browserProcessHandler: null);
// aguarda a inicialização...
while (!Cef.IsInitialized)
Application.DoEvents();
}
private void SOARecaptchaControl\_Load(object sender, EventArgs e)
{
// inicializa...
InitializeCefSharp();
// cria o browser...
this.Browser = new ChromiumWebBrowser("about:blank");
this.Browser.Dock = DockStyle.Fill;
// inicializa o callback...
this.RecaptchaCallback = new RecaptchaCallback(this.Browser);
this.RecaptchaCallback.OnSolved += new EventHandler(this.OnRecaptchaSolved);
this.Browser.RegisterJsObject("recaptchaCallbackObj", this.RecaptchaCallback);
// adiciona no UserControl...
this.Controls.Add(this.Browser);
}
private void OnRecaptchaSolved(object sender, EventArgs e)
{
// grava a resposta...
this.RecaptchaResponse = this.RecaptchaCallback.Response;
}
private void OnInitialized()
{
System.Threading.Thread.Sleep(500);
if (this.InvokeRequired)
this.Invoke(new Action(this.OnInitialized));
else
this.Browser.LoadString(Html.Replace("[SITEKEY]", this.SiteKey), this.SiteUrl);
}
}
internal class RecaptchaCallback
{
private ChromiumWebBrowser Browser = null;
public RecaptchaCallback(ChromiumWebBrowser browser)
{
this.Browser = browser;
}
/// 
/// Chave da resposta do Recaptcha
/// 
public string Response { get; private set; }
/// 
/// Evento disparado ao resolver o Recaptcha
/// 
public event EventHandler OnSolved;
public void solved(string response)
{
// guarda a resposta...
this.Response = response;
// chama o evento...
if (this.OnSolved != null)
this.OnSolved(this, EventArgs.Empty);
}
}
]]>

### Importante

O mecanismo do reCaptcha utiliza controles adicionais para verificar se realmente é uma pessoa que está utilizando. Por isso ele "facilita" a resolução do reCaptcha quando o usuário está logado em uma conta do Google. Este controle é feito através de Cookies que são repassados para o mecanismo do reCaptcha quando o Script é carregado. Para facilitar a resolução do reCaptcha, é recomendado que os Cookies sejam armazenados e que o usuário faça a autenticação no Google através da página accounts.google.com.

Para fazer o armazenamento dos Cookies no CefSharp, ao fazer a inicialização do Browser defina o valor da propriedade CachePath da classe CefSettings utilizada na inicialização para o diretório onde os dados de navegação do usuário serão armazenados.

Também é possível fazer a leitura dos Cookies da url [www.google.com](http://www.google.com), diretamente dos navegadores instalados no sistema, sugerindo que o usuário faça o login na sua conta do Google para facilitar a utilização deste recurso e "injetá-los" na requisição do Chromium.

Exemplo de extração de Cookies: <https://www.codeproject.com/Articles/330142/Cookie-Quest-A-Quest-to-Read-Cookies-from-Four-Pop>
