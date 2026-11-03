---
article_id: 360060932113
category: Escrita Fiscal - Impostos - Simples Nacional
content_hash: 96ce40803b35684360bf12afb9c288ebf6594e5d42a11409945a4e3f09a0989b
fetched_at: '2026-06-28T22:39:37.561579+00:00'
product: protheus
section_id: 1500001538461
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alteração de Simples
  Nacional para Lucro Presumido ou Lucro Real
type: support-article
updated_at: '2021-07-01T12:55:53Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060932113-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Altera%C3%A7%C3%A3o-de-Simples-Nacional-para-Lucro-Presumido-ou-Lucro-Real
---

**Dúvida:**

Qual o procedimento para alteração do regime de tributação envolvendo as escriturações de notas fiscais?  
  
**Ambiente:**

Protheus – Compras ou Faturamento – A partir da versão 11.80.  
  
**Solução:**

Primeiramente deverá ser alterado o parâmetro **MV\_CODREG** para 3 pois dessa forma o sistema entende que a empresa não está enquadrada no Simples Nacional.

Alterar os parâmetros das alíquotas do Lucro Real ou Presumido (Cumulativo ou não Cumulativo) = **MV\_TXPIS e MV\_TXCOFIN.**

No cadastro da tes deverá ser utilizar o campo **Sit. Trib. (F4\_SITTRIB)** para informar a CST da operação, ou seja, não deverá ser utilizado o campo Cod. Sit. SN (F4\_CSOSN) e alterar o campo **Tp Reg** (F4\_TPREG) = **Cumulativo ou Não Cumulativo.**

\*Importante: orientamos que sejam criadas novas tes para as operações realizadas no Lucro Presumido. Não orientamos que sejam realizadas alterações nas Tes existentes.

Boletim técnico complementar:  
<https://tdn.totvs.com/pages/releaseview.action?pageId=6076810>
