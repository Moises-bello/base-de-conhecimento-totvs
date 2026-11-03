---
content_hash: b394112768e39eaac2d85b587194817b35eda506caa8962af183d78d82458ed1
fetched_at: '2026-06-29T00:11:53.689551+00:00'
page_id: '849571236'
product: rm
source: tdn-rm
title: Telas/Páginas Web na MDI
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=849571236
version: 21
---

# Introdução

---

Com a modernização do RM, será muito comum encontrar telas/páginas **Web** sendo abertas de dentro da **MDI.**

Com o intuito de padronizar a experiencia do usuário utilizamos o [PO-UI](https://po-ui.io/) como biblioteca de componentes.

# Provedor dos serviços Web

---

Através de um serviço na camada **Server**(**Host**) da aplicação RM, o Host consegue servir páginas de aplicativos Web.

O Serviço expõe os aplicativos Web através da porta HTTP representada pela configuração  **[HttpPort](https://tdn.totvs.com/pages/releaseview.action;jsessionid=87D76DB5F0812885AF843D0B4D3E9D6C?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-HttpPort)** no arquivo de configuração do **Server(Host)**.

Para expor uma aplicação, basta adicionar o aplicativo previamente publicado na pasta **wwwroot** que encontra-se no ambiente server instalado.

Como por exemplo a aplicação RM-Globais que está localizada em C:\TOTVS\RM.NET\**wwwroot**\rm-globais.

Levando em conta que a tag **[HttpPort](https://tdn.totvs.com/pages/releaseview.action;jsessionid=87D76DB5F0812885AF843D0B4D3E9D6C?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-HttpPort)** esteja configurado com a porta 8051 Este serviço Web estaria exposto em <http://localhost:8051/rm-globais> 

# Actions Web

---

Chamamos de **Actions Web** os menu´s do sistema que utilizam funcionalidades de páginas Web.

Ao abrir uma action web **de dentro da** **MDI** o sistema monta as URLs de serviço dos aplicativos **(Front-End)** e consumo de dados **(Back-End)** baseado em algumas configurações da camada **Server(Host)**.

Atenção

O Serviço do **Front-End** será exposto na porta configurada na tag  **[HttpPort](https://tdn.totvs.com/pages/releaseview.action;jsessionid=87D76DB5F0812885AF843D0B4D3E9D6C?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-HttpPort) (8051 Default)** no arquivo de configuração do **Server**(**Host**).

**Geralmente** o serviços de **Back-End** que **atende as páginas** estão expostos na porta configurada na tag  **[ApiPort](https://tdn.totvs.com/pages/viewpage.action?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-ApiPort)** no arquivo de configuração do **Server(Host)**, caso a tag não esteja configurada, será utilizada a tag **[HttpPort](https://tdn.totvs.com/pages/releaseview.action;jsessionid=87D76DB5F0812885AF843D0B4D3E9D6C?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-HttpPort)** .

**Quem define quais Api´s serão utilizadas como Back-End são as equipes responsáveis por cada Action!**

Autenticação

Caso as actions web utilizem as Api´s  nativa do RM e necessite de autenticação, internamente é gerado um **Token** com o usuário autenticado e este **Token** é utilizado na autenticação das Api´s.

# Configurações

---

As configurações do sistema depende de como o ambiente será distribuído/utilizado.

A  [Tenantização](https://tdn.totvs.com/x/XYu9Mg) do RM é realizada a partir do **Alias de banco de dados** cadastrados **em conjunto com a tag [SubDomainMask](https://tdn.totvs.com/pages/releaseview.action;jsessionid=87D76DB5F0812885AF843D0B4D3E9D6C?pageId=126192093#Par%C3%A2metrosdosArquivosdeConfigura%C3%A7%C3%A3o(*.config)-SubdomainMask),** para mais informações acesse a documentação <https://tdn.totvs.com/x/XYu9Mg>**.**
