---
content_hash: 5dc68a0cac4e466647b24d97eedacd6b0f875187dad65f71544c79b356127141
fetched_at: '2026-06-29T00:09:29.118827+00:00'
page_id: '423938815'
product: rm
source: tdn-rm
title: Processar Movimento
type: documentation
url: https://tdn.totvs.com/display/LRM/Processar+Movimento
version: 2
---

Para processar movimentos com status Não processado e gerar rotinas como financeiro, contábil e aprovação por workflow, basta acessar, na visão do movimento, o processo Processar Grupo de Movimentos.   
Será aberta a tela de tradução de XML, onde é possível adicionar/remover movimentos e selecionar vários XMLs para realizar suas devidas traduções.   
Os movimentos selecionados são apresentados em ordem de código do Tipo de Movimento e Número do Movimento em um formato de lista.   
Ao navegar entre os registros, o sistema atualiza automaticamente as informações contidas nas abas "Identificação", "Tradução de Itens" e "Tributação".   
Na aba "Identificação", são exibidas informações gerais do movimento selecionado, onde os dados são importados do XML e por isso não podem ser alterados. Caso o sistema não tenha vinculado o XML a um pedido, por estar assim definido no Tipo de Recebimento, ou porque o número do pedido não constava do XML e o mesmo era espelho da NF-e, o sistema permite que o usuário vincule um ou mais Pedidos ao movimento que está sendo processado.   
O sistema apresentará uma tela de filtros para que sejam selecionados o(s) pedido(s) a ser(em) vinculado(s) ao movimento, sendo que o sistema filtrará apenas os pedidos que geram movimentos do tipo que está sendo processado.   
Em caso de exclusão do movimento de NF-e criado, o XML em questão será desvinculado do movimento e, voltará ao status anterior à inclusão, para que seja possível vinculá-lo a um novo movimento.
