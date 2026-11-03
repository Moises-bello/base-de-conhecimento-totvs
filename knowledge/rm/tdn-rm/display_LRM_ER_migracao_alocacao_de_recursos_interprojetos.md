---
content_hash: dc42838588977340e2a2d5c3572b75bb22d601acf841c6d007c68d8549ace020
fetched_at: '2026-06-29T00:06:00.315880+00:00'
page_id: '196052088'
product: rm
source: tdn-rm
title: ER_migracao_alocacao_de_recursos_interprojetos
type: documentation
url: https://tdn.totvs.com/display/LRM/ER_migracao_alocacao_de_recursos_interprojetos
version: 19
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Alocação de Recursos |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | R\_C&P\_TOP007 | **IRM1** | PCREQ-6028 |
| **Requisito1** | PCREQ-6029 | **Subtarefa1** |  |
| **Chamado2** |  | | |
| **Release de Entrega Planejada** | 12.1.7 | **Réplica** | Não |
| **País** | (X) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

Este documento visa detalhar a implementação/migração de uma das funcionalidades que envolvem “Alocação de Recursos” no produto TOTVS Obras e Projetos. Trata-se da tela de Inter Projetos que permite ao usuário visualizar as alocações realizadas para vários projetos em uma mesma tela.

## Definição da Regra de Negócio

A visão de Inter-Projetos do módulo de Alocação de Recurso possibilita ao usuário a visualização de todas as alocações realizadas em projetos pré-selecionados em um filtro. A opção de menu dessa funcionalidade encontra-se na pasta "Planejamento" no item "Alocação de Recursos" (Protótipo 01). Abaixo estão as características e maneira de utilização da funcionalidade:

* + Usuário seleciona a opção no menu principal (pasta "Planejamento" no item "Alocação de Recursos");
  + A tela de de seleção de projetos (Protótipo 02) será exibida para que os mesmos possam ser definidos e considerados na tela de interprojetos;
  + Em seguida a tela de alocação de recurso inter-projetos será exibida com as alocações realizadas e que estão relacionadas a equipamentos, mão de obra e transporte, juntamente com os respectivos projetos selecionados (Protótipo 03);
  + Na hierarquia de "Recursos Alocados", ao navegar em cada item, é possível visualizar o "Cronograma de Alocação" de recursos no anexo "Cronograma de Alocação - Recursos" no lado direito da tela onde é exibido a **Quantidade de Horas**, **Dias de Trabalho**, e **Alocação do Período**, em relação ao cronograma do projeto (Protótipo 03). Cada linha do anexo representa a alocação do item para os projetos que foram pré-selecionados. Nos dias dos períodos exibidos a cor **verde** representa a alocação normal e a cor **vermelha** representa a super alocação do recurso. Para os recursos alocados é possível selecionar o ano no qual as informações serão exibidas e se é necessário exibir a coluna de jornada (Protótipo 03). O filtro de "ano" é preenchido de acordo com os anos nos quais os cronograma de todos os projetos selecionados vigoram;
  + Na hierarquia de Projetos, para o Cronograma de Alocação, são exibidas as alocações relacionadas com o item selecionado no anexo "Cronograma de Alocação - Tarefas" (Protótipo 04), da seguinte forma:
    - **Projeto:** Exibe todas as alocações realizada no projeto selecionado;
    - **Obra:** Exibe todas as alocações realizada nas tarefas relacionadas à obra selecionada;
    - **Etapa:** Exibe todas as alocações realizada nas tarefas relacionadas à etapa selecionada;
    - **Tarefa:** Exibe todas as alocações realizada na tarefas selecionada;

 **Importante:**

* + **Os projetos exibidos na tela de Seleção de Projetos são aqueles que tem o status "Em andamento" ou "Em execução", projetos que não são globais e de todas as coligadas existentes no sistema;**
  + **As informações da tela de Interprojetos, também são exibidas para todas as coligadas;**
  + **No nível de "Recursos Alocados", a alocação de pessoas e bens considera todas as coligadas e projetos selecionados no filtro.**

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| [Alocação de Recursos] | [Migração] | [Planejamento -> Alocação de Recursos -> Interprojetos] | - |
|  |  |  |  |

## Protótipo de Tela

**Protótipo 01**

****Protótipo 02****

****Protótipo 03****

******Protótipo 04******

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |
