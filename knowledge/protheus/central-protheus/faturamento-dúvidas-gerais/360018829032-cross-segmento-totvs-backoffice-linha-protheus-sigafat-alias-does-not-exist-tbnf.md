---
article_id: 360018829032
category: FATURAMENTO - DÚVIDAS GERAIS
content_hash: 906317fb8b8d028bcd096d245a84973d2876059a0edb89d011fd1d509b0e1eb3
fetched_at: '2026-06-28T22:38:28.685289+00:00'
product: protheus
section_id: 1500001550422
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT -Alias does not
  exist _TBNFE
type: support-article
updated_at: '2023-02-03T19:20:09Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018829032-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Alias-does-not-exist-TBNFE
---

**Ocorrência**Erro ao tentar efetuar a contabilização da nota de saída:

Alias does not exist :**\_TBNFE**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFAT - Todas as versões.

**Causa**

O erro trata-se de um problema de semáforo contábil,  gerado no arquivo  **\_TBNFE**.

Este semáforo não é utilizado para contabilização de documento de saída (**CTBANFS**), o semáforo de documento de saída é **\_TBNFS**, e  ambos os arquivos ficam armazenados na pasta System do Protheus.

**Solução**  
Para solucionar, deixe o parâmetro **MV\_CTBNFSE** = 2.

Obs: **MV\_CTBNFSE** - Configura o uso de serialização pela integração de nota fiscal, 1 - Ligado. Controle de semáforo por processo ligado. / 2 - Desligado. Controle de semáforo por processo desligado.serv
