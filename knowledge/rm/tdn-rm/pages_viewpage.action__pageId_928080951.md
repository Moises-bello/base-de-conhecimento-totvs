---
content_hash: 26acc5ca482cc44761dbd0045cf1e99805142976e7e9b1c7287a7f6c3539e56f
fetched_at: '2026-06-29T00:12:08.031545+00:00'
page_id: '928080951'
product: rm
source: tdn-rm
title: DT - Integração RM X Ahgora - Possibilitar a geração de gatilhos por Filial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=928080951
version: 7
---

## **1. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Integração RM X Ahgora - Possibilitar a geração de gatilhos por Filial |
|  | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-12679](https://jiraproducao.totvs.com.br/browse/DRHROTRM-12679) |

## **02. LIBERAÇÃO**

Lembrando que, será a partir dos patches:

* 12.1.2406.257
* 12.1.2410.200
* 12.1.2502.121

## **03. SITUAÇÃO/REQUISITO**

Permitir que o produto TOTVS Folha de Pagamento gere os gatilhos de Funcionários e Afastamentos por filial para a integração destes registros com o produto Ponto Web da Ahgora.

## **04. SOLUÇÃO**

Para possibilitar a integração dos gatilhos de Funcionários e Afastamentos por filial, foi criada a aba **Filiais** no menu  **RH | Folha de pagamento | Configurações | Parametrizador | 06.02 - Integrações | 06.02.11 - Ahgora.**

Nesta aba, poderemos configurar as filiais que serão incluídas na integração do produto Ponto Web da Ahgora.

**ATENÇÃO:**

1. Caso nenhuma filial seja informada nesse parâmetro, o sistema considerará todas as filiais da coligada.
2. Caso o líder de um funcionário da filial informada não esteja vinculado a uma das filiais parametrizadas, ele não será enviado como funcionário para a plataforma do Ponto Web Ahgora, podendo ocasionar erro.

## **05. DEMAIS INFORMAÇÕES**

**[Integração RM X Ahgora](https://tdn.totvs.com/pages/viewpage.action?pageId=877866931)**
