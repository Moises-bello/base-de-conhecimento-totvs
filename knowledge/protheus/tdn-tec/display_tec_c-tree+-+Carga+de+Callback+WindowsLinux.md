---
content_hash: 1650c7492e8c1c7d64d0f6717cca55e5d9afa1df6dc056aa86d22ac38eba1854
fetched_at: '2026-07-02T19:24:26.785866+00:00'
page_id: '6064433'
product: protheus
source: tdn-tec
title: c-tree - Carga de Callback WindowsLinux
type: documentation
url: https://tdn.totvs.com/display/tec/c-tree+-+Carga+de+Callback+WindowsLinux
version: 4
---

BLOCK

c-tree - Carga de Callback WindowsLinux

## c-tree - Carga de Callback (Windows/Linux)

```
O banco de dados c-tree Server, disponibilizado pela TOTVS S.A., possui uma funcionalidade especial, chamada de CallBack, utilizada para a resolução de expressões de filtro que não são possíveis de serem resolvidas pelo banco.
```

Este recurso é instanciado dinamicamente pelo c-tree Server®, no momento em que o mesmo é iniciado. No ambiente Windows, o arquivo chamas-se ctreecb.dll e no Linux, chama-se ctreecb.so.

O arquivo do *CallBack,* disponibilizado junto da distribuição do c-tree Server® realizada pela TOTVS S.A., é um recurso que não é atualizado constantemente, porém, é importante que os ambientes com servidor TOTVS seja atualizado e o c-tree Server® possua o CallBack atualizado também.

### Falha de carga

Ao iniciar a aplicação (Exemplo: ERP), o primeiro programa AdvPL que estabelecer conexão com o c-tree Server® verificará se a carga foi realizada com sucesso. Se houver alguma falha na carga do recurso, o sistema apresentará a seguinte mensagem no console do TOTVS | Application Server:

* #### Ambiente Linux

  ####

```
Loading Ctree Client [/home/siga0984/space/ap7/bin_050331a/server_1/libmtclient.so]  
******************************************************************  
CtreeServer Could not Load ctreecb.so  
Make sure that ctreecb.so is on Unix default library path  
******************************************************************
```

* #### Ambiente Windows

```
Loading Ctree Client [mtclient.dll]  
******************************************************************  
CtreeServer Could not Load ctreecb.dll  
Make sure that ctreecb.dll is on Ctree Server's path  
******************************************************************
```

Além disso, no console do c-tree Server, também serão apresentadas mensagens de falha na carga.

* #### Ambiente Windows

```
LoadProtheus Error - Could not open ctreecb.dll - ERROR: 126  
It was not possible to load ctreecb.dll
```

* #### Ambiente Linux

  ####

```
PROTHEUS: It was not possible to load libctreecb.so - libctreecb.so: cannot open shared object file: No such file or directory
```

A falha na carga da dll/so do c*allback* repercute em uma consequência: Expressões de filtro que utilizam expressões e funções AdvPL, que não são resolvidas pelo banco de dados, não conseguem ser resolvidas. Logo, resultam em erro fatal no AdvPL, quando da tentativa de navegação na tabela filtrada. O erro gerado corresponde ao erro 598: *Could not evaluate conditional expression*.

#### Exemplo

```
************************ (AUTOMAN,julio) ************************  
First - Ctree Error 598 - IO Error: 0 - Could not evaluate conditional expression.  
File: d:\ap7\ap_test\advpltests_top_ctree\sigaadv\sx2010.dtc
```

Em geral, as ocorrências de erro mais comuns de falha na carga do *callback* são reproduzidas no ambiente Linux, quando o c-tree Server® é carregado, sem que antes tenhas sido setada a variável de ambiente do Linux LD\_LIBRARY\_PATH, apontando para o *path* onde está sendo executado o c-tree Server®.

Para mais detalhes, consulte a documentação de [instalação/configuração do c-tree Server em ambiente Linux](http://tdn.totvs.com/pages/viewpage.action?pageId=6064423).

### Particularidades do ambiente Linux

Em ambiente Linux, esta ocorrência de falha de resolução de expressão de filtro pode ter outra causa, também relacionada a falha na carga do *callback*. Mesmo setando a variável de ambiente LD\_LIBRARY\_PATH, deve-se ter cautela para não instalar o c-tree Server® em um *path* no Linux, que contenha qualquer letra maiúscula no *path* de acesso ao c-tree Server®. O sistema (ERP) possui esta característica operacional e o *callback* também possui essas características.

Caso o c-tree Server® seja instalado em um *path* que contenha alguma letra maiúscula no caminho, o *callback* será carregado com sucesso. Porém, no momento de sua utilização no c-tree Server®, ocorrerá um erro de inicialização do *callback*.

Desta forma, será apresentada um mensagem, no console do c-tree Server,

```
jA não encontrado  
DU6 W6 8UA\¾l¾D¾³':A  
Ctree CallBack Error - Session [envctree710] not found in ap.ini. Verify the 'Environment in the Server' in file ./lib/config.cpp at line 58
```
