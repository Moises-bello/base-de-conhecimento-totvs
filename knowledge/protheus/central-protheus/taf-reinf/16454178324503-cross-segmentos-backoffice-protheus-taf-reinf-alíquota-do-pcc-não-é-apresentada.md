---
article_id: 16454178324503
category: TAF - REINF
content_hash: 2772fd9c527f4659ee4d441edceb81df85c1ecb4f7e1ef2f9767f2b5ceac36b4
fetched_at: '2026-06-28T22:41:33.592753+00:00'
product: protheus
section_id: 1500001536841
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - TAF - REINF - Alíquota do PCC não é
  apresentada no relatório de conferência do evento R-4020.
type: support-article
updated_at: '2023-08-04T17:10:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/16454178324503-Cross-Segmentos-Backoffice-Protheus-TAF-REINF-Al%C3%ADquota-do-PCC-n%C3%A3o-%C3%A9-apresentada-no-relat%C3%B3rio-de-confer%C3%AAncia-do-evento-R-4020
---

**Dúvida** Ao gerar o relatório de conferencia do Painel Reinf não está sendo apresentada a alíquota dos impostos PIS, COFINS e CSLL.

**Ambiente**Microsiga Protheus - Livros Fiscais - A partir da versão 12.   
  
**Solução**

Para geração das informações do PCC, o relatório de conferência do painel REINF busca as informações na rotina **TAFA535** (Pagamentos)**,** acesse a rotina insira as alíquotas dos imposto para correta geração das informações.

Atualizações > Movimento REINF > Pagamento.

![Relatorio PCC 1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16454184647703)

 Após o preenchimento das alíquota, extraia o relatório novamente.

![relatorio pcc 2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16454217425431)
