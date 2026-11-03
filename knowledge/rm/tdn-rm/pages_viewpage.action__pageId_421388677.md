---
content_hash: 391412f470fe2cf4a9bebac72bacaf76dabbae99eefae448cd7fa799900842bc
fetched_at: '2026-06-29T00:09:18.128057+00:00'
page_id: '421388677'
product: rm
source: tdn-rm
title: Cálculo por Prioridade na Baixa Parcial 
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388677
version: 3
---

Para definir o cálculo na baixa acesse o Assistente de Implantação de Processos, etapa 02.01.02 Baixa, Baixa 4/6, campo: Modo de cálculo dos Valores na Baixa Parcial.   
No processo de baixa, os valores são tratados por ordem de prioridade:

1. O primeiro valor a ser calculado é o das Retenções, cuja base de cálculo é recalculada proporcionalmente em relação ao valor baixado.
2. Os valores de INSS e IR são os próximos a serem calculados, que são sempre descontados na 1ª. Parcela, ou 1º. Pagamento.
3. Na sequencia são considerados os valores a descontar, na seguinte ordem: primeiramente o valor de SEST/SENAT, depois os valores de devoluções, os valores de notas de crédito, os adiantamentos, descontos e os valores opcionais a descontar.
4. Depois os valores a acrescentar, na seguinte ordem: os juros, multa, capitalização, juros vendor e os valores opcionais a acrescentar.
5. E por último o valor original baixado, que será calculado.

**Exemplo**

Valor Original  = 1000,00  
 Juros              =   430,37  
 Multa              =    20,00  
 Outros            =    93,75  
 Valor Liquido   = 1544,12  
    
 Baixa parcial  =   700,00  
    
 Valor baixado de Juros      =   430,37  
 Valor baixado de Multa      =    20,00  
 Valor baixado Outros        =    93,75  
 Valor baixado do Original  =   155,88
