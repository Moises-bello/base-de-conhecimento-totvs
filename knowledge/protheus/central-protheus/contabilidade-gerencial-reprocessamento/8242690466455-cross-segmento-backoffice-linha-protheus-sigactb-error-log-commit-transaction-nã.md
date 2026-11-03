---
article_id: 8242690466455
category: Contabilidade Gerencial - Reprocessamento
content_hash: d7c5109f2272908e79f15ad2388e3e4ae8984133a8e8e589710e35070eb504a4
fetched_at: '2026-06-28T22:40:41.983088+00:00'
product: protheus
section_id: 1500001548742
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGACTB - Error Log COMMIT TRANSACTION
  não tem um BEGIN TRANSACTION '
type: support-article
updated_at: '2023-09-18T11:51:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/8242690466455-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-Error-Log-COMMIT-TRANSACTION-n%C3%A3o-tem-um-BEGIN-TRANSACTION
---

**Ocorrência**Erro log ao rodar reprocessamento, com procedure 01 instalada

Erro.log: A solicitação COMMIT TRANSACTION não tem um BEGIN TRANSACTION correspondente

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Contabilidade Gerencial - Sigactb  - a partir 12.1.33  
  
**Causa**

Erro por ter commit transaction e não ter begin transcation.

**Solução**

Ocorrência corrigida após atualização da rotina CTBA190 com data acima de 01/08/2022, existente no pacote acumulado, conforme portal do cliente área de Download.

12.1.33 - **<https://suporte.totvs.com/portal/p/10098/download#detail/1039084>**

Removido trecho de código que faz adição de commit transaction no script compilado no banco. Após aplicação do patch (ptm) deverá ser removido via configurador a procedure em questão e reinstalar.
