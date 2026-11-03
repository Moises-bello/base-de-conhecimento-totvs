---
article_id: 360018465192
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: b6a995373d21908fa8048277aacc07e358c458e48505ddc9ea641ff88bc3c175
fetched_at: '2026-06-28T22:39:20.503202+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Livros Fiscais -
  Regime Simplificado do ICMS-ST Mato Grosso - 392/2011
type: support-article
updated_at: '2021-07-13T17:28:18Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018465192-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Livros-Fiscais-Regime-Simplificado-do-ICMS-ST-Mato-Grosso-392-2011
---

**Dúvida**

Quais as configurações para que o calculo referente ao Regime de Estimativa Simplificado do ICMS ST - Mato Grosso seja efetuado?  
   
**Ambiente**Protheus - Livros Fiscais - A partir da versão 11.80 **Solução**

A1\_REGESIM

Esse campo no cadastro do Cliente determina se o calculo do ST utilizará o CNAE como determina esse regime.

A1\_PERCATM

Nesse campo será informado o percentual de calculo determinado pelo CNAE da empresa que está sendo destinada a mercadoria.

***Cadastro Fornecedor***

A2\_REGESIM = Sim

O campo acima determina se o fornecedor utiliza o calculo por estimativa simplificada.

**Cadastro do Produto**

B1\_REGESIM = Sim

***Parâmetros***

MV\_REGESIM

Esse parâmetro habilita a empresa a utilizar o Regime por Estimativa Simplificado.

Ex:  .T.

MV\_PERCATM

Indica o percentual determinado pelo CNAE da empresa.

Ex: 16

***PARA OPERAÇÕES DENTRO OU OPERAÇÕES DE ONDE O DESTINO É O ESTADO DO MT SERÁ NECESSÁRIO INFORMAR MVA NO PRODUTO OU EXCEÇÃO FISCAL, CONFORME DETERMINADO PELO ANEXO -*** ***Margem de Valor Agregado (MVA) constante no anexo XI do Regulamento do ICMS.***

***Exemplo de Nota de saída de MT para MT***A regra para o calculo para operações é a seguinte:

Ex: Mercadoria = 952.38

IPI = 5% = 47.62

MVA = 38% - Retirado do regulamento para móveis.

Alíquota interna = 17%

Carga média = 16%  
  
A - Mercadoria \* alíquota interna = 952.38\*17% = 161.90

B - Valor agregado = MERCADORIA+IPI+DESPESAS \* MVA = 952.38+47.62\*38% = 380.00

C- VALOR DO ICMS-ST POR ESTIMATIVA = VALOR AGREGADO \*CARGA MÉDIA = 380.00\*16% = 60.80.

BASE DE CALCULO DO ICMS-ST = A+C/ALIQUOTA INTERNA = 161.90+60.80\*17%(0.17) = 1.310,00  
  
Valor total da NF = 1.060.80  
  
***Conclusão*** – A Base de cálculo do ICMS-ST não será determinada pela soma de produtos + valor agregado como é feito no ICMS-ST “padrão”, porem é necessário que o MVA seja informado para que o sistema faça o calculo acima.  
  
***Exemplo de Nota fiscal de SP para MT***

Ex: Mercadoria = 952.38

IPI = 5% = 47.62

MVA = 38% - Retirado do regulamento para móveis.

Alíquota interna = 17% do estado de destino

Alíquota interestadual – 7%

Carga média = 16%

A - Mercadoria \* alíquota interestadual = 952.38\*7% = 66.66

B- Valor do ICMS-ST = Mercadoria+IPI + despesas \* percentual de carga média = 952.38+47.62 \* 16% = 160.00

C- Base de calculo de ICMS-ST = A+B / Alíquota interna do estado de destino = 66.66+160/0.17 = 1.333,29.

**FECOP - MT ( Regime Simplificado):**

Configurar:

**UF X UF ( FISA080):****Alq.FCP-ST"** (CFC\_AFCPST) com **2=Cliente**

**Cadastro do Cliente:****A1\_PERFECP =** Informar a Alíquota do FECOP

A alíquota do FECOP-MT nas operações com Regime de Estimativa Simplificado (FECOP-ST) é definida por CNAE, ou seja, não é possível defini-la diretamente no cadastro de regras UF x UF (Tabela CFC) como ocorre com os demais estados. Para utilizar estas regras é necessário configurar o campo **"Alq.FCP-ST"** (CFC\_AFCPST) com **2=Cliente** para indicar que a alíquota deve ser obtida do cadastro de clientes e não da regra UF x UF. Configurando desta maneira a alíquota para o cálculo do FCP-ST será obtida do campo **A1\_PERFECP**.

Nas operações com Regime de Estimativa Simplificado (FECOP-ST) a base de cálculo do FCP é o "Valor da operação": Mercadoria + IPI + Frete + Seguro + Despesas. Como existem configurações no sistema para que os valores de IPI, frete, seguro e despesas não componham a base do ICMS Próprio da operação, e a base do FCP-ST deve sempre considerar estes valores, não é possível utilizar somente a base do ICMS Próprio para o cálculo. Desta forma, para esta situação, é necessário configurar o campo **"Bs.FCP-ST"** (CFC\_BFCPST) com a opção **3=ICMS Próprio + IPI + Frete + Seguro + Despesas**.

***Conclusão*** – A Base de cálculo do ICMS-ST não será determinada pela soma de produtos + valor agregado como é feito no ICMS-ST “padrão”, porem é necessário que o MVA seja informado para que o sistema faça o calculo acima.
