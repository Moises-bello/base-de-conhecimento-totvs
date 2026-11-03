---
content_hash: 95a46e24864ffa6c4ec5e1a86245059602511b78e149866e7623b570b73f438a
fetched_at: '2026-06-29T00:11:04.254052+00:00'
page_id: '625769746'
product: rm
source: tdn-rm
title: FISCAL01-15867 LGPD - Transportador
type: documentation
url: https://tdn.totvs.com/display/LRM/FISCAL01-15867+LGPD+-+Transportador
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
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-15867 |

## **02. SITUAÇÃO/REQUISITO**

Criar regra de anonimização

**Persona:** Transportador

**Regra:** Sempre que os dados estiverem relacionados a algum Lançamento Fiscal ou Lançamento de Ajuste a anonimização deve ser negada

## **03. SOLUÇÃO**

Foi implementado as regras do provider do Transportador referente a Coleta e Entrega. A validação consiste em não permitir a anonimação de dados quando houver qualqler CNPJ/CPF relacionado a algum Lançamento Fiscal ou Ajuste. A consistencia é feita com base da DLAFTRANSP. Além disso, nestes providers ocorre a validação para verficar se o CNPJ/CPF está vazio.
