---
content_hash: 2a13a49c0b4afad61183f75fb9ca8cb68291f8964ebb99e7554745c849ee6f75
fetched_at: '2026-06-28T21:35:19.860509+00:00'
page_id: '224108112'
product: fluig
source: tdn-fluig
title: Suporte a páginas e widgets no aplicativo Fluig mobile
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=224108112
version: 38
---

# Índice

4true.\*ndicenone

# Objetivo

O objetivo deste guia é detalhar o suporte à exibição e criação de widgets do TOTVS Fluig Plataforma no aplicativo Fluig mobile.

# Widgets suportadas pelo Fluig mobile

Abaixo lista de widgets com compatibilidade para visualização no Fluig mobile:

|  |  |
| --- | --- |
|  | **Documentos Populares** |
| Veja quais são os documentos mais acessados. |
|  | **Endereço Web** |
| Acesse endereços *web* de forma fácil e rápida.  Para que o *widget* Endereço Web renderize corretamente a URL solicitada, é necessário que o servidor de destino da URL aceite requisições do tipo *cross-origin*, ou seja, requisições realizadas por páginas *web* de domínios diferentes.  Caso contrário, o seguinte erro será exibido no console do navegador: "Requisição *cross-origin* bloqueada: A política de mesma origem (*Same Origin Policy*) impede a leitura do recurso remoto em http://<URL\_USADO\_NA\_WIDGET>. (Motivo: o cabeçalho CORS '*Access-Control-Allow-Origin*' não está presente)". |
|  | **Editor de conteúdo** |
| Personalize páginas e comunidades com o conteúdo desejado. |
|  | **Analytics** |
| Visualize gráficos e *Dashboards* do Analytics de forma fácil e rápida.  Se você está utilizando o Analytics pelo iOS, atente-se às recomendações . |
|  | **Aniversariantes** |
| Visualize os aniversariantes do mês, com destaque para os aniversariantes do dia.  Esse *widget* faz parte da solução Kit Intranet e pode ser obtido através [deste *link*](https://git.fluig.com/projects/SAMPLES/repos/kit-intranet/browse/kitintranet.zip) do diretório Git do Fluig e o procedimento de instalação está disponível no [Portal do Desenvolvedor](http://tdn.totvs.com/display/fluig/Kit+Intranet#KitIntranet-Instala%C3%A7%C3%A3oeatualiza%C3%A7%C3%A3odoKitIntranet). |

# Habilitar widgets para visualização mobile

Para que uma página esteja disponível no aplicativo mobile, deve existir pelo menos uma instância de Widget habilitada para o aplicativo mobile na página. Para isso será necessário:

widgetsPasso 1

* Acessar o modo de edição da página.

Passo 2

* Assinalar quais widgets da página serão apresentadas no aplicativo mobile, clicando no ícone **Habilitar no aplicativo mobile.**

  Este ícone só estará presente para widgets que possuam suporte ao aplicativo mobile
Passo 3

* Publicar a nova versão da página.

Atenção!

A renderização das páginas no aplicativo mobile apresentará apenas o conteúdo das widgets habilitadas sequencialmente. Isso significa que serão apresentadas as widgets uma embaixo da outra, conforme a ordenação dos slots: todas as widgets do slot a, depois b, depois c e assim sucessivamente.

**Visualização dos widgets no mobile**

# Como visualizar widgets de comunidades através de dispositivos móveis

O Fluig Mobile trata os *widgets* incluídos em páginas de comunidades como **Conteúdo Adicional** da comunidade.

Para acessar esse conteúdo, basta tocar no botão **Visualizar conteúdo adicional** disponível na parte superior da *timeline* da comunidade ou na opção **Conteúdo adicional**, através do menu contextual.

Apenas as plataformas iOS e Android suportam widgets em comunidades (Conteúdo Adicional). Para obter maiores detalhes, acesse o [Guia de Utilização Fluig - Mobile](http://tdn.totvs.com/pages/viewpage.action?pageId=107940624)[.](http://tdn.totvs.com/pages/viewpage.action?pageId=107940624#GuiadeUtiliza%C3%A7%C3%A3ofluig-Mobile-Android)

analytics\_ios

# Analytics no Fluig Mobile

Para o funcionamento correto da widget de Analytics no Fluig Mobile versão iOS, devemos habilitar os *Cookies* de terceiros no dispositivo.

*Um Cookie é um arquivo de texto muito simples, cuja composição depende diretamente do conteúdo do endereço Web visitado. Por exemplo, a maioria do sites armazenam informações básica, como endereços IP e preferências sobre idiomas, cores, etc.*

Atenção

Para dispositivos IOS é **indispensável a utilização do protocolo HTTPS** para garantir o funcionamento esperado da widget Analytics. Em alguns browsers é necessária a utilização do protocolo HTTPS para que a mesma apresente o funcionamento correto.

Como habilitar cookies no iPhone ou iPad

1. e “**Privacidade e Segurança**”, garanta que as funções “**Impedir Rastreamento**” e “**Bloquear Todos os Cookies**” estejam desabilitadas.
