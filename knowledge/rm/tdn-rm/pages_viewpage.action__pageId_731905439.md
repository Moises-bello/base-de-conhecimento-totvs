---
content_hash: 862c5b66194dca1b48370711c4b2712187fce7c2f5ec902a5256e5b0aa226452
fetched_at: '2026-06-29T00:11:28.583416+00:00'
page_id: '731905439'
product: rm
source: tdn-rm
title: DT - Relatório DARF - Detalhamento para Conferência
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=731905439
version: 6
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Criar Relatório para conferencia detalhada de IRRF |
| País: | Brasil |
| Ticket: | DRHROTRM-4049 |

## **02. SITUAÇÃO/REQUISITO**

Possibilitar a geração da DARF considerando sempre a data de pagamento, ou seja, mês caixa, detalhando por Tipo de Recolhimento e por funcionário.

## **03. SOLUÇÃO**

Criado relatório com os campos abaixo:

1) A quebra será por tipo de Recolhimento (0561 / 0588 / 3562 / 1889 / 3533);

2) A DARF é gerada por CNPJ da coligada, gerando um único documento para recolhimento, não podendo ser gerada por seção, centro de custo ou filial, o relatório foi construído utilizando como base essas definições.

  IRRF Resumido
