---
article_id: 9609960373143
category: Materiais - Compras (SIGACOM)
content_hash: b229e7f0cac65ced7042f69e1ffe23bee14c77f65328ad6da0456ee2e96cbe7b
fetched_at: '2026-06-28T22:41:20.042395+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Limite de registros
  no processo de Compras
type: support-article
updated_at: '2024-08-07T18:52:06Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/9609960373143-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Limite-de-registros-no-processo-de-Compras
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20522932377239) Tempo aproximado para leitura: **00:02:00 min****Dúvida**O sistema estabelece um limite no número de registros em diversas rotinas do processo de compras, porém o limite não é o suficiente para atender a necessidade do cliente.  
  
**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - SIGACOM - Versão 12  
  
**Solução**

O sistema foi ajustado para que todas as rotinas tenham o mesmo limite(**9999**) na quantidade de registros. O limite é estabelecido através do novo parâmetro **MV\_COMLMAX**, possibilitando o cliente configurar de acordo com sua necessidade.

O parâmetro **MV\_COMLMAX** estará disponível por padrão, porém é possível criá-lo no *release* corrente e utilizar a nova funcionalidade.

O parâmetro deve ser criado conforme abaixo:

![Inclusão do parâmetro através do CFG](https://tdn.totvs.com/download/attachments/526978431/image2019-12-12_16-5-31.png?version=1&modificationDate=1576181240840&api=v2 "Inclusão do parâmetro através do CFG")

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [DT Limite de registros no processo de Compras](https://tdn.totvs.com/display/public/PROT/7095738+DMANMAT02-23420+DT+Limite+de+registros+no+processo+de+Compras)
