---
content_hash: 5c3e578cc2762bf1c6312a41acfe6217e5bca1cbd3fa2db85ccbea8b59ae3dcc
fetched_at: '2026-06-28T21:35:20.038563+00:00'
page_id: '232816834'
product: fluig
source: tdn-fluig
title: Personalização de todas as páginas da plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=232816834
version: 28
---

#e8f6f0#e8f6f0
.lms \* {
-webkit-box-sizing: border-box;
-moz-box-sizing: border-box;
box-sizing: border-box;
}
.lms-text-center {
text-align: center;
}
.lms-full-height {
height: 100%;
}
/\* Component LMS Callout \*/
.lms-callout {
border: none;
padding: 0px;
display: -moz-box;
-moz-flex-flow: row wrap;
-moz-justify-content: center;
-moz-align-items: center;
display: -ms-flexbox;
-ms-flex-flow: row wrap;
-ms-justify-content: center;
-ms-align-items: center;
display: -webkit-flex;
display: -webkit-box;
-webkit-flex-flow: row wrap;
-webkit-justify-content: center;
-webkit-align-items: center;
display: flex;
flex-flow: row wrap;
justify-content: center;
align-items: center;
}
.lms-callout .lms-callout-image {
width: 24px;
}
.lms-callout .lms-callout-body {
width: calc(100% - 24px);
padding-left: 20px;
}
.lms-callout .lms-callout-citacao {
border: 0px solid;
border-left-width: 3px;
border-left-color: #f36f21;
margin: 4px;
margin-left: 25px;
padding-left: 8px;
font-size: 13px;
}
.lms-callout .lms-callout-thumb {
width: 24px;
height: 24px;
}
.lms-callout .lms-callout-text {
color: #58595b;
line-height: 1.75;
margin: 0;
}

![](http://tdn.totvs.com/download/thumbnails/286221066/pratica.png)

**COLOQUE EM PRÁTICA!**  
Essa página contém as instruções principais e exemplos de implementação, servindo como ponto de partida para seu desenvolvimento. Os exemplos devem ser analisados e adaptados para cada cenário e necessidade específica, lembrando que as implementações realizadas são de responsabilidade do cliente e não possuem suporte do time TOTVS Fluig.

]]>Plataforma em Cloud

Clientes cloud precisam entrar em contato com o time de Cloud com os arquivos já configurados para que seja incluído no diretório do servidor.

# trueÍndicenone Objetivo

---

Este guia tem por objetivo indicar como é feita a personalização de páginas do TOTVS Fluig Plataforma.

# Personalização de todas as páginas

---

Para personalizar todas as páginas da plataforma siga os passos a seguir:

false0.5falsePersonalizacao Loginfadetrue1Passo 1  

* Procure pela pasta **[diretório\_instalação]/repository/wcmdir.** Dentro dela, crie uma nova pasta chamada **custompage**.

falseAtenção

Caso as configurações da plataforma tenham sido alteradas manualmente (por exemplo, para ambientes com alta disponibilidade), abra em um editor de texto o arquivo **[diretório\_instalação]/appserver/domain/configuration/standalone.xml** e procure nele pela propriedade **<simple name="java:global/wcm/globalDataDir"**, neste parâmetro estará indicado o caminho alternativo ao caminho **[diretório\_instalação]/repository/wcmdir/.**

2Passo 2  

* Os arquivos criados devem utilizar a codificação (*charset*) UTF-8.

* Dentro da pasta **custompage**, crie um arquivo chamado **custompagehead.ftl.** Nesse arquivo crie o fragmento de conteúdo HTML que será inserido nas páginas.

  Atenção

  O conteúdo do arquivo **custompagehead.ftl** será literalmente inserido imediatamente antes de fechar a tag </head>. O mesmo se aplica ao **custompagehead<codigo-do-tenante>.ftl**, porém nesse caso, o mesmo apenas será inserido para o tenant em questão

* Opcionalmente, crie na mesma pasta um arquivo chamado **custompage.ftl**. Nesse arquivo crie o fragmento de conteúdo HTML que será inserido nas páginas.

  Atenção

  O conteúdo do arquivo **custompage.ftl** será literalmente inserido imediatamente antes de fechar a tag **</body>**. O mesmo se aplica ao **custompage****<codigo-do-tenante>.ftl**, porém nesse caso, o mesmo apenas será inserido para o tenant em questão.

**Ilustração:**

# Exemplo simples de personalização

---

**1.** Após a etapa de criação dos arquivos, importe o código abaixo para dentro do arquivo **custompagehead.ftl**:

xmlEclipse1custompagehead.ftltrue
.menu-item a, .wcm-menu-item a {
color: cyan !important;
}
]]>

**Resultado:**

---

A cor dos itens no menu lateral irão mudar para ciano nos temas **R****esponsivo** e **S****nowflake**, já no tema **C****lássico** irá mudar apenas o label do item, conforme apresentado nas imagens abaixo:

# Exemplo avançado de personalização

---

**1.** Após a etapa de criação dos arquivos, importe o código abaixo para dentro do arquivo **custompage.ftl**:

xmlEclipse1custompage.ftltrue
<#assign fluigThemeCode = themeCode>
<#else>
<#assign fluigThemeCode = "themedefault">

**Atenção!**
amanhã o Fluig estará fora do ar para atualização

]]>

**Resultado:**

---

Será apresentado um componente de alerta fixado acima do header principal em todas as páginas dos temas **Responsivo**, **Snowflake** e **Clássico**, conforme nas imagens abaixo:
