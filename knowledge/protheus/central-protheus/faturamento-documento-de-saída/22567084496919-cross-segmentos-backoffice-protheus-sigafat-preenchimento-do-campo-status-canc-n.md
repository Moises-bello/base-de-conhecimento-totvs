---
article_id: 22567084496919
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 68a0b64dca5a8219f16999a217b63d6e4195b336275683cd8b1f182af90d841d
fetched_at: '2026-06-28T22:38:44.143069+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Preenchimento do campo "Status
  Canc. NFe (F2_STATUS)"
type: support-article
updated_at: '2024-04-05T11:38:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/22567084496919-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Preenchimento-do-campo-Status-Canc-NFe-F2-STATUS
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/22567084439191) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Qual o preenchimento do campo "Campo Status Canc. NFe (F2\_STATUS)"?  
  
**Ambiente**Cross Segmentos - Backoffice Protheus - SIGAFAT - Todas as versões  
  
**Solução**

Ao tentar a exclusão de um documento de saída com o FATJOBNFE ativo (MV\_CANNFSE/MV\_CANCNFE = .T.), é levado valor ao campo para sabermos a situação perante a SEFAZ a tentativa.

Conteúdos do "Campo Status Canc. NFe (F2\_STATUS)" (registrado apenas quando se faz uso do FATJOBNFE):

* '    ' - Não houve tentativa de cancelamento com uso do FATJOBNFE
* 015 - Cancelamento Autorizado, mas com pendencia de processo
* 025 - Cancelamento não transmitido (Aguardando retorno do SEFAZ)
* 026 - Cancelamento não autorizado
* 030 - Inutilização de numeração autorizada
* 036 - Cancelamento autorizado fora do prazo

**Saiba mais:**

[FAT0191 - Job para exclusão documento de saída (MATA521) - FATJOBNFE](https://tdn.totvs.com/x/tr44E)

[Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Legenda de Exclusão do Documento de Saída](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500005345482-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Legenda-de-Exclus%C3%A3o-do-Documento-de-Sa%C3%ADda)
