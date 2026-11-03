---
content_hash: 19cd5c1fa9b0de6579ee2aa3c3f4b0768902904c0473cefcd9b438964cbc7d56
fetched_at: '2026-06-28T21:35:22.782607+00:00'
page_id: '240288988'
product: fluig
source: tdn-fluig
title: DES - Instabilidade em formulários com componentes do Style Guide
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=240288988
version: 7
---

# Índice

4true.\*ndicenone

# Plataforma

**Produto:** TOTVS Fluig Plataforma

# Ocorrência

Instabilidade em formulários que utilizam componentes do Style Guide, como zooms por exemplo.

# Causa

Nos formulários criados pelo TDS/Eclipse são adicionados por padrão os arquivos http://style.fluig.com/css/fluig-style-guide.min.css e http://style.fluig.com/js/fluig-style-guide.min.js.   
Quando existe algum bloqueio na rede ou instabilidade de conexão, o navegador pode não conseguir acessar esses arquivos através destas URLs.

# Solução

Substituir as URLs pelos caminhos dos arquivos internos do fluig: /portal/resources/style-guide/css/fluig-style-guide.min.css e /portal/resources/style-guide/js/fluig-style-guide.min.js, como o exemplo abaixo:

* <link rel="stylesheet" type="text/css" href="/portal/resources/style-guide/css/fluig-style-guide-carousel.min.css">
* <script src="/portal/resources/style-guide/js/fluig-style-guide-carousel.min.js"></script>
* <link rel="stylesheet" type="text/css" href="/portal/resources/style-guide/css/fluig-style-guide.min.css">
* <script src="/portal/resources/style-guide/js/fluig-style-guide.min.js"></script>

Caso tenha os arquivos dentro da pasta principal do projeto substituir no HTML do seu formulário por, conforme o exemplo abaixo:

* <link rel="stylesheet" type="text/css" href="fluig-style-guide.min.css">
* <link rel="stylesheet" type="text/css" href="fluig-style-guide-carousel.min.css">
* <script type="text/javascript" src="fluig-style-guide.min.js" charset="utf-8"></script>
* <script type="text/javascript" src="fluig-style-guide-carousel.min.js" charset="utf-8"></script>
