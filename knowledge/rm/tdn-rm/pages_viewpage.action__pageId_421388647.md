---
content_hash: 1431932ed2d055154812c70fa00282d031d6417fb449167d174936e16b430d3a
fetched_at: '2026-06-29T00:09:17.783039+00:00'
page_id: '421388647'
product: rm
source: tdn-rm
title: FIN - Baixas realizadas de lançamentos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421388647
version: 12
---

Menu: Contas a Pagar/ Recedber - Operações Financeiras - Baixas Realizadas de Lançamentos

Tem objetivo de simplificar a visualização dos itens de baixas gerados. Você define quantos e quais cadastros serão apresentados, criando filtros através do Gerenciador de Filtros (localizado na Barra de Ferramentas).

**Permissão**

A Permissão para visualização do menu Baixas realizadas de lançamentos, fica disponível em Serviços Globais | Segurança | Perfis | Acesso a menus | [02] Contas a Pagar/Receber | [02.01] Operações financeiras | [02.01.09] Baixas realizadas de lançamentos.

**Regerar contabilização de baixa**

Tem como objetivo regerar a contabilização dos itens de baixa integrados ao lote zero, com a possibilidade de informar um novo evento que será considerado para a nova contabilização do lote N, ou seja, o sistema gera o estorno da contabilização do lote zero, mas a nova contabilização no lote N irá considerar o evento informado.

A opção "regerar contabilidade integrada ao lote zero" refaz a contabilização integrada ao lote zero do item de baixa selecionado e tem a possibilidade de informar a data de estorno da contabilização. Caso a data não seja informada, o processo irá considerar a data parametrizada no sistema.

A opção "regerar contabilização não integrada ao lote zero" refaz a contabilização do item de baixa seguindo o evento contábil informado ou o evento utilizado na baixa do lançamento.

**Observação:**

Ao realizar o processo “Regerar contabilização de baixa” e selecionar um evento contábil que esteja com o parâmetro "Não validar valor contabilizado zero" marcado e as partidas estiverem com valor zerado, o processo será concluído sem gerar a contabilização.

**Estornar contabilização de baixa integrada ao lote zero**

Tem como objetivo realizar o estorno e a nova contabilização do item de baixa. O evento contábil utilizado na baixa do lançamento financeiro, será utilizado para regerar a contabilização. Não existe a possibilidade de alterar o evento contábil.
