---
content_hash: 98d6ea7fc5c890d8e7fc479e8b1e7b44cf58668c2cb6bee06305f5956e6cd521
fetched_at: '2026-06-29T00:10:41.761706+00:00'
page_id: '546275034'
product: rm
source: tdn-rm
title: FISCAL01-12878 DT Cópia de Exercício Fiscal
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=546275034
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Exercício Fiscal |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-12878;  FISCAL01-13156. |

## **02. SITUAÇÃO/REQUISITO**

Criar o processo de cópia entre coligada para o Exercício Fiscal.

## **03. SOLUÇÃO**

Foi adicionado um novo processo no cadastro de Exercício Fiscal para a criação de cópias de Exercícios Fiscais entre Coligadas.

A interação entre Coligadas de Natureza Global X Não Globais (Natureza Global no menu Ambiente | Parâmetro | TOTVS Gestão Fiscal | 03.03 - Escrituração | etapa 10 - Natureza de Operação da Escrituração Fiscal) será tratada da seguinte maneira:

| Origem | Destino | Resultado |
| --- | --- | --- |
| Global | Global | Processo realizará a Cópia sem nenhuma alteração. |
| Global | Filial | Processo não realizará a Cópia. |
| Não Global | Global | Processo realizará a Cópia, mas o registro na coligada destino será global. |
| Não Global | Não Global | Processo realizará a Cópia para a Filial com o mesmo código da Filial de origem, caso esta exista na Filial de Destino. |

O processo de Cópia entre Coligadas do Exercício Fiscal não permite sobrescrever o registro na Coligada de destino.
