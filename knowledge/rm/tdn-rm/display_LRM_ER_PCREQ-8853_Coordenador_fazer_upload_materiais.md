---
content_hash: d4b9d20e3f71997abecad26b2c4a3b4e68977774af8d8e45f8b681e8ad276873
fetched_at: '2026-06-29T00:06:18.805480+00:00'
page_id: '219686695'
product: rm
source: tdn-rm
title: ER_PCREQ-8853_Coordenador_fazer_upload_materiais
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_PCREQ-8853_Coordenador_fazer_upload_materiais
version: 5
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Gestão Educacional | **Módulo** | EDU |
| **Segmento Executor** | Educacional | | |
| **Projeto1** | [WBS\_R\_EDU017\_Participativo\_LaSalle\_1](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B11311%5D+%3D+WBS_R_EDU017_Participativo_LaSalle_1 "WBS_R_EDU017_Participativo_LaSalle_1") | **IRM1** | [PCREQ-8852](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10207%5D+%3D+PCREQ-8852 "PCREQ-8852") |
| **Requisito1** | [PCREQ-8853](http://jira.totvs.com.br/secure/IssueNavigator.jspa?reset=true&jqlQuery=cf%5B10500%5D+%3D+PCREQ-8853 "PCREQ-8853") | **Subtarefa1** | [PDR\_EDU\_EDU017-3](http://jira.totvs.com.br/browse/PDR_EDU_EDU017-3) |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.9 | **Réplica** | Não |
| **País** | (X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Esta funcionalidade, visa aumentar a agilidade no processo de upload de materiais e interação da instituição de ensino e alunos.

Funcionalidade disponível para o contexto de Ensino Superior e Ensino Básico.

 

## Definição da Regra de Negócio

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Comissão Coordenadora | Alteração | Matriz Curricular > Matriz Aplicada > Comissão Coordenadora | - |
| Upload de Materiais | Alteração | Portal > Administração > Upload de Materiais | - |
|  |  |  |  |

# **Coordenador fazer upload de materiais**

O coordenador de curso deverá ser cadastrado junto a matriz aplicada pelo cadastro de comissão coordenadora.

Após ser gerado o usuário de acesso ao coordenador e concedido os devidos acessos, estará disponível no Portal do TOTVS Educacional, menu Professor, a opção de “Upload de Materiais”.

A funcionalidade de “Upload de Materiais” será alterada para permitir a associação do material a um curso, série/habilitação, turmas e turmas/disciplinas.

# **Associação de material**

## **Permissão de acesso**

Será criado um item de permissão de acesso ao menu, de nome “Associação de material – Comissão Coordenadora” (Cadastro de Perfil de Acesso > Educacional > Acesso aos menus > Outras permissões > RM Portal > Portal > Professor > Upload de Materiais > Associação de material – Comissão Coordenadora”).

Usuários do Portal com este acesso, seja do contexto do Ensino Básico ou Superior, visualizarão todos os cursos, séries, turmas e turmas/disciplinas relacionadas a matriz aplicada, que ele é coordenador, ao selecionar o botão “Associar turma”.

Não será solicitado um contexto para o coordenador nesse caso, pois o sistema já será capaz de identificar todos os cursos/séries ou habilitações/turmas/disciplinas e disponibilizá-las de forma organizada para o usuário.

## **Coordenador - Professor**

Coordenador que também possuem acesso de professor visualizará todos os períodos letivos (que não estejam encerrados), cursos/séries ou habilitações/turmas/disciplinas vinculados como coordenador e como professor.

Caso o professor não tenha a permissão de acesso supracitada, será visualizada apenas os dados das entidades citadas que o professor estiver vinculado.

## **Seleção das entidades**

Após o usuário do sistema selecionar a opção “Associar turma”, citada acima, será aberta uma nova janela para a seleção de qual entidade poderá ser associada.

Baseado no usuário do Portal, será disponibilizado os períodos letivos, cursos, séries/habilitação, turmas e turmas/disciplinas que aquele usuário esteja cadastrado na comissão coordenadora.

Não será feito nenhuma distinção do usuário devido ao cargo associado ao cadastro de comissão coordenadora. Qualquer restrição deverá ser feita exclusivamente pelo perfil de acesso aos menus.

Os dados das entidades estarão dispostos no formato de árvore de registros (*treeview*), e com opção de seleção para cada nível, exemplo:

* Período Letivo – Código e Nome (SPLETIVO)
  + Curso – Código e Nome do Curso (SCURSO)
    - Série ou Habilitação – Código e Nome (SHABILITACAO)
      * Turma – Código e Nome da Turma (STURMA)
        + Turma/Disciplina – Código da turma disciplina (STURMADISC) e nome da Disciplina (SDISCIPLINA)

Caso o usuário do sistema marque a opção para Curso, ao clicar no botão associar, o sistema irá disponibilizar o material para cada turma/disciplina daquele curso, o mesmo para Série/Habilitação, Turma.

O vínculo do material continuará sendo feito entre os registros da tabela de material “SWEBMATERIALSEC” e os registros das turmas/disciplinas “SWEBMATERIALTURMADISC”, isso se faz necessário, para manter a compatibilidade com a funcionalidade existente de “Upload de Material” pelo professor.

Na visão de upload de materiais, abaixo de cada material será listado as turmas/disciplinas associadas a aquele material, com a opção de exclusão. Estará disponível uma nova opção de exclusão das turmas disciplinas selecionadas vinculadas ao arquivo.

## **Restrições**

Serão visualizados apenas as turmas/disciplinas ativas, de períodos letivos que **não** estejam encerrados, vinculados a mesma matriz aplicada que o usuário do sistema pelo cadastro de comissão coordenadora.

## Protótipo de Tela

**Associação de turma/disciplina ao arquivo**

  

**Exclusão do vínculo de turmas/disciplinas com Arquivos**

 

Será incluído o botão de “Excluir Turmas” junto a cada arquivo. Para cada turma/disciplina selecionada abaixo, será feito a exclusão.

 

 

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
