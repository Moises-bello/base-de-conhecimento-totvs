---
content_hash: 1b54fc0432add7e85965701c602ae670163fea7f50557a375d799e5588bce2b1
fetched_at: '2026-07-02T19:24:22.552927+00:00'
page_id: '270909184'
product: protheus
source: tdn-tec
title: SmartClient - Linux packages
type: documentation
url: https://tdn.totvs.com/display/tec/SmartClient+-+Linux+packages
version: 5
---

Pacotes requeridos

A seção a seguir descreve os pacotes requeridos para o true.

INLINE

* glib2
* glibc
* libICE
* libSM
* libX11
* libXau
* libXext
* libXrender
* libuuid
* libxcb
* zlib

Para versão **20.3.2.0** ou superior pode ser necessário instalar as seguintes libs:

* libxcb-xinput0 (ubuntu 22.04)
* xcb-util-wm (red hat/oracle linux 8.0)
* xcb-util-image (red hat/oracle linux 8.0)
* xcb-util-keysyms (red hat/oracle linux 8.0)
* xcb-util-renderutil (red hat/oracle linux 8.0)
* libglvnd-opengl (red hat/oracle linux 8.0)

Em sistema operacionais 64 bits, se utilizado um true 32 bits, devem ser instalados os pacotes acima para a arquitetura correspondente - 32 bits.

 O sistema de impressão do true não é suportado em distribuições Linux rodando o servidor gráfico baseado em Wayland. Por isso é necessário utilizar o servidor gráfico baseado em X11 (Xorg).

Problema na acentuação - Framework Intelligent Input Bus (IBus)

A partir da versão **SmartClient 20.3.0.0** torna-se necessário a instalação e execução do **serviço IBus (ibus-daemon)**. Muitas distribuições Linux já incluem o ibus e o executam em background por padrão, mas caso a digitação de caracteres acentuados em qualquer campo do SmartClient apresente caracteres estranhos, verifique se o ibus daemon está operando corretamente.
