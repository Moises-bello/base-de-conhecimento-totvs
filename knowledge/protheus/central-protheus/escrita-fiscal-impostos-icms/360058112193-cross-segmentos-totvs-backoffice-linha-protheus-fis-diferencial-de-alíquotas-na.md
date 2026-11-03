---
article_id: 360058112193
category: Escrita Fiscal - Impostos - ICMS
content_hash: b8ed2ce9bc3318a8b25dd8761df92aab3390cf5aa9675d05010198c54ecef4c2
fetched_at: '2026-06-28T22:39:25.649123+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Diferencial de alíquotas
  na aquisição de Mercadorias Fornecedor Simples Nacional
type: support-article
updated_at: '2023-11-30T13:18:59Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058112193-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Diferencial-de-al%C3%ADquotas-na-aquisi%C3%A7%C3%A3o-de-Mercadorias-Fornecedor-Simples-Nacional
---

**Dúvida**

Parâmetros que devem ser preenchidos para correta apresentação dos valores referentes ao cálculo do Diferencial de Alíquota (DIFAL) no tocante ao ICMS Complementar em operações de aquisição de mercadoria de fornecedor de simples nacional

**Ambiente**

Microsiga Protheus - Livros Fiscais - a partir da versão 12

**Solução**

PARÂMETROS:

MV\_BASDENT = Define UFs que terão cálculo de base dupla na base do destino em operações de Difal de entrada para contribuinte do ICMS.

MV\_CMPALIQ = Define se o cálculo de ICMS Complementar será calculado com a diferença entre a alíquota do ICMS complementar e ICMS interestadual.

MV\_BDSIMP = Informe quais UFs optaram por expurgar o valor do ICMS do Simples Nacional ao invés do interestadual na aquisição com Difal com base dupla.

Exemplos de utilização

Cadastros   
Exemplo de cadastros utilizados nos cálculo demonstrados nos exemplos abaixo.

### **Cadastros**

Exemplo de cadastros utilizados nos cálculo demonstrados nos exemplos abaixo.

**Fornecedor:**

Simples Nacional

**TES:**

Material de Consumo (F4\_CONSUMO) = sim  
Markup ICMS Complementar (F4\_MKPCMP) = Não  
Cons. Red. ICMS no Comp. (F4\_COMPRED) = Não  
Calc. Dif ICM (F4\_COMPL) = Sim  
Calc. ICMS (F4\_ICMS) = Não  
Livro Fiscal ICMS (F4\_LFICM) = Outros

Como o fornecedor é simples nacional, não terá destaque de ICMS. O cliente aproveitará apenas o crédito do DIFAL.

**Valores:**

Valor da Operação: R$5.480,00

ICMS Interestadual 12% = 657,60

ICMS Interno 18% = 1.051,20

### **Exemplo 01 - Cálculo e Configuração com o parâmetro MV\_BASDENT = UF preenchida**

MV\_ESTADO = UF

MV\_BASDENT = UF

MV\_CMPALIQ = .F.

MV\_BDSIMP = EM BRANCO

**Base Dupla:**

DIFAL = [(V. Oper – ICMS Origem) / (1 - Alíq. Interna)] x Alíq. Interna – (V. Oper x Alíq. Interestadual)]

DIFAL = [(5.480,00 – 657,60) / (1 - 18%)] x 18% – (5.480,00 x 12%)]

DIFAL = [4.822,40 / 0,82] x 18% – (657,60)]

DIFAL = [5.880,97 x 18% – (657,60)]

DIFAL = [1.058,57 – 657,60]

**DIFAL =  400,97**

### **Exemplo 02 - Cálculo e Configuração com o parâmetro MV\_BASDENT = Em branco**

MV\_ESTADO = UF

MV\_BASDENT = EM BRANCO

MV\_CMPALIQ = .F.

MV\_BDSIMP = EM BRANCO

**Base Simples:**

DIFAL = Base ICMS x ((%Alíquota ICMS Intra - % Alíquota ICMS Inter)/100)

DIFAL = 5.840,00 x ((18 - 12)/100)

DIFAL = 5.840,00 x ((6/100)

DIFAL = 5.840,00 x 0,06

**DIFAL =** **350,40**

### **Exemplo 03 - Cálculo e Configuração com o parâmetro MV\_BDSIMP = UF preenchida**

MV\_ESTADO = UF

MV\_BASDENT = UF

MV\_CMPALIQ = .T.

MV\_BDSIMP = UF

Devido ao parâmetro MV\_DBSIMP estar preenchido com a UF, o cálculo será realizado no seguinte formato:

Base de Cálculo x (1 – % ICMS que compõe a Alíquota do Simples Nacional / 100%) = Valor expurgado o imposto (valor sem ICMS)  
5.480,00 x (1-12%/100)  
5.480,00 x 0,88 = **4.822,40 (valor expurgado)**

Valor expurgado o imposto / (1 – Alíquota interna / 100%) = Nova Base de Cálculo;  
4.822,40 / (1-18%/100%)  
4.822,40 / 0,82 = **5.880,97 (Nova Base de Cálculo)**

Nova Base de Cálculo X (Alíquota Interna – Alíquota Interestadual) = Imposto a Recolher, ou seja, o DIFAL a UF do destino  
5.880,97 x (18 – 12) = 352,86 valor do DIFAL a recolher

**DIFAL =  352,86**

### **Exemplo 04 -****Cálculo e Configuração com o parâmetro MV\_BDSIMP = UF preenchida e com Exceção Fiscal**

MV\_ESTADO = UF

MV\_BASDENT = UF

MV\_CMPALIQ = .T.

MV\_BDSIMP = UF

Cadastro na Exceção Fiscal -  MATA540

Alíquota Interna (F7\_ALIQINT) = 3,85%

Alíquota Externa (F7\_ALIQEXT) = 3,85%

UF Busca (F7\_UF\_BUSCA) = Origem

Valor da Operação: R$ 4.000,00

ICMS Interestadual 7%:  280,00

Alíquota do Simples Nacional: 3,85%: 154,00

Memória de cálculo:

Valor da Op. \* ((Alíq. Interna - Alíq SN)/100)

4.000,00 \* (17-3,85)/100

4.000,00 \* 0,1315 = **526,00**

ICMS DIFAL = [(V oper - ICMS origem) / (1 - ALQ interna)] x ((ALQ interna – Alíq Inter) /100)

ICMS DIFAL = [(4.000,00 - 154,00) / (1-(17/100)] x ((17-7)/100)

ICMS DIFAL =3.846,00 / 0,83 x ((17-7)/100)

ICMS DIFAL =4.633,73 x 0,1

**ICMS DIFAL =****463,37**

Assuntos relacionados:

* [Diferencial de Alíquota para fornecedor Simples-Nacional](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024719793-MP-FIS-Qual-%C3%A9-o-diferencial-de-al%C3%ADquota-para-o-fornecedor-optante-pelo-Simples-Nacional-)
* [FIS0003 Cálculo do DIFAL Aquisição de Mercadoria](https://tdn.totvs.com/x/cQbXIQ)
