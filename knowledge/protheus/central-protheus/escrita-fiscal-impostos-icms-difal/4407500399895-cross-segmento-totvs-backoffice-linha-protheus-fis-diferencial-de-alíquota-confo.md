---
article_id: 4407500399895
category: Escrita Fiscal - Impostos - ICMS - Difal
content_hash: 6db41d0ca970bd6a9409a05cf02aa91a2417464f384c70724a568559eda26ba0
fetched_at: '2026-06-28T22:39:19.169010+00:00'
product: protheus
section_id: 1500001549902
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus)  - FIS - Diferencial de
  Alíquota conforme Portaria SEFAZ do Estado de Sergipe 367/2016
type: support-article
updated_at: '2022-10-26T17:26:15Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4407500399895-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-FIS-Diferencial-de-Al%C3%ADquota-conforme-Portaria-SEFAZ-do-Estado-de-Sergipe-367-2016
---

**Dúvida**

Diferencial de Alíquota conforme Portaria SEFAZ do Estado de Sergipe 367/2016

Formula:

VALOR DIFAL = {[1-(AICMS INTER % – AICMS INTRA%)] / VALOR OPERAÇÃO} \* (AICMS INTER % – AICMS INTRA%)

Onde:

AICMS INTER = Alíquota prevista para as operações ou prestações interna no Estado do Sergipe

AICMS INTRA = Alíquota prevista para as operações ou prestações interestaduais para os Estados envolvidos no Protocolo.

**Ambiente**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Livros Fiscais - Todas as versões  
  
**Solução**

#### **Procedimento para entrada de documento fiscal para contribuinte**

 Para que este calculo seja realizado é necessário informar estado contido no parâmetro MV\_ESTADO nos parâmetros:

MV\_BASDENT = SE

MV\_BASDSER = SE

MV\_CMPALIQ = .T.

 

**Exemplo da memoria de Calculo:**

Valor Total da nota:             1000

Alíquota interestadual:          4

Alíquota Interna:                  18

Diferença de alíquotas:         14

Base de calculo:                   1000 / 0,86 = 1.162,79

ICMS interestadual:              1000 \* 4% = 40

Calculo ICMS complementar: 1.162,79 \* 14%  = 162,79

Valor ICMS Complementar:   162,79 

#### 

**Procedimento para ICMS ST**

 Para que este calculo seja realizado é necessário informar estado de destino nos parâmetros:

MV\_UFBDST = SE

MV\_BASDSSE = SE

MV\_UFSTALQ = SE

 

Informe no **Cadastro do Produto** ou da **Exceção Fiscal** o percentual de ICMS-ST (MVA) estabelecido por norma legal, caso não exista, informe um percentual fictício (por exemplo 0,01) somente para possibilitar o cálculo pelo diferencial: 

***TES*** 

**Calcula ICMS**(F4\_ICM) = SIM 

**L. FISC. ICMS** (F4\_LFICM) = TRIBUTADO 

**Calc Dif ICM**. (F4\_COMPL) = NÃO 

**MATL CONSUMO** (F4\_CONSUMO) = SIM 

**AGREGA SOLID.** (F4\_INCSOL) = SIM 

**MKP.ICM.COMP** (F4\_MKPCMP) = NÃO 

**MARG. SOLID.** (F4\_MKPSOL) = NUNCA (Indica que o sistema deve ignorar o MVA preenchido no produto ou exceção fiscal)

 

**Importante** 

**Ded.ICM.ST (**F4\_ICMSTMT**)** = 2 -Não 

**CLIENTE** (SA1) deve ser um dos tipos preenchido no parâmetro **MV\_TPSOLCF**, o **CLIENTE** deve ser de um Estado diferente do emitente (**MV\_ESTADO**) e ter a Inscrição Estadual preenchida.

 

**IPI na Base (F4\_INCIDE):** Este campo permite informar se valor de IPI incide na base de ICMS. Para o exemplo a seguir o IPI entrou na base de cálculo do ICMS, desta forma pode ser definido como "Consumidor Final" ou como "Sim/Não 

 Para tratar Base Dupla deverá configurar o parâmetro **MV\_UFBDST**informe os estados que devem ter base dupla para o ST e o cadastro do cliente/pedido de venda o tipo de cliente deve ser **Consumidor Final.**

 

**Exemplo da memoria de Calculo:**

Valor Total da nota:             1000

Alíquota interestadual:          7

Alíquota do Destino:             18

Diferença de alíquotas:         11

Base de calculo:                   1000 / 0,89 = 1123,60

ICMS interestadual:              1000 \* 7% = 70

Calculo ICMS ST:                 1123,60 \* 11%  = 123,60

Valor ICMS ST:                    123,60
