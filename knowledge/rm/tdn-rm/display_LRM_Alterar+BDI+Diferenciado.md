---
content_hash: 1db05c5f662ccfc6cc06ddf4b3172a29e6ab41f7c5b3eb12333c4f3f6edd0d6f
fetched_at: '2026-06-29T00:09:14.101638+00:00'
page_id: '421385123'
product: rm
source: tdn-rm
title: Alterar BDI Diferenciado
type: documentation
url: https://tdn.totvs.com/display/LRM/Alterar+BDI+Diferenciado
version: 3
---

---

Através desta opção, altera-se o valor do BDI Diferenciado das tarefas automaticamente sem que o valor total do projeto seja alterado, salvo quando o cálculo propagar um erro de arredondamento que, em geral, será da ordem de 0,001% do valor total do projeto.

Ao acionar o botão "Calcular BDIs", os BDIs das tarefas desmarcadas sofrerão as alterações necessárias para incorporar as mudanças dos BDIs que ficaram marcados, sem que o valor total do projeto seja alterado, exceto quando o cálculo gerar arredondamentos.

O botão "Carregar valores originais", desfaz as alterações feitas nas tarefas e carrega novamente os valores originais das tarefas.

Ferramenta permite fixar o BDI de algumas tarefas em valores diferentes da planilha e ratear a diferença entre os demais BDIs Diferenciados (da tarefa). É uma ferramenta normalmente usada no processo de Confecção da Proposta de Venda.

Caso o parâmetro (Menu - Opções - Parâmetros - TOTVS Obras e Projetos - Projetos - Pasta Cálculo - BDI, Utilização (Diferenciado)) do BDI não esteja habilitado, esta tela fica indisponível.  
 Não é permitido marcar todas as tarefas, é necessário deixar pelo menos uma tarefa desmarcada para que seja rateada a diferença dos BDIs. Também é vetada a execução do processo quando o cálculo do BDI gera um BDI Diferenciado zerado ou negativo.

Esta funcionalidade permitir usar tanto a Planilha de Serviços como a Planilha de Atividades. Ao começar o processo o usuário deverá informar qual planilha deseja trabalhar. O Default será a Planilha de Atividades.

**Atenção:**  
 É recomendado calcular o projeto após a execução do processo.

**Observações:**  
 As tarefas que forem marcadas terão o valor do BDI Diferenciado preservado.

Se o BDI Dif. de uma tarefa é alterado, está automaticamente será marcada.

Pelo menos uma tarefa deverá estar marcada com invariável.

Pelo menos uma tarefa deverá estar desmarcada.

Ao arrastar um serviço para a planilha de atividades o BDI diferenciado deverá ser copiado.

Se no sistema o uso da planilha de Serviços estiver parametrizados, na tela Alteração do BDI Diferenciado, habilita um campo com as opções de realizar as alterações nas Planilhas de Atividades e Planilhas de Serviços.
