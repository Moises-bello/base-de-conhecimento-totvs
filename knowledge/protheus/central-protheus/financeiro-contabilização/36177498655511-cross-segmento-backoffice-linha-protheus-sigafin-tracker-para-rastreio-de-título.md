---
article_id: 36177498655511
category: Financeiro - Contabilização
content_hash: 06298e8d7c91eb28758a957fd576a281d8703e37b1521a0230746bcaf8c5762b
fetched_at: '2026-06-28T22:38:05.195381+00:00'
product: protheus
section_id: 1500001550502
source: central-protheus
title: Cross Segmento - Backoffice Linha Protheus - SIGAFIN - Tracker para rastreio
  de títulos na contabilidade
type: support-article
updated_at: '2025-11-07T15:35:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/36177498655511-Cross-Segmento-Backoffice-Linha-Protheus-SIGAFIN-Tracker-para-rastreio-de-t%C3%ADtulos-na-contabilidade
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/36177618803735)** Tempo aproximado para leitura: **08:00 min**

**Dúvida:**  
Como funciona o rastreio dos títulos integrados à contabilidade gerencial (tracker de contabilização)?

**Ambiente:**  
Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da versão 12

**Solução:**

O objetivo desta rotina é **localizar e exibir os lançamentos contábeis a partir do documento que os originou (SE1/SE2)**

A funcionalidade utiliza as tabelas **CV3** e **CT2**.  
Ela recebe o **aliás** da tabela onde o documento original está gravado e o número do registro (**RECNO**) do título.

A **tabela CV3** atua como elo entre a origem e a tabela de destino **CT2**.  
Nela, o campo **CV3\_RECORI** armazena o registro da tabela de origem, enquanto o campo **CV3\_RECDES** referencia o registro correspondente na tabela CT2.

Os **campos da chave de busca (CTL\_KEY)** determinam as informações que serão exibidas no **Tracker Contábil**.  
Caso o sistema não localize o registro na tabela CV3, **nenhum dado será exibido**.

Para acessar o **rastreamento contábil (Tracker)** no módulo financeiro, acesse uma das rotinas **FINA740** ou **FINA750** e clique em **“Outras Ações”**.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/36177498648983)

Se o título já tiver sido contabilizado, o sistema exibirá automaticamente as informações do lançamento contábil vinculado.  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/36177498649751)

💡 **Importante:**  
O Tracker só será exibido se existirem registros na tabela **CV3 referentes ao título**, o que significa que o título precisa ter sido contabilizado.

Para validar o funcionamento, siga o fluxo abaixo:

1. Confirme que há um **LP habilitado e ativo do SIGAFIN**
2. Inclua um **título no financeiro,** realizando sua contabilização.
3. Na rotina de **funções de títulos a receber/pagar**, posicione-se sobre o registro e clique em **“Outras Ações → Tracker Contábil”**.
4. O sistema exibirá o **lançamento contábil gerado**.

**Saiba Mais:**

[Cross Segmento - Backoffice Linha Protheus - SIGACTB - CTBA102 TRACKER CONTÁBIL](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360012443412-Cross-Segmento-Backoffice-Linha-Protheus-SIGACTB-CTBA102-TRACKER-CONT%C3%81BIL)
