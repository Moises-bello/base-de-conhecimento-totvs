---
article_id: 360034832354
category: Escrita Fiscal - Impostos - ICMS - Icms St
content_hash: 15a8ebeb062f0005b101f44d5d0d86048ff68dd23e36d63054993792b2d25f93
fetched_at: '2026-06-28T22:39:20.431584+00:00'
product: protheus
section_id: 1500001538721
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Como preencher o
  CD2_MODBC = 6 para diferencial de ST?
type: support-article
updated_at: '2021-07-13T17:26:27Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360034832354-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Como-preencher-o-CD2-MODBC-6-para-diferencial-de-ST
---

**Dúvida** **COMO PREENCHER O CD2\_MODBC = 6 PARA DIFERENCIAL DE ST?**

**Ambiente**Protheus - Faturamento - A partir da versão 11.80]  
   
**Solução**Para que seja calculado o diferencial de ICMS ST , siga os procedimentos abaixo:

Cadastrar uma margem para o calculo  
 1. Cadastro de produtos  ( b1\_picmret )

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360045299734/mceclip0.png)

ou  
 2. Cadastro de exceção fiscal ( f7\_margem)

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046154413/mceclip1.png)

3. Cadastrar uma TES com a configuração abaixo:

**Calcula ICMS**(F4\_ICM) = SIM

**L. FISC. ICMS** (F4\_LFICM) = TRIBUTADO

**Calc Dif ICM**. (F4\_COMPL) = NÃO

**MATL CONSUMO** (F4\_CONSUMO) = SIM

**AGREGA SOLID.** (F4\_INCSOL) = SIM

**MKP.ICM.COMP** (F4\_MKPCMP) = NÃO

**MARG. SOLID.** (F4\_MKPSOL) = NUNCA (Indica que o sistema deve ignorar o MVA preenchido no produto ou exceção fiscal)

O calculo somente será efetuado para vendas fora do estado

MV\_estado # UF do cliente de saídas

Exemplo de uma venda

**ICMS Próprio**

Base de Cálculo = R$1000,00

Alíquota interestadual 12%

Valor do ICMS Próprio - R$120,00

**Diferencial de alíquota:**

Base de Cálculo = R$1000,00

Alíquota Interna 18%

Valor do ICMS complementar - R$60,00

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046156573/mceclip2.png)

Dessa forma será lançado o campo cd2\_modbc = 6
