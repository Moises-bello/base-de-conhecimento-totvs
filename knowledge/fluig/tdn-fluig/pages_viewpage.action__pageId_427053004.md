---
content_hash: 5e81375fd494d144375ea70623928022bed4b97c1e7845fc32179121be087817
fetched_at: '2026-06-28T21:35:26.815118+00:00'
page_id: '427053004'
product: fluig
source: tdn-fluig
title: Personalização da página de login no tema Snowflake
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=427053004
version: 25
---

Fique atento!

Esta página é válida para atualizações **1.6.5 (Liquid)** e **superiores** do TOTVS Fluig.

Plataforma em Cloud

Clientes cloud precisam entrar em contato com o time de Cloud com os arquivos já configurados para que seja incluído no diretório do servidor.

.\*ndice

# Página de *login* personalizada

---

Todos os componentes da página de *login* podem ser personalizados, basta que sejam alterados os arquivos indicados nesta documentação. As personalizações exigem que o responsável tenha os conhecimentos básicos em HTML, JavaScript e CSS.

Importante!

Essa página contém as principais instruções de como efetuar a personalização, servindo como ponto de partida para seu desenvolvimento. Lembrando que qualquer personalização realizada na plataforma é de responsabilidade do cliente e não possui suporte do time TOTVS Fluig.

## Criação da página de *login* personalizada

---

Para personalizar a página de *login* siga os passos a seguir:

false0.5falsePersonalizacao Loginfadetrue1Passo 1

* Acesse o diretório **[Instalação fluig]/repository/wcmdir/**. Dentro dele, crie uma nova pasta chamada **customlogin**.

Importante!

Caso as configurações do Fluig tenham sido alteradas manualmente (por exemplo, para ambientes com alta disponibilidade), abra em um editor de texto o arquivo:

* **a partir da atualização 2.0:** [diretório\_instalação]/appserver/standalone/configuration/**standalone.xml**;

* **da atualização 1.6.5 até a 1.8.2**: [diretório\_instalação]/appserver/domain/configuration/**domain.xml**.

No arquivo correspondente à atualização que você utiliza, localize a propriedade abaixo:

]]>

Neste parâmetro estará informado o caminho alternativo do diretório [diretório\_instalação]/repository/wcmdir/.

2Passo 2  

* Dentro dessa pasta recém criada, crie um arquivo chamado **loginsnowflake.html.** Nesse arquivo crie o fragmento de conteúdo HTML que será inserido na página de *login*. O conteúdo do arquivo **loginsnowflake****.html** será literalmente inserido dentro do HTML final da página de *login*, dentro de uma tag **<DIV>**. Portanto, não poderá conter as tags **<HTML>**, **<BODY>** ou **<HEAD>**.

* Opcionalmente, crie na mesma pasta um arquivo chamado **loginhead.html**. Nesse arquivo crie o conteúdo HTML que importa os **CSS** que serão utilizados pela personalização. O conteúdo do arquivo **loginhead.html** será literalmente inserido dentro do HTML final da página de *login*, dentro da tag **<HEAD>**, portanto deverá conter apenas tags que importam recursos como **CSS**.

* Opcionalmente, crie na mesma pasta um arquivo chamado **loginscript.html**. Nesse arquivo crie o conteúdo HTML que importa os **JS** que serão utilizados pela personalização. O conteúdo do arquivo **loginscript****.html** será literalmente inserido dentro do HTML final da página de *login*, ao final da tag **<BODY>**, portanto deverá conter apenas tags que importam recursos como **JS**.

Importante!

A configuração com o arquivo **loginscript.html** foi adicionada na atualização**Update 1.7.0-210504**. Caso esteja uma atualização anterior, como paliativo o JS pode ser importado no arquivo ****loginhead.html****, no entanto podem ocorrer inconsistências no *login* via mobile (aplicativo My Fluig).

* Caso utilize recursos estáticos, copie-os dentro desta mesma pasta, como arquivos JS, CSS e imagens. Esses recursos estáticos estarão acessíveis abaixo da URL **/portal/resources/customlogin/**.
3Passo 3 - Mobile

* Caso utilize o aplicativo Mobile, a personalização do *login* via Mobile pode ser feita da mesma forma. Basta criar os arquivos **mlogin.html**, mloginscript.html**** e **mloginhead.html**.

4Passo 4

* Reinicie os serviços do fluig.

Dica!

Sempre que houver o *login* personalizado na empresa, ao acessar a plataforma pelo navegador do dispositivo mobile, esta página de *login* será respeitada e será apresentada no momento de realizar a autenticação.

## Exemplo de personalização

---

Primeiramente foram criados os arquivos descritos acima em "[diretório\_instalação]/repository/wcmdir/customlogin/". Em seguida foram executados os seguintes procedimentos:

**01.** Importe o arquivo JavaScript customizado **loginsnowflake.js** e o arquivo de estilo **loginsnowflake.css**.

xmlEclipse1loginhead.htmltrue]]>xmlEclipse1loginscript.htmltrue]]>

**02.** Insira aqui o código HTML de customização da sua página.

xmlEclipse1loginsnowflake.htmltrue]]>Importante!

Todo conteúdo HTML deve seguir as normas do Style Guide (definidas aqui: <https://style.fluig.com/>).

**03.** O arquivo js, ao terminar de carregar a página, insere a data atual no elemento "login\_datetime" 

jsEclipse1loginsnowflake.jstrue

**04.** O arquivo css deve conter as classes de personalização do seu HTML.

cssloginsnowflake.css

**Resultado:**

---

Exibição de data na parte inferior da tela.

Importante!

* Todos os arquivos utilizados no exemplo também estão disponíveis abaixo:
* A personalização da página de *login* com o tema Snowflake pode ser feita apenas a partir da **atualização 1.6.5 - Liquid**.
