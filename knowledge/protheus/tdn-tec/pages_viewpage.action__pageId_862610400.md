---
content_hash: 84b3af647141bc231dcc5e74440fac2ffc6382a222c078a36a10285c9dd5e6a6
fetched_at: '2026-07-02T19:24:28.863273+00:00'
page_id: '862610400'
product: protheus
source: tdn-tec
title: DBAccess - Ambientes apresentam queda da aplicação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862610400
version: 1
---

Ambientes que apresentam queda da aplicação

Este documento tem o intuito de contextualizar seu leitor sobre cenários, causas e comportamentos que podem ser observados em ambientes que registraram parada abrupta da aplicação.

---

## Introdução

Na computação, é possível se deparar com a parada abrupta de uma aplicação, sistema ou programa.

Quando isto ocorre, os produtos da plataforma Totvstec estão prontos para gerar informações sobre o evento, afim de direcionar a análise e atuação dos nossos times de suporte e desenvolvimento.

Mas o que é uma parada abrupta?

Ela pode ser considerada como queda, *assert*, *access violation, throw, exception*, etc... Existem muitos nomes associados a esta ocorrência e cada um deles determina a ação que os times adotarão.

Em resumo, nada mais é do que a aplicação ser encerrada sem a intervenção do administrador do ambiente.

---

## O que pode ocasionar um *core dump*?

Existem n situações que podem acarretar em um cenário de queda e consequentemente, geração de um core dump.

Alguns exemplos:

* Falta de atualização do true: É sempre importante manter o ambiente atualizado para usufruir das ultimas correções e ajustes
* Falta de atualização da biblioteca da DBAPI: Este é o arquivo responsável pelo estabelecimento de comunicação entre o true e o true. Portanto, sempre que houver atualização true, esta biblioteca deve ser atualizada também!
* Sistema Operacional desatualizado: Sempre mantenha seu S.O atualizado para evitar que falhas do sistema impactem no funcionamento das aplicações.

---

## Como obter os *logs*?

Ambientes com S.O Microsoft Windows

Considerando a utilização da versão debug do true, após a ocorrência de queda da aplicação, será necessário coletar os logs para apoiar a análise dos times de suporte e desenvolvimento.

Para isto, sempre devem ser coletados os seguintes arquivos:

| Arquivo | Localização | Descrição |
| --- | --- | --- |
| dbaccess.ini | Diretório de instalação do true | Este arquivo contém as configurações do ambiente e é muito útil para análise destes cenários |
| dbconsole.log | Diretório de instalação do true | Este arquivo contém as mensagens registradas no console da aplicação durante o seu uso.  Ele é necessário para ter uma visão geral das operações em execução no momento da ocorrência de queda.  Vale lembrar que é sempre importante que haja o registro do Initial check-up da aplicação, que são as informações da primeira conexão entre o true e um ambiente da banco de dados, pois existem muitas informações úteis, como versão do banco de dados, versão de driver, collation utilizado, entre outros. |
| dbconsole.bak | Diretório de instalação do true | Este arquivo existirá sempre que o dbconsole.log atingir o limite de tamanho estipulado.  Ele é criado como "backup" e pode conter informações úteis para a análise. |
| coredump | Diretório de instalação do true | Este é o arquivo gerado pelo binário debug do true em cenários como os que são abordados nesse documento. |

Ambientes com S.O Linux

Considerando a utilização da versão debug do true, após a ocorrência de queda da aplicação, será necessário coletar os logs para apoiar a análise dos times de suporte e desenvolvimento.

Para isto, sempre devem ser coletados os seguintes arquivos:

| Arquivo | Localização | Descrição |
| --- | --- | --- |
| dbaccess.ini | Diretório de instalação do true | Este arquivo contém as configurações do ambiente e é muito útil para análise destes cenários |
| dbconsole.log | Diretório de instalação do true | Este arquivo contém as mensagens registradas no console da aplicação durante o seu uso.  Ele é necessário para ter uma visão geral das operações em execução no momento da ocorrência de queda.  Vale lembrar que é sempre importante que haja o registro do Initial check-up da aplicação, que são as informações da primeira conexão entre o true e um ambiente da banco de dados, pois existem muitas informações úteis, como versão do banco de dados, versão de driver, collation utilizado, entre outros. |
| dbconsole.bak | Diretório de instalação do true | Este arquivo existirá sempre que o dbconsole.log atingir o limite de tamanho estipulado.  Ele é criado como "backup" e pode conter informações úteis para a análise. |
| coredump | Diretório de instalação do true | Este é o arquivo gerado pelo binário debug do true em cenários como os que são abordados nesse documento. |

Algumas distribuições do Linux podem influenciar na geração do arquivo coredump.

Caso encontre dificuldades em localizar este arquivo, por favor, entre em contato com nosso time de suporte para avaliação.

---

## Como criar um *core dump*?

A geração de um core dump legível e com informações relevantes exige a utilização de uma versão debug dotrue.

Ao passar a utilizá-la, dada uma ocorrência de queda, deve ser gerado o arquivo em questão no mesmo path onde está seu executável!

Ainda existem alguns casos onde deseja-se obter um core dump da aplicação, mesmo não havendo queda.

Para isso, existem alguns recursos que podem nos ajudar!

Windows

#### Através do Task Manager

Para isto, devemos localizar o processo na lista de aplicações em execução e utilizar a opção **Create dump file**.

Através de aplicações de terceiros

Utilizando o **procdump**, por exemplo, é possível extrair um coredump da aplicação sempre que necessário.

Linux

#### Através do comando kill

Utilizando o comando **kill** com o sinal **-11** e o **ID** do processo é possível gerar o coredump. Lembre-se de definir o tamanho do coredump que o S.O. pode gerar como **unlimited** (*ulimit -c unlimited*). Verifique a configuração de padrão do nome do core dump (core pattern) de sua distribuição Linux.

#### Através do catchsegv

Utilizando o **catchsegv**, passando toda a linha de comando da execução do binário, é possível capturar o coredump quando ele ocorrer. Essa aplicação é útil em casos em que não é possível identificar o local de geração do coredump e/ou se está sendo gerado. Deve-se utilizar com cuidado, pois pode degradar a performance devido à monitoração. Verifique se a sua distribuição de Linux possui essa aplicação.

---

## Cenários

1 - Estou utilizando um build debug e não há core dump

Em cenários como este, os motivos mais observados são:

* Não houve uma queda (Assert, Access Violation, Throw), ou seja, o true continua no ar executando normalmente.
* O true caiu, mas por falta de espaço em disco não conseguiu gerar o arquivo de core dump.
* O true parou de ser executado, pois os serviços de monitoramento do Windows o "derrubaram". Neste caso não é gerado um core dump, pois não é efetivamente uma ocorrência de uma queda da aplicação.
* O true foi iniciado sem que previamente fossem definidos os parâmetros para geração de core dump (Linux only)
* Existem algumas distribuições de Linux que tem um serviço que monitoram queda das aplicações e acabam pegando o arquivo de dump e jogando em outro pasta; há casos ainda em que o serviço apaga o arquivo de dump.

## *Glossário*

Nesta seção, dispomos a explicação para alguns termos utilizados neste material.

Clique aqui para expandir...

| Termo | Descrição |
| --- | --- |
| *core dump* | Na computação, um *core dump* consiste no estado gravado da memória de trabalho de um programa de computador em um momento específico, geralmente quando o programa travou ou foi encerrado de forma anormal. *Fonte: [Wikipedia](https://en.wikipedia.org/wiki/Core_dump)* |
| *crash* | Na computação, um crash, ocorre quando um programa de computador para de funcionar corretamente e é encerrado.  O programa responsável pode apresentar travamento até que um serviço de monitoramento de falhas a relate. *Fonte: [Wikipedia](https://en.wikipedia.org/wiki/Crash_(computing))* |
| *hang / freeze* | Na computação, um travamento ou congelamento ocorre quando um processo ou sistema para de responder aos dispositivos de entradas.  Um exemplo típico é quando a interface gráfica do usuário não responde a comandos como digitar no teclado ou mover o mouse. *Fonte: [Wikipedia](https://en.wikipedia.org/wiki/Hang_(computing))* |
| *access violation*  *ou*  *segmentation fault* | Na computação, uma falha de segmentação (muitas vezes abreviada para segfault) ou violação de acesso é uma falha, ou condição de falha, levantada por hardware com proteção de memória, notificando um sistema operacional de que o software tentou acessar uma área restrita de memória (a violação de acesso à memória). *Fonte: [Wikipedia](https://en.wikipedia.org/wiki/Segmentation_fault)* |
| *exception* | Em computação e programação de computadores, tratamento de exceções é o processo de responder à ocorrência de exceções - condições anômalas ou excepcionais que requerem processamento especial - durante a execução de um programa. Em geral, uma exceção interrompe o fluxo normal de execução e executa um manipulador de exceção pré-registrado. *Fonte: [Wikipedia](https://en.wikipedia.org/wiki/Exception_handling)* |

---

## Veja também

* [Commando kill](http://man.he.net/man1/kill)
* [Commando catchsegv](http://man.he.net/man1/catchsegv)
