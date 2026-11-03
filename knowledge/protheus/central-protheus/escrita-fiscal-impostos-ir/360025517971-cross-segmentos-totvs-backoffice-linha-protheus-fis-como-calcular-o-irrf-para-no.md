---
article_id: 360025517971
category: Escrita Fiscal - Impostos - IR
content_hash: bd0e79847bf34432408487eba5df95e5f674a81e6883aa6f3bb6262fc740a218
fetched_at: '2026-06-28T22:39:31.836963+00:00'
product: protheus
section_id: 1500001549802
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Como calcular o
  IRRF para notas de entrada e saída?
type: support-article
updated_at: '2025-07-31T19:38:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025517971-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-IRRF-para-notas-de-entrada-e-sa%C3%ADda
---

**Dúvida**Como calcular o IRRF via retenção nas notas fiscais de entrada ou saída?    
  
**Ambiente**

Protheus - Faturamento - Compras - Versão MP12

**Solução:**

Para a retenção será necessário seguir a configuração abaixo:

**1 - Tabelas:**

**Natureza (SED):**

Calcula IRRF = SIM

Percentual de cálculo de IRRF = 1,0/1,5

Amarrar Natureza ao cadastro de Cliente/ Fornecedor

Se o fornecedor for Pessoa Física, o Sistema busca a alíquota da tabela de IRRF (CFX011) do configurador.

**CLIENTE (SA1):**

Pode ser informada a alíquota no campo**A1\_ALIQIR**

Recolhe IRRF **(A1\_RECIRRF) = SIM**

Modo **Abatimento do Imposto (A1\_ABATIMP)** = Calculado pelo sistema

**FORNECEDOR (SA2):**

**Cálculo IRRF =** Normal

**IRRF Prog = SIM** (Pessoa Física)

**Vlr.Mín.IRRF( A2\_MINIRF)** = **1 – Sim** - O Sistema não considera o parâmetro **MV\_VLRETIR**

**2 – Não** - O Sistema considera esse parâmetro.

**PRODUTOS (SB1):**

**Impos Renda (B1\_IRRF)** = Sim

**Redução de IRRF (B1\_REDIRRF)** - Caso haja redução

**TES (SF4):**

**Gera Dupl. (F4\_DUPLIC)** = Sim

**2 - Parâmetros (SX6):**

**MV\_1DUPNAT -**Campo ou dado a ser gravado na natureza do titulo.

**MV\_MP447 -**Define se a empresa terá IRRF retido na forma da MP 232. T = Considera a M.P.; F = Não considera a M.P.             

**MV\_VENCIRF -**Indica se o título de IRRF será gerado a partir da data de (E)missão, (V)encimento ou (C)ontabilização.

**MV\_VCTIRPF -** Indica se o título de IRRF (Pessoa Física) será gerado data de (E)missão, (V)encimento ou  (C)ontabilização.

**MV\_ACMIRPF** -Define se a cumulatividade dos valores de IR-PF levarão em conta a data de Emissão ou Vencimento do titulo principal. 1=Emissao; 2=Vencto Real.

**MV\_ACMIRPJ** **-**Define se a cumulatividade dos valores de IR-PJ levarão em conta a data de Emissão ou Vencimento do titulo principal. 1=Emissao; 2=Vencto Real.

**MV\_VC11196 -**Determina se fará o cálculo de data dos impostos IRRF, PIS, COFINS, CSLL conforme Lei 11196.

**1 =** Calcula os vencimentos de acordo com a lei 11.196

**2 =**Default, de acordo com 10925

**MV\_IRMP232 -**Define se a empresa terá IRRF retido na forma da MP 232. **1-Sim/ 2-Não**

**MV\_ALIQIRF -**Alíquota de IRRF para títulos com retenção na fonte.Utilizam percentuais de acordo com tabela legal.

**MV\_IMPADT -**Define utilização da geração de IRRF em adiantamento a Pagar.

**MV\_NATNDF -**Natureza do título NDF gerado via apuração de IRRF.

**MV\_PRZIRRF -**Número de dias para pagamento do IRRF após a emissão do título.

**MV\_VLRETIR -**Valor mínimo para dispensa de retenção de IRRF.

**MV\_RATIRRF -**Indica se o valor do IRRF deve ser ou não rateado pelo número de títulos a pagar em uma nota fiscal de compra.

**MV\_IRF......... -**Natureza utilizada para Imposto de Renda "IRF"

**MV\_IRMP232 -** Define se a empresa tera IRRF retido na forma da MP 232. Valores Possiveis 1-Sim, 2-Nao

**MV\_IRPJ** -Naturezas para impostos manuais IRPJ - DCTF

**.T. = Rateia**

**.F. = Não Rateia**

**MV\_RNDIRF... -**Informe o critério de arredondamento da IRRF.

**MV\_AGLIMPJ -**Define forma de verificação da base do IRRF

**1 =** Apenas Filial Corrente (DEFAULT)

**2 =** Todas Filiais por CNPJ

**3 =** Todas Filias por raiz CNPJ (8 dígitos)

# Para atender o fator da cumulatividade:

**MV\_ACMIRCR -**Define se acumula o valor mínimo do imposto IRRF - (Contas á receber)

**1 =** Acumula (Default)

**2 =** Nao Acumula

**MV\_ACMIRRF -**Define se acumula o valor mínimo do imposto IRRF - (contas à Pagar)

**1 =** Acumula (Default)

**2 =** Nao Acumula

**Boletim técnico:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=531009057>**
