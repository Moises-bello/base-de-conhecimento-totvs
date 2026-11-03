---
article_id: 18428650889111
category: Materiais - Compras (SIGACOM)
content_hash: d3b89b6c7b3f5027942c7964b4ec48eed04d6743a34d7fbe0bf4e1e7accec18b
fetched_at: '2026-06-28T22:41:20.061033+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - MATA103 - Como criar
  filtro utilizando o número do pedido no browse da MATA103
type: support-article
updated_at: '2023-10-20T12:05:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/18428650889111-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-MATA103-Como-criar-filtro-utilizando-o-n%C3%BAmero-do-pedido-no-browse-da-MATA103
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18428635187479) Tempo aproximado para leitura: **00:03:00 min** **Dúvida**

Ao acessar o "FILTRAR" da MATA103, não é possível localizar o campo de número do pedido de compras. Como posso fazer para filtrar os documentos de entrada a partir do número do pedido?

![](https://centraldeatendimento.totvs.com/hc/article_attachments/18428641603991)

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS COMPRAS -  A partir da versão 12.1.33

**Solução**Na opção Filtrar do documento de entrada, bem como da pré-nota (MATA140), os campos apresentados para serem filtrados, são da tabela SF1 (tabela do cabeçalho das notas de entrada) e, por padrão, não gravamos o número do pedido de compra dentro da SF1, mas sim só dentro da SD1(tabela dos itens do documento de entrada), porque uma mesma nota, pode conter itens de mais de um PC ou uma mesma nota, pode conter mais de um PC, por isso na opção filtrar do browser da MATA103 e MATA140, não é apresentado o campo de pedido de compra.  
  
![](https://totvssuporte.zendesk.com/attachments/token/ipFkpFPyZwaxfpet5z0AUOAsE/?name=inline-517148394.png)

​  
![](https://totvssuporte.zendesk.com/attachments/token/DC5np62QmBBW5RmY4YzCUyWdM/?name=inline2069790767.png)

​  
![](https://totvssuporte.zendesk.com/attachments/token/bUpuQhy6DFsiaYu3hR6ZtWGvR/?name=inline1344406237.png)​  
  
Para se fazer o filtro desejado, no padrão, pode-se usar a rotina "GENÉRICOS", abrindo a tabela SD1 e filtrando pelo número do PC.  
![](https://totvssuporte.zendesk.com/attachments/token/tLR5L02VBmXeGLATUG5nhugiz/?name=inline-1411550028.png)

​  
![](https://totvssuporte.zendesk.com/attachments/token/398zbuiv40pyMywDf5RXcD97n/?name=inline265322323.png)

​  
![](https://totvssuporte.zendesk.com/attachments/token/qh7asLacU8NaH5aFiotT5zt8J/?name=inline1044025175.png)

​  
![](https://totvssuporte.zendesk.com/attachments/token/JYiR91dlu9RVzCTjRjIRoSTlK/?name=inline573549516.png)

​  
![](https://totvssuporte.zendesk.com/attachments/token/Zkk9acsIxUtih5lapeHLWMmgW/?name=inline-38874955.png)

​  
![](https://totvssuporte.zendesk.com/attachments/token/SuRQ2EKtwHHpVDgEgLHPM1Y5T/?name=inline-584441158.png)​

***Saiba Mais:***

* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Manual e Artigos - Rotina Documento de Entrada - MATA103](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360000244307-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Manual-e-Artigos-Rotina-Documento-de-Entrada-MATA103)
