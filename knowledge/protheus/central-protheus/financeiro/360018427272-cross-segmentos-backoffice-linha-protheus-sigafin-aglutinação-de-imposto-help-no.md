---
article_id: 360018427272
category: Financeiro
content_hash: ee1d52083a77c98b6b79008dc69481bd7cf43bc2d6d25fc1807682348c17b8ec
fetched_at: '2026-06-28T22:38:01.197652+00:00'
product: protheus
section_id: 1500001550522
source: central-protheus
title: 'Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - Aglutinação de Imposto
  Help: NOCANAGL'
type: support-article
updated_at: '2022-06-15T00:18:10Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360018427272-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-Aglutina%C3%A7%C3%A3o-de-Imposto-Help-NOCANAGL
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)** Tempo aproximado para leitura: **00:03:00 min  
  
Ocorrência**No módulo **Financeiro**, ao tentar cancelar a **aglutinação de imposto (FINA376)** é apresentada o Help: **NOCANAGL.** Problema: Processo de Aglutinação de imposto não pode ser cancelado pois algum dos títulos gerados encontra-se baixado total ou parcialmente ou registro não foram encontrados para esse processo.  
  
![AGI.JPG](https://centraldeatendimento.totvs.com/hc/article_attachments/360014153312/AGI.JPG).  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões

**Causa**É apresentado este Help quando é posicionado o cancelamento no título de imposto do tipo **TX**.  
Para que o processo de cancelamento de aglutinação funcione, é necessário posicionar no titulo aglutinador.  
 **Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Acesse o módulo **Financeiro >** **Miscelânea >** **Recálculos >** **Aglutinação Imposto**;  
2. Posicione no título aglutinado que foi gerado de prefixo **AGL**;  
3. No menu **Outras Ações >** selecione **Cancelar** e informe o número do título posicionado.
