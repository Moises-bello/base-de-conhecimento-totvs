---
content_hash: 3a02bc70ec57460fcf71b9cf32860c58eb9423c3266a591d5cabb61475b92286
fetched_at: '2026-06-29T00:06:06.139227+00:00'
page_id: '201728611'
product: rm
source: tdn-rm
title: DT_Inclusao_Candidatos_Etapa_Turmas
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Inclusao_Candidatos_Etapa_Turmas
version: 17
---

# INCLUSÃO DE CANDIDATOS DA ETAPA EM TURMAS

## Características do Requisito

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | *TOTVS Gestão de Pessoas* |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Desenvolvimento* | *Inclusão de candidatos de etapas em turmas* | | *Planejamento e Captação* | *Inclusão de candidatos de etapas em turmas* | |
| **Versões/Release:** | *12.1.7* |

## Descrição

Esse processo serve para disponibilizar um assistente para facilitar a inscrição de candidatos de seleção em turmas de treinamento. A inserção de candidatos em turmas de treinamento tem como finalidade facilitar a logística e otimizar as taxas de ocupação de salas para treinamento. É possível filtrar candidatos com registro de funcionário, ou seja, que já foram admitidos.

## Procedimento para Utilização

O processo de Inscrição de Participantes está localizado no menu **Desenvolvimento / Inscrição de Participante** possibilita a escolha de participantes por meio da utilização de filtro por Seleção, Vaga de Seleção, Etapa de Seleção e Candidatos da Etapa. Além disso é possível filtrar candidatos com registro de funcionário, ou seja, que já foram admitidos.

Para a seleção das turmas, podem ser criados filtros personalizados. Esses filtros podem incluir critérios de pesquisa para vários campos do cadastro de turmas

O filtro por perfil para turmas, deverá ser respeitado neste assistente. Ex: De acordo com o filtro por perfil, um usuário de um certo Site/ Filial, caso parametrizado, deve apenas enxergar no filtro de turmas apenas aquelas que pertençam ao mesmo Site/Filial que ele.

Na árvore de turma, as informações a serem apresentadas referentes a cada turma são: código da turma, nome da turma, quantidade de vagas disponíveis.   
Posicionando o mouse sobre o nome da turma, será exibido um *tooltip* com as informações data e horário de início e fim.

Uma vez carregada a lista com os candidatos e a outra com as turmas, o usuário poderá incluir candidatos nas turmas que deseja através do recurso de “arrastar e soltar”, ou seja, primeiramente selecionam-se os candidatos que serão incluídos, arrasta-os até a árvore da direita (das turmas) e em seguida liberam-se os mesmos em cima da turma desejada. Caso necessário, o vínculo entre candidato e turma poderá ser desfeito selecionando o candidato na árvore da turma e em seguida pressionando a tecla “DELETE”. Somente candidatos incluídos nas turmas durante a atual execução do processo poderão ser removidos.

A opção “Remover da lista ao inscrever em uma turma” permite que o usuário escolha se o processo deixará que um candidato seja incluído em mais de uma turma durante o processo, ou se ao mover para uma turma o candidato deverá ser removido da lista.

Para evitar conflito de agenda dos participantes da turma, o usuário irá marcar a opção “Somente inscrever as pessoas que têm disponibilidade para participar do treinamento”. Esta opção, presente na primeira etapa do assistente, implica numa validação de conflito de agenda entre as turmas que o participante já está incluído e a turma que o usuário queira incluir o participante. É consideradas data e hora de início e término das turmas para esta verificação. A validação ocorre para cada participante no momento que o usuário arrastá-lo para a turma desejada.

Ao vincular um candidato à turma, o sistema irá validar se a turma possui vaga para alocar o candidato. Caso não existam vagas disponíveis, uma mensagem de alerta será exibida informando que a operação não será completada por insuficiência de vagas disponíveis. Sempre que ocorrer uma modificação, como a inclusão ou remoção do candidato de qualquer turma, as informações de vagas disponíveis nas turmas serão ser atualizadas automaticamente.

Toda a operação será efetivada no banco de dados somente após a execução completa do assistente. Ao executar a etapa final, o processo irá efetuar todas as validações e realizar a inscrição de candidatos nas turmas.

 Um assistente que executa o mesmo processo de inserção de candidatos em turmas está localizado em **Planejamento e Captação / Painel de Seleção / Perfil de Vaga / Etapas de Seleção / Candidatos em Etapa / Processos / Inscrição de Participante em Treinamento.**  O usuário irá filtrar e selecionar todos os candidatos da etapa que deseja inserir em turmas de treinamento e executar o assistente. Apenas os candidatos selecionados serão carregados na árvore de participantes. Mesmo já tendo carregado a lista de participantes no assistente, o usuário, caso deseje, pode fazer novos filtros para a seleção de pessoas.

Na mesma tela tem o botão **Inscrever candidatos automaticamente**com a funcionalidade de distribuir os candidatos automaticamente nas turmas selecionadas através dos filtros obedecendo o número de vagas disponíveis.

Os candidatos listados serão incluídos sequencialmente nas turmas exibidas na listagem de turmas, sendo que serão incluídos na ordem que aparecem na lista, preenchendo as vagas disponíveis nas turmas. Quando as vagas de uma turma se esgotarem, o sistema passará a preencher as vagas da próxima turma da lista, até que sejam incluídos todos os candidatos ou até que se esgotem as vagas das turmas listadas, o que ocorrer primeiro.

Caso ocorra o preenchimento de todas as vagas disponíveis, os candidatos remanescentes continuarão sendo exibidos na árvore de candidatos.

O anexo **Turmar do participante** tem por objetivo demonstrar quais turmas o candidato está inscrito. Este recurso é acessado através do caminho menu **Painel de Etapas / Anexos / Candidatos da Etapa / Anexos / Turmas do participante.**

## Vídeo



|  |  |
| --- | --- |
| **Título do Vídeo:** | Inscrição de Participantes |
| **Introdução:** | Este vídeo mostra como utilizar o assistente para inserção de participantes em uma turma. |
| **Passo a Passo:** | Gestão de Pessoas | Desenvolvimento | Inscrição de Participantes |
