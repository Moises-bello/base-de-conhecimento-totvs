---
content_hash: 075ce2d3812031101bc2e9f874f015cf5b73c3dec841e3bd7a97e95310677de7
fetched_at: '2026-06-29T00:10:16.344158+00:00'
page_id: '469434420'
product: rm
source: tdn-rm
title: Atualizar Competencia
type: documentation
url: https://tdn.totvs.com/display/LRM/Atualizar+Competencia
version: 5
---

Buscando simplificar o processo de nossos usuários, foi criado o processo que permite alterar a Competência Base da comissão.

O foco do processo são os registros de comissões que são do tipo RH, sendo que as do tipo BackOffice não possuem Competência Base e não se aplica a execução do processo.

As comissões que não foram pagas na competência original por alguma não conformidade (Falta de documentos, etc), precisam ser atribuídas à nova competência de pagamento, para que possa ser avaliada de novo e, se estiver em conformidade, serem pagas.

O processo pode ser executado na tela de visão de comissões (geral), suportando a seleção de várias comissões, ou dentro da edição de uma comissão específica.

Somente comissões não integradas podem ter sua competência atualizada.

Para usar o processo, devem ser selecionados os registros referentes à comissão que devem ter sua data de competência atualizada e executar o processo "Atualizar Competência Comissão(ões)".

No processo, temos que indicar a partir de qual competência as parcelas serão alteradas e a nova competência.

Ao Executar, as competências dos registros selecionados estarão atualizadas a partir da a nova data. A primeira parcela da comissão em aberto que encontrar terá exatamente a data informada na competência. As parcelas posteriores terão incrementalmente um mês a mais na competência.

**Exemplo:**

Parcela 1 - 01/2019 - Integrada

Parcela 2 - 02/2019 - Não Integrada

Parcela 3 - 03/2019 - Não Integrada

Parcela 4 - 04/2019 - Não Integrada

Parcela 5 - 05/2019 - Integrada

**Execução do processo:**

Antiga competência base: 01/2019

Nova competência base: 05/2019

**Parcela 1 - 01/2019 - Integrada**

**Parcela 2 - 05/2019 - Não Integrada**

**Parcela 3 - 06/2019 - Não Integrada**

**Parcela 4 - 07/2019 - Não Integrada**

**Parcela 5 - 05/2019 - Integrada**
