---
content_hash: 141a4ebfca6a64433b2fb9b5fe7ebc864fefbca1ea94e6e443a7a51042d1fe32
fetched_at: '2026-06-29T00:09:10.906702+00:00'
page_id: '403735177'
product: rm
source: tdn-rm
title: S-2230 - Como utilizar o parâmetro "Quantidade de dias anterior ao período
  do gozo de férias para envio do S-2230"?
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=403735177
version: 7
---

O parâmetro "**Quantidade de dias anterior ao período de gozo de férias para envio do S-2230 (Máx. 60 dias)**" foi criado com o intuito em atender as empresas que trabalham com o planejamento de férias anual, para que possam reduzir seu número de retificações, pois ao planejar as férias para todo um ano, integrar com o TAF e enviar ao governo, existe a possibilidade de que alterações no cadastro das férias sejam efetuados, e com isto se faz necessário retificar estas férias.

Com o uso deste parâmetro, as férias serão barradas para integração com TAF de acordo com o número de dias preenchido pelo cliente. Desta forma, o usuário poderá alinhar em seu processo, um determinado número de dias máximo anterior à data de início de gozo de férias para modificações nos cadastros de férias, estabelecendo assim maior integridade de seus dados e um menor retrabalho, tendo em vista que esta parametrização diminua a necessidade de retificações cadastrais.

Ao tentar efetuar a integração de um evento S-2230 relacionado a férias, o sistema irá subtrair  a data início do afastamento da data atual, se esta operação ultrapassar a quantidade de dias informada no parâmetro o sistema não irá enviar o evento e irá retornar um aviso no log do processo.

Exemplo:

A data atual é 10/01/2018 e cadastro férias que iniciam dia 01/05/2018 para um determinado funcionário. Ao parametrizar o campo em questão com o número de 60 dias, só poderei integrar minhas férias a partir do dia 01/03/2018 (01/05/2018 - 60 dias = 01/03/2018).

Antes dessa data, se tentar integrar esse evento com o TAF, o sistema não fará essa integração e gerará a informação no log de integração. O sistema represará o evento até a data calculada para a integração.

**Observações:**

Caso este campo seja preenchido com o valor 0, o sistema não realizará nenhuma validação e por consequência irá integrar os eventos de férias em qualquer data, independente do cadastro de férias.

Ao integrar com o TAF o registro S-2230 onde a coluna *Afastamento de Férias =SIM* o sistema irá preencher a coluna *Fora do prazo de envio*  conforme parametrização feita no parâmetro **“Quantidade de dias anterior ao período de gozo de férias para envio do S-2230 (Máx. 60 dias)"**
