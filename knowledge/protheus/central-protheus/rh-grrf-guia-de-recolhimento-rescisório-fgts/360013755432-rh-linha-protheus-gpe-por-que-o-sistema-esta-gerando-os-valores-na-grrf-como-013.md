---
article_id: 360013755432
category: RH - GRRF (Guia de Recolhimento Rescisório - FGTS)
content_hash: 35b4f5f82985285b1a0fdd659be31dc1e333eb7970e85aac20b446190fbf3558
fetched_at: '2026-06-28T22:43:32.414958+00:00'
product: protheus
section_id: 360010781714
source: central-protheus
title: RH - Linha Protheus - GPE - Por que o sistema esta gerando os valores na GRRF
  como 0,13 centavos ao invés de levar os valores de FGTS para GRRF?
type: support-article
updated_at: '2021-04-30T18:18:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360013755432-RH-Linha-Protheus-GPE-Por-que-o-sistema-esta-gerando-os-valores-na-GRRF-como-0-13-centavos-ao-inv%C3%A9s-de-levar-os-valores-de-FGTS-para-GRRF
---

**Dúvida**Por que o sistema esta gerando os valores na GRRF como 0,13 centavos ao invés de levar os valores de FGTS para GRRF?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
  
**Solução**O sistema não gera valores para recolhimento na GRRF quando a rescisão complementar for para pagamento de comissão, pois quando o código de movimentação é alterado para V3 - Comissão irá gerar erro no validador.  
  
Por isso o sistema gera o valor de 0,13 centavos. O recolhimento deve acontecer na SEFIP e não na GRRF.

Exemplo: Calculo de rescisão

![](http://tdn.totvs.com/download/attachments/266979862/image2016-10-6%2017%3A16%3A58.png?version=1&modificationDate=1475785130000&api=v2)

Geração GRRF:

![](http://tdn.totvs.com/download/attachments/266979862/image2016-10-6%2017%3A15%3A17.png?version=1&modificationDate=1475785130000&api=v2)

Geração SEFIP:

![](http://tdn.totvs.com/download/attachments/266979862/image2016-10-6%2017%3A15%3A36.png?version=1&modificationDate=1475785130000&api=v2)  
  
**Saiba Mais**  
Para mais informações acesse o *link* a seguir: [GPE001GRRF\_Rescisão\_complementar\_por\_pagamento\_de\_comissão](http://tdn.totvs.com/pages/viewpage.action?pageId=266979862)
