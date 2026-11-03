---
article_id: 360039485674
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 2cd6e9150afd5bd62b92c4693f372f3305dc789ae24c74e54d814735fbea7c6a
fetched_at: '2026-06-28T22:38:28.673143+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Tempo limite
  da solicitação de bloqueio excedido
type: support-article
updated_at: '2023-07-05T17:31:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360039485674-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Tempo-limite-da-solicita%C3%A7%C3%A3o-de-bloqueio-excedido
---

**Ocorrência**

Após a atualização de ambiente, o sistema está apresentado o erro indicando: **"Tempo limite da solicitação de bloqueio excedido".**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**

A ocorrência está ligada a inconsistências de comunicação entre o Dbaccess e a biblioteca DBAPI.DLL.

**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:

1. Recomendamos que adicione as chaves UseLockInDB=0 e LockTimeout=0 no arquivo de configuração do DBAccess (dbaccess.ini) e reinicie o serviço. Segue exemplo de uso das chaves:  
  
**[GENERAL]**  
**UseLockInDB=0**  
**LockTimeout=0**  
  
Caso persista, realize o mesmo procedimento utilizando o LockTimeout=1000

Documentação da Chave: [Melhoria - Novo parâmetro de time-out para MSSQL](https://tdn.totvs.com/pages/viewpage.action?pageId=306845697)

Após a aplicação das chaves, reinicie seu DBAccess, utilize-o normalmente e nos reporte se o problema reportado foi sanado.  
  
2. O arquivo DBAPI.DLL precisa estar atualizado, veja como proceder:  
  
O dbaccess e o appserver são 64 bits?  
  
Se forem, é necessário copiar o arquivo **dbapi64.dll** do dbaccess (Baixar do portal do cliente) para a pasta do **Appserver** (**Todos Slaves**) e renomeá-lo para **dbapi.dll**. Apos o procedimento realizar os devidos testes.  
  
Documentação: [MP-FRAME-Arquivo-dbapi-dll-do-DBAccess-no-AppServer](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028710652-MP-FRAME-Arquivo-dbapi-dll-do-DBAccess-no-AppServer)
