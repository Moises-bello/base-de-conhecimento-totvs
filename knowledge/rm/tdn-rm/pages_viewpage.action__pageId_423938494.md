---
content_hash: 7699073d534c062956e1891988590b03247ff4f7540649705d6be5d21d5f6153
fetched_at: '2026-06-29T00:09:27.304616+00:00'
page_id: '423938494'
product: rm
source: tdn-rm
title: Fechar Exercício Contábil
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938494
version: 4
---

Este processo é responsável por fechar o exercício contábil. O fechamento de exercício será anual e somente poderá ser executado um exercício (ano) por vez.

A execução deste processo move os dados de contabilização para tabelas de histórico deixando as tabelas de contabilização mais enxutas.

Para execução deste processo, o sistema faz algumas validações, sempre considerando o ano definido para liberação do exercício nos parâmetros do processo:

* Valida se existe lançamentos em Lotes não integrados;
* Valida se existe lançamentos com diferença;
* Valida se existe inconsistências nos lançamentos;
* Valida se existe tarefas pendentes;

Exemplo:

O sistema está parametrizado com o período contábil 01/01/2010 até 01/01/2020 e começou sua operação no dia 01/01/2010. Se o usuário executar fechamento de período do ano 2010 o sistema fará as seguintes alterações:

* Fechará o exercício contábil, que corresponderá ao período de 01/01/2010 a 31/12/2010;
* Calcula os saldos das contas de acordo com os parâmetros preenchidos para o exercício que esta sendo fechado. Para calcular o saldo das contas, o sistema considerará o saldo do último exercício fechado.

O cálculo de saldo das contas segue o seguinte agrupamento:

* Coligada
* Conta contábil
* Filial
* Departamento
* Conta gerencial
* Centro de custo
* Código da Filial
* Coligada da Eliminação (Utilizado apenas quando se trabalha com Consolidação e Eliminações de Operações Intercompany)
* Conta Contábil de Eliminação (Utilizado apenas quando se trabalha com Consolidação e Eliminações de Operações Intercompany)

O Cálculo dos saldos é a soma do Exercício anterior com o saldo do exercício fechado. Além disso o processo faz:

* Move os dados das contabilizações no período selecionado para histórico;
* Atualiza a tabela de saldo por exercício;
* Atualiza as datas do período contábil e data de fechamento.
