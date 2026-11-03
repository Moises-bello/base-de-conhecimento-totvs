---
content_hash: 6135ac723c0a7d2700a8097e8ead6906455c934df513effafa3fee38fb9ebc8f
fetched_at: '2026-06-29T00:11:17.085877+00:00'
page_id: '676588069'
product: rm
source: tdn-rm
title: 13796852 FISCAL01-17672 - DT - SPED Registro 1601
type: documentation
url: https://tdn.totvs.com/display/LRM/13796852+FISCAL01-17672+-+DT+-+SPED+Registro+1601
version: 2
---

## **01. DADOS GERAIS**

|  |  |
| --- | --- |
| Produto: | TOTVS |
| Linha de Produto: | Linha RM |
| Segmento: | Backoffice |
| Módulo: | TOTVS Gestão Fiscal |
| Função: | SPED Fiscal |
| País: | Brasil |
| Ticket: | [13796852](https://jiraproducao.totvs.com.br/issues/?jql=cf%5B11086%5D+%3D+%2213796852%22 "13796852") |
| Requisito/Story/Issue (informe o requisito relacionado) : | FISCAL01-17672 |

## **02. SITUAÇÃO/REQUISITO**

Ao gerar o registro 1601, campo 02, do Sped Fiscal, o mesmo está gerando incorretamente. 

Segundo o Manual do Sped o preenchimento deve ser conforme abaixo:

Campo 02 (COD\_PART\_IP)\* - Validação:\* o valor informado deve existir no campo COD\_PART do registro 0150. Preenchimento: Informar o CNPJ da instituição que efetuou o pagamento.

(pág. 279)

O campo está sendo preenchido com "00000000000" e o correto seria o CNPJ da instituição que efetuou o pagamento. 

TESTES REALIZADOS 

Na base de dados do cliente foi gerado o arquivo do Sped Fiscal e o registro 1601 foi gerado. Ao analisarmos, verificamos que o campo 02 foi preenchido apenas com 11 números '0', e o correto seria o CNPJ da instituição pagadora.

Além disso, no registro 1010, o campo que identifica que existe registro 1601 gerado, permaneceu como “N” e deveria gerar como “S”.

BENEFICIOS ALCANÇADOS

Isso está acontecendo pois o sistema está verificando o Cli/For que foi informado no lançamento/movimento e não o Cli/For que foi informado na forma de pagamento do mesmo.

## **03. SOLUÇÃO**

Foi ajustado os registros 1010 e 1601 do SPED:

1601 COD\_PART\_IP - Informação do CNPJ da instituição que efetuou o pagamento. (TFORMAPAGTO.CODCFO)

1010 IND\_CART - Considera se gerou 1600 ou 1601.

Disponível a partir da versão 12.1.34
