---
article_id: 1500002550601
category: Financeiro - Contas a Receber
content_hash: a5fc23c8fbed40248fcfb41cd4827ade05c44981fd5d72a2063428129b4c9a49
fetched_at: '2026-06-28T22:38:14.273079+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: 'MP - SIGAFIN - Errorlog SCGN000025: Error : 2714 (S0001) (RC=-1) - [Microsoft][SQL
  Server Native Client 11.0][SQL Server]There is already an object named ''SCGN000025''
  in the database'
type: support-article
updated_at: '2021-04-28T15:16:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500002550601-MP-SIGAFIN-Errorlog-SCGN000025-Error-2714-S0001-RC-1-Microsoft-SQL-Server-Native-Client-11-0-SQL-Server-There-is-already-an-object-named-SCGN000025-in-the-database
---

**Ocorrência**Na rotina **Calculo AVP CR** (**FINA940**) ao selecionar por índice e aplicar para os títulos, ao salvar apresenta o Errorlog na geração da tabela temporária. SCGN000025: Error : 2714 (S0001) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]There is already an object named 'SCGN000025' in the database.

**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 12.1.17  
  
**Causa**No banco de dados o *collation* está com formato diferente de *"Latin1\_General\_BIN"*  
  
**Solução**Trocar o formado do *collation* para o padrão utilizado pela TOTVS *"Latin1\_General\_BIN"*

**Importante**Esse procedimento deve ser executado por um especialista de banco de dados (DBA).   
  
**Saiba Mais:**<https://tdn.totvs.com/display/public/PROT/MSSQL>
