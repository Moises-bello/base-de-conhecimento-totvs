---
content_hash: c020de671a1920299a07ff7d471b726933b1be4c56015c0a45211d1b59c3d757
fetched_at: '2026-06-29T00:12:10.797149+00:00'
page_id: '953003707'
product: rm
source: tdn-rm
title: Grupo YA - Informações de Pagamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=953003707
version: 8
---

|  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| **Grupo YA - Informações de Pagamento** | | | | | | | | | | | | |
| # | **ID** | **Campo** | **Descrição** | **Ele** | **Pai** | **Tipo** | **Ocorrência** | **Tamanho** | **Observação** | **Campo de Origem** | **Campo na Aplicação** | **Mais Informações** |
| 398a | YA01 | pag | Grupo de Informações de Pagamento | G | A01 |  | 1-1 |  | Para as notas com finalidade de **Ajuste** ou **Devolução,** o campo Meio de Pagamento deve ser preenchido com 90=Sem Pagamento. |  |  |  |
| 398a1 | YA01a | detPag | Grupo Detalhamento do Pagamento | G | YA01 |  | 1-100 |  |  |  |  |  |
| 398a2 | YA0b | indPag | Indicador da Forma de Pagamento | E | YA01a | N | 0-1 | 1 | 0= Pagamento à Vista 1= Pagamento à Prazo |  |  | Obs.: [Dados de Cobrança](https://tdn.totvs.com/pages/viewpage.action?pageId=953003702) não  devem ser informados para "Pagamento à Vista". |
| 398b | YA02 | tPag | Meio de pagamento | E | YA01a | N | 1-1 | 2 | Utilizar a Tabela de códigos dos meios de pagamentos publicada no Portal Nacional da Nota Fiscal Eletrônica. |  |  | De/Para:  [Tipo Meio Pagamento](https://tdn.totvs.com/display/LRM/Meio+de+Pagamento) |
| 398.12a | YA02a | xPag | Descrição do Meio de Pagamento | E | YA01a | C | 0-1 | 2-60 | Descrição do meio de pagamento. Preencher informando o meio de pagamento utilizado quando o código do meio de pagamento for informado como 99-outros. |  |  |  |
| 398c | YA03 | vPag | Valor do Pagamento | E | YA01a | N | 1-1 | 13v2 |  |  |  |  |
| 398d | YA04 | card | Grupo de Cartões | G | YA01a |  | 0-1 |  |  |  |  | Será gerado sempre que o pagamento for realizado com cartão de crédito ou débito ou PIX. |
| 398d.1 | YA04a | tpIntegra | Tipo de Integração para pagamento | E | YA04 | N | 1-1 | 1 | Tipo de Integração do processo de pagamento com o sistema de automação da empresa: 1=Pagamento integrado com o sistema de automação da empresa (Ex.: equipamento TEF, Comércio Eletrônico); 2= Pagamento não integrado com o sistema de automação da empresa (Ex.: equipamento POS); |  |  | Será gerado com o valor fixo 2 sempre que o pagamento for realizado com cartão de crédito ou débito ou PIX |
| 398e | YA05 | CNPJ | CNPJ da Credenciadora de cartão de crédito e/ou débito | E | YA04 | C | 0-1 | 14 | Informar o CNPJ da Credenciadora de cartão de crédito / débito |  |  |  |
| 398f | YA06 | tBand | Bandeira da operadora de cartão de crédito e/ou débito | E | YA04 | N | 0-1 | 2 | 01=Visa 02=Mastercard 03=American Express 04=Sorocred 05=Diners Club 06=Elo 07=Hipercard 08=Aura 09=Cabal 99=Outros |  |  |  |
| 398g | YA07 | cAut | Número de autorização da operação cartão de crédito e/ou débito | E | YA04 | C | 0-1 | 1-20 | Identifica o número da autorização da transação da operação com cartão de crédito e/ou débito |  |  |  |
| 398i | YA09 | vTroco | Valor do troco | E | YA01 | C | 0-1 | 13V2 | Valor do Troco | Sempre zero, pois não utilizamos troco no movimento. |  |  |
