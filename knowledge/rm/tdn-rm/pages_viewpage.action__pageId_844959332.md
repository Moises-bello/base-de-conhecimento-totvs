---
content_hash: 0c27608d8a8c61aa56df04ac59356a238016d0a6b1fe8d923896e54876658cdb
fetched_at: '2026-06-29T00:11:50.673107+00:00'
page_id: '844959332'
product: rm
source: tdn-rm
title: DT - S-1210 - Funcionário Reintegrado com "Data de Pagamento" posterior a da
  "Data de Desligamento"
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=844959332
version: 13
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
| Requisito/Story/Issue (informe o requisito relacionado) : | [DRHROTRM-9064](https://jiraproducao.totvs.com.br/browse/DRHROTRM-9064https://jiraproducao.totvs.com.br/browse/DRHROTRM-9064) |

## **02. LIBERAÇÃO**

**Lembrando que, será a partir dos patches:**

* 12.1.2306.264
* 12.1.2310.212
* 12.1.2402.153 e superiores

## **03. SITUAÇÃO/REQUISITO**

O produto deverá gerar o evento S-1210 com a tag <tpPgto> com o valor "**2 - Pagamento de verbas rescisórias conforme apurado em ideDmDev do S-2299**" quando um funcionário é reintegrado, utilizando o mesmo cadastro, e o tipo de admissão é alterado para "I - Reintegração" e a data de pagamento é posterior a data de demissão.

## **04. SOLUÇÃO**

Para garantir a correta geração da tag <tpPgto> com o valor "**2 - Pagamento de verbas rescisórias conforme apurado em ideDmDev do S-2299**" quando ocorrer a reintegração de um funcionário, siga as verificações abaixo:

1. Verifique se o tipo de admissão do funcionário foi configurado como "I - Reintegração".
2. Verifique se a data de pagamento no envelope de pagamento (PFFINANC.DATAPAGAMENTO) é igual ou posterior à Data de Desligamento (PFUNC.DTDESLIGAMENTOREINT) na aba de Reintegração, permitindo uma diferença de até 10 dias.

Veja demonstração abaixo:

1) No Cadastro do Funcionário, acesse a tela "Dados do Registro", e no campo "Tipo de Admissão", verifique se está preenchido como "I - Reintegração".

2) No Cadastro do Funcionário, na aba "Reintegração" verifique o campo "Data de Desligamento":

3) No Cadastro do Funcionário, no anexo "Ficha Financeira" verifique que o campo "Data Pagamento" é corresponde ao intervalo de até dez dias do campo "Data de Desligamento" da aba "Reintegração":

4) Na geração do XML do evento S-1210, verifique se a tag <tpPgto> foi gerada com o valor 2:

## **05. DOCUMENTAÇÃO**

### [S-2298 – **Reintegração**](https://tdn.totvs.com/pages/viewpage.action?pageId=364908522)

###
