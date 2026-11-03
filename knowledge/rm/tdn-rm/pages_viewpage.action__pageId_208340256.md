---
content_hash: da49c99324653d528e5d5a0a256c596d2415d3f1e07f5d76c399d710e815cd13
fetched_at: '2026-06-29T00:06:13.406596+00:00'
page_id: '208340256'
product: rm
source: tdn-rm
title: ER_PCREQ-6021_Relatório_Tarefas_por_Grupo_de_Custo
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=208340256
version: 26
---

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

## Informações Gerais

|  |  |  |  |
| --- | --- | --- | --- |
| **Especificação** | | | |
| **Produto** | TOTVS Obras e Projetos | **Módulo** | Relatórios Projetos |
| **Segmento Executor** | Construção & Projetos | | |
| **Projeto1** | PDR\_CP\_TOP008 | **IRM1** | PCREQ-6020 |
| **Requisito1** | PCREQ-6021 | **Subtarefa1** | PDR\_CP\_TOP008-26 |
| **Chamado2** | Não se aplica. | | |
| **Release de Entrega Planejada** | 12.1.8 | **Réplica** | Não |
| **País** | ( X ) Brasil  (  ) Argentina  (  ) Mexico  (  ) Chile  (  ) Paraguai  (  ) Equador  (  ) USA  (  ) Colombia   (  ) Outro \_\_\_\_\_\_\_\_\_\_\_\_\_. | | |
| **Outros** | *<Caso necessário informe outras referências que sejam pertinentes a esta especificação. Exemplo: links de outros documentos ou subtarefas relacionadas>.* | | |

   Legenda: 1 – Inovação 2 – Manutenção (Os demais campos devem ser preenchidos para ambos os processos). 

## Objetivo

 Upgrade do relatório de Tarefas por Grupo de Custo utilizando o Gerador.NET.

## Definição da Regra de Negócio

O Relatório de Tarefas por Grupo de Custo exibe as tarefas da planilha de atividades, planilha de serviços ou cenários  de um projeto.  .

A funcionalidade para execução do relatório é acessada através da opção "Relatórios -> Tarefas-> Planilha de Tarefas". Podendo o usuário no momento da execução optar entre os relatórios denominados "Tarefas por Grupo de Custo (por Valor)" ou "Tarefa por Grupo de Custos (por Custo)".

O valor dos grupos de custos e o total da tarefa são compostos pela soma do valor com o valor improdutivo. Sendo que no relatório que apresenta o custo, será considerado o valor de custo e custo improdutivo.

As informações contidas no relatório são:

* Código da Tarefa;
* Nome;
* Unidade;
* Disciplina;
* Quantidade;
* Valor da mão de obra;
* Valor de materiais;
* Valor de equipamentos;
* Valor total da tarefa;
* Valor total da etapa;
* Valor total da obra;
* Valor total do projeto.

É opcional a execução do recalculo da curva ABC que poderá ocorrer antes da execução. Para isto o usuário dever marcar a respectiva opção.

**Restrições**

* Este relatório será padrão no sistema e por questão de segurança o usuário não poderá editar ou excluir o mesmo, podendo duplicá-lo para criar outro customizado.
* O padrão atende a estrutura de planilha de atividades/serviços que possuem a hierarquia definida em obra, etapa e tarefa. Contempla assim três níveis. Permite customizar, adicionando quantos níveis forem necessários.
* Ao customizar o relatório será necessário adicionar filtros específicos () para determinar o conteúdo apresentado para obra, etapa e tarefa conforme abaixo:
  + Obra -> Serviço = 0 e Quantidade > 0;
  + Etapa -> Serviço = 0 e Quantidade IS NULL;
  + Tarefa -> Serviço = 1.

**Filtros**

* Por cenário e tipo de planilha.
* Tarefa inicial e final.
* Por Disciplina.

**Localização do Relatório**

Interna: *RM/Documentos/Prj-Projetos/Relatórios/Relatorios Migrados*

Clientes: Pasta "*Objetos Gerenciais*" localizada no diretório de instalação do Produto.

|  |  |  |  |
| --- | --- | --- | --- |
| **Rotina** | **Tipo de Operação** | **Opção de Menu** | **Regras de Negócio** |
| Relatório de Tarefas por Grupo de Custos | Criação | Relatórios -> Tarefas -> Planilha de Tarefas |  |
|  |  |  |  |

***Tabelas Utilizadas***

* *MTRF – Tarefas da Planilha de Atividades*
* *MPRJ - Projetos*
* *MABCISM - Curva ABC de Insumos*
* *GCOLIGADA - Coligadas*
* *GIMAGEM - Imagens*

### Opcional

## Protótipo de Tela

**Protótipo 01 - **Tela de Filtros****

**Protótipo 02 -**Leiaute do Relatório****

****Protótipo 03 - Exemplo de Filtros****

| **Este documento é material de especificação dos requisitos de inovação, trata-se de conteúdo extremamente técnico.** |
| --- |

divs
