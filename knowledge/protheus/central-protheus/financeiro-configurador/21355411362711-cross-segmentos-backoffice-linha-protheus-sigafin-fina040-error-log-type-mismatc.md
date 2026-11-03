---
article_id: 21355411362711
category: Financeiro - Configurador
content_hash: 79d92cda53e3c0a02e7f9956e6af43d9527ecc179d71cd36ff239e8c77f69555
fetched_at: '2026-06-28T22:37:57.639104+00:00'
product: protheus
section_id: 1500001539601
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Error log
  type mismatch on $ on FA040TIPO
type: support-article
updated_at: '2024-02-15T11:51:12Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21355411362711-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Error-log-type-mismatch-on-on-FA040TIPO
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21355395219735) Tempo aproximado para leitura: **00****:02:00 min****Ocorrência**Como corrigir error.log type mismatch on $ on FA040TIPO?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Causa**

Este erro é ocasionado pela alteração dos parâmetros relacionados a natureza padrão dos impostos.

**Solução**

Para correção do erro os parâmetros deve ser mesmos conforme padrão respeitando as **" "(aspas)**.

**MV\_ISS = "ISS" (PADRAO)**

**MV\_INSS = "INSS"(PADRAO)**

**MV\_IRF = "IRF" (PADRAO)**

**MV\_CSLL = CSLL(PADRAO)**

**MV\_COFINS = CONFINS(PADRAO)**

**MV\_PISNAT = PIS (PADRAO)**

Caso seja necessário ajuste, o conteúdo dos parâmetros deverá conter ou não as aspas conforme padrão

**Exemplo:**   
MV\_ISS = "ISS" (PADRAO)

MV\_ISS = "XXXX" (AJUSTADO)

**Saiba mais:** [type mismatch on $ on FA040TIPO](https://tdn.totvs.com/pages/releaseview.action?pageId=253986603)
