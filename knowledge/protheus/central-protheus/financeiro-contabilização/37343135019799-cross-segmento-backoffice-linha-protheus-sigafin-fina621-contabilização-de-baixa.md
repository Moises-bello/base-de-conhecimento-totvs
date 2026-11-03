---
article_id: 37343135019799
category: Financeiro - Contabilização
content_hash: c9a84de1acbee1c5605c66180fbfbf3693faff3d961f36aaa2d9a9caebae826b
fetched_at: '2026-06-28T22:38:05.279297+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - FINA621 - Contabilização
  de baixa e inclusão do titulo nas filiais de origem e destino
type: support-article
updated_at: '2025-12-31T11:01:52Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/37343135019799-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-FINA621-Contabiliza%C3%A7%C3%A3o-de-baixa-e-inclus%C3%A3o-do-titulo-nas-filiais-de-origem-e-destino
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/37343134996887) Tempo aproximado para leitura: 04**:00 min**

**Dúvida:**  
Como realizar a contabilização de transferências de títulos entre filiais (FINA621), registrando a baixa na filial de origem e a entrada na filial de destino?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Financeiro - 12.1.33 e superiores

**Solução:**

Para que a contabilização ocorra de forma integrada durante o processo de transferência entre filiais, o sistema utiliza os Lançamentos Padrões (LP) de inclusão e baixa. Como as rotinas de transferência e aprovação não possuem parâmetros de configuração (F12) específicos para contabilização, o processo depende da configuração das rotinas de origem (Contas a Pagar/Receber e Baixas).

1. Certifique-se de que os **Lançamentos Padrões** estão configurados:

   * **LP 510:** Utilizado para a inclusão do título na filial de destino.
   * **LP 530:** Utilizado para a baixa do título na filial de origem.
2. Acesse a rotina de inclusão de títulos (Ex: **FINA050 - Contas a Pagar**);  
   Pressione a tecla **F12** e configure o parâmetro **Contabilização Online?** como **Sim (para contabilização online da aprovação de transferências)**
3. Acesse a rotina de baixa de títulos (Ex: **FINA080 - Baixas a Pagar**);  
   Pressione a tecla **F12** e configure o parâmetro **Contabilização Online?** como **Sim (para contabilização online da aprovação de transferências)**  
     
   **![](https://centraldeatendimento.totvs.com/hc/article_attachments/37343135002391)**

   Para visualizar o lançamento contábil gerado a partir da contabilização, a opção "Mostra Lanc. Contab?" precisa estar configurada como "SIM".
4. Realize a transferência do título e aprovação de transferencia. O sistema executará a baixa contábil na filial emitente e a nova inclusão contábil na filial receptora de forma automática.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/37343135003287)
