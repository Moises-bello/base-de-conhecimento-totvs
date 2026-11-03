---
content_hash: 60b1e3434bf8134c0e7fb046824103bc8f098017848ecff748c563fbc96439e2
fetched_at: '2026-06-29T00:05:59.805497+00:00'
page_id: '192094048'
product: rm
source: tdn-rm
title: ER_Atividades_Formula_Visual_e_Campos_Complementares
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_Atividades_Formula_Visual_e_Campos_Complementares
version: 8
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

### Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão de Pessoas | **Módulo** | RHU |
| **Segmento Executor** | Construção e Projetos | | |
| **Projeto1** | RHU – DESENVOLVIMENTO RHU006 | **IRM1** | PCREQ-1933 |
| **Requisito1** | PCREQ-1934 | **Subtarefa1** | PDR\_RHU\_RHU006-17 |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** |  |
| **País** | ( x ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** |  | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 

A Fórmula Visual é um mecanismo amplo e com finalidade geral para o desenvolvimento visual de regras de negócio com o objetivo de estender ou customizar a solução TOTVS RM. As fórmulas visuais são montadas visualmente com o auxílio de um designer (editor visual de programas), como uma sequência de atividades.

O objetivo será desenvolver novas atividades que executam regras de negócio específicas para serem utilizadas nas fórmulas visuais. As novas atividades que serão criadas estão descritas abaixo:

• Alterar Status do Candidato em uma Etapa de seleção;  
• Alterar Status de uma Etapa de Seleção;  
• Alterar Status do Perfil da Vaga;  
• Cálculo de Rota;  
• Registrar Contato;  
• Realizar Inscrição em Turma.

Obs.: O desenvolvimento das fórmulas visuais será de responsabilidade do cliente. Neste documento iremos tratar somente a criação de novas atividades para serem utilizadas em fórmulas visuais. Também iremos mostrar exemplos para utilização das novas atividades e execução da fórmula visual como processo.

Também serão disponibilizados Campos Complementares para novas entidades do sistema.

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Fórmulas Visuais | Criação | RH > Gestão de Pessoas > Gestão > Fórmula Visual | - |
|  |  |  |  |

**Atividade Alterar Status do Candidato em uma Etapa de Seleção**

Criar nova atividade para ser utilizada em fórmulas visuais para alterar o status de um candidato em uma etapa de seleção. A atividade irá atualizar o campo Status do candidato na etapa de seleção independente do status em que o candidato se encontra atualmente. Os status disponíveis atualmente são: Pendente de Análise, Aprovado e Reprovado. Este recurso deverá ser criado e acessado através do cadastro de Fórmulas Visuais, na edição de uma fórmula visual, na aba de Atividades. Caminho do menu: RH > Gestão de Pessoas > Gestão > Fórmula Visual > Aba Atividades.

Para utilizar a nova atividade Alterar Status do Candidato em uma Etapa de Seleção será necessário criar uma fórmula visual na qual será vinculada a nova atividade. Obs.: Tarefa a ser executada diretamente no sistema TOTVS RM.

A nova atividade terá parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade. Os parâmetros são:

- CODCOLIGADA – Código da Coligada;  
 - CODSELECAO – Código da Seleção;  
 - CODVAGA – Código da Vaga;  
 - CODETAPA – Código da Etapa;  
 - CODPESSOA – Código da Pessoa;  
 - STATUS – Status a ser alterado - (Pendente de análise, Aprovado ou Reprovado).

A atividade irá alterar o status do candidato dentro de uma etapa de seleção de acordo com os parâmetros informados na fórmula visual. A atividade deve seguir as mesmas regras de negócio dos processos Voltar a Pendente de Análise, Aprovar Candidatos ou Reprovar Candidatos já existentes hoje na tela de Candidatos da Etapa. Caminho do Menu: RH > Gestão de Pessoas > Planejamento e Captação > Painel de Seleção > Etapas da Seleção > Anexos > Candidatos da Etapa

**Atividade Alterar Status de uma Etapa de Seleção**

Criar nova atividade para ser utilizada em fórmulas visuais para alterar o status de uma etapa de seleção. A atividade irá atualizar o campo Status da etapa de seleção de acordo com as regras de negócio já existentes no sistema. Os status disponíveis atualmente são: Não Iniciado, Em Andamento, Concluído ou Suspenso. Atenção: uma etapa com o Status Não Iniciado não pode ter seu status alterado por processo; seu status somente será alterado quando a etapa anterior for concluída. Este recurso deverá ser criado e acessado através do cadastro de Fórmulas Visuais, na edição de uma fórmula visual, na aba de Atividades. Caminho do menu: RH > Gestão de Pessoas > Gestão > Fórmula Visual > Aba Atividades.

Para utilizar a nova atividade Alterar Status de uma Etapa de Seleção será necessário criar uma formula visual na qual será vinculada a nova atividade. Obs.: Tarefa a ser executada diretamente no sistema TOTVS RM.

A nova atividade terá parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade. Os parâmetros são:

- CODCOLIGADA – Código da Coligada;  
 - CODSELECAO – Código da Seleção;  
 - CODVAGA – Código da Vaga;  
 - CODETAPA – Código da Etapa;  
 - STATUS – Status a ser alterado - (Não Iniciado, Em Andamento, Concluído ou Suspenso).

A atividade irá alterar o status de uma etapa de seleção de acordo com os parâmetros informados na fórmula visual. A atividade deve seguir as mesmas regras de negócio dos processos Mudança de Status do Perfil da Etapa > Suspender Etapa, Concluir Etapa e Reiniciar Etapa já existentes hoje na tela de Etapas da Seleção. Caminho do Menu: RH > Gestão de Pessoas > Planejamento e Captação > Painel de Seleção > Etapas da Seleção

**Atividade Alterar Status do Perfil de Vaga**

Criar nova atividade para ser utilizada em fórmulas visuais para alterar o status de um perfil de vaga de seleção. A atividade irá atualizar o campo Status da vaga de seleção de acordo com as regras de negócio já existentes no sistema. Os status disponíveis atualmente são: Em Andamento, Concluído ou Suspenso. Atenção, somente vagas com o Status Concluído ou Suspenso podem ter seus status alterados para Em Andamento. Este recurso deverá ser criado e acessado através do cadastro de Fórmulas Visuais, na edição de uma fórmula visual, na aba de Atividades. Caminho do menu: RH > Gestão de Pessoas > Gestão > Fórmula Visual > Aba Atividades.

Para utilizar a nova atividade Alterar Status do Perfil de Vaga será necessário criar uma fórmula visual na qual será vinculada a nova atividade. Obs.: Tarefa a ser executada diretamente no sistema TOTVS RM.

A nova atividade terá parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade. Os parâmetros são:

- CODCOLIGADA – Código da Coligada;  
 - CODSELECAO – Código da Seleção;  
 - CODVAGA – Código da Vaga;  
 - STATUS – Status a ser alterado - (Em Andamento, Concluído ou Suspenso).

A atividade irá alterar o status do perfil de vaga da seleção de acordo com os parâmetros informados na fórmula visual. A atividade deve seguir as mesmas regras de negócio dos processos Mudança de Status do Perfil de Vaga > Reiniciar Perfil de Vaga, Suspender Perfil de Vaga e Concluir Perfil de Vaga já existentes hoje na tela de Vagas da Seleção. Caminho do Menu: RH > Gestão de Pessoas > Planejamento e Captação > Painel de Seleção > Vagas da Seleção

**Atividade Solicitar Rota**

Criar nova atividade para ser utilizada em fórmulas visuais para Solicitação de Rota. Este recurso deverá ser criado e acessado através do cadastro de Fórmulas Visuais, na edição de uma fórmula visual, na aba de Atividades. Caminho do menu: RH > Gestão de Pessoas > Gestão > Fórmula Visual > Aba Atividades. A atividade de Solicitar Rota seguirá as mesmas regras descritas na especificação de Cálculo de Rota.

Para utilizar a atividade Solicitar Rota será necessário criar uma fórmula visual na qual será vinculada a nova atividade. Obs.: Tarefa a ser executada diretamente no sistema.

A nova atividade de Solicitar Rota terá parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade.

- CODCOLIGADA – Código da Coligada  
 - CODPESSOA - Código da Pessoa   
- CODSECAO - Código da Seção

**Atividade Buscar Roteirização por Pessoa**

Criar nova atividade para ser utilizada em fórmulas visuais para Buscar Roteirização por Pessoa. Este recurso deverá ser criado e acessado através do cadastro de Fórmulas Visuais, na edição de uma fórmula visual, na aba de Atividades. Caminho do menu: RH > Gestão de Pessoas > Gestão > Fórmula Visual > Aba Atividades. A atividade de Buscar Roteirização por Pessoa seguirá as mesmas regras descritas na especificação de Cálculo de Rota.

Para utilizar a atividade Buscar Roteirização por Pessoa será necessário criar uma fórmula visual na qual será vinculada a nova atividade. Obs.: Tarefa a ser executada diretamente no sistema.

A nova atividade Buscar Roteirização por Pessoa terá parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade.

- CODCOLIGADA - Código da Coligada

- CODPESSOA - Código da Pessoa

**Atividade Buscar Roteirização por Rota**

Criar nova atividade para ser utilizada em fórmulas visuais para Buscar Roteirização por Rota. Este recurso deverá ser criado e acessado através do cadastro de Fórmulas Visuais, na edição de uma fórmula visual, na aba de Atividades. Caminho do menu: RH > Gestão de Pessoas > Gestão > Fórmula Visual > Aba Atividades. A atividade de Buscar Roteirização por Rota seguirá as mesmas regras descritas na especificação de Cálculo de Rota.

Para utilizar a atividade Buscar Roteirização por Rota será necessário criar uma fórmula visual na qual será vinculada a nova atividade. Obs.: Tarefa a ser executada diretamente no sistema.

A nova atividade Buscar Roteirização por Rota terá parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade.

- CODCOLIGADA - Código da Coligada

- IDROTA - ID Gerado na solicitação da rota

**Atividade Registrar Contato**

Criar nova atividade para ser utilizada em fórmulas visuais para registrar um contato. A atividade irá registrar/incluir um contato realizado e vai atualizar a visão de registro de contato que será um anexo da visão de candidatos da etapa dentro do painel de seleção. Essa atividade irá atualizar os campos Tipo de Contato, Data/Hora do Contato e Observações do cadastro de registro de contato. Os tipos de contatos são definidos através da tabela dinâmica Tipos de Contato. Este recurso deverá ser criado e acessado através do cadastro de Fórmulas Visuais, na edição de uma fórmula visual, na aba de Atividades. Caminho do menu: RH > Gestão de Pessoas > Gestão > Fórmula Visual > Aba Atividades.

Para utilizar a atividade Alterar Registrar Contato será necessário criar uma fórmula visual na qual será vinculada a nova atividade. Obs.: Tarefa a ser executada diretamente no sistema TOTVS RM.

A nova atividade terá parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade. Os parâmetros são:

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

A atividade irá registrar/incluir um registro de contato para um candidato da etapa de acordo com os parâmetros informados na fórmula visual. A atividade deve seguir as mesmas regras de negócio do processo Registro de Contato que será implementado e estará disponível na tela de candidatos da etapa. Caminho do Menu: RH > Gestão de Pessoas > Planejamento e Captação > Painel de Seleção > Vagas da Seleção > Etapas da Seleção > Anexos > Candidatos da Etapa.

**Atividade Realizar Inscrição em Turma**

Criar nova atividade para ser utilizada em fórmulas visuais para realizar a inscrição de uma pessoa em uma turma para treinamento. Este recurso deverá ser criado e acessado através do cadastro de Fórmulas Visuais, na edição de uma fórmula visual, na aba de Atividades. Caminho do menu: RH > Gestão de Pessoas > Gestão > Fórmula Visual > Aba Atividades.

Para utilizar a nova atividade Realizar Inscrição em Turma será necessário criar uma formula visual na qual será vinculada a nova atividade. Obs.: Tarefa a ser executada diretamente no sistema TOTVS RM.

A nova atividade terá parâmetros imprescindíveis para sua utilização. Esses parâmetros deverão ser preenchidos dentro da fórmula visual para a correta execução da atividade. Os parâmetros são:

- CODCOLIGADA – Código da Coligada;  
 - CODTURMA – Código da Turma;  
 - CODPESSOA – Código da Pessoa;

A atividade irá realizar a inscrição de uma pessoa em uma turma de acordo com os parâmetros informados na fórmula visual. A atividade deve seguir as regras de negócio existentes hoje no sistema para realizar a inscrição do participante, portanto, não será possível inserir um participante em uma turma encerrada ou que as vagas estejam esgotadas.

**Campos Complementares**

Serão disponibilizados campos complementares para os cadastros de Perfil de Vaga e Seção. Esse recurso deverá funcionar conforme o padrão já estabelecido no ambiente RM.

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
