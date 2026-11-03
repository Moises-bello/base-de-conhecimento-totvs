---
content_hash: 95db4797baa25162e2fc2f694e76d5100e84f41fd77ff5f43c368d228d0711d5
fetched_at: '2026-06-29T00:09:16.395200+00:00'
page_id: '421385529'
product: rm
source: tdn-rm
title: Sincronizar Folha de Ponto
type: documentation
url: https://tdn.totvs.com/display/LRM/Sincronizar+Folha+de+Ponto
version: 3
---

---

O processo de confronto entre o relatório de ponto e os apontamentos de mão de obra vindos do coletor móvel permite verificar as inconsistências entre o total de horas registradas pelo relatório de pontos e pelos apontamentos diariamente, proporcionando maior controle sobre a produtividade de cada funcionário. O registro de ponto representa o período em que o funcionário ficou na empresa e os apontamentos de mão de obra vindos do coletor móvel representam o período em que ele foi produtivo. O confronto entre os dois irá mostrar a improdutividade do funcionário. Essas comparações são realizadas diariamente. A validação entre o relatório de ponto e os apontamentos verifica duas consistências:

* Se existe uma folha de ponto para cada apontamento realizado no dia. Caso não exista, o sistema verifica se a folha de ponto está fechada. Se estiver o apontamento será excluído, mas se a folha estiver aberta o status do apontamento é alterado para "Pendente de Ponto".
* Se o total de horas apontadas condiz com o total de horas registradas no ponto em uma mesma data. Caso o total de horas apontadas for menor ou igual ao total de horas registradas no ponto, o apontamento estará consistente para ser apropriado, e as horas improdutivas (diferença entre horas de ponto e de apontamento) serão tratadas no processo de rateio e revaloração de mão de obra. Já se a quantidade de horas apontadas for maior que as horas do ponto no dia, o apontamento recebe o status de Inconsistente, não poderá ser apropriado e o campo motivo da inconsistência será preenchido.

**Observação:**

Nas validações também serão analisadas as datas que começam em um turno e terminam no turno do outro dia.

Esta validação contempla a folha de ponto quando é gerada de terceiros. Além disso, ela deverá ser tratada quando o Relatório de Ponto estiver integrado com o Protheus ou Chronus. Para controlar a integração com o Protheus deve ser utilizado o processo Sincronizar Folha de Ponto, disponível em Controle | Mobilidade | Sincronizar Folha de Ponto. Este processo irá buscar os registros de ponto do Protheus e trazer para o TOTVS Obras e Projetos.

**Atenção:**

A opção Sincronizar Folha de Ponto só estará disponível se o parâmetro "Integrado Ponto Terceiros" estiver inativo e a Integração TOTVS Folha Pagamento X Mobilidade estiver ativa.

Após sincronizar os dados, os registros de ponto podem ser vistos acessando o menu Controle -> Mobilidade -> Folhas Tarefas -> Seleciona uma tarefa -> Anexo -> Apontamento de Mão de Obra -> Editar -> Registro de Ponto e informando um período. Nesta tela são exibidos todos os registros de ponto do período apontado, para cada funcionário.

---
