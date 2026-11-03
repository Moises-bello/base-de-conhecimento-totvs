---
content_hash: c9c3a993b9088b0e7a30d9765b57a8c449ddd4af8e0c59294760f8c9939795da
fetched_at: '2026-06-29T00:11:04.467435+00:00'
page_id: '627093808'
product: rm
source: tdn-rm
title: FISCAL01-15866 LGPD - Participante Fiscal
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-15866+LGPD+-+Participante+Fiscal
version: 2
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Lançamento Fiscal |
| País: | Brasil |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15866 |

## **02. SITUAÇÃO/REQUISITO**

Criar regra de anonimização

**Persona:** Participante

**Regra:** Sempre que os dados estiverem relacionados a algum Lançamento Fiscal ou Lançamento de Ajuste a anonimização deve ser negada

## **03. SOLUÇÃO**

Foi implementado as regras do Provider do Participante.

A validação consiste em não permitir a anonimação de dados do Cliente/Fornecedor quando houver algum Lançamento Fiscal relacionado.

Foi implementada a regra para não deixar anonimizar os dados do Lançamento Fiscal ou do Item quando o CPF/CNPJ do Adquirente estiver vinculado.

Foi Implementada a regra para não deixar anonimizar os dados do Lançamento Fiscal Vinculado ao Lançamento de Ajuste quando o CPF/CNPJ CEI estiver vinculado
