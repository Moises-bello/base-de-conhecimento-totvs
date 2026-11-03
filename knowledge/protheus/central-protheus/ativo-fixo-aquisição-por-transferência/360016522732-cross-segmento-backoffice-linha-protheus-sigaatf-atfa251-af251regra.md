---
article_id: 360016522732
category: Ativo Fixo - Aquisição por Transferência
content_hash: 35ae5c0dee7b30da46bde62b6a254a3e0eae0f465620375c9779230eb1af941c
fetched_at: '2026-06-28T22:41:56.938704+00:00'
product: protheus
section_id: 1500001535341
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA251 - AF251REGRA
type: support-article
updated_at: '2023-11-20T16:10:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016522732-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA251-AF251REGRA
---

**Ocorrência**

Na rotina de **aquisição por** **transferência****(ATFA251)**, o sistema não deixa confirmar o cadastro quando tem que gerar o **CIAP,** apresentando o seguinte help:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360012765752)

**Ambiente**Protheus – Contabilidade Gerencial – 12.1.17

**Causa**

Esta mensagem é apresentada **devido a um ou mais bens** utilizados para efetuar a aquisição por transferência(ATFA251) **não possuírem o campo N1\_CODCIAP preenchido**, este campo é alimentado somente via TES(Tipo de Entrada e Saída) juntamente com o processo de Documento de Entrada(MATA103) e Classificação de Ativo(ATFA240).

**Solução**

Os bens que serão transferidos para a geração de um novo ativo deverão possuir o **N1\_CODCIAP alimentado via processo de documento de entrada**, trata-se de um conceito do sistema que traz maior integridade para os dados, pois ocorrem as devidas validações desde na parte fiscal(TES).
