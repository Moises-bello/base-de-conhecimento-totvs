---
content_hash: 38e3afff2a46c83e827003d9a49ef66e5e7b447c4ca9c9d96224670153f31d7d
fetched_at: '2026-06-28T21:35:23.790011+00:00'
page_id: '258835192'
product: fluig
source: tdn-fluig
title: ARQ - Sistema acusa que existem aplicativos JAR em aberto e a plataforma não
  conclui a atualização
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=258835192
version: 9
---

# Índice

4true.\*ndicenone

# Plataforma

**Versão:** 1.6 ou superior

# Ocorrência

Ao tentar atualizar a plataforma, o sistema acusa que existem aplicativos abertos do tipo JAR e não consigo finalizar a atualização.

# Causa

O erro com os arquivos .jar acontece porque eles são arquivos temporários do TOTVS Fluig Plataforma criados enquanto o sistema está em execução.

Toda vez que a plataforma é reiniciada, são apagados os arquivos temporários em <instalação\_fluig>\appserver\standalone\tmp (a partir da **2.0**) ou <instalação\_fluig>\appserver\domain\servers\<fluig server>\tmp (até a **1.8.2**) para que após a inicialização do serviço a pasta seja criada novamente para armazenar todos os arquivos temporários que ele utilizará.

O que acontece é que alguns arquivos ficam com o nome muito grande, maior do que o sistema operacional consegue gerenciar. Por isso, quando o sistema tenta apagá-los, o SO informa que não consegue.

# Solução

Para contornar essa situação você pode renomear esses arquivos para poder apagá-los em seguida. Siga os passos abaixo:

0.5falsesamplesslidetrue1Passo 1

* Pare os serviços da plataforma;

* Acesse a pasta **<instalação\_fluig>****\appserver\standalone** (a partir da **2.0**) ou **<instalação\_fluig>\appserver\domain\servers\<fluig server>** (até a **1.8.2**)**;**

* Remova a pasta **tmp**;

**Figura 1 - Apagar a pasta temporária**

2Passo 2

* Durante a remoção, se o sistema operacional não conseguir gerenciar o arquivo pelo tamanho do seu nome, ele exibirá a mensagem:

"Os nomes dos arquivos de origem são maiores do que o tamanho máximo permitido pelo sistema de arquivos. Tente mover um local que tenha um nome de caminho menor ou renomeie com nomes menores antes de tentar a operação".

* Marque a opção **Fazer isso para todos os itens atuais** e em seguida clique em **Ignorar**;

**Figura 2 - Ignorar exclusão de arquivos com nome muito grande**

3Passo 3

* Acesse a pasta **\tmp\vfs\deployment**;

* Se o seu ambiente tiver muitos arquivos temporários, poderão existir mais pastas dentro dessa estrutura. No exemplo abaixo existe apenas uma;

**Figura 3 - Pastas temporárias**

4Passo 4

* Acesse cada pasta, selecione todos os arquivos e pressione F2 para renomeá-los;

* Após fazer isso em todas as pastas volte para **<instalação\_fluig>****\appserver\standalone** (a partir da **2.0**) ou **<instalação\_fluig>\appserver\domain\servers\<fluig server>** (até a **1.8.2**) e apague a pasta **tmp**.

**Figura 4 - Renomear arquivos temporários**

5Passo 5

* Em seguida você já pode executar a atualização da plataforma. O sistema não terá mais problemas com os arquivos de nome muito grande.
