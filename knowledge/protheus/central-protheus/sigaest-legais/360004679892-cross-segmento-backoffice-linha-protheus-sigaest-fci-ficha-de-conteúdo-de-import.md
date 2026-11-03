---
article_id: 360004679892
category: SIGAEST - LEGAIS
content_hash: ac05c14211e704f64bf5ed2a75566ebb3174e57442c8a967c40448fe8cd1dac2
fetched_at: '2026-06-28T22:38:51.508605+00:00'
product: protheus
section_id: 1500001538941
source: central-protheus
title: Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI (Ficha de Conteúdo
  de Importação) - Método 3  - Conceito e Informações - MV_FCICALC = 3
type: support-article
updated_at: '2024-02-19T14:31:54Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360004679892-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-FCI-Ficha-de-Conte%C3%BAdo-de-Importa%C3%A7%C3%A3o-M%C3%A9todo-3-Conceito-e-Informa%C3%A7%C3%B5es-MV-FCICALC-3
---

**Dúvida**

O que é o FCI e como analisar o resultado do conteúdo de importação (FISA061/Tabela SA8) a partir das entradas e produções no Estoque?

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.  
  
**Solução**

**FCI (Ficha de Conteúdo de Importação)** é o documento responsável por reunir as informações necessárias para que se possa determinar qual a participação ou percentual de um insumo importado sobre o valor total de uma mercadoria, além de identificar o contribuinte e a mercadoria.

Desta forma, podemos resumir o FCI da seguinte forma: ele apura a importação do produto (compra), a produção e a participação do insumo no valor total do Produto Acabado (PA).

Existem algumas formas de se apurar o FCI, porém neste artigo abordaremos o **Método 3** (Pré Apuração (SA8) e Apuração (CFD), porém, como o módulo do Estoque valida **apenas a Pré-Apuração**, abordaremos apenas sobre ela.

**Método 3:** Este método de apuração se baseia em todos os apontamentos de produção realizados para o produto acabado a se apurar no período informado.

**1° - O sistema (de acordo com a legislação), gera o Valor de Importação (VI) da seguinte forma:**

**VI = VL \* FST**, sendo:

* VI = Valor de Importação;
* VL = Fator de Agregação de Valor **(F4\_AGREG).** Dependendo de como está cadastrado, existe uma formula correta para o cálculo comparando com a Situação Tributária (Que basicamente é o **B1\_ORIGEM**)**. [Clique aqui para checar qual formula enquadra na sua configuração.](https://tdn.totvs.com/pages/releaseview.action?pageId=235589761)** Deve-se pegar o valor resultante do VL e multiplicar com o Fator de Multiplicação;
* FST = Fator de Situação Tributária, que é basicamente o fator de multiplicação da tabela abaixo:

|  |  |
| --- | --- |
| Origem (B1\_ORIGEM) iniciado com 5 ou 0 | FST: Fator de multiplicação = 0 (zero) |
| Origem (B1\_ORIGEM) iniciado com 1, 2 ou 8 | FST: Fator de multiplicação = 1 (um) |
| Origem (B1\_ORIGEM) iniciado com 3 | FST: Fator de multiplicação = 0.5 (zero ponto cinco) |
| Demais valores de inicio de B1\_ORIGEM | FST: Fator de multiplicação = 0 (zero) |

**2° - Como é gravado o Valor de Importação (VI)?**

O **VI** do Item da Nota Fiscal é o resultado do **Fator Agrega Valor** (da documentação contida no 1° item) multiplicado pelo**Fator Situação Tributária**: **VI = VL \* FST**.

**3° - Geração do FCI com o campo final A8\_VLRVI (Valor da Parcela Importada).**

Os valores calculados serão acumulados por produto e no momento da geração da pré-apuração (FISA061), ocorre a divisão dos valores acumulados dos VI's e quantidades de cada item. Segue abaixo um exemplo:

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000603822)

A soma do **VI** é divido pela soma da **quantidade** apurada no período e o valor é gravado no campo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/1500000603842)

Neste caso, o valor da parcela importada é de 3,50.

**4° - E como entender em caso de consumo deste produto por Produção?**

Seguindo o fluxo para geração do FCI, para que o Sistema identifique a origem do item o mesmo verificará o conteúdo do campo na entrada SD1->D1\_CLASSFIS (entradas do período) que será preenchido pelo sistema com o conteúdo do campo de cadastro SB1->B1\_ORIGEM+SF4->F4\_SITTRIB. Após realizar esta verificação o sistema verificará a estrutura para definição do percentual de importação.

Desta forma o sistema buscará todas as movimentações automáticas RE1 (MV\_FCIMI) por Ordem Produzida (PR0) no período da pré apuração e gerará o conteúdo do campo SD3->D3\_VLRVI (Por produção).

A somatória dos **"D3\_VLRVI"s de todas as produções do período a ser apurados gerará a média ponderada (SA8 – Pré Apuração FCI, campo A8\_VLRVI)**. Este conteúdo será espelhado no campo da tabela CFD->CFD\_VPARIM, para utilização deste valor no cálculo do CI junto ao campo CFD\_VSAIIE que é verificado na Operação de saída conforme regra Fiscal, assim o CI será preenchido o CFD\_CONIMP.

**Observações importantes:**

* A pré-apuração do FCI de um produto importado deverá ser preenchida utilizando-se os valores unitários da parcela importada do exterior que serão calculados através da média ponderada aritmética dos valores praticados no **penúltimo período de importação**. Ou seja, se houve uma importação no mês de Agosto, a mesma será pré-apurada apenas a partir do FCI de Outubro com a média ponderada dos valores das notas fiscais.
* Todos os valores de importação calculados para os produtos, tanto matérias-primas quanto produtos acabados, são armazenados na tabela SA8 (Pré-Apuração FCI).
* Se não houver importação no **penúltimo período** de apuração, deverá ser considerado o **último período em que tenha ocorrido** a operação. Ou seja, se na Pré-Apuração de Outubro não houver importação em Agosto, ela buscará a última importação **anterior**que tenha ocorrido a Importação.

**Saiba Mais:**

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Como interpretar o cálculo do Valor Importado (A8\_VLRVI) em Importações?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9121923559959)*

*[Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - FCI - Como interpretar o cálculo do Valor Importado (A8\_VLRVI) em Produções?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/9129246051479)*

*[Cálculo do VI para produtos comprados na pré-apuração do FCI (SA8)](https://tdn.totvs.com/pages/releaseview.action?pageId=235589761)*

*[Clique aqui e veja mais artigos sobre Legais no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538941-SIGAEST-LEGAIS)*
