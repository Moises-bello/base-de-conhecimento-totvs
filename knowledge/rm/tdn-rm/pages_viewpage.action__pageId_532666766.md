---
content_hash: 68773b2c3ff921de66ebf73016d4713210071220273fcdd3c3decdc3018541fb
fetched_at: '2026-06-29T00:10:36.967171+00:00'
page_id: '532666766'
product: rm
source: tdn-rm
title: 'Registro 1011: Detalhamento das Contribuições de Exigibilidade Suspensa'
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=532666766
version: 20
---

Este registro refere-se à decisão judicial que autoriza a suspensão de exibilidade de parte do valor das contribuições, ou de seu valor integral, porém sem o trânsito em julgado.

## **Cadastro de Tributos Discutidos**

Disponível no TOTVS Gestão Fiscal / Cadastros Específicos / Mais.../ Processo Judicial e Administrativo / Anexos / Tributos Discutidos. Dentro desse mesmo cadastro é possível selecionar a Fórmula da Base de Cálculo, Alíquota e a CST do tributo. O Lançamento Fiscal toma como base estes campos para o correto preenchimento dos Tributos Discutidos com o Processo Judicial no "Item"

## **TOTVS Gestão de Compras, Estoque e Faturamento**

Para atender a demanda por este registro,  foi criada uma nova aba para inclusão de Processos Judiciais no item de Movimento. A Aba deve ser habilitada quando se utiliza Histórico Longo, Gera Escrituração e contém pelo um dos seguintes tributos: PIS, COFINS ou INSS.

## **I****ntegração com o TOTVS Gestão Fiscal (Escrituração)**

Com os processos judiciais informados nos Itens dos Movimentos o mesmo será escriturado para os Itens dos Lançamentos Fiscais conforme parametrização do Processo Judicial \ Tributo Discutido.

## **C****adastro de Tributos Discutidos do Item**

Disponível no item do Laçamento Fiscal. Acesse TOTVS Gestão Fiscal / Obrigações Principais / Lançamento Entrada /Saída / Situação Tributária / Itens / Tributos Discutidos. Nesse cadastro será possível informar os valores discutidos do tributo de acordo com a decisão judicial.

## **Cálculo do Tributo Discutido no Item**

O Cálculo do Tributo Discutido, será utilizado na Escrituração Fiscal e Inclusão de Lançamento Fiscal manual. 

### Como funciona:

O cálculo consiste em calcular os campos *Valor*, *Base de Cálculo* e  transportar os valores de *Alíquota* e *CST* para o cadastro de Tributo Discutido do Item do Lançamento Fiscal. Detalhadamente como cada campo funciona:

* ***Base de Cálculo** =* Será executada a fórmula que está no *Tributo Discutido*
* ***Alíquota** = Será copiada do cadastro do Tributo Discutido*
* ***CST** = Será copiada do cadastro do Tributo Discutido*
* ***Valor** = Base \* (**Alíquota / 100)*

Informação

Caso *Base de Calculo, Alíquota, CST ou Valor seja preenchido, o sistema não calculará o Tributo Discutido a partir da formulá e não carregará a Aliquota e o CST, preservando as informações inseridas pelo usuário.*

Informação

Na Inclusão manual de um Lançamento Fiscal, o Tributo Discutido será calculado, a partir da fórmula, somente na sua INCLUSÃO. Na Edição ele NÃO É CALCULADO.

## **Geração da rotina EFD-Contribuições**

Na rotina da EFD-Contribuições, o registro 1011 será gerado, tendo como origem os seguintes dados:

|  |  |  |
| --- | --- | --- |
| **Número** | **Campo** | **Origem** |
| 1 | REG | Fixo "1011" |
| 2 | REG\_REF | Não ligado |
| 3 | CHAVE\_DOC | Não ligado |
| 4 | COD\_PART | Não ligado |
| 5 | COD\_ITEM [*chave*] | TPRODUTO.CODPRD |
| 6 | DT\_OPER [*chave*] | DLAF.DATALF |
| 7 | VL\_OPER | DITEM.VALORMERC |
| 8 | CST\_PIS [*chave*] | DTRBITEM.SITTRIBUTARIA |
| 9 | VL\_BC\_PIS | DTRBITEM.BASETRB |
| 10 | ALIQ\_PIS [*chave*] | DTRBITEM.ALIQTRB |
| 11 | VL\_PIS | DTRBITEM.VALORTRB |
| 12 | CST\_COFINS [*chave*] | DTRBITEM.SITTRIBUTARIA |
| 13 | VL\_BC\_COFINS | DTRBITEM.BASETRB |
| 14 | ALIQ\_COFINS [*chave*] | DTRBITEM.ALIQTRB |
| 15 | VL\_COFINS | DTRBITEM.VALORTRB |
| 16 | CST\_PIS\_SUSP [*chave*] | DITEMTRIBDISCUTIDOS.CODSITTRIBUTARIA |
| 17 | VL\_BC\_PIS\_SUSP | DITEMTRIBDISCUTIDOS.BASETRB |
| 18 | ALIQ\_PIS\_SUSP [*chave*] | DITEMTRIBDISCUTIDOS.ALIQUOTA |
| 19 | VL\_PIS\_SUSP | DITEMTRIBDISCUTIDOS.VALOR |
| 20 | CST\_COFINS\_SUSP [*chave*] | DITEMTRIBDISCUTIDOS.CODSITTRIBUTARIA |
| 21 | VL\_BC\_COFINS\_SUSP | DITEMTRIBDISCUTIDOS.BASETRB |
| 22 | ALIQ\_COFINS\_SUSP [*chave*] | DITEMTRIBDISCUTIDOS.ALIQUOTA |
| 23 | VL\_COFINS\_SUSP | DITEMTRIBDISCUTIDOS.VALOR |
| 24 | COD\_CTA [*chave*] | DITEM.CODCONTA |
| 25 | COD\_CCUS | Não ligado |
| 26 | DESC\_DOC\_OPER | Não ligado |

Informação

Os processos judiciais vinculados ao lançamento também serão gerados no registro 1010.
