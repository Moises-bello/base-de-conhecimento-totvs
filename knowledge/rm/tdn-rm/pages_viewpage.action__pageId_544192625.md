---
content_hash: f52d9e32ca79a4258bdf1d934f716e707b6fa6a3fdf8678345fc51cbe9359a8b
fetched_at: '2026-06-29T00:10:38.195333+00:00'
page_id: '544192625'
product: rm
source: tdn-rm
title: Cópia de Como Fazer - Alterando o portal FrameHTML para utilizar a porta 80
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=544192625
version: 1
---

# Introdução

Este documento tem como objetivo auxiliar o usuário na configuração do ambiente RM, para realizar a alteração do diretório FrameHTML para que seja protegida apontando para porta 80.

# Configurações de Processos de apontamento

---

- Realize a instalação “padrão” do portal;

- Acesse o diretório C:\totvs\CorporeRM\FrameHTML e copie/mova o conteúdo da mesma para a pasta **RM**;

**Antes:**

**Depois:**

- No arquivo **Web.Config** que foi movido para o diretório **FrameHTML**, comente a tag **RMRoutePrefix**:

**Antes:**

<add key="RMRoutePrefix" value="rm" />

**Depois:**

**<!--**  <add key="RMRoutePrefix" value="rm" /> **-->**

- Crie um aplicativo dentro de Default Web Site apontando para o novo diretório dos arquivos e certifique-se que o Pool de aplicativos associado esteja na versão 4.0 do Net Framework.

- Alteração no Pool de aplicativos definindo o Identity para **ApplicationPoolIdentity**, conforme imagem abaixo:

- Verifique se a extensão .svg está registrada no IIS, através do MIME Types (Tipos de MIME):

Editar o arquivo **C:\totvs\CorporeRM\FrameHTML\RM\Web\js\totvs-app.global.config.js**, ajustando os  **VAR CONS\_GLOBAL\_URL\_BASE\_APP =’/web/’** para **VAR CONS\_GLOBAL\_URL\_BASE\_APP =’/RM/web/’** e **VAR CONST\_GLOBAL\_URL\_BASE\_API='/api'** para**VAR CONST\_GLOBAL\_URL\_BASE\_API='/RM/api/'**

- Acesse o diretório **C:\totvs\CorporeRM\Corpore.Net** e edite o arquivo web.config  e altere a porta cadastrada na tag **FrameHtmlUrl**;

- Certifique-se que a URL referente ao Frame HTML esteja correta nos parâmetros globais do sistema (neste caso, sem a informação referente a porta ou com a porta 80);

- Após a realização de todos os procedimentos, execute o comando iisreset e limpe o cache do navegador.

- Realize o teste no portal Educacional acessando diretamente o IIS no caminho Servidor\Sites\Default Web Site\RM\Web\App\Edu\PortalEducacional, conforme exemplo abaixo, utilizando o botão direito do mouse e clicando em procurar:

- Para validar a parte de RH, utilize o portal Corpore.Net e clique em “Currículo” na tela de login.

---

falsefalse

**Produto:** Framework

false

**Versão:** 11.80.XX, 12.01.XX

false

**Processo:** Gerenciamento de Alias

falsefalse

**Status:** Finalizado

false

**Data:** 05/02/2018

false

**Autores:**
