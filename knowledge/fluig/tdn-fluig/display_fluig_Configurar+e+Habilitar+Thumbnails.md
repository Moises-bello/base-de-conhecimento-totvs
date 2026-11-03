---
content_hash: 7de8bd79e061772556ad460106c48afc8d5b5e7785bf497d7372758e2abbd704
fetched_at: '2026-06-28T21:35:23.718213+00:00'
page_id: '258277602'
product: fluig
source: tdn-fluig
title: Configurar e Habilitar Thumbnails
type: documentation
url: https://tdn.totvs.com/display/fluig/Configurar+e+Habilitar+Thumbnails
version: 11
---

Atenção

Esta página é destinada para atualizações 1.6 e superiores do TOTVS Fluig Plataforma.

# Índice

2true.\*ndice; .\*4none

# Objetivo

---

O objetivo deste guia é habilitar a geração de *thumbnails* na plataforma utilizando o FFmpeg.

# Visão Geral

---

*Thumbnails* (miniaturas) são versões reduzidas de imagens ou vídeos que são apresentadas para tornar mais fácil o processo de visualização ou reconhecimento de um conteúdo.

Fique atento!

O recurso geração de *thumbnails* somente funcionará nas imagens e vídeos disponibilizados em **comunidades**.

# Configuração

---

A configuração de geração de *thumbnail* é necessária **apenas** para as atualizações **1.6.5** e **inferiores**. A partir da atualização 1.7.0 Lake apenas o item [Habilitando *thumbnails*](https://tdn.totvs.com/display/public/fluig/Configurar+e+Habilitar+Thumbnails#ConfigurareHabilitarThumbnails-HabilitandoThumbnails) é necessário.

A plataforma gera *thumbnails* de alguns tipos de imagens e vídeos na exibição de documentos e galerias. Para configurar a geração de *thumbnails* siga o passo a passo a seguir:

0.5falsethumbnail-configfade1Passo 1

* É necessário que o FFmpeg esteja instalado no servidor para que a plataforma consiga gerar *thumbnails*.

* O FFmpeg pode ser obtido no [site oficial](http://ffmpeg.org/) do projeto, em versões [Linux](http://ffmpeg.org/download.html#build-linux) e [Windows](http://ffmpeg.zeranoe.com/builds/).

* Existem três tipos de builds diferentes do FFmpeg. A plataforma utiliza a *build* de tipo ***Shared***, com DLLs separadas por biblioteca para uso externo, sendo esta portanto que deve ser baixada.

Versão do FFmpeg

O fluig necessita da versão 2.1 *stable Shared* para gerar corretamente os *thumbnails*, compilado com as seguintes dependências:

* Yasm
* x264
* libfdk\_aac
* libmp3lame
* libopus
* libogg
* libvorbis
* libvpx
2Passo 2

* Efetue o login utilizando o usuário **wcmadmin** e então acesse **Painel de Controle  →** aba **WCM → Configurações do Sistema**.

**Acessando a configuração de *thumbnail***

3Passo 3

* Na tela de configurações do sistema, acesse a aba ***Thumbnail****.*

* No campo **Caminho para o executável do FFmpeg** informe o caminho completo para o executável do FFmpeg instalado anteriormente, seguindo o seguinte modelo:
  + Servidor Linux: [Diretório FFmepeg]/bin/ffmpeg
  + Servidor Windows: [Diretório FFmepeg]/bin/ffmpeg.exe

**Configuração de *thumbnail***

* Clique no botão **Salvar** para aplicar as alterações e concluir a configuração.

# Habilitando *Thumbnails*

---

A geração de *thumbnails* deve ser habilitada por empresa. Para habilitar a geração de *thumbnails* para uma determinada empresa siga o passo a passo abaixo:

0.5falseenable-thumbnail-tenantfade1Passo 1

* Efetue o login utilizando o usuário **wcmadmin**, e então acesse **Painel de Controle  →** aba **WCM → Empresas**.

**Acessando o cadastro de empresas**

2Passo 2

* Selecione a empresa que deseja habilitar a geração de *thumbnail* e clique no *link* **Editar**.

**Selecionando empresa para habilitar *thumbnail***

3Passo 3

* A tela de edição de empresa será apresentada. Assinale a opção **Habilitar geração de *thumbnails*.**

**Habilitando a geração de *thumbnails***

* Clique no botão **Salvar** para salvar as alterações e habilitar a geração de *thumbnail* para esta empresa.
