---
content_hash: 882b82867015012676e234c104375aafa75bb12bfa51b0fd73b053db54836af2
fetched_at: '2026-06-29T00:09:28.018056+00:00'
page_id: '423938625'
product: rm
source: tdn-rm
title: Não calcular/atualizar capa do lote automaticamente ao abrir a visão de lotes
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938625
version: 8
---

Houve a necessidade de criação de um parâmetro para que a capa do lote não atualize automaticamente conforme movimentações no lote. O parâmetro da a possibilidade do usuário atualizar a capa do lote conforme sua necessidade.

Foi criado o parâmetro "Não calcular/atualizar capa do lote automaticamente ao abrir a visão de lotes", ao marcar este parâmetro, o sistema não irá realizar o cálculo automaticamente da capa do lote ao abrir a visão de dados, e para este cenário **será disponibilizado no rodapé da tela uma opção que permite ao usuário acionar um botão que realiza o cálculo dos lotes selecionados**.

A visão de lote terá o seguinte comportamento quando o parâmetro estiver marcado:

**1º Para os lotes em que a opção "Digitar Capa" está marcada**

O sistema apresentará apenas as informações que são fixadas pelo usuário ao cadastrar o lotes (valor, data inicial e data final), a informações que são calculadas (total de créditos e débitos) serão apresentadas somente se o usuário acionar o botão de calcular.

**2º Para os lotes em que a opção "Digitar Capa" não está marcada**

Os campos que são calculados (data inicial, data final, total débitos e créditos, valor soma) serão apresentados em branco e seus valores serão mostrados somente se o usuário acionar o botão de calcular.

Parâmetro Desmarcado: Atenção aos filtros

 Quando o parâmetro **não**estiver marcado, quer dizer que o sistema irá calcular o valor dos lotes sempre que a visão for aberta.

Esse cálculo do valor do lote será feito **apenas**para os lotes que forem retornados pelo filtro que foi selecionado pelo usuário na visão.

O sistema seguirá o seguinte fluxo:

Busca todos os lotes conforme o filtro que foi selecionado na visão.

Atualiza o valor de cada um dos lotes (atualizado também no banco de dados).

Exibe na visão os lotes com os valores calculados e atualizados.

Sendo assim indicamos, verifique sempre o filtro que está sendo utilizado na visão para que nenhum Lote fique de fora da atualização de valores automático.
