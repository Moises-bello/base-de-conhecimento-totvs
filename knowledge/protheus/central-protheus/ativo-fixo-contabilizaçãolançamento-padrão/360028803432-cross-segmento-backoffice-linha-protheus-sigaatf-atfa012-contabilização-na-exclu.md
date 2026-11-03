---
article_id: 360028803432
category: Ativo Fixo - Contabilização/Lançamento padrão
content_hash: 0658765ed0fb3ab46bee247e853d2e910a97e837db6c9e61ba47f710e15d39a2
fetched_at: '2026-06-28T22:41:42.300948+00:00'
product: protheus
section_id: 1500001536421
source: central-protheus
title: 'Cross Segmento - Backoffice Linha Protheus - SIGAATF - ATFA012 CONTABILIZAÇÃO
  NA EXCLUSÃO EM LOTE NO CADASTRO DO ATIVO '
type: support-article
updated_at: '2023-11-30T19:26:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360028803432-Cross-Segmento-Backoffice-Linha-Protheus-SIGAATF-ATFA012-CONTABILIZA%C3%87%C3%83O-NA-EXCLUS%C3%83O-EM-LOTE-NO-CADASTRO-DO-ATIVO
---

**Ocorrência**

O sistema não permite realizar exclusão em lote  do ativo,caso os parâmetros MV\_ALTLCTO e MV\_PRELAN não estiverem configurados.

**![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030144791)**

**Help :**Help  **Problema :** A contabilização não pode ser executada parâmetro MV\_PRELAN desabilitado

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360030144751)**

**Ambiente**

Protheus - Ativo Fixo – A partir da versão 11.80  
   
 **Causa**

Rotina ATFA012, não permite desabilitar o parâmetro de contabilização online da rotina.

**Solução**

A exclusão em lote não permite que a contabilização online seja desabilitada. Ao desabilitar esta validação é necessário que as configurações dos parâmetros MV\_PRELAN e MV\_ALTLCTO sejam modificadas.  
Para realizar o procedimento  foi disponibilizado ponto de entrada.

Link com esclarecimento sobre a contabilização na exclusão em lote e ponto de entrada

<http://tdn.totvs.com.br/pages/releaseview.action?pageId=488146688>
