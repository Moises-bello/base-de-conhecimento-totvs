---
article_id: 360048236413
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: cde90f23a1eb72e4608757b464ed72f5a936ff429a86f36898e638be55dcf8e4
fetched_at: '2026-06-28T22:39:20.375397+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como calcular o ICMS
  ST sem MVA e sem calculo do icms próprio?
type: support-article
updated_at: '2021-09-20T20:02:07Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048236413-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-calcular-o-ICMS-ST-sem-MVA-e-sem-calculo-do-icms-pr%C3%B3prio
---

**Dúvida**Como calcular o ICMS ST sem MVA e sem calculo do icms próprio?

**Ambiente**Protheus - Fiscal – A partir da versão 11.80  
  
**Solução**

Informe no **Cadastro do Produto ( B1\_picmret )** ou da **Exceção Fiscal ( f7\_margem )** o percentual de ICMS-ST (MVA) estabelecido por norma legal, caso não exista, informe um percentual fictício (por exemplo 0,01) somente para possibilitar o cálculo pelo diferencial:

**TES**

**Calcula ICMS**(F4\_ICM) = Não

**L. FISC. ICMS** (F4\_LFICM) = Outros / Isento

**Dif. Aliq**. (F4\_COMPL) = NÃO

**Mat. Consumo**(F4\_CONSUMO) = SIM

**Agrega Solid.**(F4\_INCSOL) = SIM

**Marg. Solid**(F4\_MKPSOL) = NUNCA (Indica que o sistema deve ignorar o MVA preenchido no produto ou exceção fiscal)

**Cliente**(SA1) deve ser um dos tipos preenchido no parâmetro **MV\_TPSOLCF**, o **CLIENTE** deve ser de um Estado diferente do emitente (**MV\_ESTADO**) e ter a Inscrição Estadual preenchida.

Nos casos em que o parâmetro **MV\_CODREG** estiver = 3 o campo **Venda Pres. (F4\_VENPRES)** deverá ser configurado = 2.
