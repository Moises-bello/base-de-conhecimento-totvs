---
content_hash: 4592fedc204b765543abfe2d111639f607ea00f44feba4756bed9ca13d53ea94
fetched_at: '2026-06-29T00:11:11.756601+00:00'
page_id: '648830208'
product: rm
source: tdn-rm
title: Debug Remoto - Visual Studio em servidores externos
type: documentation
url: https://tdn.totvs.com/display/LRM/Debug+Remoto+-+Visual+Studio+em+servidores+externos
version: 4
---

ATENÇÃO - Para debugar no cloud siga o documento:

A proposta deste documento é elucidar como configurar e debugar remotamente, ambiente TOTVS RM através do remote debug do visual studio.

* No servidor onde se encontra a instalação do TOTVS RM você deverá fazer o download e instalar a versão da Remote tools (Ferramentas remotas). De acordo com o documento da microsoft a versão mais atual é compatível com as versões anteriores do visual studio.   
  **Exemplo:** se estiver com o Visual Studio 2017 baixe e instale a ferramenta remota mais atual da versão 2017, se estiver com Visual Studio 2019 baixe e instale a ferramenta remota mais atual da versão 2017.  
  <https://docs.microsoft.com/pt-br/visualstudio/debugger/remote-debugging?view=vs-2019#download-and-install-the-remote-tools>
* A arquitetura a ser instalada da ferramenta remota deve seguir a arquitetura do servidor onde se encontra a instalação do TOTVS RM que é onde a mesma ficará em execução para debug.  
  Exemplo: Servidor 32bits ferramenta remota a ser instalada deverá ser 32 bits, ainda que o Visual Studio que será utilizado para o debug remoto esteja em uma máquina 64bits.

* Após ter instalado no servidor a ferramenta remota do visual studio deverá ser colocado o *msvsmon.exe* para ser executado, como administrador:
* Com o msvsmon.exe executando a tela deverá ficar em aberto, e para que seja possível a conexão do attach debug do visual studio ainda deverá ser configurado no menu ferramentas do aplicativo em opções a conexão anônima.

* No Visual Studio que irá ser utilizado para o debug, deverá selecionar para o campo 'Connection type: Remote (no authentication)' e para o 'Connection target: ' que deverá ser colocado o caminho do IP e porta para que seja possível o attach, geralmente deverá ser selecionado o service do host em execução após ter disparado o processo no client do RM para que o debug funcione.
