---
article_id: 360035336833
category: Escrita Fiscal - Impostos - ICMS
content_hash: d686d16f5bf6c5c8b7be7e8e0dde364835a3dc863f89d91ca505dea5cc0360ca
fetched_at: '2026-06-28T22:39:24.119518+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS -  Como preencher o
  CD2_MODBC = 5 Calculo com pauta?
type: support-article
updated_at: '2024-06-20T13:47:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035336833-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-preencher-o-CD2-MODBC-5-Calculo-com-pauta
---

**Dúvida**COMO PREENCHER O CD2\_MODBC = 5 Calculo com pauta ?  
  
**Ambiente**Protheus - Faturamento  – A partir da versão 11.80  
  
**Solução**

Para que seja calculado o ICMS ST pauta , siga os procedimentos abaixo:

Cadastrar uma Pauta para o calculo   
1. Cadastro de produtos  ( B1\_VRL\_ICM  )

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045303634/mceclip0.png)

ou  
2. Cadastro de exceção fiscal ( F7\_VRL\_ICM )

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045304154/mceclip1.png)

3. Cadastrar uma TES com a configuração abaixo:

**Calcula ICMS**(F4\_ICM) = SIM

**L. FISC. ICMS** (F4\_LFICM) = TRIBUTADO

**AGREGA SOLID.** (F4\_INCSOL) = SIM

**MKP.ICM.COMP** (F4\_MKPCMP) = NÃO

**MARG. SOLID.** (F4\_MKPSOL) =CONFIGURAÇÃO

Exemplo de calculo

Valor da mercadoria = 20,00

Valor da Pauta = 25,00

Quantidade = 05

Valor total da Nota fiscal 100,00

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046161953/mceclip2.png)

CD2

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046162373/mceclip3.png)

Dessa forma será criada a CD2\_CODBC=5
