---
content_hash: f55d96c804f5c4b902cc7ea3e84fec9b04c84a48b804c9a56325c4d97b9d853c
fetched_at: '2026-06-29T00:11:11.785677+00:00'
page_id: '650484111'
product: rm
source: tdn-rm
title: Discriminar Valores de retenção, dedução e adiantamento
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=650484111
version: 8
---

Parâmetro: **Discriminar Valores de Retenção, dedução e adiantamento.**

Quando este parâmetro estiver marcado no projeto, a liberação dos valores de retenção, dedução e adiantamento serão enviados de forma separada e para os respectivos campos no BackOffice.

IMPORTANTE

No movimento de destino no Backoffice, o tipo do campo que será enviado o adiantamento (Valor Extra 1, 2, 3, 4, 5, 6, 7, 8, 9 ou 10), deverá estar parametrizado como Valor ou Ambos:

Observação: Valor Extra de 3 a 10 disponível a partir da versão 12.1.2606.

**Exemplo**: Em um contrato, temos a seguinte situação para liberação:

R$ 4.045,95 em Deduções, R$ 4.912,59 em Retenções e R$ 100.000,00 em Adiantamentos.

Na liberação para o BackOffice, temos os seguintes valores:

Valor Medido: R$ 202.297,88 e o Calculado para liberação R$ 93.339,33. Ou seja, com R$ 108.958,55 (Deduções, Retenções e Adiantamentos) descontados do valor medido.

Ao enviar esse movimento para o BackOffice, esses valores são enviados da seguinte forma:

**Adiantamento:** Pode ser enviado no campo de desconto, ou Valor Extra 1, ou Valor Extra 2 do MOVIMENTO, dependendo do campo informado na primeira tela (Parâmetro do projeto>Contrato>Liberação):

**Deduções** e **Retenções**:

São enviados para os campos de **RETENÇÃO** e **DEDUÇÃO** no ITEM DO MOVIMENTO.

Com isso, o preço unitário do item **não** sofre alteração, pois os valores de descontos e deduções foram enviados para seus campos do movimento:

**Importante:** Quando este parâmetro está **marcado**, o controle de saldo e abatimentos passa a ser do Totvs Construção e Projetos e não mais do BackOffice. Dessa forma, não se deve gerar Notas de Crédito ao enviar adiantamentos para o BackOffice, pois dessa forma, seria considerado duas vezes esse adiantamento.

Funcionamento com o parâmetro **DESMARCADO**:

Valor Medido: R$ 202.297,88 e o Calculado para liberação R$ 93.339,33. Ou seja, com R$ 108.958,55 (Deduções, Retenções e Adiantamentos) descontados do valor medido.

Ao enviar esse movimento para o BackOffice, esses valores são enviados da seguinte forma:

**Adiantamento:** **Não** é enviado no campo de desconto do MOVIMENTO.

**Deduções e Retenções: Não** serão discriminados em seus campos específicos no item do movimento.

**Com isso, o preço unitário do item, já chega no BackOffice com o desconto dos valores de Adiantamento, Deduções e Retenções.**
