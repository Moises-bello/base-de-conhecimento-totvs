---
content_hash: 122f7c00a2142f65500ad4782813daafa598e018d7d08b7f94d3c8339148e512
fetched_at: '2026-06-29T00:09:16.411260+00:00'
page_id: '421385534'
product: rm
source: tdn-rm
title: Revalorar Custos de Equipamentos.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385534
version: 2
---

---

Após receber os apontamentos e os custos dos equipamentos vindos do Manutenção de Ativos, deve ser executada a rotina de Apropriar Custos e logo após, a rotina de Revalorar Custos de Equipamentos.

Através do menu Cadastros | Mobilidade | Equipamentos | Custos Indiretos, o usuário acessa a opção Processos | Apropriar Custos de Equipamentos e informa o mês e o ano para apropriação. Este processo gera apropriações, que podem ser visualizadas através do menu Cadastros| Apropriação de Serviços/Insumos. Nesta mesma tela é possível revalorar os custos dos equipamentos com os custos importados do SIGA-MNT, o usuário acessa a opção Processos | Mobilidade | Revalorar Custos de Equipamentos, seleciona o período para o qual deseja efetuar a revaloração e o sistema efetua validações. Caso sejam encontradas informações inválidas o sistema armazena informações no log, mas não aborta a execução. A revaloração é executada e a rotina atualiza o valor das apropriações existentes.

O cálculo do valor da apropriação é realizado da seguinte forma: para cada equipamento calcula-se o valor do ticket médio acrescido dos custos indiretos. Os custos indiretos serão rateados proporcionalmente, conforme o número de horas de cada frente de trabalho. Será considerada a parametrização de quais custos indiretos devem ser considerados para compor o custo final do equipamento. O valor do Ticket Médio será calculado dividindo-se o custo total pelo volume de horas (produtivas e improdutivas).

**Atenção:**

Caso só existam custos indiretos para o equipamento no período informado (não existiram apontamentos para determinado equipamento), antes de realizar a apropriação, o usuário deve acessar a visualização dos Custos Indiretos, onde estará habilitado o box "Custo Avulso – Apropriação", deverá informar a tarefa e a data para a apropriação. Será gerada uma apropriação com valor igual a soma de todos os custos indiretos do período.

---
