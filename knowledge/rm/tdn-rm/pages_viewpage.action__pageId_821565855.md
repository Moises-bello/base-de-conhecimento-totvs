---
content_hash: 87d1e3aab7361f817b577d8ea3c277c7920fa65e24c35624574a8f8bf5643791
fetched_at: '2026-06-29T00:11:45.730851+00:00'
page_id: '821565855'
product: rm
source: tdn-rm
title: 'DT - S-1210:  Funcionário Reintegrado com "Data de Pagamento" igual a da "Data
  de Desligamento"'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=821565855
version: 17
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: |  |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | eSocial - S-1210 - Funcionário Reintegrado |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-5882](https://jiraproducao.totvs.com.br/browse/DRHROTRM-5882) |

## **02. SITUAÇÃO/REQUISITO**

O produto deverá gerar o evento S-1210 com a tag <tpPgto> com o valor "**2 - Pagamento de verbas rescisórias conforme apurado em ideDmDev do S-2299**" quando um funcionário é reintegrado, utilizando o mesmo cadastro, e o tipo de admissão é alterado para "I - Reintegração" e a data de pagamento é igual a data de demissão.

## **03. SOLUÇÃO**

Para garantir a correta geração da tag <tpPgto> como **"2 - Pagamento de verbas rescisórias conforme apurado em ideDmDev do S-2299"** quando ocorrer a reintegração do funcionário, siga as seguintes verificações:

1. Verifique se o tipo de admissão do funcionário foi configurado como "I - Reintegração".
2. Confirme se, na aba de Reintegração, a Data de Desligamento (PFUNC.DTDESLIGAMENTOREINT) é igual à data de pagamento no envelope de pagamento (PFFINANC.DATAPAGAMENTO).

Veja demonstração abaixo:

No cadastro do Funcionário, acessar a tela "Dados do Registro" e no campo "Tipo de Admissão" verificar se está preenchido "I - Reintegração":

No cadastro do Funcionário, na "Reintegração" verificar o campo "Data de Desligamento":

No cadastro do Funcionário no anexo "Ficha Financeira" verificar se o campo "Data Pagamento" é igual a data de desligamento da aba "Reintegração":

Na geração do XML do evento S-1210 a tag <tpPgto> será gerada com o valor 2:

## **04. DOCUMENTAÇÃO**

### [S-2298 – **Reintegração**](https://tdn.totvs.com/pages/viewpage.action?pageId=364908522)
