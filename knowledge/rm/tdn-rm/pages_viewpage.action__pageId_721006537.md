---
content_hash: 2a58c088b7fe69d1928810e0f7197e1488f18cc4fb61d1c211ca92866b9fd30f
fetched_at: '2026-06-29T00:11:26.852733+00:00'
page_id: '721006537'
product: rm
source: tdn-rm
title: Pré-Conciliação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=721006537
version: 8
---

Esse processo apresenta sugestões de conciliação, onde o próprio sistema compara débitos e créditos, cruzando informações de acordo com determinadas regras, as partidas e respectivos lançamentos elegíveis são então sinalizados (caixa de seleção da linha marcada). Após isso, devem ser avaliadas pelo usuário que poderá confirmá-las, efetuando a conciliação, ou descartá-las, desmarcando-as.

**Para utilizá-la basta, a partir da visão da conciliação, acionar o botão** **Pré-conciliação** (abaixo à direita na visão de conciliação). A rotina de conciliação será iniciada para todos os registros da visão.

O procedimento de pré-conciliação seguirá o seguinte formato:

Tendo como base a integração dos dados entre os módulos da Linha RM e os lançamentos recuperados para a conciliação o sistema irá sugerir conciliações para o usuário. Para isso, a partir do lançamentos recuperados com base nos filtros, o sistema localizará automaticamente provisão e a baixa (débito = crédito) equivalentes através das regras abaixo:

* Recuperação dos dados do Faturamento e Financeiro que retornam as movimentações das operações contábeis;
* A partir dos dados retornados fazer a pré-conciliação: Débito e Crédito precisam "fechar" por coligada considerando o movimento recuperado nos módulos citados acima.

A imagem abaixo é um exemplo da pré-conciliação considerando o Contábil x Faturamento x Baixa no Financeiro por isso está utilizando o campo **Identificador Movimento** mas o mesmo se aplica ao cenário Contábil x Financeirox Baixa no Financeiro basta utilizar o campo **Lançamento Financeiro**

Visualização da tela
