---
content_hash: dd9b06528dd704940751d7b7d698af97e49edf790e61dd5794fe11d224ffb35b
fetched_at: '2026-06-29T00:09:14.334539+00:00'
page_id: '421385203'
product: rm
source: tdn-rm
title: Consultas SQL.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385203
version: 1
---

**Consultas SQL**   
Nesta pasta será possível parametrizar para que caso um campo esteja configurado para não ser consultado, ele não seja exibido na execução de consulta SQL.  
   
Ativa segurança na execução de Consultas SQL (segurança de campos e filtro por usuário):  
Marcando esta opção, os campos que não forem permitidos para visualização não serão exibidos nas consultas SQL.  
   
Ativa bloqueio de execução de Consultas SQL caso não seja possível aplicar segurança:  
Esta opção, caso não seja permitido aplicar a segurança do campo acima, a consulta não será executada.  
**Atenção:** Essa funcionalidade será permitida somente em banco de dados MS-SQLServer e somente para consultas SQL's que não sejam Visíveis para todas as Coligadas.  
   
**Para bancos de dados Oracle, os campos da consulta SQL devem ser escritos por completo. Exemplo: "SELECT PFUNC.NOME FROM PFUNC".**
