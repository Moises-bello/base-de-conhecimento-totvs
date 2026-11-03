---
content_hash: 003f3d1a6c1374e7be6ac9043be756fe73fbdf28e7bc6acf20a2359ab54761aa
fetched_at: '2026-06-28T21:35:30.233224+00:00'
page_id: '819058035'
product: fluig
source: tdn-fluig
title: Erros comuns ao instalar/atualizar a plataforma
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=819058035
version: 98
---

Índice

# Objetivo

---

O objetivo deste guia é apresentar quais os problemas mais comuns ao efetuar a atualização do TOTVS Fluig Plataforma e como resolvê-los.

# Pré-requisitos

---

* Interesse em instalar/atualizar o ambiente de acordo com o  ou o , respectivamente.
* Servidores respeitando o [Modelo de dimensionamento](https://tdn.totvs.com/display/fluig/Modelo+de+dimensionamento).
* Plataforma de acordo com os padrões da [Matriz de portabilidade](https://tdn.totvs.com/display/fluig/Matriz+de+portabilidade).
* Conferir outras [Especificações Técnicas](https://tdn.totvs.com/pages/viewpage.action?pageId=144409649) necessárias.

# Sistema operacional Windows

---

Descrevemos abaixo algumas situações que podem impactar diretamente na instalação/atualização das mídias do TOTVS Fluig Plataforma no Sistema Operacional Windows.

## Alterar o tipo de inicialização dos serviços para manual

---

**01.** Alterar o tipo de inicialização dos serviços do Fluig para **"manual"** é importante para evitar que o serviço inicialize e impeça a atualização da plataforma.

Importante!

Essa configuração será utilizada apenas para reiniciar o servidor e fazer a atualização. Depois o serviço poderá ser configurado novamente para **inicialização automática**.

identificarPasso 1

* Acessar a tela de **Serviços** do **Windows** e procure pelos serviços: (1) fluig, (2) fluig\_Indexer e (3) fluig\_RealTime.

Passo 2

* Acessar as **propriedades** dos serviços.

Passo 3

* Alterar o **Tipo de Inicialização** de Automático para **Manual**.
* Fazer isso para (1) fluig, (2) fluig\_Indexer e (3) fluig\_RealTime.

## Serviço "fluig" permanece com o status "stopping" (ou "parando")

---

Não é incomum que, ao encerrar o **serviço "fluig"**, o status permaneça em **"stopping"** e não finalize a ação. Esse comportamento não é específico da plataforma e, geralmente, está associado a interferências externas, seja de outra aplicação, servidor, etc. A maior parte dos relatos estão relacionados ao **serviço "fluig"**, os demais serviços **(fluig\_Indexer e fluig\_RealTime)** nunca apresentaram tal eventualidade.

Os motivos mais comuns para a situação ocorrer são:

* Aplicação de **backup** sendo executada nas pastas e no mesmo servidor da plataforma, de forma que, o serviço não consiga fazer os procedimentos necessários para parar.
* **Antivírus** ativado, ou funcionando no mesmo servidor, sem ter o Fluig configurado como exceção. Isso pode impedir a plataforma de apagar pastas temporárias, que é um procedimento padrão no desligamento.
Recomendação

O ideal é que o servidor seja **dedicado** à plataforma, sem que haja outros sistemas operando em conjunto.

Preparamos alguns procedimentos a serem feitos para que a instalação/atualização possa prosseguir:

**01.** Desativar outras aplicações **Java** e avaliar se ainda ocorre interferências ao finalizar o **serviço "fluig"**.

**02.** Conferir a documentação de  utilizados pelo Fluig e descartar a possibilidade de conflitos nas portas pela utilização de outras aplicações.

**03.** Recortar os arquivos da **pasta apps** para outro local, fora do diretório de instalação do Fluig: **<diretório de instalação do Fluig>\appserver\apps**

**04.** Limpar os **arquivos temporários** do **Windows**, seguindo os passos abaixo:

identificarPasso 1

* Fechar **todas** as aplicações abertas.
* Acionar **Executar**.

Passo 2

* Digitar o termo **%tmp%** ou **%temp%** (ambos são válidos).

* Clicar em **Ok**.

Passo 3

* Abrirá a pasta de **arquivos temporários** do **Windows**.
* Selecionar todos os arquivos **(Ctrl + A)**.

Passo 4

* Clicar com o botão direito do mouse em cima dos arquivos selecionados e acionar **Excluir**.
* Confirme a exclusão dos arquivos.
* Também é possível realizar a exclusão com o botão **Delete**, no teclado.

**05.** Encerrar todas as tarefas do **OpenJDK Platform binary** e do **Node.js JavaScript Runtime** no **Gerenciador de Tarefas** do **Windows**:

Nota:

O **Node.js JavaScript Runtime** é um ambiente de execução do código JavaScript do lado servidor (*server-side*). Na prática, o **Node.js** gera a possibilidade de criar aplicações autossuficientes (*standalone*) em uma máquina servidora, sem a necessidade do navegador.

Já o**OpenJDK Platform binary** é um serviço que executa o Servidor de Aplicação Java, que serve como base para a aplicação Fluig.

A plataforma funciona tanto de forma **reativa**, quando os usuários a acessam; quanto **proativa**, quando se tratam de fluxos automáticos, agendamentos de processamentos e demais tarefas automatizadas que possam estar configuradas.

Assim, mesmo sem usuários utilizando o ambiente, existem integrações ou agendamentos de tarefas que são executados em **segundo plano** pelo Fluig.

identificarPasso 1

* Acionar o atalho **Ctrl + Alt + Del** no teclado e clicar em **Gerenciador de Tarefas**.
* Também é possível pesquisar por **Gerenciador de Tarefas** no campo de busca do **Windows**.

Passo 2

* Se certifique que está na aba **Processos**.
* Buscar em **Processos em segundo plano** pelos termos **"OpenJDK Platform binary"** e **"Node.js JavaScript Runtime"**.

Passo 3

* Acionar o recurso **Finalizar tarefa** para cada processo em segundo plano relacionado ao **"OpenJDK Platform binary"** e ao **"Node.js JavaScript Runtime"**.

Passo 4

* Após finalizar as tarefas, abra novamente a tela de **Serviços** do **Windows**. Todos os serviços deverão aparecer sem nenhuma informação na coluna **Status**.

## Mensagens durante a instalação/atualização

---

**01.** Durante a instalação ou atualização da plataforma, podem surgir as seguintes mensagens de erro:

* *O serviço Fluig está em execução. Finalize o serviço para continuar a atualização.*
* *Existe algum arquivo aberto ou em uso. Feche todas as aplicações que possam estar usando arquivos.*
* *O serviço do Solr está em execução. Finalize o serviço para continuar a atualização.*
* *The system cannot find the path specified.*
* *Mensagens em branco.*
* *Unable to evaluate expression using this context.*
* *[...]\dataset.author.csv (O dispositivo não está pronto).*

Nota:O instalador da plataforma verifica se todos os serviços e arquivos da plataforma estão abertos ou em uso durante a instalação/atualização. Isso garante que o procedimento seja realizado com segurança.Atenção!Ao ignorar os erros e prosseguir com a instalação, é possível finalizá-la. No entanto, ao tentar inicializar a plataforma, os serviços são encerrados logo em seguida.

**02.** Abaixo seguem alguns exemplos das mensagens que podem aparecer em tela:

identificarExemplo 1Exemplo 2Exemplo 3Exemplo 4Exemplo 5Exemplo 6Exemplo 7

## Renomear o diretório de instalação (teste)

---

**01.** Certifique-se de ter fechado todos os arquivos e finalizado os serviços do Fluig: (1) fluig, (2) fluig\_Indexer e (3) fluig\_RealTime.

**02.** Tente renomear a pasta de instalação da plataforma.

**03.** Se o Sistema Operacional não permitir que a pasta seja renomeada, significa que algum arquivo está aberto ou em execução.

## Verificar as permissões do usuário executor da mídia

---

**01.** O usuário que está executando o instalador deve possuir permissão de **administrador**.

**02.** Iniciar a sessão no Sistema Operacional com um usuário que possua propriedades administrativas no servidor.

**03.** Verificar se o usuário autenticado é realmente um usuário administrador:

identificarPasso 1

* Buscar pelo o **Painel de Controle** do **Windows**.

Passo 2

* Acionar **Contas de Usuário**.

Passo 3

* Acionar **Contas de Usuário** novamente.

Passo 4

* Clicar em **Gerenciar Contas de Usuários**.

Passo 5

* Selecionar o usuário que está autenticado e clicar em **Propriedades**.

Passo 6

* A opção **Administrador** precisa estar marcada.

**04.** Em caráter de teste, tente iniciar o instalador por linha de comando:

identificarPasso 1

* Abrir o **Prompt de Comando** através do botão direito do mouse e escolha a opção **Executar como administrador**, conforme a imagem abaixo:

Passo 2

* Se sua sessão **não for** de administrador, será necessário informar um **login** e **senha** antes de prosseguir;
* Com o **Prompt de Comando** aberto, navegue até a pasta descompactada onde contém a **mídia** do Fluig.

Passo 3

* Ao acessar a pasta do instalador, execute o arquivo **Fluig-Installer-64.exe**.
* A tela do instalador/atualizador será exibida e o processo de atualização prosseguirá normalmente.

## Consultar o log de eventos do Windows

---

O **Windows** possui o **Visualizador de Eventos** como recurso nativo para consulta de logs de eventos. Essa ferramenta registra detalhes sobre erros no sistema, inclusive os que são causados por falha de hardware, como HD ou memória RAM. **Para consultar:**

identificarPasso 1

* Pesquisar pelo **Painel de Controle** no campo de busca do **Windows**.

Passo 2

* Acionar a opção **Sistema e Segurança**.

Passo 3

* Clicar em **Ferramentas do Windows**.

Passo 4

* Clicar em **Visualizador de Eventos****.**

Passo 5

* O **Visualizador de Eventos** mostra diversas informações a respeito do tipo de evento e qual aplicação fez o disparo.

## Monitor de recursos do Windows

---

**01.** O **Monitor de Recursos** é um recurso do **Windows** que pode auxiliar no mapeamento das aplicações que estão conectadas ou utilizando o **Java.exe**. **Para acessá-la:**

identificarPasso 1

* Pesquisar pelo **Painel de Controle** no campo de busca do **Windows**.

Passo 2

* Acionar a opção **Sistema e Segurança**.

Passo 3

* Clicar em **Ferramentas do Windows**.

Passo 4

* Clicar em **Monitor de Recursos****.**

Passo 5

* Ao abrir o **Monitor de Recursos**, aparecerá a aba **“Visão Geral"** com os recursos de **hardware**.
* Selecionar a aba **CPU** e buscar pelo **java.exe**.

Passo 6

* Com o **java.exe** selecionado, é possível consultar, nas abas **Identificadores Associados** e **Módulo Associados**, todas as aplicações que estão utilizando o recurso.

## Limpeza de arquivos temporários e pastas keys

---

**01.** Realizar a limpeza dos arquivos temporários e pastas keys, conforme o passo a passo abaixo:

**a)** Parar a execução dos serviços do Fluig: (1) fluig, (2) fluig\_Indexer e (3) fluig\_RealTime.

**b)** Acessar o diretório **<diretório de instalação do Fluig>\appserver\standalone\log** (a partir da **2.0**) ou **<diretório de instalação do Fluig>\appserver\domain\servers\fluig1\log** (**1.6 até 1.8.2**).

**c)** Eliminar as pastas: **data, log, servers** e **tmp**.

Atenção!Nesse diretório existe a pasta **configuration**, que**não deve ser excluída**, pois se trata de uma pasta fundamental para o funcionamento da plataforma. As demais pastas são todas temporárias. Caso a plataforma não as encontre, ela automaticamente recria as pastas.Nota:Esse procedimento reiniciará a plataforma e limpará os arquivos de log do ambiente.

**d)** Apagar as pastas keys disponíveis nos caminhos:

* **<diretório de instalação do Fluig>\repository\wcmdir**
* **<volume do Fluig>\keys***.*

**e)** Verificar se existem arquivos que **NÃO**estejam nos formatos **.war**, **.ear** ou **.jar** dentro das pastas **apps**, **core**e **system**. Caso existam, é necessário remover esses arquivos **fora do formato** das pastas:

* **<diretório de instalação do Fluig>\appserver\apps**
* **<diretório de instalação do Fluig>\appserver\core**
* **<diretório de instalação do Fluig>\appserver\system**

Importante!Os arquivos temporários gerados nestas pastas são excluídos no momento da finalização dos serviços, porém, em casos de desligamentos forçados do ambiente estes arquivos podem não ser excluídos automaticamente. Assim, é necessário fazer a exclusão manualmente, geralmente, **os arquivos temporários estão no formato .tmp ou são diretórios como o mesmo nome**.

## Nova tentativa de atualização

---

**01.** Reiniciar o servidor.

**02.** Tentar efetuar a atualização da plataforma novamente.

**03.** Iniciar novamente os serviços do Fluig: (1) fluig\_Indexer, (2) fluig\_RealTime e (3) fluig.

# Sistema operacional Linux

---

Em servidores Linux essas situações não costumam ocorrer, no entanto, caso ocorra alguma eventualidade, realize a abertura de um ticket na [Central do cliente](https://suporte.totvs.com/), através da opção: **Abrir ticket** e anexe esses arquivos ao chamado. Essa ação agilizará todo o processo de atendimento:

falseVersão1A partir da 2.0

* **<diretório de instalação do Fluig>\appserver\standalone\configuration\standalone.xml**
* **<diretório de instalação do Fluig>\appserver\bin\standalone.conf**
* **<diretório de instalação do Fluig>\appserver\standalone\log\server.log**
* **<diretório de instalação do Fluig>\node\fluig.rt\package.json**
* **<diretório de instalação do Fluig>\node\fluig.rt\logs**
* **<diretório de instalação do Fluig>\install.log**
* **<fluig.conf> (Arquivo que fica dentro do servidor do Proxy Reverso)**
21.6 até 1.8.2

* **<diretório de instalação do Fluig>\appserver\domain\configuration\domain.xml**
* **<diretório de instalação do Fluig>\appserver\domain\configuration\host.xml**
* **<diretório de instalação do Fluig>\appserver\domain\servers\fluig1\log\server.log**
* **<diretório de instalação do Fluig>\appserver\domain\log\host-controller.log**
* **<diretório de instalação do Fluig>\appserver\domain\log\process-controller.log**
* **<diretório de instalação do Fluig>\node\fluig.rt\package.json**
* **<diretório de instalação do Fluig>\node\fluig.rt\logs**
* **<diretório de instalação do Fluig>\install.log**
* **<fluig.conf> (Arquivo que fica dentro do servidor do Proxy Reverso)**
