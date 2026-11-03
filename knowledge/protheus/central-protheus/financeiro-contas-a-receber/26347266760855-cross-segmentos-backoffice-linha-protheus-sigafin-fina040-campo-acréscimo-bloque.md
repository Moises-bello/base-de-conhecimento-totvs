---
article_id: 26347266760855
category: Financeiro - Contas a Receber
content_hash: 46bc52dc8b5144b047d8317b57fb5791f46d4d72f3061f2e7c054c3dacf3017e
fetched_at: '2026-06-28T22:38:13.928656+00:00'
product: protheus
section_id: 1500001539421
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA040 - Campo Acréscimo
  bloqueado quando tipo do titulo é RA
type: support-article
updated_at: '2024-09-13T19:55:31Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26347266760855-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA040-Campo-Acr%C3%A9scimo-bloqueado-quando-tipo-do-titulo-%C3%A9-RA
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26347266745111) Tempo aproximado para leitura: **00****:03:00 min** **Dúvida**Campo Acréscimo bloqueado quando tipo do titulo é RA.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - Todas as versões  
  
**Solução**O campo é bloqueado por uma questão de **regra de negócio/conceito**, no sistema Protheus o titulo **RA** se trata de um recebimento antecipado, e entende que o cliente não atrasou, pois antecipou o pagamento, por esse motivo não trata o **juros**.  
O **acréscimo** não é considerado pois o **RA** é o valor fixo, se tiver **acréscimo** ou **decréscimo** deve ser incluído no valor do **RA** em si.  
Ainda que os valores estejam na **NF** na compensação o **RA** irá compor o mesmo para compensar, sendo assim para o **RA** não existe **acréscimo ou juros.**  
  
Se precisar cobrar o **juros/acréscimo** no titulo, deve usar a rotina de baixas a receber manual **FINA070** e baixar o RA como dação para não movimentar banco.
