---
content_hash: d7c4675940f8051c45a8912cb7451c36bc282cc1557535858d5b2a3dca79e327
fetched_at: '2026-07-02T19:24:26.733445+00:00'
page_id: '6064423'
product: protheus
source: tdn-tec
title: c-tree - Guia de instalação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=6064423
version: 6
---

Guia de instalação

A TOTVS utiliza uma solução customizada do c-treeACE ISAM Server, desenvolvido pela FairCom, para arquivos temporários, arquivos de help, arquivos de senhas, gerenciamento do dicionário de dados e para banco de dados ISAM, através da linguagem true e RDD CTREECDX e CTREETMP.

Pela parceria TOTVS e FairCom, o c-tree Server é disponibilizado para gerenciamento do banco de dados e previamente liberado para 64 usuários. Para um número maior de usuários, por favor, entre em contato com seu Executivo de Atendimento e Relacionamento.

## Instalação

### Windows

1. Crie um diretório, por exemplo “C:\CTREESERVER” e descompacte o arquivo da pasta **Windows** dentro do diretório criado, com a opção ***use folder names*** habilitada. Desta forma, a estrutura do subdiretório do c-tree Server® será criada.
2. Para iniciar o servidor c-tree, em modo console, execute o aplicativo ***ctsrvr.exe***, localizado na pasta *\ctreeServers\ctreeISAMServer*.*ctstop -auto*”,*\ctreeTools\ctreeAdmin\Client\.*
3. Para parar o servidor c-tree, tanto em modo console quanto como serviço, execute ***ctstop -auto***, na pasta *\ctreeTools\ctreeAdmin\Client\*.
4. Para parar o serviço em modo console, na tela do c-tree Server, escolha a opção ***Control\Shutdown***. Acesse com usuário e senha (ADMIN, ADMIN).
5. Para aplicar uma nova licença, execute o aplicativo ***fcactvat.exe***, na pasta *\ctreeServers\ctreeISAMServer.* É necessário que o serviço do c-tree esteja parado para aplicação da licença.
6. Para instalar o c-tree Server como serviço do Windows, execute o aplicativo ***ctntinst.exe -install***, localizado na pasta *\ctreeServers\ctreeISAMServer*.  
    O serviço é instalado como ***ctreeserver*** e será configurado com ***start*** manual.

### Linux

1. Crie um diretório, por exemplo ctreeserver, e descompacte o arquivo da pasta Linux no diretório criado.  
    Exemplo: tar -zxvf ctsrvr\_linux\_v8\_050520.tar.gz
2. Na seção de execução do servidor c-tree, defina o diretório do c-tree Server® para busca do arquivo **libctreecb.so** (biblioteca de *callback* utilizada para resolução de alguns índices e filtros), e aumente o número máximo de arquivos do sistema operacional, através dos comandos:  
    export LD\_LIBRARY\_PATH=/ctreeserver/server/  
    ulimit -n 65535
3. Para iniciar o servidor c-tree, execute o aplicativo ***ctsrvr***, através do comando ***./ctsrvr***, na pasta */ctreeserver/server*.
4. Para parar o c-tree Server®, execute o aplicativo ***ctstop***, através do comando **./ctstop -auto**, na pasta */ctreeserver/client*.
5. Para aplicar uma nova licença, execute o aplicativo ***fcactvat***, através do comando ***./fcactvat***, na pasta */ctreeserver/server*.  
    É necessário que o serviço do c-tree esteja parado para a aplicação da licença.

## Observações

* Quando o rootPath for compartilhado por mais de uma instância do true, além da chave rootPath, deve ser configurado a chave ctreeRootPath.
* Quando a base de dados principal (RPODB) é configurada para ADS ou para DBF, não é possível utilizar as engine local do c-tree nem utilizar o c-tree Server
* Para o correto funcionamento do c-tree Server recomendamos, após a análise prévia, a inclusão do mesmo e de arquivos \*.FCS às listas de exceção para evitar que eventuais análises preemptivas bloqueiem, rejeitem recursos aos mesmos e ocorrências (registradas em ctstatus.fcs) como:  

  ```
  - User# 00017 WRITE_ERR: L0000351.FCS at 0:852000x  sysiocod=33 bufsiz=8192 bytes written=0[0]  ioLoc=0: 37  
   Mon Sep 21 23:54:54 2009  
    - User# 00017 ctwrtlog: sysiocod: 33  
   Mon Sep 21 23:54:54 2009  
    - User# 00017 ctwrtlog:    error: 37  
   Mon Sep 21 23:56:19 2009  
    - User# 00005 CHKPNT ctwrtlog error: 541  
   Mon Sep 21 23:56:19 2009  
    - User# 00005 CHKPNT error on exit: 541  
   Mon Sep 21 23:56:19 2009  
    - User# 00005 Checkpoint failure: 541  
   Mon Sep 21 23:56:19 2009  
    - User# 00005 Dumped stack for server process 4876, log=1, loc=37, rc=0  
   Mon Sep 21 23:56:19 2009  
    - User# 00005 O5 M0 L37 F541 P0x (recur #1) (uerr_cod=541)
  ```

### Configuração básica do TOTVS | Application Server

Para utilização adequada do c-tree Server®, é necessário alterar o arquivo de configuração (appserver.ini), do TOTVS | Application Server, com as seguintes seções e chaves:

1. Finalize o TOTVS | Application Server.  
    Para alterar o arquivo de configuração, o TOTVS | Application Server não deve estar em execução.
2. Incluir, no arquivo de configuração (appserver.ini), as seguintes seções e chaves:  
    [General]  
    ctreeMode=Server  
   [CtreeServer]  
    [ctServerName=FAIRCOMS@IP\_do\_servidor](mailto:ctServerName=FAIRCOMS@IP_do_servidor)
3. Na chave **ctServerName**, no lugar do IP\_do\_servidor, informe o IP do servidor em que o c-tree Server® está sendo executado.   
   Exemplo:  
    [CtreeServer]  
    [ctServerName=FAIRCOMS@183.34.63.01](mailto:ctServerName=FAIRCOMS@183.34.63.01)

## Veja também
