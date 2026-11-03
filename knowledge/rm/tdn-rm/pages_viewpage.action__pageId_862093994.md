---
content_hash: 92f49befc4f96480681dce16eaa680d7f520733e5f9fb18221a8a122043e697f
fetched_at: '2026-06-29T00:11:55.477436+00:00'
page_id: '862093994'
product: rm
source: tdn-rm
title: Migração dos tipos de dados LONG e LONG RAW nas colunas em Oracle
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=862093994
version: 14
---

A partir da versão 12.1.2410 foi disponibilizado um script no RM Atualizador que irá modificar as colunas das tabelas que utilizam os tipos de dados LONG e LONG RAW para CLOB e BLOB, respectivamente. Esta migração é necessária porque os tipos LONG e LONG RAW estão sendo depreciados pela Oracle, o que atualmente dificulta o reparo de dados e a modelagem do banco de dados.

Mais informações técnicas a respeito destes tipos de dados descontinuados no site do fabricante:  [Datatype Limits](https://docs.oracle.com/en/database/oracle/oracle-database/19/refrn/datatype-limits.html)

Esta migração em tabelas com um grande número de registros pode levar mais tempo do que o normal. Essa situação é prevista e esperada, portanto, não devemos cancelar o processo de atualização do banco de dados, a fim de garantir a correta execução do script e a alteração das respectivas colunas.

Para identificar quais colunas serão migradas no seu banco de dados, basta executar a consulta SQL abaixo a partir do [cadastros de consultas sql do Corpore](https://tdn.totvs.com/x/qC4mDg) ou diretamente no Oracle Management de sua preferência, usando o login do Owner do banco de dados Corpore:

sqlFadeToGreySugestão de homologação

Se necessário, é uma boa prática criar um ambiente de teste para simular a execução do RM Atualizador em sua base de homologação e avaliar os tempos adicionais resultantes dessa migração de tipos de dados.

Algumas colunas ainda não serão migradas nesta etapa, estamos tratando com celeridade estas exceções.
