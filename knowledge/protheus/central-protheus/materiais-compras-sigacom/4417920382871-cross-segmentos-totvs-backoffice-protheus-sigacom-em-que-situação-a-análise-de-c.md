---
article_id: 4417920382871
category: Materiais - Compras (SIGACOM)
content_hash: 90b32ed7f556cad7600c9259612925ff2f33e190d883748e9cc25b011d840ced
fetched_at: '2026-06-28T22:41:17.587824+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Em que situação a Análise
  de Cotação fica com a legenda da cor Preta - " Cotação analisada por Auditoria com
  pedido de Compra/contratos em aberto " ?
type: support-article
updated_at: '2022-01-03T20:01:03Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4417920382871-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Em-que-situa%C3%A7%C3%A3o-a-An%C3%A1lise-de-Cota%C3%A7%C3%A3o-fica-com-a-legenda-da-cor-Preta-Cota%C3%A7%C3%A3o-analisada-por-Auditoria-com-pedido-de-Compra-contratos-em-aberto
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:05:00 min**

**Dúvida**Em que situação a Análise de Cotação MATA161 fica com a legenda da cor Preta - " Cotação analisada por Auditoria com pedido de Compra/contratos em aberto " ?

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4417905167383/mceclip0.png)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Gestão Fiscal - Todas as versões]

**Solução**A legenda Preta em questão se refere ao processo da documentação do link abaixo em que quando são gerados mais de um Pedido de Compras ou Contrato para uma Cotação a partir da opção de "Auditoria", e não foram excluídos todos os pedidos gerados para os diferentes do Fornecedor informados na Auditoria, mas sim apenas alguns destes pedido gerados (Exclusão Parcial do Pedidos gerados por Auditoria).

[PCOM10017 - Nova legenda para cotações analisadas pelo processo de auditoria e que possua pedido de compra/contratos excluído parcialmente](https://tdn.totvs.com/x/1q4pJw)

***Obs:***

Conforme orientado na Documentação, esta possibilidade acontece quando é utilizado o parâmetro ***MV\_PCEXCOT = 1***, onde é restaurada a cotação ao se excluir pedidos de compra gerado pela cotação.

Abaixo artigo sobre a utilização da opção "***Auditoria***" na Analise da Cotação (MATA161):

[Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Auditoria no processo de cotação (MATA161)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022836692)

Para uma nova análise desta cotação com esta legenda devem ser excluídos **todos os pedidos** gerados na cotação no uso da opção "Auditoria", onde então a cotação ficará com a Legenda Verde, disponível para uma nova Análise.

***Saiba Mais***

* [PCOM10017 - Nova legenda para cotações analisadas pelo processo de auditoria e que possua pedido de compra/contratos excluído parcialmente](https://tdn.totvs.com/x/1q4pJw)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Auditoria no processo de cotação (MATA161)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022836692)
* [PCOM10010 - Auditoria no processo de cotação (MATA161)](http://tdn.totvs.com/pages/releaseview.action?pageId=442958967)
* [DMANMAT02-12535 DT Funcionalidade Auditoria](http://tdn.totvs.com/display/public/PROT/DMANMAT02-12535+DT+Funcionalidade+Auditoria)
* [CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
