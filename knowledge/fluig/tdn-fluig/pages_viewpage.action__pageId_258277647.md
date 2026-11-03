---
content_hash: cc5c1e0291f4e69d0d6b17a64b45f5fe9da0878dceaf89a9c1d49dca8fb8d5b4
fetched_at: '2026-06-28T21:35:23.745592+00:00'
page_id: '258277647'
product: fluig
source: tdn-fluig
title: Personalização da página de login no tema Clássico
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=258277647
version: 24
---

Atenção

Esta página é destinada para atualizações 1.6.0 até 1.6.4 do TOTVS Fluig Plataforma.

Plataforma em Cloud

Clientes cloud precisam entrar em contato com o time de Cloud com os arquivos já configurados para que seja incluído no diretório do servidor.

# Índice

true.\*ndicenone

# Página de login personalizada

---

Todos os componentes da página de login podem ser personalizados, basta que sejam alterados os arquivos indicados nesta documentação. As personalizações exigem que o responsável tenha os conhecimentos básicos em HTML, JavaScript e CSS.

Atenção!

Essa página contém as principais instruções de como efetuar a personalização, servindo como ponto de partida para seu desenvolvimento. Lembrando que qualquer personalização realizada na plataforma é de responsabilidade do cliente e não possui suporte do time TOTVS Fluig.

## Passos para personalização

---

Para personalizar a página de login siga os passos abaixo:

false0.5falsePersonalizacao Loginfadetrue1Passo 1

* Acesse o diretório **[diretório\_instalação]/repository/wcmdir/**. Dentro dele, crie uma nova pasta chamada **customlogin**.

Atenção

Caso as configurações da plataforma tenham sido alteradas manualmente (por exemplo, para ambientes com alta disponibilidade), abra em um editor de texto o arquivo **[diretório\_instalação]/appserver/domain/configuration/domain.xml** e localize nele a propriedade abaixo:

]]>

Neste parâmetro estará informado o caminho alternativo do diretório [diretório\_instalação]/repository/wcmdir/.

2Passo 2  

* Dentro dessa pasta recém criada, crie um arquivo chamado **login.html.** Nesse arquivo crie o fragmento de conteúdo HTML que será inserido na página de login. O conteúdo do arquivo **login.html** será literalmente inserido dentro do HTML final da página de login, dentro de uma tag **<DIV>**, substituindo a logomarca. Portanto, não poderá conter as tags **<HTML>**, **<BODY>** ou **<HEAD>**.

* Opcionalmente, crie na mesma pasta um arquivo chamado **loginhead.html**. Nesse arquivo crie o conteúdo HTML que importa os **CSS** que serão utilizados pela personalização. O conteúdo do arquivo **loginhead.html** será literalmente inserido dentro do HTML final da página de login, dentro da tag **<HEAD>**, portanto deverá conter apenas tags que importam recursos como **CSS**.

* Opcionalmente, crie na mesma pasta um arquivo chamado **loginscript.html**. Nesse arquivo crie o conteúdo HTML que importa os **JS** que serão utilizados pela personalização. O conteúdo do arquivo **loginscript****.html** será literalmente inserido dentro do HTML final da página de login, ao final da tag **<BODY>**, portanto deverá conter apenas tags que importam recursos como **JS**.

A configuração com o arquivo **loginscript.html** foi adicionada na atualização **1.7.0-210504**. Caso esteja uma atualização anterior, como paliativo o JS pode ser importado no arquivo ****loginhead.html****, no entanto podem ocorrer inconsistências no login via mobile (aplicativo My Fluig).

* Caso utilize recursos estáticos, copie-os dentro desta mesma pasta, como arquivos JS, CSS e imagens. Esses recursos estáticos estarão acessíveis abaixo da URL **/portal/resources/customlogin/**.
3Passo 3 - Mobile

* Caso utilize o aplicativo Mobile, a personalização do login via Mobile pode ser feita da mesma forma. Basta criar os arquivos **mlogin.html, mloginscript.html** e **mloginhead.html**.

4Passo 4

* Reinicie os serviços do fluig.

Sempre que houver o login personalizado na empresa, ao acessar a plataforma pelo navegador do dispositivo mobile, esta página de login será respeitada e será apresentada no momento de realizar a autenticação.

## Exemplo de personalização

---

Primeiramente foram criados os arquivos descritos acima em "[diretório\_instalação]/repository/wcmdir/customlogin/". Em seguida foram executados os seguintes procedimentos:

**1.**Importe o arquivo CSS customizado **login.css**.

xmlEclipse1loginhead.htmltrue]]>

**2.** Insira a imagem **Sua-Empresa-Horizontal.png**, juntamente com o texto "**logotxt**". Ex: 

xmlEclipse1login.htmltrue

# 

]]>

**3**. Importe o arquivo JavaScript customizado **login.js**.

xmlEclipse1loginscript.htmltrue]]>Fique atento

Todo conteúdo HTML deve seguir as normas do Style Guide (definidas aqui: <https://style.fluig.com/>).

**4.** Ao terminar de carregar a página, substitua o texto "**logotxt**" pela data atual.

jsEclipse1login.jstrue

**5.**Deixe o **"logotxt"**em negrito.

cssEclipse1login.csstrue

**6.** Customização também para o mobile.

xmlEclipse1mloginhead.htmltrue]]>xmlEclipse1mlogin.htmltrue

# 

]]>xmlEclipse1mloginscript.htmltrue]]>

**Resultado:**

---

Alteração de logomarca e exibição de data.

Importante

* Todos os arquivos utilizados no exemplo também estão disponíveis em [http://git.fluig.com/](https://git.fluig.com/projects/SAMPLES). Para ver o exemplo vejo o arquivo [**login-personalizado**](https://git.fluig.com/projects/SAMPLES/repos/componentes/browse/login-personalizado) do repositório [Componentes](https://git.fluig.com/projects/SAMPLES/repos/componentes/browse)
* A personalização da página de login pode ser feita apenas a partir da atualização 1.5.5
