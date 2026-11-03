---
content_hash: 3b4eeeee1a5c1908bf45c6ddc0b70a64f90511f4d49ea70b25dc6d82f268dbd1
fetched_at: '2026-06-29T00:11:11.751743+00:00'
page_id: '648818407'
product: rm
source: tdn-rm
title: FISCAL01-16960 DT - Sped Fiscal 2022 Versão e Registro 1600
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=648818407
version: 1
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | Sped Fiscal |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16960 |

## **02. SITUAÇÃO/REQUISITO**

**Default da tela de geração**

Deverá ser alterado o Default da versão do SPED na tela de geração do SPED Fiscal.

A mudança só poderá afetar períodos posteriores a 12/2021

**Registro 1600**

O registro 1600 não deverá ser gerado a partir da 01/2022.

Considere que o Registro não deve ser removido pois o cliente poderá gerar retificação para períodos anteriores a 01/2022 e neste caso o registro deve ser gerado normalmente.

## **03. SOLUÇÃO**

Adicionado validação na geração do registro 1600:

O 1600 não deverá ser gerado a partir da 01/2022.

Obs.: o cliente poderá gerar retificação para períodos anteriores a 01/2022 e neste caso o registro deve ser gerado normalmente.

Alterado o Default da versão do SPED na tela de geração do SPED Fiscal.
