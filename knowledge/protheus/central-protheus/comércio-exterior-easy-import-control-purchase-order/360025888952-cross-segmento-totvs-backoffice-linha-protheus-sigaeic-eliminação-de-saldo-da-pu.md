---
article_id: 360025888952
category: Comércio Exterior - Easy Import Control - Purchase - Order
content_hash: 25fd127e63f8bdd281570b8ee927cd7cd7e0ee5c0df5bf541927dccd0391cfc3
fetched_at: '2026-06-28T22:39:41.143381+00:00'
product: protheus
section_id: 1500001538481
source: central-protheus
title: Cross Segmento - TOTVS Backoffice Linha Protheus - SIGAEIC - Eliminação de
  Saldo da Purchase Order
type: support-article
updated_at: '2024-10-23T19:52:16Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025888952-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-SIGAEIC-Elimina%C3%A7%C3%A3o-de-Saldo-da-Purchase-Order
---

***![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26510174929687)Tempo aproximado para leitura: 00:02:00 min*****Dúvida**Após a criação de um pedido com 100 peças, por exemplo, criei um embarque com 50 peças, como faço para eliminar esse saldo de 50 peças?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – *Easy Import Control* – a partir da versão 12.1.33  
**Solução  
1.** Acesse o módulo **SIGAEIC** em "**Atualizações / Purchaser Order / Manutenção (EICPO400)**", posicione sobre o processo e em seguida selecione "**Outras Ações / Eliminar Saldo**".

![](https://totvssuporte.zendesk.com/attachments/token/4YiEWqYgAlcNOVLiP9TKcozdx/?name=inline1159498096.png)​  
  
**2.** Selecione os itens que terão os saldos eliminados e clique em confirmar. Ao confirmar, o saldo será eliminado.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360025290032)

Para pedidos que não tenham nenhum item utilizado em fases posteriores a Purchase Order, como Licença de importação ou Embarque/Desembaraço:

Caso tente eliminar o Saldo será apresentada a seguinte mensagem abaixo:   
"Não será possível realizar a eliminação de saldo para o item que não foi utilizado em fases posteriores."

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26510174938263)

Neste caso, deve acessar a rotina de Purchase Order/Pedido de Nacionalização e proceder com o estorno ou exclusão do item.  
  
Segue abaixo a documentação oficial do Time de Produto, com relação a alteração da rotina de Eliminação de Resíduo:  
  
<https://tdn.totvs.com/pages/releaseview.action?pageId=863286592>  
***"Incluído validação na eliminação do saldo nas fases de PO, LI e Pedido de nacionalização, onde quando integrado com o módulo de compras, somente será possível realizar a eliminação do saldo quando o saldo utilizado for classificado na sua nota fiscal, devido o saldo previsto do estoque ser desconsiderado quando o saldo de pedido de compras é eliminado antes desse processo."***  
  
  
**Saiba mais:**  
[Purchase Order](https://tdn.totvs.com/display/public/PROT/Purchase+Order+-+EICPO400)  
[EIC0014\_Elimina Saldo do PO](https://tdn.totvs.com/display/PROT/EIC0014_Elimina+Saldo+do+PO)  
[DTRADE-10396 DT Eliminação de Saldo da LI - Error LOG](https://tdn.totvs.com/pages/releaseview.action?pageId=863286592)
