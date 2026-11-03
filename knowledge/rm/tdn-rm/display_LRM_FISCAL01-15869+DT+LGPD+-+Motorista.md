---
content_hash: ec2d24580ab251de48ddcaa3e4aa9267d47a470868bd4797bab845379894b1a8
fetched_at: '2026-06-29T00:11:04.310082+00:00'
page_id: '626351982'
product: rm
source: tdn-rm
title: FISCAL01-15869 DT LGPD - Motorista
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-15869+DT+LGPD+-+Motorista
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro de Motorista |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15869 |

## **02. SITUAÇÃO/REQUISITO**

**Persona:** Motorista

**Regra:** Sempre que os dados estiverem relacionados a algum Lançamento Fiscal ou Lançamento de Ajuste a anonimização deve ser negada

## **03. SOLUÇÃO**

Implementação de regras de anonimização da Entidade Motorista para LGPD. Nega anonimização se o motorista estiver associado a Lançamento Fiscal ou Lançamento de Ajuste.
