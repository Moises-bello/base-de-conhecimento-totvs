---
content_hash: 5c9c3403ae8d82012ce4ca448df5e1753f836f192056ee7aa15312c16b697cd1
fetched_at: '2026-06-28T21:35:23.490178+00:00'
page_id: '257622732'
product: fluig
source: tdn-fluig
title: Guia de instalação da plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=257622732
version: 43
---

.\*ndice

# Introdução

---

A mídia desenvolvida para instalar o TOTVS Fluig é muito fácil e rápida. No instalador se encontra o servidor de aplicações utilizado para executar o sistema, o Java Development Kit 11 e o servidor de indexação.

# Componentes do instalador

---

Veja a lista de componentes contidos na instalação da plataforma:

* Servidor de indexação;
* Servidor de gerenciamento de mensagens;
* Componente para visualização de documentos;
* Java;
* Servidor de aplicação.

# Pacotes de instalação

---

Existem dois pacotes de instalação disponíveis na [Central do cliente](https://suporte.totvs.com/portal/p/10098/download#000035), cada um referente a um sistema operacional específico. Para ter acesso ao portal de clientes, é necessário ser um cliente TOTVS Fluig.

| Pacote de instalação | |
| --- | --- |
| **Arquivo** | **Descrição** |
| Fluig-[release]-Win64.zip | Utilize em sistemas operacionais Windows 64 bits. |
| Fluig-[release]-Linux64.zip | Utilize em sistemas operacionais Linux 64 bits. |

Importante!

Ressaltamos que não disponibilizamos o instalador para **pacotes específicos**que não estejam disponíveis na [Central do cliente](https://suporte.totvs.com/portal/p/10098/download#000035). Sempre disponibilizamos o instalador para a última atualização disponível, que já contempla todas as correções e melhorias liberadas.

É possível acompanhar nosso calendário de atualizações em .

# Instalação ou atualização da plataforma

---

Veja a seguir as opções de instalação ou atualização da plataforma.

## Informações importantes

---

* Por questões de segurança, orientamos não expor sua plataforma diretamente à internet. Para isso, será necessário [criar uma rede DMZ](http://tdn.totvs.com/x/MZIbCQ) juntamente com o [protocolo HTTPS](http://tdn.totvs.com/x/vdMgFQ).

* Habilite o acesso ao serviço de **licenciamento** da plataforma liberando a conexão com o endereço [https://version.fluig.com](https://version.fluig.com/) (porta 443) na rede local onde a plataforma está instalada. Para verificar a disponibilidade do serviço de licenciamento, acesse o site [status.fluig.com](http://status.fluig.com).

* Em ambientes de produção não é recomendado utilizar o recurso de **varredura do antivírus** na pasta de instalação da plataforma, pois pode interferir na sua performance.

* É obrigatório executar a instalação como **administrador do sistema**.

* Em servidores Linux, é necessário conceder permissão de execução no arquivo java, no diretório jdk-64/bin e no arquivo Fluig-Installer-64.sh para iniciar a instalação.

* Caso ocorra alguma inconsistência durante a instalação, antes de fazer o *rollback*, recomendamos salvar os arquivos **server.log** – localizado em  [diretório\_instalação]\appserver\standalone\log (a partir da **2.0**) ou [diretório\_instalação]\appserver\domain\servers\fluig1\log (até a **1.8.2**) – e **install.log** – localizado em [diretório\_instalação] – e abrir um *ticket* com essas evidências, para que o time de atendimento TOTVS Fluig possa analisar.

  

## Como iniciar

---

Após verificar o pacote de instalação adequado para o servidor e descompactá-lo, é possível iniciar a instalação pelos seguintes arquivos:

* Fluig-Installer-64.exe - Para sistema operacional Windows.

* Fluig-Installer-64.sh - Para sistema operacional Linux.

Após executar o instalador, é possível optar entre instalar ou atualizar a plataforma.

A opção **Instalar** irá executar a instalação a partir do zero, criando todos os arquivos necessários. Mais detalhes sobre esse procedimento podem ser obtidos em:

* ;

* ;

Importante!

Em modo caractere, a **instalação** da plataforma pode ser realizada de forma **modularizada**. Este procedimento só pode ser executado a partir da atualização 1.6.1.

**Acesse as documentações abaixo e verifique!**

* ;

* .

A opção **Atualizar** é utilizada para atualização da plataforma por meio dos pacotes liberados no [Central do cliente](https://suporte.totvs.com/portal/p/10098/download#000035). Mais detalhes sobre esse procedimento podem ser obtidos no .

# Fluig Studio

---

Para instalar o *plugin* Fluig Studio, siga os passos descritos na página .

# Ambiente de homologação X ambiente de produção

---

O ambiente de homologação é indicado para que desenvolvimentos sobre a plataforma (criação de processos, formulários, páginas, widgets, etc.) e pacotes de atualização sejam aplicados e testados com segurança.

Isso permite que o impacto e eventuais inconsistências causadas pelos desenvolvimentos e alterações possam ser identificados e analisados pelos desenvolvedores e administradores da empresa antes da liberação no ambiente de produção.

Verifique a documentação  para informar-se sobre os procedimentos de configuração de um ambiente de homologação.

Nota:

Acompanhe, na página , as especificações mínimas obrigatórias para um servidor dedicado. Outros produtos, como o , também devem ser instalados em um servidor próprio.

Importante!

A instalação de múltiplas instâncias em um único servidor **não é homologado** **para atualizações 1.6 e superiores** do TOTVS Fluig, pois gera concorrência pelos recursos e portas do servidor entre as instâncias, provocando comportamentos inesperados. A partir desta atualização não será fornecido suporte quando identificado este cenário.

No caso específico do ambiente de homologação, o banco de dados pode estar instalado no mesmo servidor, além de possuir no mínimo 8 GB de RAM. As demais configurações de  permanecem as mesmas.
