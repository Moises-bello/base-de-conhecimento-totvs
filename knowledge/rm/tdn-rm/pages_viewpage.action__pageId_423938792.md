---
content_hash: 755b59b470aea02bf27bc6a5d98cc257cb422b89c118901ae62d1393a5a5322f
fetched_at: '2026-06-29T00:09:29.060604+00:00'
page_id: '423938792'
product: rm
source: tdn-rm
title: Transferência de Valores do Orçamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938792
version: 4
---

Por esse processo é possível transferir valores de orçamento para qualquer item de período, desde que tenha o mesmo Tipo de Orçamento(**Despesa/Despesa ou Receita/Receita**).

**Período de Orçamento**: deve ser informado o [Período do Orçamento](http://tdn.totvs.com/pages/viewpage.action?pageId=423938809) de onde será a origem e destino do valor a ser transferido.

**Orçamento de Origem/Item de Período**: deve ser selecionado o Item de Período do Orçamento, em seguida dever ser escolhido o Centro de Custo/Natureza Orçamentária o qual irá ceder o valor ao item do orçamento de destino. Somente são listados os Centro de Custo/Natureza Orçamentária que possuem valor disponível para transferência.

***Importante!*** é possível bloquear transferências de orçamento de determinadas Naturezas Orçamentárias, para isso deve-se acessar o cadastro de [Natureza Orçamentária](http://tdn.totvs.com/pages/viewpage.action?pageId=423937949) e marcar a opção "Não Permite Transferir Valores".

**Orçamento de Destino/Item de Período**: deve ser selecionado o Item de Período do Orçamento, em seguida dever ser escolhido o Centro de Custo/Natureza Orçamentária o qual irá receber o valor do item do orçamento de origem.  
 O valor a transferir deve ser informado no Orçamento de destino diretamente na grid após seleção do Item de Período de Destino. O saldo a ser transferido respeita a seleção da Centro de Custo/Natureza feita diretamente na grid de origem, permitindo que o saldo de um Centro de Custo/Natureza de origem seja transferido para mais de um Centro de Custo/Natureza de destino.

**Permissões**

Existem permissões de transferência vinculadas ao perfil do usuário que podem ser definidas para permitir ou não ao usuário realizar determinados tipos de transferências, essas permissões são:

* Nível 1 - Transfere entre Naturezas do Centro Custo: Somente é permitido transferir saldo entre Naturezas do mesmo Centro de Custo.
* Nível 2 - Transfere entre Naturezas e Centros de Custo que está Associado: Permite transferir saldo entre Naturezas e Centros de Custo diferentes.
* Nível 3 - Transfere entre Naturezas e Centros de Custo que está Associado, com Valores dos Períodos Anteriores: Permite transferir saldo entre Naturezas e Centros de Custo diferentes, mas que tenham itens de período inferiores aos do orçamento de origem.
* Nível 4 - Transfere entre Naturezas e Centros de Custo que está Associado, com Valores de Todos os Períodos: Permite transferir saldo entre Naturezas e Centros de Custo diferentes, para todos os itens de período disponíveis.

***Observações**:*  
- Para os níveis 1 e 2 o item de período do orçamento de destino será carregado automaticamente conforme escolha do orçamento de origem.  
- As permissões de nível maior prevalecem sobre as de nível inferior. Exemplo: se estiver habilitada a permissão de Nível 4, as funções das permissões de Nível 1,2,3 são automaticamente habilitadas.  
- Para qualquer tipo de transferência é necessário que o usuário esteja vinculado ao Centro de Custo/Natureza Orçamentária participantes da transferência.
