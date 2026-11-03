---
article_id: 360024805754
category: ADVPL - Classe e Função
content_hash: 062f9c7fb9abdaad43eee6af83e65658fae4b2ff411cbbe54013c347be4588c0
fetched_at: '2026-06-28T22:40:14.247373+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus  - ADVPL - Comandos DML em
  SQL: DBAccess'
type: support-article
updated_at: '2024-01-24T10:59:29Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024805754-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Comandos-DML-em-SQL-DBAccess
---

*![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)*Tempo aproximado para leitura: **00:02:00 min  
  
Dúvida**Qual função pode ser utilizada para executar comandos DML?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus)  – ADVPL – A partir da versão 11.8  
  
**Solução**Para executar comandos **DML** (**Data Manipulation Language**),pode ser utilizada a função **TCSqlExec**, esta permite executar comandos **DML e** **DDL**(**Data Definition Language**) retornando o status da execução.   
Se menor que **0** (**Zero**) indica que a sentença não foi executada com sucesso.  
Principais comandos **DML** são:

* **Select**
* **Insert**
* **Update**
* **Delete**.

Principais comandos **DDL** são:

* **Create.**
* **Drop**
* **Alter**
* **Truncate**

Para executar queries **DQL -** *(Data Query Language),* podem ser utilizadas as funções como **Embedded SQL**,  **TCGENQRY**, **TCGenQry2** ou **TCQUERY** estas permitem apenas o envio de comandos **DQL**, istoé, apenas o comando **Select**.

*![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8877780786455/mceclip0.png)*

**Saiba mais**[TCSQLExec](https://tdn.totvs.com/display/tec/TCSQLExec)  
[Embedded SQL](https://tdn.totvs.com/display/framework/Embedded+SQL)  
[TCGenQry](https://tdn.totvs.com/display/tec/TCGenQry)  
[TCGenQry2](https://tdn.totvs.com/display/tec/TCGenQry2)  
[TCQUERY](https://tdn.totvs.com/display/tec/Comando+TCQUERY)
