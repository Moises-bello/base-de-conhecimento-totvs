---
content_hash: 37286c1447a9e116e53e75264e04d17068dc1aa8ed6d382ab91deaabe53c6a39
fetched_at: '2026-06-29T00:10:37.305655+00:00'
page_id: '539529238'
product: rm
source: tdn-rm
title: DEDUINTEGRACOES-6629 DT Funções de fórmula no Financeiro para buscar valores
  auxiliares de bolsas e descontos por antecipação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=539529238
version: 13
---

## ****01. DADOS GERAIS****

|  |  |
| --- | --- |
| Linha de Produto: | RM |
| Segmento: | Educacional |
| Módulo: | TOTVS Educacional |
| Função: | Fórmula |
| Ticket: |  |
| Requisito/Story/Issue (informe o requisito relacionado) : | [DEDUINTEGRACOES-6629](https://jiraproducao.totvs.com.br/browse/DEDUINTEGRACOES-6629) |

## **02. SITUAÇÃO/REQUISITO**

Com a disponibilização do recurso “[Valor Auxiliar](https://tdn.totvs.com/display/LRM/Valor+Auxiliar)” no TOTVS Educacional passou a existir a possibilidade de contabilizar através do TOTVS Financeiro valores provenientes dos valores auxiliares processados pelo TOTVS Educacional.

## **03. SOLUÇÃO**

No módulo Financeiro foram disponibilizadas funções de fórmulas para obter os valores auxiliares calculados para a bolsa e para o desconto por antecipação durante a geração do lançamento da parcela do contrato.

Segue as fórmulas e suas descrições.

formulaVALORAUXILIARBOLSALANFórmula VALORAUXILIARBOLSALAN

A fórmula **VALORAUXILIARBOLSALAN** retorna o valor auxiliar da bolsa conforme os parâmetros passados para a mesma.

**Declaração da fórmula:** ValorAuxiliarBolsaLan(string codValorAuxiliar, int tipoBolsa, string codBolsa)

=> string codValorAuxiliar:

* Código do valor auxiliar

=>int tipoBolsa:

* 0: Bolsa escalável (condicional)
* 1: Bolsa especial (incondicional)
* -1: Todas as bolsas

=> string codBolsa

* Código da bolsa, se for passado vazio ou -1, indica que o sistema vai somar todas as bolsas

**Exemplos:**

* ValorAuxiliarBolsaLan('VAUX001', 0, '62'): Indica que a fórmula deverá retornar o valor auxiliar para a bolsa escalável de código 62.
* ValorAuxiliarBolsaLan('VAUX001', 0, TabBolsaLan('CODBOLSA', 'S')): Indica que a fórmula deverá retornar o valor auxiliar para a bolsa que a fórmula TabBolsaLan retornar.
* ValorAuxiliarBolsaLan('VAUX001', -1, '-1'): Indica que a fórmula deverá retornar o somatório de todos dos valores auxiliares calculados para as bolsas.
VALORAUXILIARBOLSALANDESCANTFórmula VALORAUXILIARBOLSALANDESCANT

A fórmula **VALORAUXILIARBOLSALANDESCANT**retorna o valor auxiliar do item de desconto por antecipação para a bolsa condicional conforme os parâmetros passados para a mesma.

**Declaração da fórmula:**ValorAuxiliarBolsaLanDescAnt(string codValorAuxiliar, int tipoBolsa, string codBolsa, object vencimento)

=> string codValorAuxiliar:

* Código do valor auxiliar

=>int tipoBolsa:

* 0: Bolsa escalável (condicional)
* 1: Bolsa especial (incondicional)
* -1: Todas as bolsas

=> string codBolsa

* Código da bolsa, se for passado vazio ou -1, indica que o sistema vai somar todas as bolsas

=> object vencimento

* Número do vencimento: Se o valor passado for um número inteiro, indica que o usuário deseja o número do vencimento do item do desconto por antecipação calculado para a bolsa. E o sistema o interpretará como fosse os vencimentos do desconto por antecipação.   
  Exemplo:
  + 1: Indica primeiro vencimento
  + 2: Indica segundo vencimento
  + 3: Indica terceiro vencimento, e assim por diante
* Data: Se o valor passado for uma data, indica que o usuário deseja o item do desconto por antecipação calculado para a bolsa até a data informada. Isto é, até data limite calculado para o desconto por antecipação.

  ATENÇÃO

  A data informada deve estar no formatado **DD/MM/AAAA**, caso contrário o sistema irá exibir uma mensagem para o usuário.

**Exemplos:**

* ValorAuxiliarBolsaLanDescAnt('VAUX001', 0, '62', 1): Indica que a fórmula deverá retornar o valor auxiliar para o primeiro vencimento da bolsa escalável de código 62.
* ValorAuxiliarBolsaLanDescAnt('VAUX001', 0, TabBolsaLan('CODBOLSA', 'S'), 3): Indica que a fórmula deverá retornar o valor auxiliar para o terceiro vencimento da bolsa que a fórmula TabBolsaLan retornar
* ValorAuxiliarBolsaLanDescAnt('VAUX001', -1, '-1', '10/01/2020'): Indica que a fórmula deverá retornar o somatório de todos dos valores auxiliares calculados para o desconto por antecipação até 10/01/2020 para as bolsas.
VALORAUXILIARLANDESCANTFórmula VALORAUXILIARLANDESCANT

A fórmula **VALORAUXILIARLANDESCANT**retorna o valor auxiliar do item de desconto por antecipação para a bolsa condicional conforme os parâmetros passados para a mesma.

**Declaração da fórmula:**ValorAuxiliarLanDescAnt(string codValorAuxiliar, object vencimento)

=> string codValorAuxiliar:

* Código do valor auxiliar

=> object vencimento

* Número do vencimento: Se o valor passado for um número inteiro, indica que o usuário deseja o número do vencimento do item do desconto por antecipação calculado para a bolsa. E o sistema o interpretará como fosse os vencimentos do desconto por antecipação.    
  Exemplo:
  + 1: Indica primeiro vencimento
  + 2: Indica segundo vencimento
  + 3: Indica terceiro vencimento, e assim por diante
* Data: Se o valor passado for uma data, indica que o usuário deseja o item do desconto por antecipação calculado para a bolsa até a data informada. Isto é, até data limite calculado para o desconto por antecipação.

  ATENÇÃO

  A data informada deve estar no formatado **DD/MM/AAAA**, caso contrário o sistema irá exibir uma mensagem para o usuário.

**Exemplos:**

* ValorAuxiliarLanDescAnt('VAUX001', 1): Indica que a fórmula deverá retornar o valor auxiliar para o primeiro vencimento do desconto por antecipação
* ValorAuxiliarLanDescAnt('VAUX001', 3): Indica que a fórmula deverá retornar o valor auxiliar para o terceiro vencimento do desconto por antecipação
* ValorAuxiliarLanDescAnt('VAUX001', '10/01/2020'): Indica que a fórmula deverá retornar o valor auxiliar para o desconto por antecipação até 10/01/2020.
