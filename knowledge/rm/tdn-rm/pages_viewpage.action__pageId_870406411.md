---
content_hash: 7fce1d26c3e0eee074dbeb39d83c6aba44aebc555b37b10dd1d0488d4f4abbff
fetched_at: '2026-06-29T00:11:56.752484+00:00'
page_id: '870406411'
product: rm
source: tdn-rm
title: DT - Geração de XML - Geração da tag <racaCor>
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=870406411
version: 14
---

## **01. DADOS GERAIS**

| Produto: | **RM** |
| --- | --- |
| Linha de Produto: | Linha RM |
| Segmento: | RH |
| Módulo: | TOTVS Folha de Pagamento |
| Função: | Geração de XML - Geração da tag <racaCor> |
| País: | Brasil |
| Requisito/Story/Issue (informe o requisito relacionado): | [DRHROTRM-11423](https://jiraproducao.totvs.com.br/browse/DRHROTRM-11423 "View this issue") |

## **02. LIBERAÇÃO**

Lembrando que, será a partir da release:

* 12.1.2402.228
* 12.1.2406.156
* 12.1.2410 e superiores

## **03. SITUAÇÃO/REQUISITO**

Com a liberação da [Nota Técnica S-1.2 Nº 01/2023 Revisada](https://www.gov.br/esocial/pt-br/documentacao-tecnica/manuais/nota-tecnica-s-1-2-01-2023-rev.pdf/view), expedida em 03/04/2024, não é mais permitida a geração do valor "6-" na tag `<racaCor>`.

## **04. SOLUÇÃO**

Atualmente, quando o campo Cor/Raça no cadastro do funcionário está preenchido com os valores "9-Não Informado" e "10-Não Declarado", o sistema gera o valor "6-" na tag `<racaCor>`.

Realizamos algumas tratativas na geração da tag `<racaCor>` para os seguintes eventos:

**EVENTOS**

* S-2205 - Alteração de Dados Cadastrais do Trabalhador
* S-2405 - Cadastro de Beneficiário - Entes Públicos - Alteração

Quando a tag `<dtAlteracao>` desses eventos estiver preenchida com uma data **posterior a 22/04/2024** e a tag `<racaCor>` for igual a "6-", será exibida a seguinte mensagem de erro:

Quando a tag `<dtAlteracao>` estiver preenchida com uma data **anterior a 22/04/2024** e a tag `<racaCor>` for igual a "6-", **não** será exibida a mensagem de erro.

**EVENTOS**

* S-2200 - Cadastramento Inicial do Vínculo e Admissão/Ingresso de Trabalhado
* S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário - Início
* S-2400 - Cadastro de Beneficiário - Entes Públicos - Início

A validação da tag `<racaCor>` continuará sendo realizada com base na data de admissão.

## **05.****DEMAIS INFORMAÇÕES**
