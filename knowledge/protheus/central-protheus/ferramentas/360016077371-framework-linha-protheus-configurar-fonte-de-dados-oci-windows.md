---
article_id: 360016077371
category: Ferramentas
content_hash: b37019d719089f8383b4487e56924b51ddb9d7479d32bc1daeac1d794e0aa378
fetched_at: '2026-06-28T22:42:18.015657+00:00'
product: protheus
section_id: 360000075448
source: central-protheus
title: Framework - Linha Protheus - Configurar Fonte de Dados (OCI) (Windows)
type: support-article
updated_at: '2025-10-17T20:56:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016077371-Framework-Linha-Protheus-Configurar-Fonte-de-Dados-OCI-Windows
---

**Dúvida**Como configurar fonte de dados (OCI) para Oracle e comunicar com o DBAccess (Windows)?  
   
 **Ambiente**Protheus - DBAccess - Todas as versões  
   
**Solução**Para realizar a configuração da fonte de comunicação de dados (OCI) listamos os seguintes passos:  
 **1.** Realize o download do **Instant Client Oracle**, compatível com a sua versão;  
Link Instant Client Oracle: <https://www.oracle.com/technetwork/database/database-technologies/instant-client/downloads/index.html>  
**Obs.:** Caso não esteja ativo o link acima, realize uma busca rápida por Download Instant Client Oracle e localize no site da Oracle.  
  
**2.** Baixe o Instant Client compatível com o Sistema Operacional onde está o DBAccess  
**Obs.:** Será necessário criar a variável de ambiente TNS\_ADMIN  
 **3.** Crie a **Variável de Ambiente** no Windows:  
  
**4.** Acesse **Propriedades do Sistema > Avançado**;  
  
![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011307231)  
  
**5.** Clique em **Novo...**;  
  
 ![Variavel_do_sistema.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011264312)

**6.** Inclua nos campos Nome da **Variável: TNS\_ADMIN** e **Valor da variável: Caminho\_do\_Client**;  
  
![Editar_Variavel_de_Sistema.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011307351)  
  
**7.** Configure o arquivo **TNSNAMES.ORA**, conforme o exemplo abaixo:  
<NOME\_DA\_CONEXAO> =  
(DESCRIPTION =  
   (ADDRESS = (PROTOCOL = TCP)(HOST = **<IP\_DO\_SERVER\_BANCO>**)(PORT = **<PORTA\_BANCO>**))  
      (CONNECT\_DATA =  
         (SERVER = DEDICATED)  
            (SERVICE\_NAME = **<NOME\_DO\_DB>**)  
       )  
)  
  
**8.** Configure o **DBAccess** e **dbaccess.ini**;

![DBAccess.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360011264932)

--dbaccess.ini  
[ORACLE]  
ORACLE\_HOME=D:\oracle\oracle\client\_1  
ClientLibrary=<Diretorio\_da\_OCI.DLL> (Ex.: D:\oracle\oracle\client\_1\oci.dll)  
OCIVersion=8  
memoasblob=1  
BindLobFields=1  
environments=<NOME\_DA\_CONEXAO\_TNSNAMES>

[ORACLE/<NOME\_DA\_CONEXAO\_TNSNAMES>]  
user=<USUARIO\_DO\_BANCO> (Este campo será preenchido pelo DBMonitor)  
password=üÓóÔß£®ËÔÁ (Este campo será preenchido pelo DBMonitor)  
TableSpace=<TABLESPACE\_DO\_BANCO>  
IndexSpace=<TABLESPACE\_DO\_BANCO>  
LogAction=0
