---
content_hash: 214edc872a33ca6f12d346c6f61aa47cc837a66b997680ab0081df5ffb95ebb1
fetched_at: '2026-06-29T00:08:47.323568+00:00'
page_id: '319787302'
product: rm
source: tdn-rm
title: Manual - Stored Procedure
type: documentation
url: https://tdn.totvs.com/display/LRM/Manual+-+Stored+Procedure
version: 3
---

O contexto de Stored Procedure permite a utilização de Stored Procedures para fazer a leitura dos dados. É possível utilizar qualquer Stored Procedure que retorne um SELECT como resultado. A Stored Procedure também poderá conter parâmetros de entrada, que serão informados pelo gerador no momento da execução.

![](/download/attachments/319787302/stored_procedure.png?version=1&modificationDate=1512921920000&api=v2)

1Stored Procedure

Selecione a Stored Procedure do banco de dados que irá retornar os dados do contexto.

2Parâmetros

Informe os parâmetros de execução da Stored Procedure. Estes parâmetros serão utilizados para que o gerador execute a Stored Procedure e obtenha a lista de campos do resultado da execução.

Atenção

Os valores dos parâmetros também devem ser informados na aba de Parâmetros do Contexto, que serão os valores utilizados para a execução da Stored Procedure no momento da geração, para mais informações consulte [Parâmetros do Contexto](/pages/viewpage.action?pageId=319787287).

#### Exemplo (SQL Server)

CREATE PROCEDURE SP\_CARREGALANCAMENTOS@CODCOLIGADA SMALLINT

AS

BEGIN  SELECT \* FROM FLAN (NOLOCK)  WHERE CODCOLIGADA = @CODCOLIGADA

END

GO
