---
article_id: 12156210973847
category: SIGAEST - CUSTOS
content_hash: d8c6fe3b41f2784e84d6b35afdb69d01eea9dc789524496dc73af0b57f6d1adb
fetched_at: '2026-06-28T22:39:02.397821+00:00'
product: protheus
section_id: 1500001538901
source: central-protheus
title: 'Cross Segmento - Backoffice (Linha Protheus) - SIGAEST - Work area not in
  use ( PREVIOUS ERROR : Alias does not exist CV3 )  on TABLECREATE'
type: support-article
updated_at: '2025-03-12T12:27:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/12156210973847-Cross-Segmento-Backoffice-Linha-Protheus-SIGAEST-Work-area-not-in-use-PREVIOUS-ERROR-Alias-does-not-exist-CV3-on-TABLECREATE
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: 00:01:12 min**

**Ocorrência**Ao executar a rotina de Contabilização no módulo de estoque ocorre o seguinte error.log: **"Work area not in use ( PREVIOUS ERROR : Alias does not exist CV3 )**  
**on TABLECREATE"**

**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - Estoque/Custos - Todas as versões.

**Causa**Esse cenário ocorre quando possui um índice customizado ou quando quando possuí um índice na tabela SIX, onde os campos que constam dentro desse índice da tabela CV3, estão criados na SX3 porém não foi criado fisicamente no banco de dados ao acessar a tabela CV3 pela APSDU por exemplo não é localizado.

**Solução**Para solucionar essa ocorrência, realize o seguinte passo:

1. Deixar com o índice da tabela CV3 padrão conforme print abaixo:

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/12156380368407)  
  
Com isso a tendência é que o problema seja solucionado.

**Saiba mais:**

*[Clique aqui e veja mais artigos sobre Custos no Estoque](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001538901-SIGAEST-CUSTOS)*
