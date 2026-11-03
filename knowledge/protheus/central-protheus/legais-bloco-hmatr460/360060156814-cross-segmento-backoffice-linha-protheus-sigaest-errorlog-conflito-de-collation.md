---
article_id: 360060156814
category: LEGAIS - BLOCO H/MATR460
content_hash: bd2d6f21786dff875bf60c1e802167d2ec0d846ec5543369a143a6d76772d4ad
fetched_at: '2026-06-28T22:42:14.963447+00:00'
product: protheus
section_id: 1500001538741
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST -  Error.log - Conflito
  de collation entre"Latin1_General_BIN" e "SQL_Latin1_General_CP1_CI_AS" '
type: support-article
updated_at: '2021-05-03T18:03:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060156814-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Error-log-Conflito-de-collation-entre-Latin1-General-BIN-e-SQL-Latin1-General-CP1-CI-AS
---

**Dúvida**

Ao gerar o SPED Fiscal para geração também do Bloco H ocorre o seguinte error.log:

"*THREAD ERROR ([6024] : Error : 468 (37000) (RC=-1) - [Microsoft][SQL Server Native Client 11.0][SQL Server]Cannot resolve the collation conflict between "Latin1\_General\_BIN" and "SQL\_Latin1\_General\_CP1\_CI\_AS" in the equal to operation.*"

O que fazer para resolver este problema?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - A partir da versão 12.1.17

**Solução**

Este problema ocorre devido um conflito de *collation* entre duas D*atabases* (D*atabase* onde estão os dados do *Protheus* x *Database* de sistema "TempDB").

**Obs:** *Collation* - É o mapa de caracteres utilizados em um D*atabase* (Banco de Dados).

O *Database* criado para armazenar as tabelas do Microsiga Protheus possui o mapa de caracteres "Latin\_General\_BIN" e o database de sistema "TempDB" possui o collation "Latin\_General\_CI\_AS".

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500001576341/mceclip0.png)

Essa incompatibilidade resulta no erro quando o sistema processa consultas pesadas no banco ou quando precisa criar tabelas temporárias para processamento (SPEDFISCAL é um deles).

**Como resolver esta incompatibilidade?**

O usuário têm duas opções para resolver este problema:

**1° opção  - Alterar o Tipo do Agrupamento configurado no Banco de Dados.**

Realizar a conversão do Banco de Dados de sistema "TEMPDB - Ex. SQL Server" para a *collation* "Latin\_General\_BIN (Padrão Protheus).

Em seguida, inicie os serviços e o Protheus e processe novamente o SPED.

**2° Opção** - **Atualize o ambiente com o último DBAccess , Build e LIB disponibilizados no Portal do Cliente**

As novas atualizações de tecnologia do *Protheus* já contemplam tratamento para converter os caracteres e evitar as diferenças entre as c*ollations*.

DBAcess (para Windows)-  [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/DBAccess_Windows) **|** LIB- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/LIB_LABEL) **|**AppServer- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/appserver) **|**SmartClient- [Clique aqui](https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/smartclient)

Após atualizar os artefatos acima, gerar o SPED novamente para correta geração do arquivo.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Bloco H e MATR460 (P7) no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000219382-LEGAIS-BLOCO-H)*
