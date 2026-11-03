---
article_id: 4619699449111
category: Materiais - Compras (SIGACOM)
content_hash: 199ba5a50dcd1b8e3a5dfadd0572b2f7663ffed299228fadc64905238489758c
fetched_at: '2026-06-28T22:41:24.347900+00:00'
product: protheus
section_id: 1500001537201
source: central-protheus
title: Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - Reajuste no frete de
  forma proporcional PC x Documento de Entrada
type: support-article
updated_at: '2022-03-10T14:31:00Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4619699449111-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGACOM-Reajuste-no-frete-de-forma-proporcional-PC-x-Documento-de-Entrada
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:03 min** **Dúvida**

Como ativar/ desativar frete proporcional quando alterado o Item da Nota fiscal que possui  possui frete vinculado a um Pedido de Comras ?   
  
**Ambiente**

Cross Segmentos - Totvs Backoffice Protheus - SIGACOM - A partir da Versão 12  
  
**Solução**

Foi criado um parâmetro  que estará disponível automaticamente a partir do release 12.1.37,porém poderá ser criado manualmente e  aplicação da expedição contínua de compras com data corte igual ou superior à : 25.02.2021

Detalhes do parâmetro :

* Se MV\_FRT103E = .T. (default), Sempre irá proporcionalizar o frete ao alterar o item.  
  **Exemplo**: Quantidade do item: 1000 unidades, Frete: 100. Ao alterar a quantidade para 900, frete será proporcionalizado para 90.
* Se MV\_FRT103E = .F., não irá proporcionalizar o frete ao alterar o item.  
  **Exemplo**: Quantidade do item: 1000 unidades, Frete: 100. Ao alterar a quantidade para 900, frete continuará 100.

![20220307_190635.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/4619657146903/20220307_190635.gif)

**Saiba mais em :**

* [MV\_FRT103E](https://tdn.totvs.com.br/pages/releaseview.action?pageId=312158183)
* [PÁGINA CENTRALIZADORA COMPRAS](https://tdn.totvs.com/display/public/PROT/CENTRALIZADORA+COMPRAS)
* [Mais Artigos Materiais - Compras (SIGACOM)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500001537201)
