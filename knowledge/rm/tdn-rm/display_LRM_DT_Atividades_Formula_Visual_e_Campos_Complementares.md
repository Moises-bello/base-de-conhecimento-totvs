---
content_hash: a032573ac6f27d116480e569606046fb03d50c89b7f9855736bb45863dd0957b
fetched_at: '2026-06-29T00:06:06.922162+00:00'
page_id: '201733380'
product: rm
source: tdn-rm
title: DT_Atividades_Formula_Visual_e_Campos_Complementares
type: documentation
url: https://tdn.totvs.com/display/LRM/DT_Atividades_Formula_Visual_e_Campos_Complementares
version: 9
---

# ATIVIDADES PARA EXECUÇÃO EM FÓRMULA E CAMPOS COMPLEMENTARES

**Características do Requisito**

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Construção e Projetos* |
| **Módulo:** | **TOTVS Gestão de Pessoas** |
| **Rotina:** | |  |  | | --- | --- | | **Rotina** | **Nome Técnico** | | *Fórmulas Visuais* | *Fórmula Visual* | |
| **Versões/Release:** | *12.1.7* |

## Descrição

A Fórmula Visual é um mecanismo amplo e com finalidade geral para o desenvolvimento visual de regras de negócio com o objetivo de estender ou customizar a solução TOTVS RM.

As atividades que executam regras de negócio específicas utilizadas nas fórmulas visuais são: Alterar Status do Candidato em uma Etapa de seleção; Alterar Status de uma Etapa de Seleção; Alterar Status do Perfil da Vaga; Cálculo de Rota; Registrar Contato; Realizar Inscrição em Turma.

Obs.: O desenvolvimento das fórmulas visuais será de responsabilidade do cliente.

## Procedimento para Utilização

No processo para Alterar Status do Candidato em uma Etapa de seleção, a atividade atualiza o campo Status do candidato na etapa de seleção independente do status em que o candidato se encontra atualmente. Os status disponíveis atualmente são: Pendente de Análise, Aprovado e Reprovado. Este recurso é criado e acessado através do cadastro de Fórmulas Visuais. Caminho do menu: **RH / Gestão de Pessoas / Gestão / Fórmula Visual / Aba Atividades.**

Para utilizar a atividade Alterar Status do Candidato em uma Etapa de Seleção é necessário criar uma fórmula visual na qual será vinculada a atividade.

A atividade terá parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade. Os parâmetros são:

- CODCOLIGADA – Código da Coligada;  
- CODSELECAO – Código da Seleção;  
- CODVAGA – Código da Vaga;  
- CODETAPA – Código da Etapa;  
- CODPESSOA – Código da Pessoa;  
- STATUS – Status a ser alterado - (Pendente de análise, Aprovado ou Reprovado).

Para o processo Alterar Status de uma Etapa de Seleção, a atividade irá alterar o status do candidato dentro de uma etapa de seleção de acordo com os parâmetros informados na fórmula visual. A atividade deve seguir as mesmas regras de negócio dos processos Voltar a Pendente de Análise, Aprovar Candidatos ou Reprovar Candidatos já existentes hoje na tela de Candidatos da Etapa. Caminho do Menu: **RH / Gestão de Pessoas / Planejamento e Captação / Painel de Seleção / Etapas da Seleção / Anexos / Candidatos da Etapa.**

A atividade irá atualizar o campo Status da etapa de seleção de acordo com as regras de negócio já existentes no sistema. Os status disponíveis atualmente são: Não Iniciado, Em Andamento, Concluído ou Suspenso. Atenção: uma etapa com o status Não Iniciado não pode ter seu status alterado por processo; seu status somente será alterado quando a etapa anterior for concluída. Caminho do menu: **RH / Gestão de Pessoas / Gestão / Fórmula Visual / Aba Atividades.**

Para utilizar a atividade Alterar Status de uma Etapa de Seleção será necessário criar uma formula visual na qual será vinculada a nova atividade. Obs.: Tarefa a ser executada diretamente no sistema TOTVS RM.

A atividade tem parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade. Os parâmetros são:

- CODCOLIGADA – Código da Coligada;  
- CODSELECAO – Código da Seleção;  
- CODVAGA – Código da Vaga;  
- CODETAPA – Código da Etapa;  
- STATUS – Status a ser alterado - (Não Iniciado, Em Andamento, Concluído ou Suspenso)  
A atividade irá alterar o status de uma etapa de seleção de acordo com os parâmetros informados na fórmula visual. A atividade deve seguir as mesmas regras de negócio dos processos Mudança de Status do **Perfil da Etapa / Suspender Etapa,** Concluir Etapa e Reiniciar Etapa já existentes hoje na tela de Etapas da Seleção. Caminho do Menu: **RH / Gestão de Pessoas / Planejamento e Captação / Painel de Seleção / Etapas da Seleção**

O processo para alterar status do Perfil de Vagas, a atividade irá atualizar o campo Status da vaga de seleção de acordo com as regras de negócio já existentes no sistema. Os status disponíveis atualmente são: Em Andamento, Concluído ou Suspenso. Atenção: somente vagas com o Status Concluído ou Suspenso podem ter seus status alterados para Em Andamento. Este recurso deverá ser criado e acessado através do cadastro de Fórmulas Visuais, na edição de uma fórmula visual, na aba de Atividades. Caminho do menu: **RH / Gestão de Pessoas / Gestão / Fórmula Visual / Aba Atividades.**

Para utilizar a nova atividade Alterar Status do Perfil de Vaga será necessário criar uma fórmula visual na qual será vinculada a nova atividade. Obs.: Tarefa a ser executada diretamente no sistema TOTVS RM.

A nova atividade tem parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade. Os parâmetros são:

- CODCOLIGADA – Código da Coligada;  
- CODSELECAO – Código da Seleção;  
- CODVAGA – Código da Vaga;  
- STATUS – Status a ser alterado - (Em Andamento, Concluído ou Suspenso).

A atividade irá alterar o status do perfil de vaga da seleção de acordo com os parâmetros informados na fórmula visual. A atividade deve seguir as mesmas regras de negócio dos processos Mudança de Status do **Perfil de Vaga / Reiniciar Perfil de Vaga, Suspender Perfil de Vaga e Concluir Perfil de Vaga** já existentes hoje na tela de Vagas da Seleção. Caminho do Menu: **RH / Gestão de Pessoas / Planejamento e Captação / Painel de Seleção / Vagas da Seleção**

O recurso Solicitar Rota também é acessado através do cadastro de Fórmulas Visuais no caminho do menu: **RH / Gestão de Pessoas / Gestão / Fórmula Visual / Aba Atividades**. A atividade de Solicitar Rota seguirá as mesmas regras descritas na especificação de Cálculo de Rota.

A atividade de Solicitar Rota tem parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade.

- CODCOLIGADA – Código da Coligada  
- CODPESSOA - Código da Pessoa   
- CODSECAO - Código da Seção

O recurso Buscar Roteirização por Pessoa está no caminho **RH / Gestão de Pessoas / Gestão / Fórmula Visual / Aba Atividades**. A atividade de Buscar Roteirização por Pessoa seguirá as mesmas regras descritas na especificação de Cálculo de Rota.

A  atividade Buscar Roteirização por Pessoa tem parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade.

- CODCOLIGADA - Código da Coligada  
- CODPESSOA - Código da Pessoa

 O recurso para  Buscar Roteirização por Rota está no caminho do menu **RH / Gestão de Pessoas / Gestão / Fórmula Visual / Aba Atividades**. A atividade de Buscar Roteirização por Rota seguirá as mesmas regras descritas na especificação de Cálculo de Rota.

A atividade Buscar Roteirização por Rota tem parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade.

- CODCOLIGADA - Código da Coligada

- IDROTA - ID Gerado na solicitação da rota

Para Registrar Contato, a  atividade irá registrar/incluir um contato realizado e vai atualizar a visão de registro de contato que é um anexo da visão de candidatos da etapa dentro do painel de seleção. Essa atividade atualiza os campos Tipo de Contato, Data/Hora do Contato e Observações do cadastro de registro de contato. Os tipos de contatos são definidos através da tabela dinâmica Tipos de Contato. Caminho do menu: **RH / Gestão de Pessoas / Gestão / Fórmula Visual / Aba Atividades.**

A  atividade tem parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade. Os parâmetros são:

- CODCOLIGADA – Código da Coligada;  
- CODSELECAO – Código da Seleção;  
- CODVAGA – Código da Vaga;  
- CODETAPA – Código da Etapa;  
- CODPESSOA – Código da Pessoa;  
- CODTIPOCONTATO – Código do Tipo de Contato;  
- Data/Hora – Data e Hora do Contato;  
- Responsável pelo contato – usuário que realizou o contato de acordo com log in no sistema  
- Contato com sucesso – check box do campo “Sim”  
- OBSERVACOES – Observações a serem registradas.

A atividade irá registrar/incluir um registro de contato para um candidato da etapa de acordo com os parâmetros informados na fórmula visual. A atividade deve seguir as mesmas regras de negócio do processo Registro de Contato. Caminho do Menu: **RH / Gestão de Pessoas / Planejamento e Captação / Painel de Seleção / Vagas da Seleção / Etapas da Seleção / Anexos / Candidatos da Etapa**.

O Recurso Realizar Inscrição em Turma está no caminho **RH / Gestão de Pessoas / Gestão / Fórmula Visual / Aba Atividades.**

A atividade tem parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade. Os parâmetros são:

- CODCOLIGADA – Código da Coligada;  
- CODTURMA – Código da Turma;  
- CODPESSOA – Código da Pessoa;

A atividade irá realizar a inscrição de uma pessoa em uma turma de acordo com os parâmetros informados na fórmula visual. A atividade deve seguir as regras de negócio existentes hoje no sistema para realizar a inscrição do participante, portanto, não será possível inserir um participante em uma turma encerrada ou que as vagas estejam esgotadas.
