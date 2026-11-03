---
content_hash: ea8271b31925d8e452b9c0655cb6492f67ef53dae252ca66a4a6beb5aa10af62
fetched_at: '2026-07-02T19:24:21.541293+00:00'
page_id: '268578881'
product: protheus
source: tdn-tec
title: TranslateLikeOracle
type: documentation
url: https://tdn.totvs.com/display/tec/TranslateLikeOracle
version: 6
---

TranslateLikeOracle

Define novo comportamento para o comando de banco **"LIKE"** que poderá ser traduzido para o comando **"REGEXP\_LIKE"**. Está chave é valida apenas nas seções de **"Environment"**.

Esta configuração será disponibilizada a partir do build **7.00.131227A** version **1.3.0** e aplica-se somente a ambientes **4GL** que utilizem **banco de dados ORACLE.**

Recurso criado como solução a um problema identificado no **banco de dados ORACLE,** que apresenta um comportamento não esperado em comparações de tipos CHAR, VARCHAR e VARCHAR2 quando utilizado com comando **"LIKE",** não retornando corretamente os registros no **"SELECT"**.

## Valores válidos

| Valor | Descrição |
| --- | --- |
| 0 (Padrão) | Comportamento **padrão**, com recurso de tradução do comando LIKE **desligado**. |
| 1 | **Liga** o recurso de tradução para o comando **LIKE**. |

## Exemplos

Definição da chave na seção [Environment]:
