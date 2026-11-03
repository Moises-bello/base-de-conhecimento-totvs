---
article_id: 35986480264599
category: SIGAEST - CUSTOS
content_hash: 5e9e9a14ca78e855071a2dddabf84b3cc80aecc0a023a52eb4fa26e94dc35196
fetched_at: '2026-06-28T22:39:00.924985+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Error : 195 (37000)
  (RC=-1) - [Microsoft][SQL Server Native Client 10.0][SQL Server]''CONCAT'' is not
  a recognized built-in function name.'
type: support-article
updated_at: '2025-10-30T13:52:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/35986480264599-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Error-195-37000-RC-1-Microsoft-SQL-Server-Native-Client-10-0-SQL-Server-CONCAT-is-not-a-recognized-built-in-function-name
---

O erro "'CONCAT' is not a recognized built-in function name" ocorre ao executar o custo médio no TOTVS Protheus devido à função CONCAT não ser reconhecida em versões não homologadas do SQL Server, geralmente SQL Server 2008 ou 2008 R2 com Native Client 10.0. Recomenda-se verificar a versão do banco com "SELECT @@VERSION" e avaliar a compatibilidade conforme os bancos homologados pela TOTVS.

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/35986480122775) Tempo aproximado para leitura: **00:01:00 min**  
  
**Dúvida**  
Ao executar o custo médio apresenta o error.log **'CONCAT' is not a recognized built-in function name'.**  
  
**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Solução**  
Aparentemente esse é um erro de banco. Error : 195 (37000) (RC=-1) - [Microsoft][SQL Server Native Client **10.0**][SQL Server]**'CONCAT' is not a recognized built-in function name.**  
   
O banco de dados está retornando erro na função, pois a função CONCAT não é reconhecida no banco de dados SQL Server não homologados

[Veja aqui os bancos de dados homologados](https://tdn.totvs.com/display/public/PROT/MSSQL)   
   
Apesar que na maioria das vezes, A versão do Native Client 10.0 sugere que o SQL Server em uso é provavelmente uma destas versões:

* SQL Server 2008 (Native Client 10.0 foi lançado com SQL Server 2008)
* SQL Server 2008 R2

Para certificarmos da versão que utiliza, por gentileza, executar o comando abaixo direto no banco de dados, e confira se ele é ou não homologado conforme boletim, validação para SQL

**SELECT @@VERSION**

Caso não seja homologado, precisa avaliar internamente para ajustes.

Apenas para conhecimento, segue informação oficial da Microsoft sobre o [CONCAT](https://learn.microsoft.com/en-us/sql/t-sql/functions/concat-transact-sql?view=sql-server-2016).

**Saiba Mais:**

[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)
