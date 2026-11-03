---
content_hash: d5c3195dbe2bb0b8476d9995fad9ef866bf266e4bf37cc2894ab042dafe44f66
fetched_at: '2026-06-29T00:09:18.137673+00:00'
page_id: '421388681'
product: rm
source: tdn-rm
title: Cálculo por Proporcionalização na Baixa Parcial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388681
version: 4
---

Para definir o cálculo na baixa acesse o Assistente de Implantação de Processos, etapa 02.01.02 Baixa, Baixa 3/4, campo: Modo de cálculo dos Valores na Baixa Parcial.  
O valor pago é distribuído proporcionalmente por cada valor do lançamento, inclusive  os valores de Integração:

1. Considera o valor das retenções do item de baixa;
2. Considera  valor TOTAL de: IRRF, INSS, SEST/SENAT, Devoluções, Notas de Crédito e Adiantamentos;
3. Considera  os valores proporcionais de:  Desconto, Vr. opcionais a DESCONTAR, Valores de Integração à DESCONTAR;
4. Considera os valores a ACRESCENTAR proporcionalmente;
5. Considera o valor ORIGINAL proporcionalmente;
6. Ajusta a diferença de cálculo entre os valores Calculados e o efetivamente BAIXADO.

**Resultado**

Valores do item de Baixa = Valores restantes do Lançamento que não foram baixados.

**Exemplo 1 - Lançamentos com valores de juros, multa e opcionais:**

Valor Original  = 1000,00  
Juros              =   430,37  
Multa              =    20,00  
Outros            =    93,75  
Valor Liquido   = 1544,12  
   
Valor baixado =   700,00 que corresponde a 45,33% do valor liquido, ou seja:  
700,00 \* 100 / 1544,12 = 45,33%  
   
Portanto, para o cálculo dos demais valores será aplicado 45,33% do seu total.

Valor baixado dos Juros =  430,37 \* 45,33% = 195,10  
Valor baixado da Multa  =    20,00 \* 45,33%  =    9,07  
Outros                         =    93,75 \* 45,33%  =   42,40

**Exemplo 2 - Lançamentos vinculados a uma devolução com valor de multa:**

Lançamento 1 - Sem classificação

Valor Original              = 1000,00

Valor vinculado           = 500,00

Multa                          = 55,00

Lançamento 2 - Devolução

Valor Original              = 1000,00

Valor vinculado           = 500,00

Multa                          = 55,00

Valor baixado Lançamento 1 - Sem classificação vinculado:

Valor da baixa parcial: 250,00

Valor Multa: 24,77

Devolução: 500,00

Valor baixado Lançamento 2 - Devolução:

Valor da baixa parcial: 0,00

Valor multa: 55,00

Valor vinculado baixado: 500,00

**Exemplo 3 - Lançamentos gerador de IRRF/INSS:**

Valor original: 280000,00

Valor IRRF: 4200,00

Valor parcial baixado: 180000,00

Valor IRRF: 4200,00

Lançamento gerado de IRRF:

Valor parcial baixado: 3000,00

Multa: 5,99
