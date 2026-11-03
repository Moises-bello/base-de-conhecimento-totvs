---
article_id: 360041899373
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 19c6c327b1b814a763b783b182ac18e327c447bebd3758471485e6a118d0af64
fetched_at: '2026-06-28T22:38:33.128844+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: MP - FAT - Lock request time out period exceeded (Tempo limite da solicitação
  de bloqueio excedido)
type: support-article
updated_at: '2021-04-28T15:53:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360041899373-MP-FAT-Lock-request-time-out-period-exceeded-Tempo-limite-da-solicita%C3%A7%C3%A3o-de-bloqueio-excedido
---

**Ocorrência**Ao realizar um processamento de uma rotina no sistema, é gerado um erro informando "Lock request time out period exceeded" (Tempo limite da solicitação de bloqueio excedido).  
   
 **Ambiente**Microsiga Protheus – Faturamento – A partir da versão 12  
 **Causa**Este erro ocorre quando a operação de update no registro falha com a ocorrência de erro AdvPL "DB error (Update): -29", ocorrência reportada pelo driver do MSSQL ao DBAccess, impedindo a atualização do registro inserido ou alterado dentro do processo transacionado pela função TCSqlExec().  
   
 **Solução**

**1.** Recomendamos que adicione as chaves **UseLockInDB=0** e **LockTimeout=0** no arquivo de configuração do **DBAccess (dbaccess.ini)** e reinicie o serviço. Segue exemplo de uso das chaves:

**[GENERAL]**  
**UseLockInDB=0**  
**LockTimeout=0**

Caso **persista**, realize o mesmo procedimento utilizando o **LockTimeout=1000**  
**Documentação da Chave**: https://tdn.totvs.com/pages/viewpage.action?pageId=306845697

Após a aplicação das chaves, **reinicie seu DBAccess**, utilize-o normalmente e nos reporte se o problema reportado foi sanado.

**2.** O arquivo **DBAPI.DLL** precisa estar atualizado, veja como proceder:

O **dbaccess** e o **appserver** são **64 bits**?

Se forem, é necessário copiar o arquivo **dbapi64.dll** do dbaccess (Baixar do portal do cliente) para a pasta do **Appserver** (Todos Slaves) e **renomeá-lo para dbapi.dll**. Apos o procedimento realizar os devidos testes.

**Documentação**: <https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028710652-MP-FRAME-Arquivo-dbapi-dll-do-DBAccess-no-AppServer>
