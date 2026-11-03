---
article_id: 24847289168663
category: CRM - Dúvidas Gerais
content_hash: 127708bf5022080ec0690f0af08e0d9aca21714d6a8a017c33863ba5e9b47d80
fetched_at: '2026-06-28T22:40:27.432739+00:00'
product: protheus
section_id: 1500001538021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGACRM - Contrato de Parceria - (FATA400)
  Campo ADB_QTDENT não é preenchido ao efetivar remessa
type: support-article
updated_at: '2024-07-12T15:05:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/24847289168663-Cross-Segmentos-Backoffice-Protheus-SIGACRM-Contrato-de-Parceria-FATA400-Campo-ADB-QTDENT-n%C3%A3o-%C3%A9-preenchido-ao-efetivar-remessa
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24847313174807) Tempo aproximado para leitura: **00:02:00 min** **Dúvida:**Ao efetivar o contrato de parceria por remessa o campo **ADB\_QTDENT** não é preenchido.   
  
**Ambiente:**Cross Segmentos - Backoffice Protheus - SIGACRM - A partir da release 12  
  
**Solução:**

O campo **ADB\_QTDENT** não é preenchido pelo módulo Faturamento.

Além do módulo Faturamento, o contrato de parceria também é utilizado pelo módulo "**SIGAAGR - Gestão Agrícola**". Quando utilizado o contrato via Gestão Agrícola, houve a necessidade pelo time de produto, de alimentar o campo **ADB\_QTDENT**, devido a complexidade de controle quantitativo dos itens entregues por nota fiscal originados através deste módulo (como por exemplo gestão e venda de grãos).

Já pelo faturamento, recomenda-se o controle pelo campo do pedido de venda **C6\_QTDENT**, uma vez que o campo **ADB\_QTDENT** não será atualizado.

**Veja também:**

**[Quais são os pontos de entrada na rotina de Contrato de Parceria (FATA400)?](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4403785079831-Cross-Segmentos-TOTVS-Backoffice-Linha-Protheus-SIGAFAT-Pontos-de-entrada-na-rotina-Parcerias-FATA400)**
