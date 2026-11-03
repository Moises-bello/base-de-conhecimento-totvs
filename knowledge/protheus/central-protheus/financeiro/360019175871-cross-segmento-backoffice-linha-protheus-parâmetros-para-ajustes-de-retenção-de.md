---
article_id: 360019175871
category: Financeiro
content_hash: d23d3ba476ff57bcaa8f7e55743a9b2f4b64c2e6fc0ff6d70880f8eddd55458e
fetched_at: '2026-06-28T22:38:01.042572+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - Parâmetros para ajustes de Retenção
  de INSS no Módulo (06) FINANCEIRO
type: support-article
updated_at: '2025-10-10T13:42:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360019175871-Cross-Segmento-Backoffice-Linha-Protheus-Par%C3%A2metros-para-ajustes-de-Reten%C3%A7%C3%A3o-de-INSS-no-M%C3%B3dulo-06-FINANCEIRO
---

**Dúvida**Quais parâmetros é preciso configurar para o imposto INSS?  
  
**Ambiente**Microsiga Protheus – Financeiro – A partir da versão 11.80  
  
  
**Solução****Configuração do imposto: INSS**

**NATUREZA**  
Calcula **INSS** (**ED\_CALCINSS**) = SIM  
Percentual de **INSS** (**ED\_PERCINS**) =   
Dedução **INSS** (**ED\_DEDINSS**) = sim (Para que **INSS**seja deduzido no total da **NF**)

**FORNECEDORES/CLIENTES**  
Natureza do cadastro de fornecedores (módulo **Compras/Estoque**)  
Natureza do cadastro de cliente (para módulo **Faturamento**)  
Calcula **INSS** (**A1\_RECINSS**) = SIM

**PRODUTO**  
Calcula INSS (**B1\_INSS**) = SIM  
Verificar também o parâmetro **MV\_VLRETIN** – Valor mínimo para dispensa de retenção de **INSS**.

\* Valor do imposto **INSS** não é acumulativo

**PARÂMETROS**

**MV\_COMIINS** =   
Indica se o **INSS** será considerado para pagamento de comissão.Informar (S) ou (N)  
**MV\_FORINSS** = Código do Fornecedor  
Fornecedor padrão para títulos de **INSS**  
**MV\_INSS** =  INSS  
Natureza de Títulos de Pagamento de **INSS**  
**MV\_VLRETIN** =   
Valor mínimo para dispensa de retenção de **INSS**.  
**MV\_LIMINSS**=    
Valor limite de retenção para o **INSS** de pessoa física  
**MV\_INSIRF** =   
Define se o valor do **INSS** deve ser abatido da base de calculo do **IRRF** no Financeiro. “1” = Abate o valor e o valor da base de calculo do IRRF. "2" = Näo abate    
**MV\_RNDINS** =   
Informe o critério de arredondamento da **INSS**. As hipóteses válidas são: .**T**. arredonda, .**F.** trunca (título principal. 1=Emissão; 2=Vencto Real)

**MV\_RNDPREC=**

Indica a precisão de arredondamento dos valores de impostos das Notas Fiscais.  
**MV\_ACMINSS** =   
Define se a acumulatividade dos valores de **INSS** levarão em conta a data de Emissão ou Vencimento do de 1=Emissao; 2=Vencto Real  
**MV\_RATINSS** =   
Indica se o valor do INSS deve ser ou não rateado pelo numero de títulos a pagar em uma nota fiscal de compra (T = Rateia, F = Não Rateia)    
**MV\_MININS** =   
Valor mínimo para retenção de **INSS**. Caso o valor de **INSS** calculado no período seja inferior, o INSS não será retido.

**Saiba mais:**

[CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Arredondamento de Impostos](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023920652-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Arredondamento-de-Impostos?source=search)
