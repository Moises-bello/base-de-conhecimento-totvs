---
content_hash: 2f89cb03970edcd33e0e7d615b84514e1f3cffe95e3b14d2cad473f7c4ef001a
fetched_at: '2026-06-29T00:10:21.965029+00:00'
page_id: '494992433'
product: rm
source: tdn-rm
title: SCANC - CTB
type: documentation
url: https://tdn.totvs.com/display/LRM/SCANC+-+CTB
version: 23
---

SCANC - Sistema de Captação e Auditoria dos Anexos de Combustíveis, deverá ser gerado a partir da digitação e/ou importação dos estoques e notas fiscais de entrada e saída, transmitido mensalmente para as Unidades Federadas e fornecedores, de acordo com o [disposto no capítulo V do Convênio ICMS 03/99](https://www.confaz.fazenda.gov.br/legislacao/convenios/1999/CV003_99)[, de 16 de abril de 1999](https://www.confaz.fazenda.gov.br/legislacao/convenios/1999/CV003_99), relativo às operações interestaduais com combustíveis derivados de petróleo.  
Serão selecionados todos os Lançamentos Fiscais dentro do período informado na tela de geração da rotina, que não estejam cancelados ou estornados e que possuírem produtos com a Codificação Fiscal preenchida para o estado de Minas Gerais em Anexos | Dados Fiscais por UF. Os registros gerados são:

Registrosleft10Tipo 10

**Identificação do Estabelecimento Informante**

Este Registro será preenchido com os dados no cadastro da Filial selecionada.

 **Observação**!

***Campo 06 - Unidade Federada (ST) e Campo 07 - Inscrição Estadual (ST)***: Estes campos serão preenchidos pelos registros presentes no cadastro de Inscrição Estadual S.T. disponível nos Anexos do cadastro da filial.

20Tipo 20

**Fornecedor / Clientes**

Este registro será gerado com os dados contidos no cadastro de Clientes / Fornecedores.  
Os dados serão selecionados dos Clientes / Fornecedores presentes nas Notas Fiscais selecionadas.

 **Observação**!

***Campo 04 -Inscrição Estadual (ST)***: Este campo será preenchido pela Inscrição Estadual ST informada no Anexo do cadastro do Cliente / Fornecedor , caso esta seja do estado de Minas Gerais. 

***Campo 12 - Categoria***: Preenchido conforme Tipo de operação com combustível, selecionado no Anexo do cadastro da Filial, na pasta Tipo de Estabelecimento.

40Tipo 40

**Nota Fiscal**

Este registro será gerado com os dados contidos nas Notas Fiscais selecionadas.

 **Observação**!

***Campo 15 - Segunda Placa***: não será gerado.

***Campo 16 - Terceira Placa***: não será gerado.

***Campo 17 - Código do Produto***: Este campo será preenchido preenchido para o estado de Minas Gerais em [Anexos | Dados Fiscais | CÓDIGO FISCAL SCANC](http://tdn.totvs.com.br/pages/releaseview.action?pageId=501455694), de acordo com a tabela 4.1 do layout.

| CÓDIGO | DESCRIÇÃO | UNIDADE |
| --- | --- | --- |
| 22403 | GLP - Gás Liquefeito de Petróleo | L |
| 22450 | GLP - Gás Liquefeito de Gás Natural | L |
| 42020 | ÓLEO DIESEL MARÍTIMO (DMA-MGO, DMB-MDO) | L |
| 62006 | GASOLINA A | L |
| 62103 | GASOLINA B | L |
| 62154 | GASOLINA C | L |
| 62155 | GASOLINA ADITIVADA | L |
| 62308 | GASOLINA DE AVIAÇÃO | L |
| 62448 | GASOLINA A PREMIUM,62Y | L |
| 62456 | GASOLINA C PREMIUM | L |
| 63991 | QUEROSENE ILUMINANTE | L |
| 64106 | QUEROSENE DE AVIAÇÃO | L |
| 64300 | DSL - ÓLEO DIESEL A (SEM ADIÇÃO DE B100) | L |
| 64301 | S10 - ÓLEO DIESEL A S10 (SEM ADIÇÃO DE B100) | L |
| 64432 | BIODIESEL B100 | L |
| 64433 | BIODIESEL B100 IMPORTADO | L |
| 64440 | BXD - ÓLEO DIESEL B S500 COMUM | L |
| 64475 | BXD - ÓLEO DIESEL B S500 ADITIVADO | L |
| 64483 | BXD - ÓLEO DIESEL B S10 COMUM | L |
| 64491 | BXD - ÓLEO DIESEL B S10 ADITIVADO | L |
| 66575 | ÓLEO COMBUSTÍVEL TIPO 1A | L |
| 66664 | ÓLEO COMBUSTÍVEL TIPO 1B | L |
| 65583 | ÓLEO COMBUSTÍVEL TIPO 2A | L |
| 66591 | ÓLEO COMBUSTÍVEL TIPO 3A | L |
| 66680 | ÓLEO COMBUSTÍVEL TIPO 3B | L |
| 66605 | ÓLEO COMBUSTÍVEL TIPO 4A | L |
| 66699 | ÓLEO COMBUSTÍVEL TIPO 4B | L |
| 66702 | ÓLEO COMBUSTÍVEL TIPO 5B | L |
| 66621 | ÓLEO COMBUSTÍVEL TIPO 6A | L |
| 66710 | ÓLEO COMBUSTÍVEL TIPO 6B | L |
| 66630 | ÓLEO COMBUSTÍVEL TIPO 7A | L |
| 66729 | ÓLEO COMBUSTÍVEL TIPO 7B | L |
| 66648 | ÓLEO COMBUSTÍVEL TIPO 8A | L |
| 99600 | ÁLCOOL ANIDRO | L |
| 99610 | ÁLCOOL ANIDRO IMPORTADO | L |
| 99900 | ÓLEO FUSEL | L |

***Campo 19 - Valor Total do Produto***: Este campo será preenchido com o valor da seguinte operação, Preço do Produto X Quantidade do Produto.

***Campo 20 – Quantidade de Gasolina** **“A”***: Este campo só será preenchido, se houver integração com o TOTVS Gestão de Estoque, Compras e Faturamento. Caso contrário o contribuinte deverá, após a importação do arquivo no programa do SCANC CTB, complementar as notas fiscais. No caso de haver a integração com o TOTVS Gestão de Estoque, Compras e Faturamento, este campo será preenchido com a quantidade do produto Gasolina “A” (Código Fiscal 62006) presente na composição do produto que está sendo informado. A composição é definida no TOTVS Gestão de Estoque, Compras e Faturamento no Anexo do cadastro do produto, Produtos Compostos.

***Campo 21 – Valores da BC-ST e ICMS-ST Obtidos na NF***: não será gerado.

***Campo 22 – Valor Base de Cálculo***: não será gerado.

***Campo 23 – Valor Total do ICMS***: não será gerado.

falseATENÇÃO!

* *O produto 22450 (GLN - Gás Liquefeito Derivado de Gás Natural) em cima, não deverá ser informado no registro 40. O registro das Notas Fiscais através do registro 41 que já pressupõe o código 22450, não sendo necessário.*
* *A partir da versão 3.0.75 do SCANC CTB, as operações com Óleo Diesel nas formulações DMA-MGO (Código ANP 420201001) e DMB-MGO 420201003) serão apuradas em separado nos Anexos I e II de Óleo Diesel. Dessa forma, para as Notas Fiscais destes produtos deve-se utilizar o código 42020. Observar a instruções na página 61 do Manual SCANC no Menu A.*
60Tipo 60

**Estoque**

Registro não gerado no sistema, deve ser complementado diretamente no programa validador.

62Tipo 62

**Estoque por Fornecedor**

Registro não gerado no sistema, deve ser complementado diretamente no programa validador.

70Tipo 70

**Variação do Estoque**

Registro não gerado no sistema, deve ser complementado diretamente no programa validador.

80Tipo 80

**GNRE – Guia Nacional de Recolhimento de Tributos Estaduais**

Este registro será gerado com os dados contidos nas guias do tipo GNR dentro do período do mês e ano de referência selecionada.

90Tipo 90

**Totalizador de Registros**

Este registro será gerado com os totais de cada registro gerado anteriormente.
