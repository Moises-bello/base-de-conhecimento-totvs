---
article_id: 6772441861143
category: Financeiro
content_hash: afa3a06d0d06492736cad12c16e3a7ece4fb93c755db7e24d4df8d3a72c09b93
fetched_at: '2026-06-28T22:38:03.032659+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA450 - Como estornar
  uma compensação entre carteiras
type: support-article
updated_at: '2024-08-07T14:57:25Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/6772441861143-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA450-Como-estornar-uma-compensa%C3%A7%C3%A3o-entre-carteiras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/25470909401495) Tempo aproximado para leitura: **00:03:00 min****Dúvida**Como estornar uma compensação entre carteiras?  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - FINA450 - Todas as versões  
  
**Solução**

Para proceder com a compensação entre carteiras, é possível optar por duas abordagens: cancelamento ou estorno.

**Cenário Cancelar:** Ao optar pelo cancelamento, será gerado o movimento da **compensação da SE5**, no entanto, **não será gerado o registro de estorno da compensação**.

![Compensação cancela.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25471454314135)

**Cenário Estorno:** Ao optar pelo estorno, será gerado um movimento de **compensação na SE5**, além da criação do registro correspondente ao **estorno da compensação**.

**![estornar.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/25471468097559)**

**Importante**

A operação de estorno da compensação entre carteiras é feita com base nas tabelas **FK1** e **FK2** utilizando o campo **IDPROC** para localizar os registros compensados, é imprescindível a integridade dessas tabelas para essa operação.

**Saiba Mais**[Compensação entre carteiras - FINA450 - Financeiro P12](https://tdn.totvs.com/pages/releaseview.action?pageId=516194467#processos-3)  
[E5\_TIPODOC](Cross%20Segmentos%20-%20Backoffice%20Linha%20Protheus%20-%20SIGAFIN%20-%20Descri%C3%A7%C3%B5es%20dos%20tipos%20de%20movimenta%C3%A7%C3%B5es%20do%20campo%20E5_TIPODOC)
