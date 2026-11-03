---
content_hash: 12a1edb03c9bf55bff2bc503a40259892cc169c0ddf25bbcdb50bac487b21235
fetched_at: '2026-06-29T00:05:54.872544+00:00'
page_id: '110431529'
product: rm
source: tdn-rm
title: COMO FAZER - Alteração Horário_Novo cálculo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=110431529
version: 6
---

|  |
| --- |
| **Produto**: TOTVS Automação de Ponto **Versão**: 11.5X ou Superior |
| **Processo**: Alteração Global de Horários (.Net) |

**Introdução**

A alteração de horários permite que se altere o horário executado pelo funcionário, ou apenas o índice do dia de execução da jornada.  
Essa alteração pode ser feita através da guia Cadastros I Alterações Globais I Escala de Horário e Descanso.

O sistema abrirá a tela abaixo para realizar a seleção de funcionários e o período onde serão feitas as alterações. Preencha os campos e clique em avançar:

Na tela seguinte deverá ser feito a parametrização para alteração de horário.  
Existe um parâmetro que é primordial para o restante da parametrização:  
**Manter Horário para Funcionários**: se este parâmetro estiver marcado o horário informado será mantido para o funcionário, sem retorno do antigo horário; se estiver desmarcado você pode definir por quantos dias o funcionário poderá cumpri-lo, assim o campo **"Manter Horário por .... dias"** ficará habilitado para preenchimento.

Ao manter este parâmetro desmarcado é necessário que o funcionário tenha um histórico de horário cadastrado para um dia menor que o começo da seleção de mudança.

Para os demais campos:

1. **Código do horário**: informe o novo horário que o funcionário irá cumprir, caso precisa modificar apenas o índice, mantenha o código do horário atual e altere apenas o campo **"Índice Data Mudança"**;
2. **Índice Data Mudança**: neste campo informe o índice referente ao dia da escala de horário, automaticamente o campo **"Índice Data Base"** será preenchido.

Os campos: **"Comportamento Horário Anterior"** e **"Comportamento Horário Atual"** são preenchidos automaticamente e não necessitam de alteração, já o campo **"Motivo da Mudança do Horário"** não é obrigatório e fica a critério o seu preenchimento.

Abaixo dos campos referidos, estará uma grade onde serão apresentados os funcionários selecionados e o calendário, mostrando os dias para alteração. Para definir o dia da alteração selecione o dia (coluna) na mesma linha do funcionário.  
 OBS: Para selecionar mais de um dia ou mais de um funcionário, selecione a tecla **CTRL** do teclado e clique no dia ou no funcionário.

 Para que os dados sejam aplicados clique no botão "Aplicar Seleção"  
 OBSERVAÇÃO:

1. Caso queira verificar se a alteração do horário ou do índice está correta, clique no botão "Visualizar Horário Planejado", caso não esteja correto, altere o índice até ter o resultado esperado;
2. Se optar por não aplicar a seleção ou alterar o dia/funcionário, clique no botão "Remover Horários das células".

Depois de todos os campos preenchidos e as alterações aplicadas, clique em avançar e depois em executar que o processo será realizado.
