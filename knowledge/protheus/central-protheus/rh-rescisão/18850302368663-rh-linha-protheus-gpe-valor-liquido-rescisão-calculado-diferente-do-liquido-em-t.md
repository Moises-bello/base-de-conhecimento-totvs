---
article_id: 18850302368663
category: RH - Rescisão
content_hash: 4641f4d48d72790959493e9f4a501235e6a40331c943fd8ee419d5fe1409e575
fetched_at: '2026-06-28T22:43:54.494724+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Valor liquido rescisão calculado diferente do liquido
  em TRCT
type: support-article
updated_at: '2025-04-16T18:50:49Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18850302368663-RH-Linha-Protheus-GPE-Valor-liquido-rescis%C3%A3o-calculado-diferente-do-liquido-em-TRCT
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18850289246231) Tempo aproximado para leitura: **00:01:30 min** **Dúvida**Por que valor liquido rescisão calculado apresenta valor diferente do liquido em TRCT?  
  
**Ambiente**TOTVS RH - TOTVS RH ( Linha Protheus ) GPE Gestão de Pessoal - A partir da versão 12.  
  
**Solução**Um dos motivos do valor liquido rescisão calculado ser diferente do liquido TRCT, seria alguma verba calculada em rescisão com Sim campo Emp. Cons (RV\_EMPCONS) e com Sim Pagto. Obrig (RV\_OBRIGAT).

O campo Emp. Cons (RV\_EMPCONS) só pode ser utilizado com Sim para as verbas de fato de Desconto do Empréstimo Consignado.

O campo Pagto. Obrig (RV\_OBRIGAT) será utilizado com Sim para verbas especificas como verba Salário Familia.

**Campo Emp. Cons (RV\_EMPCONS)**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18850277523095)

**Campo Pagto. Obrig (RV\_OBRIGAT)**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26584863589143)**

**Saiba mais**Para adquirir maior conhecimento acesse o *link* abaixo:

<https://tdn.totvs.com/pages/viewpage.action?pageId=562474674>

[RH - Linha Protheus - GPE - Como descontar empréstimo consignado na rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360026281133-RH-Linha-Protheus-GPE-Como-descontar-empr%C3%A9stimo-consignado-na-rescis%C3%A3o?source=search)

[RH - Linha Protheus - GPE - Por que o cálculo de rescisão mesmo não tendo desconto de empréstimo consignado emite mensagem de desconto de empréstimo consignado](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008650402-RH-Linha-Protheus-GPE-Por-que-o-c%C3%A1lculo-de-rescis%C3%A3o-mesmo-n%C3%A3o-tendo-desconto-de-empr%C3%A9stimo-consignado-emite-mensagem-de-desconto-de-empr%C3%A9stimo-consignado?source=search)
