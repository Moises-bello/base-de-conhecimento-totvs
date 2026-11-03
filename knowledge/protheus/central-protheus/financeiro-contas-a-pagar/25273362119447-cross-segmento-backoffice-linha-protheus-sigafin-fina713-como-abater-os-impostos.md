---
article_id: 25273362119447
category: Financeiro - Contas a Pagar
content_hash: 04aa8416510050f2418770e11b9d260dfd67e1407b2b65c0e3f4b096aff2319e
fetched_at: '2026-06-28T22:38:08.331798+00:00'
product: protheus
section_id: 1500001539541
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA713 - Como abater
  os impostos na geração do boleto API.
type: support-article
updated_at: '2024-07-30T17:02:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/25273362119447-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Como-abater-os-impostos-na-gera%C3%A7%C3%A3o-do-boleto-API
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25273362088599) Tempo aproximado para leitura: **00:01:00 min****Dúvida**Como deixar o valor do boleto sem os impostos?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA713 - A partir da release 2210.  
  
**Solução**

Para remover o valor dos impostos na geração do boleto, vá até a configuração na rotina FINA710 e substitua o campo "Valor cobrado" com a seguinte fórmula de  **SE1->E1\_VALOR** para **SE1->E1\_VALOR - SE1->E1\_IRRF - SE1->E1\_CSLL - SE1->E1\_COFINS - SE1->E1\_PIS**. Selecione a engrenagem ao lado do campo para fazer essa alteração

![](https://centraldeatendimento.totvs.com/hc/article_attachments/25273331030935)

**SAIBA MAIS:**

**[Comunicação bancária online - FINA710](https://tdn.totvs.com.br/pages/releaseview.action?pageId=734394374)**
