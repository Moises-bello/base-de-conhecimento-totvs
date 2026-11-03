---
article_id: 360048690193
category: Escrita Fiscal - Impostos - ICMS
content_hash: b5ddb2dfc43ce9ae7603ca7dfdc7994af078ac001911b76366451e74f07c8189
fetched_at: '2026-06-28T22:39:25.997452+00:00'
product: protheus
section_id: 1500001549842
source: central-protheus
title: CROSS Segmentos - TOTVS Backoffice Linha Protheus - FIS- Qual a configuração
  para que não ocorra desconto de PIS COF da base de ICMS para operações com alíquota
  zero - SUFRAMA?
type: support-article
updated_at: '2021-07-20T13:10:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048690193-CROSS-Segmentos-TOTVS-Backoffice-Linha-Protheus-FIS-Qual-a-configura%C3%A7%C3%A3o-para-que-n%C3%A3o-ocorra-desconto-de-PIS-COF-da-base-de-ICMS-para-opera%C3%A7%C3%B5es-com-al%C3%ADquota-zero-SUFRAMA
---

**[Remover as instruções entre colchetes]**  
 **Dúvida**Qual a configuração para que não ocorra desconto de PIS COF da base de ICMS para operações com alíquota zero - SUFRAMA?  
   
 **Ambiente**Protheus - todas as Versões

**Solução**Alterado cálculo da base de ICMS para não descontar PIS e COFINS na área de livre comércio (ALC) onde alíquota de PIS/COFINS igual a zero ( CST - "06 Operação Tributável a Alíquota Zero").

observações: para atender esta situação será necessário configurar os campos da TES conforme abaixo:

PIS/COFINS (F4\_PISCOF) = 4-Não Considera

Cred. PIS/COFINS (F4\_PISCRED) = 3-Não Calcula
