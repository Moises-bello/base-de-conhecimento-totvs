---
content_hash: e26036883a6bf0186f611985bd964be67ce96d864282441b99a7ee22c5c356b1
fetched_at: '2026-06-29T00:11:21.997416+00:00'
page_id: '697720906'
product: rm
source: tdn-rm
title: Alterar locais de estoque
type: documentation
url: https://tdn.totvs.com/display/LRM/Alterar+locais+de+estoque
version: 5
---

Atenção

Recurso disponível na release 12.1.2209 ou superior.

Esta funcionalidade possui a finalidade de alterar os locais de estoque dos itens de movimento selecionados por uma escolha do usuário desde que seja um dos locais de estoque disponibilizados na filial e que estejam ativos. Além disso, tem o intuito de facilitar a alteração de locais de estoque de itens dentro do movimento.

Para que tal função fique disponível (o botão apareça na barra de ferramentas da visão de itens de movimento na edição do movimento) são necessárias as seguintes parametrizações:

* Local de estoque NÃO pode estar parametrizado como **Usar Local Único** (Parâmetros Gerais > Etapa 11 - Local de estoque);
* Tipo de movimento estar parametrizado com o **Edição do Local de Emissão** definido como "**Edita**" (Parametrização do tipo de movimento > Etapa 2 - Movimento - Emitente e Destinatário 1/2);
* Tipo de movimento estar parametrizado como **Local de Estoque por Item** (parametrização do tipo de movimento Etapa 42 - Estoque - Estoque 2/3).

Ao clicar no botão será exibida uma janela onde é possível selecionar os locais de estoque disponíveis na filial do movimento.

Após clicar no botão OK o local de estoque escolhido será atualizado nos itens de movimento selecionados e bastará o usuário salvar o movimento.
