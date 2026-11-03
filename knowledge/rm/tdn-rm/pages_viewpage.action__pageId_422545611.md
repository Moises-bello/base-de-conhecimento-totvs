---
content_hash: f86c9e58c11f26899564299ff2a60289a22c4112f417c7218153ac36a9e39c9d
fetched_at: '2026-06-29T00:09:19.554990+00:00'
page_id: '422545611'
product: rm
source: tdn-rm
title: Informações Adicionais sobre Documentos Emitidos por ECF
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=422545611
version: 4
---

Existem alguns tipos de documentos referentes a bilhetes de passagem que podem ser emitidos tanto por equipamento ECF ou por Nota Fiscal, são eles: Bilhete de Passagem Rodoviário (Modelo 13), Bilhete de Passagem Aquaviário (Modelo 14), Bilhete de Passagem e Nota de Bagagem (Modelo 15), Bilhete de Passagem Ferroviário (Modelo 16).

O método de emissão irá determinar em qual registro do SPED Fiscal estes documentos serão declarados. Quando emitidos por Nota fiscal estes modelos devem ser declarados nos registros D300, D301 e D310. Quando emitidos por equipamento ECF este modelos devem ser declarados nos registros D350, D355, D360, D370 e D390.

Para diferenciar os métodos de emissão foi criado no cadastro de Tipos de Documento o  campo "UTILIZA CUPOM FISCAL". Todos os tipos de documento emitidos por ECF devem ter este campo marcado para que os mesmo sejam gerados no registro correto do SPED Fiscal.

Nesta versão este campo só estará disponível em bases nas quais tenha sido executado script para a criação do mesmo. Nas bases nas quais este script não for executado a seleção dos lançamentos de Cupom Fiscal continuará sendo feita pela informação constante no campo CODMODDOC do cadastro do tipo de documento associado ao Lançamento Fiscal.

Ainda para os tipos de documento 2E, 13, 14, 15 e 16 ao serem associados a Lançamentos Fiscais será apresentada nos seus itens as informações de transporte.
