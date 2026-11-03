---
content_hash: 7c65bd0cb80b05a8f34eb3f548e46dcac5fce4aca60c76592fee20d711e2fcb1
fetched_at: '2026-06-29T00:11:06.914208+00:00'
page_id: '636948276'
product: rm
source: tdn-rm
title: 12231114 FISCAL01-16518 - Erro no envio do R-1000
type: documentation
url: https://tdn.totvs.com/display/LRM/12231114+FISCAL01-16518+-+Erro+no+envio+do+R-1000
version: 5
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | REINF |
| País: | Brasil |
| Ticket: | 12231114 |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-16518 |

## **02. SITUAÇÃO/REQUISITO**

Cliente informa que ao realizar a transmissão do evento R-1000 é apresentado inconsistência abaixo:

"Falha ao processar o evento de identificador 6 e tipo R-1000: Erro na validação de schema:  
Element '

{<http://www.reinf.esocial.gov.br/schemas/evtInfoContribuinte/v1_05_01>}

evtInfoContri', attribute 'id': [facet 'length'] The value 'ID2004863949482021081913020800000' has a length of '33'; this differs from the allowed length of '36'.  
Element '

{<http://www.reinf.esocial.gov.br/schemas/evtInfoContribuinte/v1_05_01>}

evtInfoContri', attribute 'id': [facet 'pattern'] The value 'ID2004863949482021081913020800000' is not accepted by the pattern 'I

{1}D{1}

[0-9]

{34}

'.  
Element '

{<http://www.reinf.esocial.gov.br/schemas/evtInfoContribuinte/v1_05_01>}

evtInfoContri', attribute 'id': 'ID2004863949482021081913020800000' is not a valid value of the local atomic type."

Cenário do cliente: O cliente possui um certificado de Pessoa Fisica e a coligada também é referente à Pessoa Física, porém o XML está sendo montado incorretamente, com 3 caracteres a menos.

TESTES REALIZADOS  
Verificado que o cliente, por ter a coligada pessoa física e o certificado pessoa física, o sistema está montando o XML de envio incorretamente no campo <evtInfoContri>:

 ​

A inconsistência é apresentada, devido a montagem do evento estar faltando 3 zeros(0) a direita do CPF, pois o campo espera receber 36 caracteres e está recebendo 33, seguindo informações contidas no Manual da rotina.

Conforme Anexo II dos leiautes da EFD-Reinf - Regras de Validação Versão 1.

Deve-se colocar 3 zeros a direita quando for CPF.

ID da Tag **evtInfoContri deve conter 36 caracteres (contando com o "ID").**

## **03. SOLUÇÃO.**

Na geração do ID da R-1000, foi acrescentado mais 3 zeros à direita caso o CGC da filial seja CPF.

O  resultado para todos os casos devem dar 36 caracteres (contando com o "ID").
