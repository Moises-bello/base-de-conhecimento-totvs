---
article_id: 360043004834
category: Financeiro
content_hash: 404b2a5cb0320931c8bb31f1eb55cc5ba915a65a094c2b407c39050c12ee2157
fetched_at: '2026-06-28T22:38:03.387926+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Lock request time out
  period exceeded (Tempo limite da solicitação de bloqueio excedido)
type: support-article
updated_at: '2022-06-15T00:46:56Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043004834-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Lock-request-time-out-period-exceeded-Tempo-limite-da-solicita%C3%A7%C3%A3o-de-bloqueio-excedido
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)**Tempo aproximado para leitura: **00:03:00 min**

**Ocorrência**Ao realizar um processamento de uma rotina no sistema, é gerado o errorlog "Lock request time out period exceeded" (Tempo limite da solicitação de bloqueio excedido).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**Este erro ocorre quando a operação de update no registro falha com a ocorrência de erro AdvPL "DB error (Update): -29", ocorrência reportada pelo driver do MSSQL ao DBAccess, impedindo a atualização do registro inserido ou alterado dentro do processo transacionado pela função TCSqlExec().  
  
**Solução****1.** Recomendamos que adicione as chaves **UseLockInDB=0** e **LockTimeout=0** no arquivo de configuração do **DBAccess (dbaccess.ini)** e reinicie o serviço. Segue exemplo de uso das chaves:

**[GENERAL]**  
**UseLockInDB=0**  
**LockTimeout=0**

Caso **persista**, realize o mesmo procedimento utilizando o **LockTimeout=1000**  
**Documentação da Chave**: https://tdn.totvs.com/pages/viewpage.action?pageId=306845697

Após a aplicação das chaves, **reinicie seu DBAccess**, utilize-o normalmente e nos reporte se o problema reportado foi sanado.

**2.** O arquivo **DBAPI.DLL** precisa estar atualizado, veja como proceder:

O **dbaccess** e o **appserver** são **64 bits**?

Se forem, é necessário copiar o arquivo **dbapi64.dll** do dbaccess (Baixar do portal do cliente) para a pasta do **Appserver** (Todos Slaves) e **renomeá-lo para dbapi.dll**. Apos o procedimento realizar os devidos testes.

**Saiba mais**:  
[MP - FRAME - Arquivo dbapi.dll do DBAccess no AppServer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028710652)
