---
content_hash: 01c59115bd440c1819643f530f1a8b1c9772e15bd03d831fbd9df6fe3100ee5b
fetched_at: '2026-06-29T00:11:50.510270+00:00'
page_id: '842272408'
product: rm
source: tdn-rm
title: DT - Integração RM X Feedz - Descrição e Código da Filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=842272408
version: 9
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Feedz - Descrição e Código da Filial |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-10054](https://jiraproducao.totvs.com.br/browse/DRHROTRM-10054 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2310.206
* 12.1.2402.145
* 12.1.2406 e superiores

## **03. SITUAÇÃO/REQUISITO**

Possibilidade em integrar o código da filial juntamente com a descrição, seguindo o mesmo padrão já estabelecido para cargos e departamentos. Essa atualização é especialmente útil para clientes que possuem filiais com nomes ou descrições semelhantes, permitindo uma integração perfeita com a Feedz.

## **04. SOLUÇÃO**

Foi criado o parâmetro "**Concatenar Descrição da Unidade (Descrição + Código)"** no parametrizador, ao marca-lo o sistema incluirá tanto a descrição (GFILIAL.NOME) da filial quanto o seu código (GFILIAL.CODIGO) correspondente.

No exemplo abaixo, o funcionário foi enviado com os parâmetros mencionados acima marcados. Observa-se que a unidade (Filial) foi enviada com a descrição (GFILIAL.NOME) seguida pelo código (GFILIAL.CODIGO).

Tela do cadastro da Filial 2:

## **05. DEMAIS INFORMAÇÕES**
