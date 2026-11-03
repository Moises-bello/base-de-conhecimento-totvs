---
article_id: 26623746622615
category: Financeiro - Comissão
content_hash: 4917d61df548be72c0691e5f085adaa79e54d43c3d3a127739148630e992e4aa
fetched_at: '2026-06-28T22:37:50.804252+00:00'
product: protheus
section_id: 26655771327895
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA440 - Cálculo de
  comissões de títulos com impostos
type: support-article
updated_at: '2026-02-10T14:35:43Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26623746622615-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA440-C%C3%A1lculo-de-comiss%C3%B5es-de-t%C3%ADtulos-com-impostos
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26626184625175) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**

Como configurar os impostos para serem considerados no cálculo da comissão?

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Solução**

Os parâmetros para o tratamento da **RETENÇÃO DE IMPOSTOS** na **comissão** são os seguintes:

**MV\_COMISIR - IRRF**  
**MV\_COMIINS - INSS**  
**MV\_COMIPIS - PIS**  
**MV\_COMICOF - COFINS**  
**MV\_COMICSL - CSLL**

a) Para que os valores de **retenção de impostos** não sejam somados à **base da comissão**, é necessário que esses parâmetros sejam preenchidos com "**N" (Não)**. Assim, o cálculo da comissão será realizado sobre o valor líquido (valor do título menos os impostos).

b) Para que os valores de **retenção de impostos** sejam somados à **base da comissão**, os parâmetros devem ser preenchidos com "**S" (Sim)**. Neste caso, o cálculo da comissão será feito sobre o valor total do título.

Caso esses parâmetros não existam, será necessário criá-los. Na ausência desses parâmetros na base, o tratamento padrão da rotina será não considerar os impostos na base da comissão.

Todos os parâmetros são do tipo caractere, com as opções possíveis sendo "**S" ou "N**".

**Apuração de PIS e COFINS**

Para controlar a composição de base cálculo da comissão neste caso, temos:

Os parâmetros, são responsáveis por definir se a **RETENÇÃO** de seus respectivos impostos, serão **SOMADOS** a **base de cálculo da comissão (S) - Sim ou (N) - Não**

**MV\_COMIPIS**  
**MV\_COMICOF**

Já o campo **A3\_PISCOF** definirá se os valores de **APURAÇÃO**, serão **SUBTRAÍDOS** da **base de cálculo da comissão:**

**1 - NÃO**

**2 - PIS - (Somente o PIS)**

**3 - COF - (Somente Cofins)**

**4 - Ambos - (PIS e COFINS)**

**Imposto IRRF na Base de Comissão**

**A3\_BASEIR** - Refere-se à base de cálculo do **IRRF**, que, no **Cadastro de Vendedor (MATA040)**, determina se a base do **IRRF** será incluída no valor da **comissão**.

* Se definido como **1 - Não**, **o sistema não considera o valor do IRRF na base da comissão.**
* Se definido como **2 - Sim**, **o sistema considera o valor do IRRF na base da comissão.**

Na ausência do campo **A3\_BASEIR**, será considerado o parâmetro **MV\_COMISIR**.

**Campo Base c/ICMS (A3\_ICM) para Comissão do Vendedor**

A lógica de funcionamento do campo **A3\_ICM** na geração da **comissão do vendedor** é a seguinte:

**A3\_ICM = 'S': O valor do ICMS não é descontado da base de comissão do vendedor.**  
**A3\_ICM = 'N': O valor do ICMS é descontado da base de comissão do vendedor.**  
  
**Exemplo:**

**Vendedor** com **A3\_ICM = 'S'**

Valor da Nota Fiscal: R$ 2.000,00  
**ICMS** 18%: R$ 360,00  
**Base de comissão do vendedor**: R$ 2.000,00  
**Vendedor** com **A3\_ICM = 'N'**

Valor da Nota Fiscal: R$ 2.000,00  
**ICMS** 18%: R$ 360,00  
**Base de comissão do vendedor**: R$ 1.640,00

**Saiba mais**

[FINA440 - Calculo de comissões de títulos com impostos.](https://tdn.totvs.com/pages/releaseview.action?pageId=550308062)

[Recálculo de Comissões (FINA440 - SIGAFIN)](https://tdn.totvs.com/pages/releaseview.action?pageId=312162528#Rec%C3%A1lculodeComiss%C3%B5es(FINA440SIGAFIN)-Tratamentodeimpostos)
