---
content_hash: 3854494ff227d0b0a8c4039a6a2010bad045c11fb23b0252bd53230615f7b804
fetched_at: '2026-06-29T00:10:31.143181+00:00'
page_id: '520670595'
product: rm
source: tdn-rm
title: FISCAL01-11409 DT Sped Fiscal - Alteração dos Parâmetros
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=520670595
version: 1
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | BackOffice |
| Módulo: | Gestão Fiscal |
| Função: | Sped Fiscal |
| Ticket: | FISCAL01-11409 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-11409 |

## **02. SITUAÇÃO/REQUISITO**

1. Na tela de geração da rotina, mudar a versão para “**014**”. Essa versão só é válida a partir de 01/01/2020.
2. Os registros referentes ao ressarcimento de ICMS ST serão solicitados a critério de cada UF. Será preciso um parâmetro de tela na geração do SPED para o usuário informar se deseja gerar os registros ou não. A definição de qual registro deve ser gerado depende do modelo de documento, tipo de lançamento (entrada/saída) e o Código do motivo da restituição ou complementação.

## **03. SOLUÇÃO**

* Alteração do SPED Fiscal, onde foi adicionado a flag "Gerar ressarcimento/complemento ICMS ST". (Sped Fiscal → Parametrização)

* A versão foi alterada automaticamente para “014”, quando a parametrização da data final for a partir de 01/01/2020.
