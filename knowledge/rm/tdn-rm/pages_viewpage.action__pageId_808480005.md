---
content_hash: 67fded0d68da3d564e72738756de8e23cf0a91b0a45fef38baf600059dd11744
fetched_at: '2026-06-29T00:11:44.024681+00:00'
page_id: '808480005'
product: rm
source: tdn-rm
title: Aluguel Complementar - Fórmulas de Cálculo do Aluguel Complementar
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=808480005
version: 12
---

### Introdução

---

Este campo é usado para vincular uma fórmula ao cálculo do Faturamento do Aluguel Complementar. Além disso, a partir da versão 12.1.2310, estamos ampliando estas funções de fórmula para considerar campos do contrato de shopping.

### Utilização

---

Existem as seguintes funções de fórmula:

* ALGCAMPOCOMPLCONTRATOLOC
* COMPETENCIAALGCOMPLEMENTAR
* VALORBASEALUGUEL
* FATURAMENTOALGCOMPLEMENTARVALOR
* PERCENTUALFATURAMENTOALGCOMPLEMENTAR

As funções de fórmula abaixo são utilizadas para considerar campos de um contrato de shopping.

* PERCFAT - Percentual Faturamento a ser aplicado no faturamento Medição;
* PERCFAT2 - Percentual Faturamento 2 a ser aplicado no faturamento Medição;
* PERCFPP - Percentual do fundo promocional sobre locação;
* PERCFPPCOMPL - Percentual do fundo promocional complementar sobre faturamento;
* VALORBASEALUGUEL - Valor base locação parcela competência;
* VALORFATURAMENTO - Valor do faturamento Medição;
* VALORENCARGOS - Valor dos encargos condominiais;
* VALORFATAPLICADOTOTAL - Valor do faturamento calculado (Valor a pagar sobre vendas = (Perc\_Fat + Perc\_Fat2));
* VALORFATAPLICADO - Valor do faturamento calculado (Valor a pagar sobre vendas = Perc\_Fat);
* VALORFAT2APLICADO - Valor do faturamento calculado (Valor a pagar sobre vendas = Perc\_Fat2);
* VALORCTOMENSAL - Valor do CTO mensal (Faixa complementar);
* VALORFPPLAN - Valor do fundo promocional lançamento;
* PERCENTUALALUGUELDOBRO - Valor do Percentual em dobro, cadastrado no contrato de locação.
* VLRINTEGRACAOITEMCOBRANCA - Essa função irá retornar o valor de um item de cobrança definido. Este valor pode então, ser usado para descontar do cálculo total de encargos.

Importante: A partir da versão 12.1.2310, ao utilizar uma fórmula, todo o cálculo do aluguel complementar será composto **somente** pelo resultado da fórmula associada ao contrato. O sistema não irá realizar nenhum outro tipo de cálculo se valendo do resultado da fórmula. Desta forma, deixamos todos os cálculos flexíveis e atendendo a diversos cenários ao mesmo tempo, que deverão ser confeccionados na fórmula de cálculo.

Mesmo em cenários onde o valor resultante da fórmula gerado seja inferior aos valores do encargos gerados no sistema (Considera Condomínio / Fundo promocional) o sistema SEMPRE irá gerar o valor complementar, visto que todo o cálculo é realizado por ela.

A função **VLRINTEGRACAOITEMCOBRANCA** somente terá efeito em itens de cobrança que possuem valor de integração associados. Para os itens de cobrança que compõem o valor original e não são associados à valores de integração, esta função **não** retornará resultado.

Abaixo, seguem exemplos de fórmula utilizadas no cálculo do aluguel complementar:

c#Valor do Faturamento Calculado - Valor Base Parcela Competênciac#Valor do Faturamento Calculado - Valor Base Parcela Competência + Valor dos encargos condominiais + FPP / Percentual FPP Complementarc#Valor do Faturamento Calculado - Valor Base Parcela Competência + Valor dos encargos condominiais (- Valor do Item de Cobrança id11) + FPP / Percentual FPP Complementar
