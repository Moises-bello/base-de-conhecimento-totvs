---
content_hash: 9a9b2874d50ec73ed4f69a9093516a56a815ab962af14804477450fd727d6831
fetched_at: '2026-06-29T00:09:26.614452+00:00'
page_id: '423938337'
product: rm
source: tdn-rm
title: Cenários - Gestão Patrimonial
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938337
version: 10
---

Este recurso permite que sejam criados cenários com  diferentes permitindo que os valores dos patrimônios sejam calculados para mais de uma moeda. Durante o cadastro do cenário deve-se informar a descrição, o cálculo, a moeda e o índice sendo este último não obrigatório.

O cenário cadastrado deve ser associado ao grupo de patrimônio para que os valores a serem calculados para o patrimônio respeitem a moeda e o índice (e suas respectivas cotações), bem como o tipo de depreciação (integral ou proporcional).

No cadastro do cenário pode-se também definir as informações relacionadas ao . Estas informações serão utilizadas, posteriormente, no evento contábil para que seja realizada a contabilização a ser enviada ao sistema contábil.

O processo de cálculo de Depreciação poderá ser executado a partir da tela de Cenários. Para isto deve-se selecionar o cenário desejado e executar o processo Calcular Cenário.

**Observação**

Somente os patrimônios associados a grupo de patrimônio que possui o cenário em questão serão calculados.

A edição do cenário de cálculo, somente será permitida, quando a moeda do cenário for diferente da **moeda corrente** e a **data de aquisição do patrimônio**, estiver dentro do **período atual de cálculo.**

Veja também

* Cálculos

* Grupo de patrimônio
