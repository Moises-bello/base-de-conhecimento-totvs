---
article_id: 39452627233303
category: Financeiro - Contabilização
content_hash: 651edf6adbff9abe62a2820c7ee3a67dfd06a5afa661ac318a6bef879a1b3aa3
fetched_at: '2026-06-28T22:38:05.297929+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGAFIN - Rastreamento
  de itens contabilizados via CV3
type: support-article
updated_at: '2026-04-01T18:16:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/39452627233303-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAFIN-Rastreamento-de-itens-contabilizados-via-CV3
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/39452639105815) Tempo aproximado para leitura: **00:09 min**  
  
**Dúvida**  
Como configurar e importar o arquivo de extrato?  
  
**Ambiente**  
Como realizar o rastreamento da origem de um lançamento contábil (tabela CT2) quando a contabilização provém das rotinas FINA370 ou CTBAFIN?  
  
**Solução**  
O rastreamento de lançamentos contábeis gerados por meio de uma contabilização (quando o campo **CT2\_MANUAL = 2**) pode ser realizado por meio da tabela **CV3 – Rastreamento de Lançamentos**.

Essa tabela atua como um elo entre a contabilidade e a origem do movimento, permitindo identificar exatamente qual registro deu origem ao lançamento contábil.

**Passos para rastreamento**

**1. Identificar o lançamento na contabilidade (CT2)**  
Localize o lançamento desejado na tabela CT2 e verifique o campo **CT2\_MANUAL**:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39452639107479)

* **1**: Lançamento manual
* **2**: Lançamento automático

**2. Localizar o vínculo na tabela CV3**  
Para rastrear a origem, consulte a tabela **CV3** utilizando as informações do lançamento identificado:

* Utilize o campo **CT2\_MSUIDT** do lançamento na CT2;
* Localize esse mesmo identificador no campo **CV3\_IDDEST**;
* Alternativamente, o **R\_E\_C\_N\_O\_** da CT2 também pode ser relacionado com o campo **CV3\_RECDES**.  
  ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39452639108503)

**3. Identificar a tabela de origem**  
Após localizar o registro na CV3, verifique os seguintes campos:

1. **CV3\_TABORI**: indica a tabela de origem (ex: SE1, SE2, SE5);
2. **CV3\_RECORI**: contém o **R\_E\_C\_N\_O\_** do registro na tabela de origem;
3. **CV3\_IDORIG**: corresponde ao identificador único (MSUIDT) do registro de origem;  
   ![](https://centraldeatendimento.totvs.com/hc/article_attachments/39452627217559)

**4. Analisar a origem do lançamento**  
Com essas informações, acesse a tabela indicada em **CV3\_TABORI** e posicione o registro utilizando o **R\_E\_C\_N\_O\_** (CV3\_RECORI).

Dessa forma, será possível identificar exatamente qual título ou movimentação financeira originou o lançamento contábil.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/39452639109399)

Além disso, você pode verificar o campo **XX\_ROTINA** (quando disponível) para entender qual rotina do sistema foi responsável pela geração do lançamento.
