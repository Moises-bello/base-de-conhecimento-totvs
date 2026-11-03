---
article_id: 13432698748695
category: Financeiro - Contas a Pagar - Comunicação Bancária CNAB
content_hash: ed3ebd0d9c7c8bd94a781d1cfc64f835f5307d984ddbe673cfba4be494339bfe
fetched_at: '2026-06-28T22:37:56.298823+00:00'
product: protheus
section_id: 1500001550622
source: central-protheus
title: Cross Segmentos - Backoffice Linha Protheus - SIGAFIN - FINA713 - Boleto não
  pertence ao convênio do usuário
type: support-article
updated_at: '2023-03-28T19:48:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/13432698748695-Cross-Segmentos-Backoffice-Linha-Protheus-SIGAFIN-FINA713-Boleto-n%C3%A3o-pertence-ao-conv%C3%AAnio-do-usu%C3%A1rio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:10:00****min****Ocorrência**No módulo Financeiro, ao tentar realizar a transmissão de titulos via API Boletos, ocorre a mensagem de erro "Operação não permitida, pois o boleto não pertence ao convênio do usuário"

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13432561900823)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - Financeiro - A partir da release 12.1.33  
  
**Causa**Esse incidente ocorre, pois a parametrização do sistema está para a rotina **FINA130 - Parâmetros de Bancos** para o campo **Cod. Empresa**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/13432605675543)  
  
**Solução**Para solucionar essa ocorrência, realize os seguintes passos:  
1. Ajustar o campo com o número de **convênio do Banco** e realizar uma nova transmissão  
2. Caso persiste o problema, deve acionar o suporte do Banco junto ao seu gerente de contas e solicitar o código de convênio para transmissão

Saiba mais  
[Parâmetros de Bancos - FINA130](https://tdn.totvs.com/pages/releaseview.action?pageId=624116777)  
[Contas a receber (Comunicação bancária online)](https://tdn.totvs.com/pages/releaseview.action?pageId=612548392)
