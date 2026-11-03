---
article_id: 360058054294
category: Escrita Fiscal - Impostos - PIS/COFINS
content_hash: 734872e83c23022573b0678de5f3c8799397816072a77426a7abcded6f6495ee
fetched_at: '2026-06-28T22:39:36.845511+00:00'
product: protheus
section_id: 1500001538521
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS - Alíquota de COFINS
  majorada por conta e ordem de terceiros.
type: support-article
updated_at: '2021-06-24T13:12:44Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360058054294-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Al%C3%ADquota-de-COFINS-majorada-por-conta-e-ordem-de-terceiros
---

**Dúvida**Como utilizar as alíquotas de importação quando contrato importação por terceiros (conta e ordem)?  
  
**Ambiente**Protheus– Compras – A partir da versão 11.80.  
  
**Solução**

Atualmente, o sistema só agrega a alíquota de COFINS majorada para notas de importação em que o fornecedor é do Estado EX e a TES inicie com 3. No entanto quando a Importação é executada por outra empresa, a entrada não é realizada com o CFOP 3.XXXe nem com um fornecedor do Estado EX e neste caso não é aplicada a alíquota. Foi criado o campo Importação Indireta (F4\_IMPIND) na rotina Tipos de Ent/Saída(MATA080) para indicar se é uma importação por Conta e Ordem, e caso seja, também será aplicada a alíquota de COFINS majorada.

Objeto de estudo da nossa consultoria tributária:

<https://tdn.totvs.com/pages/releaseview.action?pageId=73084542&preview=%2F73084542%2F73408620%2FFIS_Aliquota_Majorada_x_Importacao_Conta_Ordem_BRA.pdf>
