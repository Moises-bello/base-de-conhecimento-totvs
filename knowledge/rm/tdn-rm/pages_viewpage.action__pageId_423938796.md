---
content_hash: 09a83e31dc645f4a905afadcd58ca3c58936ba62ed989c043016d9dea6166210
fetched_at: '2026-06-29T00:09:29.070684+00:00'
page_id: '423938796'
product: rm
source: tdn-rm
title: Transferência de Valores do Orçamento para Itens de Períodos Posteriores
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938796
version: 3
---

Utilizando esse processo é possível transferir valores de orçamento do mesmo tipo (**Despesa/Despesa ou Receita/Receita**) para item de período posteriores.   
 **Período de Orçamento**: deve ser informado o [Período do Orçamento](http://tdn.totvs.com/pages/viewpage.action?pageId=423938809) de onde será a origem e destino do valor a ser transferido.

**Orçamento de Origem/Item de Período**: deve ser selecionado o Item de Período do Orçamento, em seguida dever ser escolhido o Centro de Custo/Natureza Orçamentária o qual irá ceder o valor ao item do orçamento de destino. Somente são listados os Centro de Custo/Natureza Orçamentária que possuem valor disponível para transferência.

**Orçamento de Destino/Item de Período**: deve ser selecionado o Item de Período do Orçamento, em seguida dever ser escolhido o Centro de Custo/Natureza Orçamentária o qual irá receber o valor do item do orçamento de origem.  
 ***Observação**:* No Orçamento de destino são exibidos somente os itens de períodos posteriores ao item do orçamento de origem selecionado*.*  
 Ao executar o processo todo o saldo do Centro de Custo/Natureza Orçamentária de origem será transferido para o Centro de Custo/Natureza Orçamentária de destino.  
    
 **Permissões**

Existem permissões de transferência vinculadas ao perfil do usuário que podem ser definidas para permitir ou não ao usuário realizar determinados tipos de transferências, essas permissões são:

* Nível 1 - Transfere entre Naturezas e Centros de Custo que está Associado: Permite transferir saldo entre Naturezas e Centros de Custo que estão vinculados ao usuário.
* Nível 2   Transfere entre qualquer Natureza e Centro de Custo: Permite transferir saldo entre todas as Naturezas e todos os Centros de Custo, independente de estar vinculado ao usuário.

***Observação**:*  
- As permissões de nível maior prevalecem sobre as de nível inferior. Exemplo: se estiver habilitada a permissão de Nível 2, as funções da permissão de Nível 1 são automaticamente habilitadas.
