---
content_hash: 9e849a6acb3737243a48ecd121f3d28e3387e0b0cc07c29c9e38cce6485a014e
fetched_at: '2026-06-29T00:05:59.829826+00:00'
page_id: '192096245'
product: rm
source: tdn-rm
title: ER_Inclusao_Candidatos_Etapa_Turmas
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Inclusao_Candidatos_Etapa_Turmas
version: 20
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** |  | | |
| **Projeto1** | RHU – DESENVOLVIMENTO RHU006 | **IRM1** | PCREQ-1947 |
| **Requisito1** | PCREQ-1948 | **Subtarefa1** | PDR\_RHU\_RHU006-77 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** |  | **Réplica** |  |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## 

## Objetivo

Disponibilizar um assistente para facilitar a inscrição de candidatos de seleção em turmas de treinamento.

## 

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Desenvolvimento | Alteração | Desenvolvimento -> Inscrição de Participantes | - |
| Planejamento e Captação | Inclusão | Planejamento e Captação -> Painel de Etapas -> Anexos ->  Candidatos da Etapa -> Anexos -> Turma do Participante | - |
|  |  |  |  |

**Processo “Inscrição de Participantes”**

Para inserção de candidatos em turmas de treinamento, com a finalidade de facilitar a logística e otimizar as taxas de ocupação de salas para treinamento, o processo de Inscrição de Participantes localizado na aba **Desenvolvimento> Inscrição de Participante**, deverá ser ajustado para possibilitar a escolha de participantes por meio da utilização de filtro por Seleção, Vaga de Seleção, Etapa de Seleção e Candidatos da Etapa. Além disso deverá ser possível filtrar candidatos com registro de funcionário, ou seja, que já foram admitidos.

Para a seleção das turmas podem ser criados filtros personalizados. Esses filtros poderão incluir critérios de pesquisa para vários campos do cadastro de turmas, como pode ser visto no Protótipo 02.

Deverá ser habilitado o filtro por perfil para turmas, e ele deverá ser respeitado neste assistente. Ex: De acordo com o filtro por perfil, um usuário de um certo Site/ Filial, caso parametrizado, deverá apenas enxergar no filtro de turmas apenas aquelas que pertençam ao mesmo Site/Filial que ele.

Na árvore de turma, as informações que deverão ser apresentadas referentes a cada turma são: código da turma, nome da turma, quantidade de vagas disponíveis. Posicionando o mouse sobre o nome da turma, será exibido um tooltip com as informações data e horário de início e fim.

Uma vez carregada a lista com os candidatos e a outra com as turmas, o usuário poderá incluir candidatos nas turmas que deseja através do recurso de “arrastar e soltar”, ou seja, primeiramente selecionam-se os candidatos que serão incluídos, arrasta-os até a árvore da direita (das turmas) e em seguida liberam-se os mesmos em cima da turma desejada. Caso necessário, o vínculo entre candidato e turma poderá ser desfeito selecionando o candidato na árvore da turma e em seguida pressionando a tecla “DELETE”. Somente candidatos incluídos nas turmas durante a atual execução do processo poderão ser removidos.

O checkbox “Remover da lista ao inscrever em uma turma” será disponibilizado e permitirá que o usuário escolha se o processo deixará que um candidato seja incluído em mais de uma turma durante o processo ou se, ao mover para uma turma, o candidato deverá ser removido da lista.   
O objetivo desta opção é facilitar a operação e evitar a inclusão em mais de uma turma caso esse comportamento não seja desejado. Com essa opção marcada, o candidato voltará a ser exibido na lista se ele for removido da turma para a qual foi movido.

Para evitar conflito de agenda dos participantes da turma, o usuário poderá marcar a opção “Somente inscrever as pessoas que têm disponibilidade para participar do treinamento”. Esta opção, presente na primeira etapa do assistente, implica numa validação de conflito de agenda entre as turmas que o participante já está incluído e a turma que o usuário queira incluir o participante. Serão consideradas data e hora de início e término das turmas para esta verificação. A validação ocorre para cada participante no momento que o usuário arrastá-lo para a turma desejada.

Ao vincular um candidato à turma, o sistema deverá validar se a turma possui vaga para alocar o candidato. Caso não existam vagas disponíveis, uma mensagem de alerta será exibida informando que a operação não será completada por insuficiência de vagas disponíveis. Sempre que ocorrer uma modificação, como a inclusão ou remoção do candidato de qualquer turma, as informações de vagas disponíveis nas turmas deverão ser atualizadas automaticamente.

Toda a operação será efetivada no banco de dados somente após a execução completa do assistente. Ao executar a etapa final do assistente, o processo irá efetuar todas as validações e realizar a inscrição de candidatos nas turmas.

**Assistente de Inscrição de Participantes em Etapas de Seleção**

De acordo com o grande volume de seleções que ocorrem simultaneamente no processo do Grupo Contax, com o objetivo de facilitar a alocação de candidatos na devida turma de treinamento, originada a partir da demanda do próprio processo seletivo, deverá ser criado um assistente que execute o mesmo processo de inserção de candidatos em turmas também na aba **Planejamento e Captação> Painel de Seleção> Perfil de Vaga> Etapas de Seleção> Anexo> Candidatos em Etapa > Processos> Inscrição de Participante**.

O usuário deverá filtrar e selecionar todos os candidatos da etapa que deseja inserir em turmas de treinamento e executar o assistente. Apenas os candidatos selecionados seriam carregados na árvore da esquerda da tela. Mesmo já tendo carregado a lista de participantes no assistente, o usuário, caso deseje, poderá fazer novos filtros para a seleção de pessoas.

O assistente proposto será o mesmo descrito no primeiro item deste documento. Ele ganhará um tratamento especial para que possa ser executado a partir da lista de candidatos de uma etapa e seleção e já traga carregada a lista de candidatos selecionados na visão.

**Inscrever candidatos automaticamente**

Na mesma tela será criado o botão “Inscrever candidatos automaticamente”, que terá a funcionalidade de distribuir os candidatos automaticamente, nas turmas selecionadas através dos filtros, obedecendo o número de vagas disponíveis.

Os candidatos listados serão incluídos sequencialmente nas turmas exibidas na listagem de turmas, sendo que serão incluídos na ordem que aparecem na lista, preenchendo as vagas disponíveis nas turmas. Quando as vagas de uma turma se esgotarem o sistema passará a preencher as vagas da próxima turma da lista, até que sejam incluídos todos os candidatos ou até que se esgotem as vagas das turmas listadas, o que ocorrer primeiro.

Caso ocorra o preenchimento de todas as vagas disponíveis, os candidatos remanescentes continuarão sendo exibidos na árvore de candidatos.

**Anexo: Turmas do participante**

Como forma de viabilizar a visualização da participação de candidatos em turmas, deve ser criado o anexo “Turmas do participante” para a visão de Candidatos. Este anexo tem por objetivo demonstrar quais turmas o candidato está inscrito. Este recurso deverá ser criado e acessado através do caminho menu **Painel de Etapas > Anexos > Candidatos da Etapa > Anexos > Turmas do participante.**

## Protótipos de Tela

**Protótipo 01– Processo de Inscrição de Candidatos em Turmas**

**Protótipo 02 - Filtro personalizado para Turmas**

**Protótipo 03 - Inscrição a partir de candidatos de Etapa de Seleção**

## Regras de Integridade

* Na árvore de exibição de turmas, somente serão apresentadas turmas que possuírem status “aberta” ou “proposta”;
* O processo nunca será executado se houver violação no número de vagas.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
