---
content_hash: d9a06a31faa3c79fab05845a8b945026e6b31b573f238ff766bff569b1da4078
fetched_at: '2026-06-29T00:11:04.297927+00:00'
page_id: '626142057'
product: rm
source: tdn-rm
title: FISCAL01-15868 DT LGPD - Filial
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-15868+DT+LGPD+-+Filial
version: 4
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Cadastro de Filial |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15868 |

## **02. SITUAÇÃO/REQUISITO**

**Persona:** Filial

**Regra:** Sempre que os dados estiverem relacionados a algum Lançamento Fiscal ou Lançamento de Ajuste ou a Eventos da EFD-Reinf a anonimização deve ser negada.

## **03. SOLUÇÃO**

Implementação de regras de anonimização da Entidade Filial para LGPD. Nega anonimização se a Filial estiver associada a Lançamento Fiscal, Lançamento de Ajuste ou a Eventos da EFD-Reinf.
