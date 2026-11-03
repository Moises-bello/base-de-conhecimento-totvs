---
content_hash: 79830518154d22e046019f17061935af0e9f6f49671d528a153b442c4600357e
fetched_at: '2026-06-29T00:11:26.662949+00:00'
page_id: '71925932'
product: rm
source: tdn-rm
title: Limitar Visibilidade de ícones no Portal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=71925932
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Gestão de conteudos                         **Versão:**11.50 |
| **Processo** | **:** | Acesso ao portal WEB |
| **Subprocesso** | **:** | Limitar Visibilidade de ícones no Portal |
| **Data da publicação** | **:** | 03/07/2013 |

**Introdução**

Este processo possibilitará abrir um aplicativo no portal sem a necessidade de executar o mesmo após a realização do Login.

**Desenvolvimento/Procedimento**

**1.1.** **Edição do arquivo Menu.XML**

No diretório: **C:\totvs\CorporeRM\Corpore.Net** localize o arquivo Menu.xml

Para este exemplo será utilizado o aplicativo Educacional.

- Edite o arquivo Menu.xml e localize a **TAG:**

<MenuItem>

      <ID>MainEducacional</ID>

      <Caption>Educacional</Caption>

**Selecione esta TAG até ao final da mesma que é:**

          <ActionID>EduAcessoPortalEducActionWeb?OpenPopUp:false</ActionID>

        </MenuItem>

      </MenuItem>

    </MenuItem>

**Esta TAG deverá ser copiada para o início do arquivo ente:**

<Menu>

  <MenuItem>

    <ID>Inicio</ID>

    <Caption>Início</Caption>

    <ImageURL>images/mn\_Inicio.gif</ImageURL>

**\*\*\*\*\*\*\*\*\*\*\*  COPIAR A TAG NESTE ESPAÇO \*\*\*\*\*\*\*\*\*\*\*\*\*\***

<MenuItem>

      <ID>MainPortal</ID>

      <Caption> Portal </Caption>

      <Description>Gerencie os conteúdos, notícias e demais serviços do seu portal.</Description>

      <ImageURL>images/mn\_Portal.gif</ImageURL>

**Salve o arquivo aos realizar estas alterações**

**1.2** - **Edição do arquivo Web.config**

No diretório: **C:\totvs\CorporeRM\Corpore.Net** localize o arquivo **Web.config**

- Edite o arquivo (Web.config) e localize a **TAG:**

<add key="LoadDefaultMenuOnLogin" value="**true**"/>

Alterando o Value para **TRUE**

**Salve o Arquivo e restart o IIS (Iniciar executar e digite IISRESET).**

Ao realizar acesso ao Portal WEB será apresentada após Login e Senha a Abertura do aplicativo em questão. Caso seja necessário utilizar as outras opções do portal basta clicar em inicio para direcionar novamente as opções do portal Web.

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
