---
article_id: 21734438991127
category: Materiais - Compras (SIGACOM)
content_hash: d10211e26970d45cdf3ee5bdfd4f6c8edab0f3a083749a65cf3fe96ca973ab2d
fetched_at: '2026-06-28T22:41:17.456101+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - É possivel colocar
  o campo C7_CC como obrigatório e preencher quando o pedido tem rateio?
type: support-article
updated_at: '2024-03-01T14:57:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21734438991127-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-%C3%89-possivel-colocar-o-campo-C7-CC-como-obrigat%C3%B3rio-e-preencher-quando-o-pedido-tem-rateio
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21734438982039) Tempo aproximado para leitura: **00:02min** **Dúvida**É possivel colocar o campo C7\_CC como obrigatório e preencher quando o pedido tem rateio?  
  
**Ambiente**

Cross Segmento - TOTVS Backoffice (Linha Protheus) - TOTVS Compras - versão 12

**Solução**

Por padrão quando o campo C7\_CC está obrigatório, o sistema solicitará o seu preenchimento sempre, mesmo que haja rateio, pois ele é gravado em outra tabela ( SCH ) e não SC7. Ou seja, não conseguimos ter o campo como obrigatório no dicionário e ter rateio por centro de custo ao mesmo tempo.  
  
Nesse cenário verifiquei os pontos de entrada disponíveis na MATA120, para que possa ser validado o centro de custo e o C7\_CC não precise ficar como obrigatório.

* MT120OK - Validações Específicas de Usuário: <http://tdn.totvs.com/pages/viewpage.action?pageId=6085483>

***Saiba Mais :***

* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201-Materiais-Compras-SIGACOM-)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
