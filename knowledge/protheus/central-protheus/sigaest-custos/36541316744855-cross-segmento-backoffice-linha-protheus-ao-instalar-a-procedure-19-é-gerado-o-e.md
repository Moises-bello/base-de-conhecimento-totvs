---
article_id: 36541316744855
category: SIGAEST - CUSTOS
content_hash: 6022e6ed46efb89f8471fcff304047e1811cc1b4090703328bc45a2ecffa6b2a
fetched_at: '2026-06-28T22:39:00.256817+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - Ao instalar a procedure 19
  é gerado o erro: ''TRIM'' is not a recognized built-in function name.'
type: support-article
updated_at: '2026-03-27T18:43:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36541316744855-Cross-Segmento-Backoffice-Linha-Protheus-Ao-instalar-a-procedure-19-%C3%A9-gerado-o-erro-TRIM-is-not-a-recognized-built-in-function-name
---

O erro "'TRIM' is not a recognized built-in function name" ocorre ao instalar a procedure 19 devido à incompatibilidade da versão do SQL Server, pois a função TRIM só está disponível a partir do SQL Server 2017 (nível de compatibilidade 130). A solução é atualizar o SQL Server ou ajustar o nível de compatibilidade conforme orientação do DBA.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36541322194967) Tempo aproximado para leitura: **00:01:00 min**  
  
**Ocorrência**

Ao executar a instalação da procedure 19, o sistema apresenta o erro:

`'TRIM' is not a recognized built-in function name.`

|  |
| --- |
| IDSPS: 4791 -  - Origem: RPO  **Erro ao instalar a procedure [MAT009\_19\_01]** - Error : 195 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server**]****'TRIM' is not a recognized built-in function name**. Error : 195 (00000) (RC=-1) -  ( From tDBServer::ROP\_SQLEXEC ) Thread ID [13784]    User [admin]    IO [12844]    Tables [151]    MaxTables [152]    Comment [CFGX051 - TCPIP - ThreadID(11116)]    SP [ ]    Traced [No]    SQLReplay [No]    InTran [No]    DBEnv [MSSQL/PROTHEUS12]    DBThread [(SPID 51,54,57)]    Started [30/11/2025 21:42:28]    IP [127.0.0.1:10500]    IDLE [ ]    InTransact [ ]    Memory [0]    Running [ROP\_SQLEXEC for 0 s.]    RCV [3476568]    SND [2536104]    TCBuild [20240224-20250929]    TCVersion [24.1.1.0]    ARCH [64]    OS [WINDOWS]    BUILD [RELEASE] |

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Causa**

O erro ocorre devido a uma **incompatibilidade de versão do banco de dados SQL Server**. A função **TRIM**, responsável por remover espaços em branco no início e fim de uma string, foi introduzida apenas a partir do **SQL Server 2017** e versões superiores.

Se o banco de dados estiver configurado com:

* **Nível de compatibilidade inferior a 130** (equivalente ao SQL Server 2016), ou
* **Servidor utilizando versão anterior ao SQL Server 2017**

A função **TRIM não estará disponível**, ocasionando o erro reportado durante a instalação da procedure.  
  
**Solução**  
Solicite ao time de TI ou ao DBA da empresa que valide:

**- 1 -** Versão do SQL Server instalada: Recomendamos verificar e confirmar a versão do banco de dados.  
Caso esteja utilizando uma versão anterior ao SQL Server 2017 ou com nível de compatibilidade abaixo de 130, será necessário:

**- 2 -** Atualizar o SQL Server para versão compatível, **ou**

**- 3 -** Ajustar o nível de compatibilidade, conforme orientação do DBA.

**Nesse link** [**https://tdn.totvs.com/x/P4pc**](https://tdn.totvs.com/x/P4pc) **consta a lista de Banco de Dados homologados**

***Saiba mais:***

[SIGAEST - Procedure Desatualizada ou Incompatível](https://centraldeatendimento.totvs.com/hc/pt-br/articles/15131065568791-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Procedure-Desatualizada-ou-Incompat%C3%ADvel)

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
