---
content_hash: 3f570b39c49ebfe1774f609e223908bf30744703b30802431b55d74823e91ad4
fetched_at: '2026-06-29T00:08:43.746887+00:00'
page_id: '305930904'
product: rm
source: tdn-rm
title: CannotConnect ao utilizar Direct mode (Oracle)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=305930904
version: 106
---

## Problema

A partir da versão 12.1.18 os produtos da linha RM passarão a utilizar o direct mode do provider de conexão utilizado para bases de dados Oracle.

Com este cenário o erro abaixo poderá ocorrer devido a configuração do alias de conexão a base de dados:

O direct mode implementa a conexão da aplicação RM sem a necessidade de utilizar dll's, provider ou outros artefatos de terceiros para conexão a base Oracle. Antes da implementação, utilizávamos a oracle call interface (OCI) para conexão ao banco de dados Oracle.

Atenção: O client do Oracle continua sendo necessário para acesso aos executáveis Delphi que ainda utilizam o BDE (Borland Database Engine) para conexão com o banco.

## Causa

Embora seja uma melhoria no funcionamento da aplicação,  esta configuração poderá provocar o erro acima nos seguintes cenários:

* Utilização de conexão via tnsnames do client Oracle
* Utilização de servidor de banco de dados Oracle RAC

A mudança implementada no RM foi habilitada através de tags no arquivo de configuração do rm.host (RM.Host.Service.exe.config , RM.Host.exe.config e RM.Host.JobRunner.exe.config), sendo esta tag oculta no config padrão da instalação e definida como true.

Esta configuração ocasionará o erro nos casos em que a forma de conexão ao oracle não for direta, exemplo (host/sid) ou nos casos em que o servidor Oracle esteja em RAC (Real Application Cluster).

## Solução

Para solução do problema os seguintes passos poderão ser seguidos

#fff

1. **Caso não utilize Oracle RAC**

   * + Recomendamos aos clientes que não utilizam Oracle RAC que mantenham a configuração do direct mode como true, pois além dos ganhos relativos a instalação, manutenção e adminsitração de clients Oracle nas máquinas em que o produto TOTVS está instalado, teremos outros ganhos em potencial, uma vez que neste modelo a aplicação trabalhará diretamente com o Oracle através do protocolo TCP/IP,sem o envolvimento do client do Oracle.  
       Para a não ocorrência do erro acima você deverá realizar o seguinte procedimento.  
       No alias manager informar a conexão direta ao banco de dados ao qual deseja se conectar. Para isso, você deverá informar o nome ou ip do host onde o banco de dados se encontra instalado "/" (barra) o SID "Service Identifier do Oracle", que é o nome do serviço Oracle.  
       Exs:   
         
       10.31.0.159/orcl   
        serverbd/orcl  
         
       Ex:
   * **Obs.:** Caso não utilize a porta padrão 1521, será necessário informá-la, conforme exemplo: BHD050101104**:1527**/exemplo12116

1. **Caso utilize Oracle RAC**

* + O modo direct não é compatível com o Oracle RAC. Sendo assim, clientes que utilizam o Oracle RAC poderão no momento da instalação do RM marcar o flag "utilização do Oracle RAC" que automáticamente irá setar a tag USEDEVARTDIRECT para false conforme imagem abaixo.  
      
      
      
    Caso não tenha marcado a opção durante a instalação, basta incluir a tag abaixo nos arquivos de configuração  (RM.Host.Service.exe.config , RM.Host.exe.config e RM.Host.JobRunner.exe.config conforme abaixo:  
      
    <add key="USEDEVARTDIRECT" value="false" />

Para verificar se a instancia é ou não Oracle RAC, você poderá executar a seguinte consulta:

select name, value from v$parameter where name='cluster\_database';

Caso o campo VALUE retorne TRUE a instancia é Oracle RAC.

## Artigos relacionados

Os artigos relacionados aparecem aqui baseados nos rótulos que você selecionar. Clique para editar a macro e adicionar ou alterar os rótulos.

false5LRMfalsemodifiedtruepagelabel in ("directmode","tnsnames","oracle","devart","connect","cannot","usedevartdirect","connection") and type = "page" and space = "LRM"devart directMode Oracle TnsNames connection USEDEVARTDIRECT cannot connect

true

|  |  |
| --- | --- |
| Ocorrências relacionadas |  |
