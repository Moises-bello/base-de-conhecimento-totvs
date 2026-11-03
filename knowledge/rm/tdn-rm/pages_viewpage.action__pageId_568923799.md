---
content_hash: 7d8a0b14d531467f649bc34a94cb699b2ea13c6a552ba2f4374d6e225335b2a8
fetched_at: '2026-06-29T00:10:51.482366+00:00'
page_id: '568923799'
product: rm
source: tdn-rm
title: Gerar Movimento a partir da Apropriação
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=568923799
version: 4
---

Através do processo de **Gerar Movimento a partir da Apropriação** é possível gerar movimentos no TOTVS Backoffice.

O controle de segurança do processo se encontra na seguinte hierarquia:

Existem dois parâmetros de projeto que devem ser definidos para que o processo possa ser executado:

O produto pode ser alterado na tela do processo.

Para a execução do processo, a seleção de registros na visão de Apropriação é opcional, sendo que a tela terá um comportamento diferente em relação à existência de linhas selecionadas.

* **Com linhas selecionadas**: Os campos de Intervalo e Origem da Apropriação estarão indisponíveis pois serão consideradas as apropriações selecionadas.
* **Sem linhas selecionadas**: Todos os campos do processo estarão disponíveis.

  + A Data Inicial é obrigatória;
  + A Data Final é opcional e se não for definida, todas as Apropriações a partir da Data Inicial serão consideradas.

**Validações:**

* Necessário informar o Tipo de Movimento nos parâmetros de projeto;
* Necessário informar o Produto nos parâmetros de projeto ou na própria tela do processo;
* Somente apropriações com as seguintes origens poderão ser selecionadas:
  + Construção Obras e Projetos;
  + Apontamento de Mão de Obra;
  + Rateio de Mão de Obra
  + Apontamento de Equipamentos;
  + Apontamento de Timesheet;
  + Apropriação da Importação via Excel.
* Se não existirem linhas selecionadas:
  + Necessário informar a Data Inicial;
  + Necessário selecionar ao menos uma origem da apropriação.

A execução desse processo poderá ser agendada.

Se executado com sucesso, as apropriações envolvidas terão o identificador do movimento associado à elas e poderá ser visualizado na visão de Apropriação:

**Anexo de Movimentos:**

Os dados do movimento gerado pela apropriação podem ser visualizado no anexo de "Movimento".

**Excluir Movimentos:**

Para excluir os movimentos gerados basta utilizar o processo "Excluir Movimentos".

O controle de segurança do processo se encontra na seguinte hierarquia:

Basta selecionar ao menos um registro de apropriação que tenha a coluna "Id. Movimento" preenchida para que o processo possa ser executado.

Após a execução, todas as apropriações que tinham os movimentos selecionados estarão com a coluna de movimento vazia.

Não será prmitido executar o processo de "Gerar Movimento a partir de Apropriação" para uma apropriação do tipo transferência, e por isso será exibida a mensagem abaixo:

Para saber mais sobre Transferência de Apropriação, .
