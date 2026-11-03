---
content_hash: a6ae0ad1e1d782c9df678fc08953c5cc6759bff1d10132edfc3cbb36ec95a1c4
fetched_at: '2026-06-29T00:09:32.553834+00:00'
page_id: '425458873'
product: rm
source: tdn-rm
title: Contabilização por Competência - Contratos
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425458873
version: 13
---

---

A funcionalidade de contabilização por competência tem como objetivo a escrituração das parcelas contábeis de determinado contrato financeiro tomando como base a competência definida em um período letivo ou parametrização por curso em detrimento do período válido do contrato financeiro nessa competência definida.

Visando flexibilizar a contabilização por competência nas instituições de ensino superior que possuem um período de contratação menor que a competência (cursos de curta duração) ou maior que a competência (cenários de pós graduação), foi criado a possibilidade de definição deste período contábil por contrato.

**Parametrização**  
Na parametrização do sistema (Parâmetros > Integrações > Contabilidade) foi adicionada a opção do sistema buscar a data contábil por contrato.

A parametrização da contabilização por competência será alterada para ter a nova opção de parametrização do período: Data contábil baseado no Contrato e Plano de pagamento (default);

O sistema foi adequado para que os campos de definição da competência, sejam visíveis baseado no tipo de parametrização feita, ou seja:

* O cadastro de período letivo a aba contabilização só ficará disponível se o parâmetro utiliza contabilização por competência estiver marcado e data contábil selecionada seja período letivo;
* Cadastro parametrização por curso a aba contabilização só ficará disponível se o parâmetro utiliza contabilização por competência estiver marcado e data contábil selecionada seja parametrização por curso;
* Cadastro de contrato e plano de pagamento incluir aba de contabilização com competência inicial e final. Esta aba contabilização só ficará disponível se o parâmetro utiliza contabilização por competência estiver marcado e data contábil selecionada seja contrato / plano de pagamento.

O cadastro de período letivo passa a ter um novo campo "Período Letivo encerrado para Contabilização", assim o processo de contabilização por competência irá processar apenas os contratos que não estejam encerrados para contabilização, evitando assim inconsistências referente ao período contábil.

Caso esteja parametrizado para utilizar a contabilidade por competência e o parâmetro de data contábil estando por plano de pagamento e contrato, a definição da data contábil passa a ser **cadastrada no plano de pagamento por padrão**.

Todo contrato vinculado a este plano de pagamento receberá essa definição de competência por padrão durante a inclusão e **não será possível editar essa definição no contrato** caso tenha plano de pagamento vinculado ou caso o usuário não tenha permissão específica para tal ("Permite alteração de data contábil do contrato").

Os processos abaixo serão adequados com os novos campos de data de início e fim de competência, sendo preenchidos automaticamente com os valores do plano de pagamento selecionado, ou obrigatórios caso não tenha um plano de pagamento padrão e esteja parametrizado para permitir contabilizar usando o período por contrato:

* Processo de cópia de planos de pagamento entre períodos letivos;
* Matrícula Presencial;
* Matrícula Online;
* Matrícula em Lote;
* Processo Seletivo RM;
* Processo Seletivo Terceirizado;
* Alteração de situação de matrícula no período letivo.

  Informações Complementares

---

[Geração da contabilização por competência](http://tdn.totvs.com/pages/viewpage.action?pageId=425458827)

 Veja Também

---

[Modelos de Contabilização por competência](http://tdn.totvs.com/pages/viewpage.action?pageId=425459507)  
[Competência contábil](http://tdn.totvs.com/pages/viewpage.action?pageId=425458867)  
[Cálculo do valor do contrato X Contabilização](http://tdn.totvs.com/pages/viewpage.action?pageId=425459064)   
[Cálculo do valor de bolsas X Contabilização](http://tdn.totvs.com/pages/viewpage.action?pageId=425458834)  
[Cancelamento do contrato X Contabilização](http://tdn.totvs.com/pages/viewpage.action?pageId=425458749)
