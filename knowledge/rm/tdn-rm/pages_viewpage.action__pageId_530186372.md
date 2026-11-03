---
content_hash: 013393fbe32ad32eafd50100122e5bf0f0390e36f48b5c1a63ac79b6691804c7
fetched_at: '2026-06-29T00:10:35.507141+00:00'
page_id: '530186372'
product: rm
source: tdn-rm
title: Meu Imóvel - Comunicados
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=530186372
version: 32
---

**Índice**

---

# **1) Visão Geral**

---

A funcionalidade **Comunicados**estará disponível a partir da versão **12.1.28**da Biblioteca RM. Esta funcionalidade apresentará os comunicados enviados para o usuário do aplicativo.

Ao tocar no menu de comunicados, serão exibidos todos os comunicados do usuário, lidos e não lidos, ordenados por data de publicação. Os comunicados serão apresentados em forma de cards, que serão exibidos com as informações do Empreendimento ao qual ele pertence. Caso o comunicado seja global, ele virá com a informação "Todos os empreendimentos". Caso possua dois ou mais empreendimentos, o nome dos Empreendimentos será listado no topo do card. Além das descrições do empreendimento, será mostrada também a descrição do comunicado, **em negrito**, caso o mesmo ainda não esteja lido. Além disso, no rodapé do card de comunicado terá a informação da data de publicação do mesmo, simplificada em dias, semanas ou meses.

No card do comunicado, caso existam muitos empreendimentos associados haverá um botão "**mais"** que ao ser tocado, irá exibir todos os empreendimentos. A partir dessa ação o botão "**menos"** irá voltar para a exibição recolhida quando tocado.

O usuário poderá também fazer uma pesquisa, tocando na caixa de pesquisa identificada com a lupa, no topo da visão.

**Importante**: O sistema irá salvar as 5 últimas pesquisas realizadas pelo usuário, de forma a facilitar a busca futura por comunicados que possuam o termo desejado.

O padrão de exibição inicial será de 5 comunicados. Caso existam outros comunicados cadastrados, basta o usuário rolar para cima com os dedos que o sistema irá carregá-los automaticamente.

---

# **2) Filtros e Ordenação**

---

A visão de comunicados irá oferecer uma opção de filtros, bastando selecionar o ícone de filtro localizado na direita da barra de menu.

O **filtro** poderá ser composto por empreendimento, listando apenas os empreendimentos selecionados pelo usuário, como mostra a imagem:

Importante: Comunicados globais, ou seja, que são apresentados para todos os empreendimentos, serão mostrados independente do filtro escolhido.

A **ordenação** poderá ser realizada de dois modos:

* Mais recentes: Mostra os comunicados mais novos primeiros, ou seja, cuja data de publicação é mais próxima da data atual;
* Mais Antigos: Mostrará os comunicados mais antigos primeiro, ou seja, cuja data de publicação é mais distante da data atual.

---

# **3) Exibição do conteúdo do comunicado**

---

Quando o usuário tocar em dos comunicados, será aberta a página exibindo o seu conteúdo e ele será marcado como lido.   
Caso toque em "**Marcar todos como lidos"**, todos os comunicados serão marcados como lidos. Essa ação não poderá ser desfeita.

Importante

Para que o comunicado seja apresentado de forma responsiva nos dispositivos, recomendamos que ao cadastrar o comunicado no Portal do Cliente, seja utilizado no corpo do comunicado a tag html viewport, para que a exibição não apresente divergências por conta do tamanho da tela do dispositivo.   
Abaixo segue um exemplo de estrutura HTML que irá ser apresentada responsivamente em todos os dispositivos.

**Título do Comunicado.**

![Imagem](img.jpg)

Texto do Comunicado

]]>
