---
article_id: 360047574054
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: d5c5b49d1442b1c6565692539062a32a299e569a35f6f3320cfddebd7d88402d
fetched_at: '2026-06-28T22:39:20.391262+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como configurar Base
  dupla ICMS ST recolhida por diferencial aliquotas, conv 52/91?
type: support-article
updated_at: '2021-07-13T18:10:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360047574054-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-configurar-Base-dupla-ICMS-ST-recolhida-por-diferencial-aliquotas-conv-52-91
---

**Dúvida**Como configurar Base dupla ICMS ST recolhida por diferencial aliquotas, conv 52/91?

**Ambiente**Protheus  - Fiscal - A partir do MP11.80

**Solução**

Após estudo identificamos duas formas para efetuar o cálculo, nos exemplos a seguir será considerada uma venda de São Paulo para a Bahia.

### **1) Composição do valor de ICMS-ST a ser recolhido por diferencial de alíquota, considerando redução na base de cálculo do ICMS Próprio e também na base de cálculo do ICMS-ST:**

[DIFAL - Redução base de cálculo referente ao Convênio 52/91 - BA](https://tdn.totvs.com/x/8Yw0Fg)

Foi preciso ajustar o sistema para utilizar o campo **CFC\_MGLQST (Margem Líquida ST)**do cadastro UFxUF (FISA080)  para o cálculo da base dupla do ICMS-ST:

**1. -** Parâmetros:

MV\_STREDU = .F. (Indica se a redução da base de ST deverá ser no valor bruto, ou seja, no valor do item, ou no valor liquido, no final do calculo.)

MV\_UFBDST = "BA" (Informe os estados que devem ter base dupla de ST. Válido apenas quando a venda for destinada a consumo e entre estados distintos.)

**2. -** Configuração do TES no módulo Livros Fiscal em Atualizações > Cadastro > Tipos de Entrada e Saída (MATA080):

Aba Impostos:

F4\_ICM (Calcula ICMS)= "S - Sim"

F4\_LFICM (L.Fisc. ICMS) = "T - Tributado"/"O - Outros"/"I-Isento"

F4\_CONSUMO (Mat.Consumo) = "S-Sim" (em caso de nota fiscal de entrada, essa configuração é obrigatória)

F4\_BASEICM (%Red.do ICMS) = 73,43

F4\_BSICMST (Red.ICMS ST) = 48,89

F4\_AGREG (Agrega Valor) = "S - Sim"

F4\_INCSOL (Agrega Solid) = "S - Sim"

F4\_MKPSOL (Marg. Solid.) = "2 - Configuracao"

F4\_MKPCMP (MKP ICM Comp) = "2-Não"

**3. -** Cadastro de Produtos no módulo Livros Fiscal em Atualizações > Cadastros > Produtos (MATA010).

Aba Impostos:

B1\_PICMRET (Solid. Saida) = 0,01 (MVA Fictício para possibilitar o cálculo do ICMS-ST ou informar o MVA correspondente ao produto)

B1\_PICMENT (Solid. Entr.) = 0,01

O percentual poderá ser informado também via Exceção Fiscal (MATA540) ou UFxUF (FISA080).

**4. -** Cadastro de Clientes no módulo Livros Fiscal em Atualizações > Cadastro > Clientes (MATA030).

A1\_TIPO (Tipo) = "F - Cons.Final"

A1\_EST (Estado) = "BA"

**5. -** Rotina UFxUF no módulo Livros Fiscal em Atualizações > Sped > UFxUF (FISA080).

Link caso tenha dúvida para utilizar a rotina UFxUF: <https://tdn.totvs.com/x/uIYtCw>

Lembrando que essa configuração deve ser utilizada em operações interestaduais ou seja a UF de origem e destino devem ser diferentes, no nosso caso de São Paulo para Bahia **CFC\_UFORIG e CFC\_UFDEST**.

Na aba ICMS preencher a **CFC\_MGLQST** (Mar.Liq.ST)= 8,8

Com essas configurações serão gerados os impostos da seguinte forma na planilha financeira e posteriormente na nota fiscal:

![](https://tdn.totvs.com/download/attachments/517120311/NOTA1.PNG?version=1&modificationDate=1570646037937&api=v2)

**Veja abaixo exemplo de cálculo:**

Valor da operação: **1000,00**

Redução no ICMS próprio do convênio 52/91: 5,14% / 7% = **73,42%**

Redução no ICMS-ST: 8,8% / 18% = **48,89%**

Alíquota aplicada na base dupla do ICMS-ST: (100% - 8,8%)  = 91,2/100 =**0,912**(Neste ponto será carregada a alíquota informada no campo CFC\_MGLQST)

ICMS Próprio:

1000 x 73,43% = 734,3 x 7% = **51,40(A)**

ICMS ST:

1000 - 51,40 = 948,6/0,912 = 1040,13 - Base dupla ICMS-ST

1040,13 x 48,89% = 508,52 x 18% = **91,53 (B)** ICMS-ST

Valor Devido (B)-(A) = 91,53-51,40 = **40,13**

### **2)****Composição do valor de ICMS-ST a ser recolhido por diferencial de alíquota, considerando a diferença entre as alíquotas de ICMS Próprio e ICMS-ST:**

[Convênio ICMS 52/91 - ICMS-ST - Diferencial de alíquota - GO](https://tdn.totvs.com/x/ExJZEg)

Neste cenário o sistema já atendia, é preciso fazer a seguinte configuração:

**1. -** Parâmetros:

MV\_UFBSTGO = "BA" (Informe os estados que devem ter base dupla de ST. Conforme art. 65 do RCTE/GO. Para Operações destinada a consumo e entre estados distintos) Esse parâmetro pode ser utilizado para o convênio 52/91 também.

MV\_UFSTALQ = "BA" (Define se cálculo de ICMS ST com base dupla será calculado entre diferença entre as Alíquotas ST e ICMS interestaduais)

MV\_STREDU = .F. (Indica se a redução da base de ST devera ser no valor bruto, ou seja, no valor do item, ou no valor liquido, no final do calculo.)

**2. -** Configuração da TES no módulo Livros Fiscal em Atualizações > Cadastro > Tipos de Entrada e Saída (MATA080).

Aba Impostos:

F4\_ICM (Calcula ICMS)= "S - Sim"

F4\_LFICM (L.Fisc. ICMS) = "T - Tributado"/"O - Outros"/"I-Isento"

F4\_CONSUMO (Mat.Consumo) = "S-Sim" (em caso de nota fiscal de entrada, essa configuração é obrigatória)

F4\_ICMSTMT (Ded.ICM.ST) = "2 - Não"

F4\_AGREG (Agrega Valor) = "S - Sim"

F4\_MKPSOL (Marg. Solid.) = "2 - Configuracao"

F4\_MKPCMP (MKP ICM Comp) = "2-Não"

**3. -** Rotina Exceções Fiscais no módulo Livros Fiscal em Atualizações > Cadastros > Excecoes Fiscais (MATA540).

Link caso tenha dúvida para utilizar a rotina de Exceções Fiscais: <https://tdn.totvs.com/x/t3MPE>

Informar o estado da exceção fiscal, no nosso caso Bahia, campo F7\_EST (Estado) = BA.

Preencher os campo F7\_ALIQEXT (Aliq. Externa) e F7\_ALIQDST (Al.ICMS Dest) com as alíquotas desejadas:

**4. -** Cadastro de Produtos no módulo Livros Fiscal em Atualizações > Cadastros > Produtos (MATA010).

Aba Impostos:

B1\_PICMRET (Solid. Saida) = 0,01 (MVA Fictício para possibilitar o cálculo do ICMS-ST ou informar o MVA correspondente ao produto)

B1\_PICMENT (Solid. Entr.) = 0,01

B1\_GRTRIB (Grupo Trib.) = 002

O percentual poderá ser informado também via Exceção Fiscal (MATA540) ou UFxUF (FISA080).

**5. -** Cadastro de Clientes no módulo Livros Fiscal em Atualizações > Cadastro > Clientes (MATA030).

A1\_TIPO (Tipo) = "F - Cons.Final"

A1\_EST (Estado) = "BA"

Com essas configurações serão gerados os impostos da seguinte forma na planilha financeira e posteriormente na nota fiscal:

![](https://tdn.totvs.com/download/attachments/517120311/nota.PNG?version=1&modificationDate=1570639401650&api=v2)

**Veja abaixo exemplo de cálculo:**

Valor da operação: **1000,00**

Alíquota do ICMS próprio = **5,14%**

Alíquota aplicada na base dupla do ICMS-ST: (100% - 8,8%)  = 91,2/100 =**0,912**

Diferencial de alíquota para cálculo do ICMS-ST: 8,8% - 5,14% = **3,66%**

ICMS Próprio:

1000 x 5,14% = **51,40(A)**

ICMS ST:

1000/0,912 = 1096,49 - Base dupla ICMS-ST

1096,49 x 3,66% = 508,52 x 3,66% = **40,13 (B)** ICMS-ST

Com os dois exemplos chegamos no mesmo resultado com R$51,40 de ICMS próprio e R$40,13 de ICMS-ST.

## **Informações**

[DIFAL - Redução base de cálculo referente ao Convênio 52/91 - BA](https://tdn.totvs.com/x/8Yw0Fg)

[Convênio ICMS 52/91 - ICMS-ST - Diferencial de alíquota - GO](https://tdn.totvs.com/x/ExJZEg)
