---
content_hash: 19fa940995b1eb98a4294ea91dca205cbbbc9fecb1026251553ddf0ae5562a48
fetched_at: '2026-06-28T21:35:18.254972+00:00'
page_id: '155583041'
product: fluig
source: tdn-fluig
title: ARQ - Quais os procedimentos para atualização na release 1.5.13 ou anterior?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=155583041
version: 53
---

Atenção

Página destinada a atualizações 1.5.13 ou anterior.

Acesse a página original para atualizações a partir da release 1.6: .

# Índice

4true.\*ndicenone

# Objetivo

O objetivo desta página é apresentar os procedimentos necessários para efetuar a atualização do TOTVS Fluig Plataforma.

Nota

Para acompanhar informações sobre Atualização Programada e sobre o Ciclo de Atualização Obrigatório acesse .

Fluig no Cloud

Caso tenha contratado o serviço de Cloud, a instalação, atualização ou configuração da plataforma é realizada por uma equipe de atendimento específica. Para solicitar o atendimento, acha um chamado para a equipe de Cloud pela página de [suporte](http://suporte.totvs.com/).

# Procedimentos para efetuar a atualização da plataforma

Para efetuar a atualização, é necessário seguir os passos descritos a seguir:

Atenção!  

* É imprescindível parar todos os serviços antes de atualizar: FLUIG, fluig\_Memcached, fluig\_Realtime, Prizm (esse serviço só existe se você utiliza o Fluig Viewer *on premises*).

* Para realizar o backup recomendamos acompanhar o guia: .

* Se houver a necessidade de *downgrade*, a base deverá ser restaurada para o *backup* da versão.   
  Sobre o *downgrade*: Caso a plataforma for atualizada para a versão 1.3.6 e deseja-se retornar para a versão 1.3.5, será necessário restaurar o backup da versão 1.3.5, não contendo os dados adicionados na versão mais atual.

* Para atualização para a 1.5 atente-se guia .

* Clientes que estiverem utilizando a plataforma abaixo da atualização 1.2.8 devem entrar em contato cm o [Suporte TOTVS Fluig](http://suporte.totvs.com) ***antes*** de executar a atualização.

* Para atualizar a plataforma instalada em *Load Balance* é necessário que o pacote de atualização seja executado em cada nó e, como mencionado acima, os serviços  FLUIG, fluig\_Memcached, fluig\_Realtime e Prizm devem estar parados antes que o processo de atualização seja iniciado.

* Caso o Indexer estiver instalado em servidor separado é necessário, logo após a atualização ser executada em cada nó, que o arquivo foundation-addon-indexer-web.war, que foi gerado no diretório [Instalação fluig]/jboss/apps, seja movido para o diretório [fluig\_Indexer]/webapps, substituindo o arquivo foundation-addon-indexer-web.war que se encontra neste diretório, que é de uma versão anterior.
0.5falsesamplesfadetrue1Passo1

* Efetue o *download* do instalador no [Portal de Clientes](https://suporte.totvs.com/portal/p/10098/download#000035/FLUIG%201.5/FLUIG/) e descompacte-o.

2Passo 2

* Pare os serviços *fluig*, *fluig\_MemCached* e *fluig\_RealTime*.

3Passo 3

* Execute o instalador e escolha a opção "Atualizar minha instalação".

* Clique em "**Próximo**" até o sistema apresentar a mensagem de que a atualização foi concluída com sucesso.

4Passo 4  

* Inicie os serviços respeitando a seguinte ordem:  
   **1.** fluig\_MemCached;  
   **2.** fluig\_RealTime;  
   **3.** fluig.

Importante

Habilite o acesso ao serviço de versionamento da plataforma, liberando acesso ao endereço <https://version.fluig.com> (porta 443), na rede local onde a plataforma está instalada.

# Atualização em ambiente Linux - Modo Caractere

Movimente-se nas abas abaixo e acompanhe o passo a passo de atualização.

0.5falsesamplesfadetrue1Passo 1

* Descompacte o instalador da plataforma.

2Passo 2

* Abra o console no diretório onde o instalador foi descompactado e execute o comando:

  Substitua o [Diretório fluig] pelo diretório onde se localiza a instalação da plataforma a ser atualizada.
